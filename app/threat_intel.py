from __future__ import annotations

"""Ingest an external threat-intel incident feed (e.g. DPRK/Russia/Iran crypto-exchange
hacks) into raw/threat-intel/ as the "reality" layer of the mirror-world mode.

The feed schema is not fixed: `adapt_payload` maps a provider's JSON onto an internal
`IncidentRecord` via a forgiving field map, so this works against a sample file today
and a live API later. For each incident it can also trigger the existing news ingest
with a focus query, dropping the "official narrative" coverage next to the reality file.

Attribution of cyber incidents is contested, so records carry a confidence level and are
written as *sourced claims*, never asserted as fact.
"""

import json
import os
import random
import re
import time
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

import httpx
from dotenv import load_dotenv


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_THREAT_INTEL = PROJECT_ROOT / "raw" / "threat-intel"
SESSIONS_DIR = PROJECT_ROOT / "sessions"
STATE_PATH = SESSIONS_DIR / "threat-intel-state.json"

load_dotenv(PROJECT_ROOT / ".env")

THREAT_INTEL_BASE_URL = os.getenv("THREAT_INTEL_BASE_URL", "")
THREAT_INTEL_API_KEY = os.getenv("THREAT_INTEL_API_KEY", "")


@dataclass
class IncidentRecord:
    id: str
    timestamp: str
    state: str = ""          # attributed nation-state actor (DPRK/Russia/Iran/...)
    group: str = ""          # named group (Lazarus/APT38/...)
    confidence: str = ""     # attribution confidence (low/medium/high)
    target: str = ""         # exchange/entity hit
    amount_usd: float | None = None
    asset: str = ""          # chain/asset
    vector: str = ""         # short technique category, not operational detail
    summary: str = ""
    references: list[str] = field(default_factory=list)


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", (text or "")).strip("-").lower()
    return re.sub(r"-{2,}", "-", slug) or "incident"


def _first(payload: dict, *keys, default=None):
    for key in keys:
        if key in payload and payload[key] not in (None, ""):
            return payload[key]
    return default


def _extract_target_label(raw: dict) -> str:
    """Target can arrive as a plain string or a nested object (e.g. {"country": null, ...});
    some providers leave every sub-field null, so fall back to the incident id, which
    tends to embed a readable name (e.g. "CHA-Ronin-Network-149")."""
    target = raw.get("target")
    if isinstance(target, dict):
        label = _first(target, "name", "entity", "exchange", "victim", "label", default="")
        if label:
            return str(label)
        target = ""
    elif target in (None, ""):
        target = ""
    label = str(target or _first(raw, "victim", "entity", "exchange", default="") or "")
    if not label:
        rid = str(_first(raw, "id", "incident_id", "uuid", default="") or "")
        parts = [p for p in rid.split("-") if p and not p.isdigit()][1:]  # drop state prefix + trailing numeric id
        label = " ".join(parts)
    return label


def _format_reference(ref) -> str:
    """References can arrive as a bare URL string or a {source, title, url} object."""
    if isinstance(ref, dict):
        url = _first(ref, "url", "link", default="")
        title = _first(ref, "title", "source", default="")
        if url and title:
            return f"{title} ({url})"
        return str(url or title or ref)
    return str(ref)


def adapt_payload(raw: dict) -> IncidentRecord:
    """Map an arbitrary provider payload onto IncidentRecord, tolerating common shapes."""
    attribution = raw.get("attribution") if isinstance(raw.get("attribution"), dict) else {}
    state = (
        _first(attribution, "state", "country", "actor", default="")
        or _first(raw, "region", "attribution_state", "state", "actor", default="")
    )
    group = _first(attribution, "group", "threat_actor", "name", default="") or _first(raw, "attribution_group", "group", default="")
    confidence = _first(attribution, "confidence", default="") or _first(raw, "confidence", "attribution_confidence", default="")
    target = _extract_target_label(raw)
    timestamp = str(_first(raw, "timestamp", "date", "occurred_at", "published_at", default=""))
    references = _first(raw, "references", "sources", "links", default=[]) or []
    if isinstance(references, str):
        references = [references]
    amount = _first(raw, "amount_usd", "amount", "value_usd", "loss_usd")
    try:
        amount = float(amount) if amount is not None else None
    except (TypeError, ValueError):
        amount = None
    rid = str(_first(raw, "id", "incident_id", "uuid", default="") or f"{timestamp[:10]}-{slugify(target)[:40]}")
    return IncidentRecord(
        id=rid,
        timestamp=timestamp,
        state=str(state or ""),
        group=str(group or ""),
        confidence=str(confidence or ""),
        target=str(target or ""),
        amount_usd=amount,
        asset=str(_first(raw, "asset", "chain", "token", default="") or ""),
        vector=str(_first(raw, "vector", "method", "technique", "category", default="") or ""),
        summary=str(_first(raw, "summary", "description", "details", default="") or ""),
        references=[_format_reference(r) for r in references],
    )


