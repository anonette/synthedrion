# Threat-Intel Feed Integration (Mirror-World Reality Layer)

> Updated: 2026-06-17

## What this is

The `mirror-world` mode stages a three-layer clash: **reality** (a threat-intel incident — e.g. DPRK/Russia/Iran-attributed crypto-exchange hacks) vs the **official narrative** (media + regulations) vs a **speculative** satirical extrapolation. This feed supplies the reality layer.

The ingestion is **adapter-based**, so the whole mirror world runs on a sample file today and just needs an endpoint + key when the friend's API is ready. Attribution is always treated as a **sourced claim at a stated confidence**, never asserted fact.

## Pipeline

```
friend's API ──▶ app/threat_intel.py ──▶ raw/threat-intel/<date>-<slug>.md   (reality)
                         │
                         └─ run_news_ingest(focus_query=incident) ──▶ raw/focus-issues/<slug>/  (official narrative)
                                                                              │
                                  mirror-world session (seed_incident=true) ◀─┘
                                                                              │
                                                                   POST /session/{id}/mirror-card
```

## Running it today (sample, no API)

```powershell
python scripts/run_threat_intel_ingest.py --sample docs/sample_incidents.json --no-official
python scripts/build_ingest_manifest.py
# then start a mirror-world session seeded from the latest incident (seed_incident: true)
```

## Connected feed: collaborator's DPRK crypto-incident sandbox

A collaborator's feed (`sandbox.hacksleuths.com/feed`, ~205 DPRK/Lazarus-attributed crypto-theft incidents, 2021–2026) is wired up as of 2026-07-19. Root-URL convention: `THREAT_INTEL_BASE_URL` is the feed **root** (e.g. `https://sandbox.hacksleuths.com/feed`, no `/incidents` suffix) — `app/threat_intel.py` builds `/health`, `/incidents`, and `/incidents/{id}` off it.

Schema quirks this feed has vs the generic field map: a top-level `region` (redundant with `attribution.state`, folded into the same fallback chain), and `target` arriving as a **nested object** (`{"country": null, ...}`) rather than a flat string — `_extract_target_label()` handles both shapes and falls back to parsing a readable name out of the incident `id` (e.g. `CHA-Ronin-Network-149`) if the target object is entirely null, which it is throughout this feed. `asset` is also null throughout — tolerated as `"unknown"` in the rendered markdown.

Pagination is cursor-based (`pagination.next_cursor` / `has_more`), not just `since` — `fetch_all_incidents()` loops until exhausted, and handles 401/400/404 as hard errors and 429 by sleeping `Retry-After` and retrying (bounded).

## Setting up a new feed — the steps

1. **Set credentials** in `.env` (gitignored — never commit, never expose client-side):
   ```
   THREAT_INTEL_BASE_URL=https://<feed-root>
   THREAT_INTEL_API_KEY=<read-only token>
   ```
2. **Check connectivity:** `python scripts/run_threat_intel_ingest.py --check`
3. **Adjust the field map if the schema differs.** `app/threat_intel.py::adapt_payload` tolerates common shapes — `attribution{state,group,confidence}` or flat `attribution_state`/`region`; `target` as a string or a nested object; `amount_usd`/`amount`/`value_usd`; `vector`/`method`/`technique`; `references`/`sources`/`links`; list response under `data`/`incidents`/`results` or a bare array. Add unmatched field names to the `_first(...)` fallback lists.
4. **Validate offline first** against a sample file before touching the live feed:
   ```powershell
   python scripts/run_threat_intel_ingest.py --sample docs/sample_incidents.json --no-official
   ```
5. **Pull:**
   ```powershell
   python scripts/run_threat_intel_ingest.py --no-official                                 # full initial sync (paginated)
   python scripts/run_threat_intel_ingest.py --since 2026-06-01T00:00:00Z --no-official     # incremental
   ```
   Dedups by incident `id` via `sessions/threat-intel-state.json`. `--no-official` is recommended for a large initial backfill — official coverage (media/regulatory search via Tavily/SerpAPI) is better pulled per-incident, on demand, when actually staging a mirror-world session from it, not for all ~200 records up front.
6. **Run a mirror-world session** with `seed_incident: true` (via `/stage`, the API, or Lovable).

## What to ask a new feed provider for

- **Access:** auth method (bearer/API key), a **read-only** key out-of-band, base URL, and whether it's **REST poll** (`since`/cursor param — easiest) or a **stream** (SSE/WebSocket).
- **Schema per incident:** stable `id`, ISO-8601 `timestamp`, `attribution` (state + named group + **confidence**), `target`, `amount_usd`, `asset`, a short `vector` *category* (classification, not operational detail), `summary`, and `references` (source URLs).
- **Provenance:** can the data be stored and cited? Historical **backfill** vs live-only, pagination, update cadence.
- **A sample payload + test key first**, so the field map can be confirmed before the event.

## Files

- `app/threat_intel.py` — `IncidentRecord`, `adapt_payload`, `ingest`, `render_markdown`, `fetch_all_incidents`, `fetch_incident`, `check_feed_health`, `pull_official_coverage`, `prompt_from_incident`, `latest_incident`.
- `scripts/run_threat_intel_ingest.py` — CLI (`--check`, `--sample`, `--since`, `--no-official`).
- `docs/sample_incidents.json` — illustrative sample feed.
- Mode wiring: `app/llm.py` (`generate_openrouter_mirror_turn` / `_mirror_card`), `app/agent_logic.py` (`generate_actor_mirror_turn` / `build_mirror_card`), `app/main.py` (mirror-world branch + `/session/{id}/mirror-card`).

## See Also

- [Roundtable Frontend Contract](roundtable-frontend-contract.md) — Mirror-World Contract section (mode + `/mirror-card` shapes).
