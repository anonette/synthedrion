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
import re
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


def adapt_payload(raw: dict) -> IncidentRecord:
    """Map an arbitrary provider payload onto IncidentRecord, tolerating common shapes."""
    attribution = raw.get("attribution") if isinstance(raw.get("attribution"), dict) else {}
    state = _first(attribution, "state", "country", "actor", default="") or _first(raw, "attribution_state", "state", "actor", default="")
    group = _first(attribution, "group", "threat_actor", "name", default="") or _first(raw, "attribution_group", "group", default="")
    confidence = _first(attribution, "confidence", default="") or _first(raw, "confidence", "attribution_confidence", default="")
    target = _first(raw, "target", "victim", "entity", "exchange", default="")
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
        references=[str(r) for r in references],
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


def fetch_incidents_from_api(since: str | None = None, limit: int = 50) -> list[dict]:
    """Pull raw incident payloads from the friend's feed. Returns [] if not configured."""
    if not THREAT_INTEL_BASE_URL:
        return []
    headers = {"Accept": "application/json"}
    if THREAT_INTEL_API_KEY:
        headers["Authorization"] = f"Bearer {THREAT_INTEL_API_KEY}"
    params = {"limit": limit}
    if since:
        params["since"] = since
    with httpx.Client(timeout=45.0) as client:
        res = client.get(THREAT_INTEL_BASE_URL, headers=headers, params=params)
        res.raise_for_status()
        data = res.json()
    # tolerate {"incidents": [...]} / {"data": [...]} / [...]
    if isinstance(data, dict):
        return data.get("incidents") or data.get("data") or data.get("results") or []
    return data if isinstance(data, list) else []


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


def prompt_from_incident(rec: IncidentRecord) -> str:
    """Seed a mirror-world session prompt from an incident (the reality layer)."""
    amount = f"${rec.amount_usd:,.0f}" if rec.amount_usd is not None else "an undisclosed sum"
    return (
        f"MIRROR-WORLD INTELLIGENCE (reality layer — sourced claim at {rec.confidence or 'unstated'} confidence): "
        f"{rec.target or 'An exchange'} lost {amount} in a {rec.state or 'state'}-attributed operation "
        f"({rec.group or 'unknown group'}) via {rec.vector or 'unknown means'}. {rec.summary} "
        f"The official story and the regulations will say something cleaner. Stage the clash between what actually "
        f"happened and what each actor claims, then extrapolate where this absurdly goes next."
    )


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


def latest_incident() -> IncidentRecord | None:
    """Return the most recent ingested incident, for seeding a mirror-world session."""
    files = sorted(RAW_THREAT_INTEL.glob("*.md"))
    if not files:
        return None
    text = files[-1].read_text(encoding="utf-8")
    def grab(label: str) -> str:
        m = re.search(rf"^> {re.escape(label)}: (.+)$", text, flags=re.M)
        return m.group(1).strip() if m else ""
    title = (re.search(r"^# (.+)$", text, flags=re.M) or [None, ""])[1]
    attribution = grab("Attribution")
    state = attribution.split("/")[0].strip() if attribution else ""
    body = text.split("\n\n", 1)[-1].strip()
    return IncidentRecord(
        id=grab("Incident ID"),
        timestamp=grab("Timestamp"),
        state=state,
        target=grab("Target"),
        asset=grab("Asset"),
        vector=grab("Vector"),
        summary=body[:600],
    )