def _date_prefix(rec: IncidentRecord) -> str:
    match = re.search(r"(\d{4}-\d{2}-\d{2})", rec.timestamp or "")
    return match.group(1) if match else datetime.now().strftime("%Y-%m-%d")


def incident_path(rec: IncidentRecord) -> Path:
    label = " ".join(p for p in [rec.target, rec.state] if p) or "incident"
    return RAW_THREAT_INTEL / f"{_date_prefix(rec)}-{slugify(label)[:70]}.md"


def render_markdown(rec: IncidentRecord) -> str:
    amount = f"${rec.amount_usd:,.0f}" if rec.amount_usd is not None else "unknown"
    refs = "; ".join(rec.references) if rec.references else "none"
    title = " ".join(p for p in [rec.target, "—", f"{rec.state}-attributed incident" if rec.state else "incident"] if p)
    lines = [
        f"# {title}".rstrip(),
        "",
        "> Type: threat-intel incident (SOURCED CLAIM — treat attribution as a claim at the stated confidence, not fact)",
        f"> Incident ID: {rec.id}",
        f"> Timestamp: {rec.timestamp or 'unknown'}",
        f"> Attribution: {rec.state or 'unattributed'} / {rec.group or 'unknown group'} (confidence: {rec.confidence or 'unstated'})",
        f"> Target: {rec.target or 'unknown'}",
        f"> Amount (USD): {amount}",
        f"> Asset: {rec.asset or 'unknown'}",
        f"> Vector: {rec.vector or 'unknown'}",
        f"> References: {refs}",
        "",
        rec.summary.strip() or "No summary provided by the feed.",
        "",
    ]
    return "\n".join(lines)


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"seen": []}
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {"seen": []}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")


class ThreatIntelFeedError(RuntimeError):
    """Non-retryable feed error (bad token, malformed request, unknown id) with a clear message."""


def _feed_headers() -> dict:
    headers = {"Accept": "application/json"}
    if THREAT_INTEL_API_KEY:
        headers["Authorization"] = f"Bearer {THREAT_INTEL_API_KEY}"
    return headers


def _get_with_retries(client: httpx.Client, url: str, params: dict, max_retries: int) -> httpx.Response:
    for attempt in range(max_retries + 1):
        res = client.get(url, headers=_feed_headers(), params=params)
        if res.status_code == 429 and attempt < max_retries:
            time.sleep(float(res.headers.get("Retry-After") or 1))
            continue
        if res.status_code == 401:
            raise ThreatIntelFeedError("feed rejected the token (401) — check THREAT_INTEL_API_KEY")
        if res.status_code == 400:
            raise ThreatIntelFeedError(f"malformed request (400) for params={params}")
        res.raise_for_status()
        return res
    raise ThreatIntelFeedError("rate-limited (429) past max retries")


def check_feed_health() -> dict:
    """GET {base}/health — unauthenticated connectivity check."""
    if not THREAT_INTEL_BASE_URL:
        return {"status": "unconfigured"}
    with httpx.Client(timeout=15.0) as client:
        res = client.get(f"{THREAT_INTEL_BASE_URL}/health")
        res.raise_for_status()
        return res.json()


def fetch_incident(incident_id: str) -> dict:
    """GET {base}/incidents/{id} — re-pull or refresh a single record."""
    if not THREAT_INTEL_BASE_URL:
        raise ThreatIntelFeedError("THREAT_INTEL_BASE_URL not set")
    with httpx.Client(timeout=45.0) as client:
        res = client.get(f"{THREAT_INTEL_BASE_URL}/incidents/{incident_id}", headers=_feed_headers())
    if res.status_code == 404:
        raise ThreatIntelFeedError(f"unknown incident id: {incident_id}")
    if res.status_code == 401:
        raise ThreatIntelFeedError("feed rejected the token (401) — check THREAT_INTEL_API_KEY")
    res.raise_for_status()
    return res.json()


def _page_records(page) -> list[dict]:
    """Tolerate {"data": [...]} / {"incidents": [...]} / {"results": [...]} / a bare [...]."""
    if isinstance(page, list):
        return page
    if isinstance(page, dict):
        return page.get("data") or page.get("incidents") or page.get("results") or []
    return []


