# AI Cold War 2026

A local FastAPI runtime that simulates a geopolitical "AI Cold War" roundtable between three blocs — **China**, the **US**, and the **EU** — who argue, negotiate, and generate propaganda based on a hand-curated markdown knowledge base. A handful of guest characters (a peace-builder, satirical caricature avatars, a crypto-native analyst) can interject on top of the core debate. The backend serves a Lovable frontend, both live over the API and via a static JSON snapshot fallback.

Docs at `http://127.0.0.1:8000/docs` once running; a bare-bones test UI at `/test`.

## The cast

| Actor | Type | Role |
|---|---|---|
| **China** | core, always on | Sovereignty, non-interference, developmental legitimacy, long-horizon industrial policy |
| **United States** | core, always on | Frontier competition, alliance power, market scale; prosecutorial, impatient with euphemism |
| **European Union** | core, always on | Brussels institutionalism, strategic autonomy; disciplines louder powers through regulation |
| **Halcyon** | guest, via `/intervene` | An outsider peace-builder belonging to no bloc — opens with real hopeful news, then dares the other three toward something built together |
| **The Satire Heads** | guest, "Brutal Satire" toggle | Xi / Trump / von der Leyen caricature avatars rewriting each real turn as a savage one-liner, delivered as talking-head video avatars |
| **James** (the Machiavellian Crypto-Native Analyst) | guest, on demand | A contrarian counter-take naming a specific mechanism (liquidity, exit liquidity, MEV) — no canned fallback; a failed call surfaces as a real error |

China/US/EU each run on their own model via OpenRouter (`ACTOR_MODELS` in `app/config.py`: DeepSeek, GPT-4.1-mini, Ministral). Halcyon runs on a separate CERIT-hosted endpoint with its own fallback model. Live roster data (including current archetypes/triggers) is served at `GET /roster`.

## Modes

- **`debate`** — the default: alternating argument/rebuttal between actors, grounded in wiki source notes.
- **`propaganda-lab`** — actors produce structured propaganda artifacts (slogan, image prompt, artifact type — poster, meme, campaign ad, infographic...) instead of prose. `app/images.py` renders an actual image per turn (per-actor image model, Pollinations URL as fallback). Rides along as `message.metadata` / replay `event.metadata` for the frontend to render as poster cards.
- **`mirror-world`** — a real DPRK crypto-incident (from `app/threat_intel.py`'s ingested feed) is prepended as the "buried reality" layer underneath the actors' official lines, contrasting stated position against ground truth.

## Guest characters, in detail

The core debate is always China/US/EU. On top of that, three optional guests can be summoned — none of them are round-robin actors, so summoning one doesn't consume a turn slot; it just appends an extra message to the transcript.

### Halcyon — the peace-builder

An outsider who belongs to no bloc. Opens with a real hopeful news item, then dares the other three toward something built together, mid-debate.

- Trigger: `POST /session/{session_id}/summon-halcyon` (operator-token guarded), or via `/intervene`
- Voice: a separate CERIT-hosted model (`HALCYON_MODEL`/`HALCYON_BASE_URL`/`HALCYON_API_KEY`), with `OPENROUTER_MODEL_HALCYON_FALLBACK` as a real backup model — **no canned fallback text**; if both are down the endpoint 502s in-character ("Even Halcyon needs a signal to hope with...")
- Source material: `halcyon/positive-stories.md`, a ledger of hopeful stories that grows over time; served on its own as `GET /halcyon/good-news`. Each summon pulls the next unused entries so Halcyon doesn't repeat himself within a session (tracked via how many times he's already spoken)

### The Satire Heads — brutal caricature rewrites

Xi / Trump / von der Leyen (plus a Halcyon caricature) talking-head avatars that rewrite a real turn into a savage one-liner, toggled by the "Brutal Satire" switch on the `/stage` UI.

