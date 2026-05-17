# AI Cold War 2026

This repository currently contains:

- `raw/`: source material
- `wiki/`: actor and shared knowledge bases
- `app/`: a minimal local runtime for testing live actor sessions

## Project Structure

- `app/` - backend runtime, orchestration, image generation, audio generation
- `wiki/` - the live knowledge base that agents actually read
- `raw/` - source documents waiting to be synthesized into the wiki
- `scripts/` - utility scripts for ingest, snapshots, and imports
- `public/roundtable-archive/` - frontend snapshot fallback JSON
- `sessions/` - local generated memos, replay audio, and ingest manifests
- `lovable-frontend-package/` - scaffold for eventual frontend-side static asset packaging

See also:

- `CONTRIBUTING.md`

## Run the local runtime

Create and activate a virtual environment, then install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run the API:

```powershell
uvicorn app.main:app --reload
```

Open the docs at:

- `http://127.0.0.1:8000/docs`

Open the simple local test page at:

- `http://127.0.0.1:8000/test`

## What this test runtime does

- loads actor hub pages directly from the wiki
- follows allowed wiki links inside actor and shared scopes
- starts synchronous live sessions
- runs as an alternating dialogue where one actor speaks and the next responds
- supports human intervention and shocks
- returns simple grounded actor turns
- generates summaries and wiki proposals

## Optional: enable real per-actor models through OpenRouter

Set your API key before starting the server:

```powershell
$env:OPENROUTER_API_KEY="your_key_here"
```

Optional model overrides:

```powershell
$env:OPENROUTER_MODEL_CHINA="deepseek/deepseek-chat-v3-0324"
$env:OPENROUTER_MODEL_US="openai/gpt-4.1-mini"
$env:OPENROUTER_MODEL_EU="mistralai/mistral-large-2411"
```

Default routing is already:

- China -> DeepSeek
- U.S. -> OpenAI
- EU -> Mistral

Without `OPENROUTER_API_KEY`, the backend falls back to deterministic local heuristic turns for testing.

## Operator Access For Lovable

The weekly roundtable frontend can expose public archive browsing while requiring an operator token for live session actions.

Set this before starting the backend:

```powershell
$env:ROUNDTABLE_OPERATOR_TOKEN="your-shared-secret"
```

Protected mutating endpoints now require the header `X-Roundtable-Token`:

- `POST /session/start`
- `POST /session/message`
- `POST /session/intervene`
- `POST /session/shock`
- `POST /session/{session_id}/summary`
- `POST /session/{session_id}/wiki-proposals`

Public endpoints remain readable without the operator token:

- `GET /health`
- `GET /weekly/current`
- `GET /weekly/archive`
- `GET /session/{session_id}`
- `GET /api/replay/{session_id}`

Example:

```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/session/start" `
  -Headers @{"X-Roundtable-Token"="your-shared-secret"} `
  -ContentType "application/json" `
  -Body '{"prompt":"test","actors":["china","us","eu"],"mode":"debate","include_shared":true,"auto_generate_opening_turn":true}'
```

## Weekly Roundtable Endpoints

The backend now supports a featured weekly session and archive browsing for Lovable:

- `GET /weekly/current`
- `GET /weekly/archive?limit=12&offset=0`
- `GET /weekly/{week_key}`
- `GET /api/replay/{session_id}`

Weekly sessions are persisted in the same session store as live runs, but are tagged with weekly metadata such as `week_key`, `week_start`, `title`, `theme`, and `is_featured`.

To generate the current featured weekly session locally:

```powershell
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/session/scheduled/sync"
```

## Snapshot Fallback For Lovable

To publish a static fallback of the current weekly archive and replay payloads:

```powershell
Set-Location "C:\dev\AIcoldWar2026"
node scripts/snapshot-roundtable.mjs
```

This writes:

- `public/roundtable-archive/current.json`
- `public/roundtable-archive/archive.json`
- `public/roundtable-archive/recent.json`
- `public/roundtable-archive/replay/<session_id>.json`

To snapshot from a public tunnel instead of localhost:

```powershell
$env:ROUNDTABLE_BASE_URL="https://your-ngrok-url.ngrok-free.app"
node scripts/snapshot-roundtable.mjs
```

Lovable can use these files as a read-only fallback when the live backend is unavailable.

Use the endpoints like this:

- `GET /weekly/current` for the featured weekly session
- `GET /weekly/archive` for the curated weekly archive
- `GET /sessions/recent` for recent live and weekly sessions

Suggested frontend behavior:

- use `weekly/current` for the main hero session
- use `weekly/archive` for official previous weeks
- use `sessions/recent` for ad hoc live sessions that should appear quickly without being promoted into the weekly archive

## Refreshing The Knowledge Base

Important: adding files to `raw/` does not automatically change the agents.

The agents read `wiki/` at runtime, so new source files only affect behavior after the relevant wiki pages are updated to incorporate them.

Fast workflow:

1. Add new source files under `raw/`
2. Build an ingest manifest:

```powershell
python scripts/build_ingest_manifest.py
```

3. Review:

- `sessions/ingest-manifest.md`

4. Ask for a wiki update pass using those files
5. Start a new round
6. Regenerate snapshots if needed

See also:

- `wiki/ops/knowledge-base-refresh-workflow.md`

## Propaganda Lab Poster Dialogue

`propaganda-lab` now supports a poster-dialogue style exchange instead of only long-form rhetoric.

When this mode is active, agent turns may include structured metadata with:

- `format`
- `slogan`
- `commentary`
- `image_prompt`
- `image_url`
- `image_provider`
- `image_model`
- `image_status`
- `response_target`
- `intended_image_stack`

Live session messages include this data under `message.metadata`.
Replay payloads include the same data under `event.metadata` from `GET /api/replay/{session_id}`.

The intended frontend behavior is to render propaganda turns as poster cards rather than normal transcript bubbles.

## Lovable connection

See:

- `wiki/ops/lovable-connection-guide.md`
- `wiki/ops/lovable-page-build-steps.md`

## Current limitations

- no external LLM integration yet
- turn generation is deterministic and extractive, intended only for testing the runtime flow
- no persistent database, sessions are kept in memory for now