def fetch_all_incidents(since: str | None = None, limit: int = 100, max_retries: int = 5) -> list[dict]:
    """Pull raw incident payloads from the feed, following cursor pagination (`pagination.
    next_cursor` / `has_more`) until exhausted. `since` restricts to an incremental pull;
    omit it for a full sync. Returns [] if not configured."""
    if not THREAT_INTEL_BASE_URL:
        return []
    records: list[dict] = []
    cursor: str | None = None
    with httpx.Client(timeout=45.0) as client:
        while True:
            params: dict = {"limit": limit}
            if cursor:
                params["cursor"] = cursor
            if since:
                params["since"] = since
            page = _get_with_retries(client, f"{THREAT_INTEL_BASE_URL}/incidents", params, max_retries).json()
            records.extend(_page_records(page))
            pagination = page.get("pagination") or {} if isinstance(page, dict) else {}
            cursor = pagination.get("next_cursor")
            if not pagination.get("has_more") or not cursor:
                break
    return records


def load_sample(path: str | Path) -> list[dict]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return data.get("incidents") or data.get("data") or data.get("results") or [data]
    return data


def ingest(raw_records: list[dict]) -> dict:
    """Adapt + write incident reality files, deduped by id. Returns {saved, skipped}."""
    RAW_THREAT_INTEL.mkdir(parents=True, exist_ok=True)
    state = load_state()
    seen = set(state.get("seen", []))
    saved: list[dict] = []
    skipped: list[dict] = []
    for raw in raw_records:
        rec = adapt_payload(raw)
        if rec.id in seen:
            skipped.append({"id": rec.id, "reason": "already-seen"})
            continue
        path = incident_path(rec)
        path.write_text(render_markdown(rec), encoding="utf-8")
        seen.add(rec.id)
        saved.append({"id": rec.id, "path": str(path.relative_to(PROJECT_ROOT).as_posix()), "record": rec})
    state["seen"] = sorted(seen)
    state["last_run"] = datetime.now().isoformat()
    save_state(state)
    return {"saved": saved, "skipped": skipped}


def incident_focus_query(rec: IncidentRecord) -> str:
    parts = [rec.target, rec.state, rec.asset, "crypto exchange hack sanctions"]
    return " ".join(p for p in parts if p)


def prompt_from_incident(rec: IncidentRecord, stats: dict | None = None) -> str:
    """Seed a mirror-world session prompt from an incident (the reality layer). When `stats`
    (from dataset_stats()) is given, adds a comparative-pattern clause — how this incident's
    confidence and scale sit relative to the whole dataset — so actors have more than one
    isolated anecdote to argue with: they can contest the PATTERN, not just the case."""
    amount = f"${rec.amount_usd:,.0f}" if rec.amount_usd is not None else "an undisclosed sum"
    base = (
        f"MIRROR-WORLD INTELLIGENCE (reality layer — sourced claim at {rec.confidence or 'unstated'} confidence): "
        f"{rec.target or 'An exchange'} lost {amount} in a {rec.state or 'state'}-attributed operation "
        f"({rec.group or 'unknown group'}) via {rec.vector or 'unknown means'}. {rec.summary} "
    )
    if stats and stats.get("median_confidence") is not None:
        try:
            this_conf = float(rec.confidence)
        except (TypeError, ValueError):
            this_conf = None
        if this_conf is not None:
            median = stats["median_confidence"]
            if this_conf > median + 0.15:
                cmp = "notably more solid than"
            elif this_conf < median - 0.15:
                cmp = "notably weaker than"
            else:
                cmp = "roughly in line with"
            top_group = stats["top_groups"][0][0] if stats["top_groups"] else "unnamed groups"
            base += (
                f"\n\nDATASET CONTEXT: this is one of {stats['total_incidents']} tracked incidents (combined modeled "
                f"losses over ${stats['total_amount_usd']:,.0f}); its {this_conf:.2f} attribution confidence is "
                f"{cmp} the dataset's own median of {median:.2f}, and only "
                f"{stats['vector_known_count']}/{stats['total_incidents']} incidents in the set even have a known "
                f"attack vector. The most-named group across the set is {top_group}. "
            )
    base += (
        "The official story and the regulations will say something cleaner. Stage the clash between what actually "
        "happened and what each actor claims — including whether this case is representative of the pattern or a "
        "convenient outlier — then extrapolate where this absurdly goes next."
    )
    return base