- Trigger: `POST /satire` — takes `{actor, text, speak?, voice?, drift?}` and returns a rewritten quip; unauthenticated and read-only (it never touches session state), generated on a low-censorship CERIT endpoint, with a canned per-actor fallback line (`SATIRE_FALLBACKS`) if that's unreachable — this one *does* degrade gracefully, unlike Halcyon/James, so the show never stops
- `drift` (0–1) tunes faithful-and-savage vs. absurd; `speak: true` also synthesizes the line as audio (`TTS_SERVICE`: OpenAI / ElevenLabs / free edge-tts)
- `POST /session/{session_id}/satire-take` persists a full ordered take plus per-line audio so a whole performance replays later (including from an external frontend); `GET /api/satire-replay/{session_id}` and `GET /api/satire-takes` read them back
- Avatar assets live under `app/static/heads/`; packaging/publishing the static archive is `scripts/snapshot-satire.mjs` + `scripts/pack-satire.ps1` / `publish-satire.ps1` → `public/satire-archive/`

### James — the Machiavellian Crypto-Native Analyst

No other name, just the title. Trusts no one's stated motive and talks in the room's real currency — liquidity, exit liquidity, MEV. Gives a grounded, contrarian counter-prediction naming a specific mechanism, never a generic cynical aside.

- Trigger: `POST /session/{session_id}/james-take` for his closing take (cached on the session row; `?regenerate=true` forces a fresh one), or `POST /session/{session_id}/summon-james` for a live mid-debate interjection
- Works on any existing log, not just live sessions — checks the database first (so he can comment on archived/weekly sessions after a restart), falling back to the in-memory store, same lookup order as `/api/replay`
- Feed of past takes: `GET /james/takes`
- **By design, no fallback voice at all**: if `OPENROUTER_API_KEY` isn't set, or the model call fails, the endpoint raises a real error in-character ("The Analyst has nothing to say without a model to say it with") rather than ever returning a canned line

## Repository layout

- `app/` — the FastAPI runtime: session orchestration, LLM prompting, image/audio generation, threat-intel ingest, auth, DB persistence (see `app/main.py` for the full route table)
- `wiki/` — the markdown knowledge base agents actually read at runtime (see below — **this is the only layer that changes agent behavior**)
- `raw/` — source documents (articles, reg-documents, RAND papers, news ingest) waiting to be synthesized into `wiki/`; agents never read this directly
- `scripts/` — ingest, manifest-building, Drive download, and frontend-snapshot utilities
- `public/roundtable-archive/` — static JSON fallback for the main roundtable frontend (mirrors the live API shape)
- `public/satire-archive/` — static fallback/pack for the satire talking-heads module
- `sessions/` — generated manifests, ingest reports, and per-session local artifacts
- `halcyon/positive-stories.md` — Halcyon's ledger of hopeful news items, crawled and appended over time; served live at `GET /halcyon/good-news`
- `docs/sample_incidents.json` — sample threat-intel incident data for local testing without a live feed
- `lovable-frontend-package/` — scaffold for packaging frontend-side static assets
- `sessions.db` — local SQLite DB (see Persistence, below); gitignored

## The central data-flow rule

Three layers feed agent behavior, and the boundary between them is the thing most likely to trip you up:

- `raw/` — source documents. **Agents never read `raw/` at runtime.**
- `wiki/` — the markdown knowledge base agents actually load. **This is the only layer that changes behavior.**
- `app/` — the runtime that loads wiki pages and generates turns.

Dropping files into `raw/` does nothing until the relevant `wiki/` pages are edited to incorporate them. The workflow is: collect into `raw/` → build a manifest (`scripts/build_ingest_manifest.py` → `sessions/ingest-manifest.md`) → hand-synthesize into `wiki/` → start a new session.

### How the wiki is loaded

