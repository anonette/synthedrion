"""Halcyon's crawler: refresh the Ledger of Hope with recent, real, cooperative news.

Fetches Google News RSS for cooperation-themed queries on the fronts the roundtable
fights over (chips, minerals, energy, talent, safety/standards), asks the recap model
to select the genuinely hopeful items, and appends a new "## Crawl" section to the
ledger at HALCYON_LEDGER_PATH in the exact format app/main.py's parser expects.

Usage (locally or on the server):
    python scripts/halcyon_crawl.py            # appends up to 6 fresh entries
Requires OPENROUTER_API_KEY — Halcyon's hope is curated, never fabricated: with no
model to judge hopefulness, the crawler refuses to run rather than guess.

Weekly cron on the server keeps Halcyon's opening news fresh:
    0 6 * * 1  cd /opt/aicoldwar && ./.venv/bin/python scripts/halcyon_crawl.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote
from xml.etree import ElementTree as ET

import httpx

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.config import HALCYON_LEDGER_PATH, OPENROUTER_API_KEY, OPENROUTER_APP_NAME, OPENROUTER_BASE_URL, OPENROUTER_SITE_URL, RECAP_MODEL

QUERIES = [
    "US China AI cooperation agreement",
    "international AI safety agreement summit",
    "rare earth recycling breakthrough",
    "semiconductor supply chain cooperation",
    "AI standards international collaboration",
    "clean energy data center breakthrough",
    "US China technology dialogue",
    "global south AI development partnership",
]

FRONTS = "chips, minerals, energy, talent, standards, safety, dialogue"


def fetch_candidates(max_per_query: int = 6) -> list[dict]:
    items: list[dict] = []
    seen: set[str] = set()
    with httpx.Client(timeout=30.0, follow_redirects=True) as client:
        for q in QUERIES:
            url = f"https://news.google.com/rss/search?q={quote(q)}+when:14d&hl=en-US&gl=US&ceid=US:en"
            try:
                res = client.get(url)
                res.raise_for_status()
                root = ET.fromstring(res.text)
            except Exception as exc:
                print(f"query failed ({q}): {exc}")
                continue
            for item in root.iter("item"):
                title = (item.findtext("title") or "").strip()
                link = (item.findtext("link") or "").strip()
                source = (item.findtext("{http://news.google.com/rss}source") or item.findtext("source") or "").strip()
                if not title or title.lower() in seen:
                    continue
                seen.add(title.lower())
                items.append({"title": title, "link": link, "source": source or "news"})
                if sum(1 for i in items if i.get("_q") == q) >= max_per_query:
                    break
    return items[:60]


def select_hopeful(candidates: list[dict], count: int = 6) -> list[dict]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set — Halcyon's hope is curated, not guessed")
    listing = "\n".join(f"{i}. {c['title']} ({c['source']})" for i, c in enumerate(candidates))
    system = (
        "You curate Halcyon's Ledger of Hope for an AI-cold-war roundtable. From the headlines, pick the "
        f"{count} that are GENUINELY hopeful, real, recent developments on the fronts the powers fight over "
        f"({FRONTS}): cooperation, breakthroughs that ease zero-sum pressure, dialogue, shared standards. "
        "Reject hype, product launches, opinion pieces, and anything adversarial. Return ONLY a JSON array; "
        "each element: {\"idx\": <number from the list>, \"front\": \"<one of: chips|minerals|energy|talent|standards|safety|dialogue>\", "
        "\"eases\": \"<2-4 words: what pressure it eases>\", \"unites\": \"<comma list of actors it brings together: us, china, eu, global south>\", "
        "\"why\": \"<one sentence: why this is hopeful, concrete and factual>\"}"
    )
    payload = {
        "model": RECAP_MODEL,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": listing}],
        "temperature": 0.3,
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=90.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        text = res.json()["choices"][0]["message"]["content"]
    start, end = text.find("["), text.rfind("]")
    picks = json.loads(text[start:end + 1])
    out = []
    for p in picks[:count]:
        try:
            c = candidates[int(p["idx"])]
        except (KeyError, ValueError, IndexError):
            continue
        out.append({**c, "front": p.get("front", "dialogue"), "eases": p.get("eases", ""),
                    "unites": p.get("unites", ""), "why": p.get("why", "")})
    return out


def append_to_ledger(entries: list[dict]) -> None:
    path = Path(HALCYON_LEDGER_PATH)
    path.parent.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    lines = [f"\n## Crawl {stamp}\n"]
    for e in entries:
        lines.append(f"- **{e['title']}** — _{e['source']}_")
        lines.append(f"  - front: `{e['front']}` · eases: {e['eases']} · unites: {e['unites']}")
        lines.append(f"  - why hopeful: {e['why']}")
        lines.append(f"  - {e['link']}")
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Halcyon — Ledger of Hope\n\nPositive AI-cold-war stories: evidence that another path exists.\n"
    path.write_text(existing.rstrip() + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"appended {len(entries)} entries to {path}")


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    candidates = fetch_candidates()
    print(f"{len(candidates)} candidate headlines")
    if not candidates:
        raise SystemExit("no candidates fetched — network problem?")
    hopeful = select_hopeful(candidates)
    if not hopeful:
        raise SystemExit("model selected nothing hopeful — ledger left untouched")
    append_to_ledger(hopeful)
    for e in hopeful:
        print(" +", e["title"][:80])


if __name__ == "__main__":
    main()