async def pull_official_coverage(records: list[IncidentRecord], max_per_query: int = 4) -> dict:
    """For each incident, pull media/regulatory coverage via the existing news ingest,
    landing the 'official narrative' under raw/focus-issues/<incident-slug>/."""
    from .news_ingest import run_news_ingest  # async; avoids a hard import cycle at module load

    results = []
    for rec in records:
        focus = incident_focus_query(rec)
        try:
            report = await run_news_ingest(days=14, max_per_query=max_per_query, focus_query=focus)
            results.append({"id": rec.id, "focus": focus, "saved": len(report.get("saved", []))})
        except Exception as exc:
            results.append({"id": rec.id, "focus": focus, "error": str(exc)})
    return {"official": results}


def _parse_incident_file(path: Path) -> IncidentRecord:
    """Reconstruct an IncidentRecord from a rendered raw/threat-intel/*.md file."""
    text = path.read_text(encoding="utf-8")

    def grab(label: str) -> str:
        m = re.search(rf"^> {re.escape(label)}: (.+)$", text, flags=re.M)
        return m.group(1).strip() if m else ""

    attribution = grab("Attribution")
    state, _, rest = attribution.partition("/")
    group = rest.split("(")[0].strip() if rest else ""
    conf_m = re.search(r"confidence:\s*([\d.]+)", attribution)
    confidence = conf_m.group(1) if conf_m else ""
    # Body is the prose after the metadata blockquote — strip the title and every
    # "> " metadata line rather than splitting on the first blank line, which used
    # to glue the raw metadata block onto the front of the "summary" (a real bug:
    # this summary seeds every mirror-world session's prompt via prompt_from_incident).
    body_lines = [
        line for line in text.splitlines()
        if line.strip() and not line.startswith("#") and not line.startswith(">")
    ]
    body = "\n".join(body_lines).strip()
    amount_raw = grab("Amount (USD)").replace("$", "").replace(",", "")
    try:
        amount = float(amount_raw)
    except ValueError:
        amount = None
    return IncidentRecord(
        id=grab("Incident ID"),
        timestamp=grab("Timestamp"),
        state=state.strip(),
        group=group,
        confidence=confidence,
        target=grab("Target"),
        amount_usd=amount,
        asset=grab("Asset"),
        vector=grab("Vector"),
        summary=body[:600],
    )


def latest_incident() -> IncidentRecord | None:
    """Return the most recent ingested incident (by filename date prefix)."""
    files = sorted(RAW_THREAT_INTEL.glob("*.md"))
    if not files:
        return None
    return _parse_incident_file(files[-1])


def random_incident() -> IncidentRecord | None:
    """Return a random ingested incident — the default for seed_incident, so a mirror-world
    session draws from the whole dataset instead of always the same 'latest' file."""
    files = list(RAW_THREAT_INTEL.glob("*.md"))
    if not files:
        return None
    return _parse_incident_file(random.choice(files))


def get_incident_by_id(incident_id: str) -> IncidentRecord | None:
    """Look up one specific incident by its Incident ID field, for seeding a chosen case."""
    for path in RAW_THREAT_INTEL.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        m = re.search(r"^> Incident ID: (.+)$", text, flags=re.M)
        if m and m.group(1).strip() == incident_id:
            return _parse_incident_file(path)
    return None


def dataset_stats() -> dict:
    """Aggregate stats across every ingested incident, so a single seed can be presented
    IN CONTEXT of the pattern (confidence, group, scale) rather than as an isolated crime —
    the 'more complex interpretation' layer for mirror-world debates."""
    confidences: list[float] = []
    groups: Counter = Counter()
    total_amount = 0.0
    vector_known = 0
    files = list(RAW_THREAT_INTEL.glob("*.md"))
    for path in files:
        text = path.read_text(encoding="utf-8")

        def grab(label: str) -> str:
            m = re.search(rf"^> {re.escape(label)}: (.+)$", text, flags=re.M)
            return m.group(1).strip() if m else ""

        attribution = grab("Attribution")
        conf_m = re.search(r"confidence:\s*([\d.]+)", attribution)
        if conf_m:
            confidences.append(float(conf_m.group(1)))
        _, _, rest = attribution.partition("/")
        group = rest.split("(")[0].strip()
        if group and group.lower() != "unknown group":
            groups[group] += 1
        amount_raw = grab("Amount (USD)").replace("$", "").replace(",", "")
        try:
            total_amount += float(amount_raw)
        except ValueError:
            pass
        vector = grab("Vector")
        if vector and vector.lower() not in ("", "unknown"):
            vector_known += 1
    confidences.sort()
    median_confidence = confidences[len(confidences) // 2] if confidences else None
    return {
        "total_incidents": len(files),
        "total_amount_usd": total_amount,
        "median_confidence": median_confidence,
        "confidence_count": len(confidences),
        "top_groups": groups.most_common(5),
        "vector_known_count": vector_known,
    }