At session start, each actor loads its **hub page** (`ACTOR_HUBS` in `app/config.py`) plus the shared hub, then follows markdown links breadth-first. Link-following is sandboxed: a page only loads if it's under that actor's `ALLOWED_PATH_PREFIXES` (its own policy folder + `shared-ai-geopolitics` + `geopolitics` + `ai-governance`). `extract_notes()` then scrapes prose/bullet lines into short "source notes" (capped at 40/actor) — the grounding context fed to the model. **Adding a wiki page only affects an actor if it's reachable by a link from that actor's hub and inside its allowed prefixes.**

## Turn generation: LLM path vs. deterministic fallback

Every turn has two code paths, selected by `openrouter_enabled()` (true iff `OPENROUTER_API_KEY` is set):

- **LLM path** — `app/llm.py` builds per-actor system/user prompts and calls OpenRouter with a per-actor model. If the call throws, it falls back to the deterministic path with the error inlined.
- **Deterministic path** — `app/agent_logic.py` produces extractive, heuristic turns from the source notes with no network call. This is the default when no API key is present, and is useful for testing the flow offline.

`app/main.py::_generate_session_turn` is the single funnel all of the above flows through.

## Persistence — two stores, not equivalent

- **In-memory** `SESSIONS` dict (`app/session_store.py`) — the live working copy. All mutating endpoints (`/session/message`, `/intervene`, `/shock`, `/summary`, `/wiki-proposals`) read from here, so **they only work for sessions still in memory; restarting the backend loses them.**
- **Database** (`app/database.py`, SQLAlchemy, `sessions.db` by default) — every mutation also persists here. `/api/replay/{id}`, `/weekly/*`, and `/sessions/recent` read from the DB (replay falls back to memory). `init_db()` runs additive `ALTER TABLE` migrations on startup.

Weekly sessions are ordinary sessions tagged `session_type="weekly"` with `week_key`/`week_start`/`is_featured_weekly`/`title`/`theme`. Only one can be featured at a time.

## Auth — two independent schemes

- `require_roundtable_operator` — guards live mutating session endpoints (`/session/start`, `/session/message`, `/intervene`, `/shock`, per-session `/summary`, `/wiki-proposals`, `/summon-halcyon`, `/summon-james`, etc). Requires header `X-Roundtable-Token` to equal `ROUNDTABLE_OPERATOR_TOKEN`. Always enforced once the env var is set; returns 500 if unset.
- `verify_token` — Bearer-token guard on `/health/detailed`, `/session/scheduled*`, `/session/test`. **No-op in development** (returns a stub unless `PRODUCTION=true`), then checks against `API_TOKEN`.

Public/read endpoints (`/health`, `/weekly/*`, `/sessions/recent`, `/session/{id}`, `/api/replay/{id}`, `/roster`, `/halcyon/good-news`, `/james/takes`) are unauthenticated. CORS allows all origins unless `PRODUCTION=true`.

## Frontend contract

Data is intentionally split across four read shapes, mirrored by both the live API and the snapshot JSON files in `public/roundtable-archive/`:

| Endpoint | Snapshot file | Use |
|---|---|---|
| `GET /weekly/current` | `current.json` | featured weekly hero |
| `GET /weekly/archive` | `archive.json` | curated weekly archive |
| `GET /sessions/recent` | `recent.json` | ad-hoc live sessions |
| `GET /api/replay/{id}` | `replay/{id}.json` | full transcript + audio + summary + propaganda metadata |

`scripts/snapshot-roundtable.mjs` regenerates these from a running backend. Replay audio is generated lazily in `/api/replay` via `app/audio.py` (per-actor TTS voices; OpenAI / ElevenLabs / edge-tts).

The satire module has its own snapshot path: `scripts/snapshot-satire.mjs` + `scripts/pack-satire.ps1` / `publish-satire.ps1` build and publish `public/satire-archive/`.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the API:

```powershell
uvicorn app.main:app --reload
# or, matching CONTRIBUTING.md / production:
.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

- Docs: `http://127.0.0.1:8000/docs`
- Test UI: `http://127.0.0.1:8000/test`
- Roundtable stage UI: `http://127.0.0.1:8000/roundtable`, `/stage`

