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

## When the live API arrives — the only steps

1. **Set credentials** in `.env`:
   ```
   THREAT_INTEL_BASE_URL=https://<friend-endpoint>
   THREAT_INTEL_API_KEY=<read-only key>
   ```
   (Server-side only — never put this in Lovable/the browser.)
2. **Adjust the field map if his schema differs.** `app/threat_intel.py::adapt_payload` already tolerates common shapes — `attribution{state,group,confidence}` or flat `attribution_state`; `target`/`victim`/`exchange`; `amount_usd`/`amount`/`value_usd`; `vector`/`method`/`technique`; `references`/`sources`/`links`; list response under `incidents`/`data`/`results` or a bare array. If his field names are different, add them to the `_first(...)` fallback lists.
3. **Pull:**
   ```powershell
   python scripts/run_threat_intel_ingest.py --since 2026-06-01     # live API + official coverage
   ```
   Dedups by incident `id` via `sessions/threat-intel-state.json`. Official coverage needs `TAVILY_API_KEY` / `SERPAPI_API_KEY` set (reuses the existing news ingest); use `--no-official` to skip.
4. **Run a mirror-world session** with `seed_incident: true` (via `/stage`, the API, or Lovable).

## What to ask the friend to provide

- **Access:** auth method (bearer/API key), a **read-only** key out-of-band, base URL, and whether it's **REST poll** (a `since`/cursor param — easiest) or a **stream** (SSE/WebSocket).
- **Schema per incident:** stable `id`, ISO-8601 `timestamp`, `attribution` (state + named group + **confidence**), `target`, `amount_usd`, `asset`, a short `vector` *category* (classification, not operational detail), `summary`, and `references` (source URLs).
- **Provenance:** can the data be stored and cited? Historical **backfill** vs live-only, pagination, update cadence.
- **A sample payload + test key first**, so the field map can be confirmed before the event.

## Files

- `app/threat_intel.py` — `IncidentRecord`, `adapt_payload`, `ingest`, `render_markdown`, `fetch_incidents_from_api`, `pull_official_coverage`, `prompt_from_incident`, `latest_incident`.
- `scripts/run_threat_intel_ingest.py` — CLI (`--sample`, `--since`, `--no-official`).
- `docs/sample_incidents.json` — illustrative sample feed.
- Mode wiring: `app/llm.py` (`generate_openrouter_mirror_turn` / `_mirror_card`), `app/agent_logic.py` (`generate_actor_mirror_turn` / `build_mirror_card`), `app/main.py` (mirror-world branch + `/session/{id}/mirror-card`).

## See Also

- [Roundtable Frontend Contract](roundtable-frontend-contract.md) — Mirror-World Contract section (mode + `/mirror-card` shapes).
