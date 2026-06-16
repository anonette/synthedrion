# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A local FastAPI runtime that simulates a geopolitical "AI Cold War" roundtable between three actors — `china`, `us`, `eu` — who argue, negotiate, and generate propaganda based on a markdown knowledge base. The backend serves a Lovable frontend (live API + static snapshot fallback).

## Commands

```powershell
# Setup
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

# Run the API (docs at http://127.0.0.1:8000/docs, test UI at /test)
uvicorn app.main:app --reload
# or, matching CONTRIBUTING.md:
.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000

# Generate a weekly featured session locally (needs operator token, see below)
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/session/scheduled/sync" -Headers @{"X-Roundtable-Token"="$env:ROUNDTABLE_OPERATOR_TOKEN"}

# Refresh static frontend fallback JSON (reads from a running backend)
node scripts/snapshot-roundtable.mjs
# Snapshot from a tunnel instead of localhost:
$env:ROUNDTABLE_BASE_URL="https://your-ngrok-url.ngrok-free.app"; node scripts/snapshot-roundtable.mjs

# News ingest + manifest building (writes into raw/ and sessions/)
python scripts/run_news_ingest.py --days 3 --max-per-query 5 --build-manifest
python scripts/build_ingest_manifest.py
```

There is **no test suite, linter, or build step** configured. "Building a round" means starting a session via the API, not compiling anything.

## The central data-flow rule

Three layers feed agent behavior, and the boundary between them is the thing most likely to trip you up:

- `raw/` — source documents (articles, reg-documents, RAND papers, news ingest). **Agents never read `raw/` at runtime.**
- `wiki/` — the markdown knowledge base agents actually load. **This is the only layer that changes behavior.**
- `app/` — the runtime that loads wiki pages and generates turns.

Dropping files into `raw/` does nothing until the relevant `wiki/` pages are edited to incorporate them. The intended workflow is: collect into `raw/` → build a manifest (`scripts/build_ingest_manifest.py` → `sessions/ingest-manifest.md`) → hand-synthesize into `wiki/` → start a new session.

## How the wiki is loaded (app/wiki_loader.py + app/config.py)

At session start, each actor loads its **hub page** (`ACTOR_HUBS` in `config.py`) plus the shared hub, then follows markdown links breadth-first. Link-following is sandboxed: a page is only loaded if it lives under that actor's `ALLOWED_PATH_PREFIXES` (its own policy folder + `shared-ai-geopolitics` + `geopolitics` + `ai-governance`). `extract_notes()` then scrapes prose/bullet lines into short "source notes" (capped at 40/actor), which become the grounding context fed to the model. So **adding a wiki page only affects an actor if it is reachable by a link from that actor's hub and inside its allowed prefixes.**

## Turn generation: LLM path vs deterministic fallback

Every turn has two code paths, selected by `openrouter_enabled()` (true iff `OPENROUTER_API_KEY` is set):

- **LLM path** — `app/llm.py` builds per-actor system/user prompts (`ACTOR_PROMPT_PROFILES`, `MODE_PROMPT_GUIDANCE`) and calls OpenRouter with a **per-actor model** (`ACTOR_MODELS`: China→DeepSeek, US→OpenAI, EU→Mistral). If the call throws, it falls back to the deterministic path with the error inlined.
- **Deterministic path** — `app/agent_logic.py` produces extractive, heuristic turns from the source notes with no network call. This is the default when no API key is present.

`propaganda-lab` mode is a third shape: it returns structured JSON (`slogan`, `image_prompt`, `artifact_type`, etc.), then `app/images.py` generates an image (per-actor image model with a Pollinations URL fallback). This metadata rides along on `message.metadata` and replay `event.metadata`; the frontend renders these as poster cards.

`app/main.py::_generate_session_turn` is the single funnel that all of the above flows through.

## Session persistence — two stores, and they are not equivalent

- **In-memory** `SESSIONS` dict (`app/session_store.py`) — the live working copy. All mutating endpoints (`/session/message`, `/intervene`, `/shock`, `/summary`, `/wiki-proposals`) read from here, so **they only work for sessions still in memory; a server restart loses them.**
- **Database** (`app/database.py`, SQLAlchemy) — `DATABASE_URL` env var, defaults to `sqlite:///./sessions.db`. Every mutation also persists here via `_persist_session_state`. `/api/replay/{id}` and all `/weekly/*` and `/sessions/recent` reads come from the DB (replay falls back to memory). `init_db()` runs additive `ALTER TABLE` migrations on startup for the weekly columns.

Weekly sessions are ordinary sessions in the same table tagged `session_type="weekly"` with `week_key`, `week_start`, `is_featured_weekly`, `title`, `theme`. Only one can be featured at a time (`clear_featured_weekly`).

## Auth — two independent schemes

- `require_roundtable_operator` — guards live mutating session endpoints. Requires the `X-Roundtable-Token` header to equal `ROUNDTABLE_OPERATOR_TOKEN`. Always enforced (even in dev) once the env var is set; returns 500 if the env var is unset.
- `verify_token` — Bearer-token guard on `/health/detailed`, `/session/scheduled*`, `/session/test`. **No-op in development** (returns a stub unless `PRODUCTION=true`), then checks against `API_TOKEN`.

Public/read endpoints (`/health`, `/weekly/*`, `/sessions/recent`, `/session/{id}`, `/api/replay/{id}`) are unauthenticated. CORS allows all origins unless `PRODUCTION=true`.

## Frontend contract

Data is intentionally split across four read shapes, mirrored by both the live API and the snapshot JSON files in `public/roundtable-archive/`:

| Endpoint | Snapshot file | Use |
|---|---|---|
| `GET /weekly/current` | `current.json` | featured weekly hero |
| `GET /weekly/archive` | `archive.json` | curated weekly archive |
| `GET /sessions/recent` | `recent.json` | ad-hoc live sessions |
| `GET /api/replay/{id}` | `replay/{id}.json` | full transcript + audio + summary + propaganda metadata |

`scripts/snapshot-roundtable.mjs` regenerates these from a running backend. Replay audio is generated lazily in `/api/replay` via `app/audio.py` (per-actor TTS voices; OpenAI / ElevenLabs / edge-tts).

## Config & secrets

All runtime config is environment-driven (`app/config.py`, loaded from `.env` at project root). Notable vars: `OPENROUTER_API_KEY` (gates the whole LLM path), `OPENROUTER_MODEL_{CHINA,US,EU}`, `IMAGE_MODEL_*`, `OPENAI_API_KEY` / `TOGETHER_API_KEY` / `SILICONFLOW_API_KEY` (image providers), `ELEVENLABS_API_KEY` (TTS), `ROUNDTABLE_OPERATOR_TOKEN`, `API_TOKEN`, `DATABASE_URL`, `PRODUCTION`. Without `OPENROUTER_API_KEY` everything still runs on deterministic fallbacks — useful for testing the flow offline.

## Operator references

For the prose-level operational docs (prompts, control surface, propaganda-lab, Lovable wiring), see `wiki/ops/` — especially `agent-simulation-control-surface.md`, `propaganda-lab-mode.md`, `knowledge-base-refresh-workflow.md`, and the `lovable-*` guides.