Without `OPENROUTER_API_KEY`, everything still runs on deterministic fallbacks — useful for testing the flow offline.

## Environment variables (`.env` at project root)

| Var | Purpose |
|---|---|
| `OPENROUTER_API_KEY` | Gates the whole LLM path; unset = deterministic fallback everywhere |
| `OPENROUTER_MODEL_{CHINA,US,EU,RECAP,PULSE,JAMES,HALCYON_FALLBACK}` | Per-role model overrides |
| `IMAGE_PROVIDER_{CHINA,US,EU}` / `IMAGE_MODEL_{CHINA,US,EU}` / `IMAGE_FALLBACK_MODEL_{CHINA,US,EU}` | Per-actor image generation routing (propaganda-lab) |
| `MIRROR_VISUAL_MODEL` | Image model for mirror-world visuals |
| `OPENAI_API_KEY` / `TOGETHER_API_KEY` / `SILICONFLOW_API_KEY` | Image provider credentials |
| `HALCYON_MODEL` / `HALCYON_BASE_URL` / `HALCYON_API_KEY` / `HALCYON_LEDGER_PATH` | Halcyon's separate CERIT-hosted model + ledger location |
| `ELEVENLABS_API_KEY` / `OPENAI_TTS_MODEL` / `TTS_SERVICE` | Replay/satire audio (TTS) |
| `ROUNDTABLE_OPERATOR_TOKEN` | Required header value (`X-Roundtable-Token`) for all live mutating endpoints |
| `API_TOKEN` | Bearer token for `verify_token`-guarded endpoints (no-op unless `PRODUCTION=true`) |
| `DATABASE_URL` | SQLAlchemy DB URL, defaults to `sqlite:///./sessions.db` |
| `PRODUCTION` | `true` restricts CORS and enforces `verify_token` |

## Weekly roundtable generation

```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/session/scheduled/sync" -Headers @{"X-Roundtable-Token"="$env:ROUNDTABLE_OPERATOR_TOKEN"}
```

This runs the full pipeline server-side (3 actors × LLM turns + images) and can take minutes — prefer letting the Lovable frontend trigger it over blocking a client call on it.

## Refreshing the knowledge base

```powershell
python scripts/run_news_ingest.py --days 3 --max-per-query 5 --build-manifest
python scripts/build_ingest_manifest.py
```

Writes `sessions/ingest-manifest.md`. Review it, then hand-synthesize the relevant items into `wiki/` — dropping files into `raw/` alone changes nothing (see above). `--focus "<topic>"` promotes a weekly issue to the top of the manifest and saves matching items under `raw/focus-issues/<slug>/`.

## Refreshing frontend snapshots

```powershell
node scripts/snapshot-roundtable.mjs
# from a tunnel instead of localhost:
$env:ROUNDTABLE_BASE_URL="https://your-ngrok-url.ngrok-free.app"; node scripts/snapshot-roundtable.mjs
```

## Operator references

For prose-level operational docs (prompts, control surface, propaganda-lab, mirror-world, threat-intel feed, Lovable wiring), see `wiki/ops/` — especially:

- `agent-simulation-control-surface.md`
- `propaganda-lab-mode.md`
- `mirror-world-mode.md`
- `threat-intel-feed-integration.md`
- `knowledge-base-refresh-workflow.md`
- `lovable-connection-guide.md`, `lovable-roundtable-ui-spec.md`, `lovable-satire-integration.md`, `lovable-roster-whos-who.md`

See also `CONTRIBUTING.md` for repo hygiene notes.

## Current limitations

- No test suite, linter, or build step — "building a round" means starting a session via the API
- In-memory session state is lost on backend restart (DB-backed reads like replay/weekly survive; live mutation on that session does not)
- Deterministic fallback turns are extractive/heuristic, meant for testing the flow, not for real argumentative quality
