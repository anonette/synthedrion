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

## How The System Works

This project has four main layers:

1. `raw/`
- source material collected from articles, PDFs, policy documents, news ingest, and manual uploads

2. `wiki/`
- the actual knowledge base the agents read at runtime
- this is the layer that changes agent behavior

3. `app/`
- the simulation runtime
- loads actor-specific and shared wiki pages
- generates live sessions, weekly sessions, propaganda sessions, replay, images, and audio

4. `public/roundtable-archive/`
- static snapshot fallback for the frontend
- used when the live backend is unavailable

The important rule is:

- adding files to `raw/` does not automatically change the agents
- updating `wiki/` does

So the real flow is:

1. collect sources into `raw/`
2. synthesize them into the relevant `wiki/` pages
3. start a new round
4. optionally refresh frontend snapshots

## The End-To-End Workflow

### 1. Add Source Material

Put new files into one of:

- `raw/articles/`
- `raw/reg-documents/`
- `raw/rand/`
- `raw/focus-issues/<weekly-theme>/`

You can also use:

```powershell
python scripts/run_news_ingest.py --days 3 --max-per-query 5 --build-manifest
```

Or with a weekly focus:

```powershell
python scripts/run_news_ingest.py --days 3 --focus "petrodollars AI geopolitics Gulf sovereign wealth compute" --build-manifest
```

### 2. Build The Ingest Manifest

Run:

```powershell
python scripts/build_ingest_manifest.py
```

Useful variants:

```powershell
python scripts/build_ingest_manifest.py --days 3
python scripts/build_ingest_manifest.py --since 2026-05-20
python scripts/build_ingest_manifest.py --reset-state
```

This writes:

- `sessions/ingest-manifest.md`

If a weekly focus issue exists, it is promoted to the top of the manifest under:

- `## Weekly Focus Priority`

### 3. Update The Wiki Knowledge Base

After you have raw files and a manifest, the next step is to update the `wiki/` so the agents actually change.

### 4. Start A New Simulation Round

Once the wiki is updated, start a new round:

- live session
- propaganda-lab session
- scheduled weekly session

Because the runtime reads the wiki at session start, the new behavior takes effect in the next round automatically.

### 5. Refresh Frontend Snapshots

If you want Lovable or other frontend fallback data updated:

```powershell
node scripts/snapshot-roundtable.mjs
```

This writes:

- `public/roundtable-archive/current.json`
- `public/roundtable-archive/archive.json`
- `public/roundtable-archive/recent.json`
- `public/roundtable-archive/replay/<session_id>.json`

## Prompts To Use

### Add New Sources To The Wiki

```text
Ingest these new raw files into the knowledge base.
Update the relevant actor and shared wiki pages.
Then start a fresh round so the new material is reflected in agent behavior.
```

### Add New Sources With Explicit File List

```text
Ingest these new raw files into the knowledge base.
Update the relevant actor and shared wiki pages.
Then start a fresh round so the new material is reflected in agent behavior.

Files:
- raw/articles/...
- raw/reg-documents/...
- raw/rand/...
```

### Prioritize A Weekly Issue

```text
Ingest the files from sessions/ingest-manifest.md, especially the focus issue folder under raw/focus-issues/, into the knowledge base and make that weekly issue influence the next round.
```

### Update One Actor Specifically

```text
Update the [China / U.S. / EU] agent behavior based on these sources.
Change what the actor wants, fears, treats as legitimate action, and how it talks.
Also update propaganda motifs if relevant.
```

### Tune Propaganda-Lab

```text
Make propaganda-lab less repetitive and more surprising.
Let each turn choose the most effective propaganda artifact type while preserving bloc-specific political identity.
```

### Promote A Session To Featured Weekly

```text
Promote session <session_id> to this week's featured roundtable and regenerate snapshots.
```

### Refresh The Frontend Fallback

```text
Regenerate the public roundtable snapshots so weekly current, archive, recent live sessions, and replay payloads match the latest backend state.
```

## Which Files Actually Matter For Agent Behavior

Most important:

- actor hub pages in `wiki/`
- linked actor pages in `wiki/china-ai-policy/`, `wiki/us-ai-policy/`, `wiki/eu-ai-policy/`
- linked shared pages in `wiki/shared-ai-geopolitics/` and related folders
- prompt logic in `app/llm.py`

Not enough by itself:

- dropping PDFs or news directly into `raw/`

## Which Session Feeds The Frontend Should Use

Frontend data is intentionally split:

- `GET /weekly/current`
  - featured weekly session

- `GET /weekly/archive`
  - curated weekly archive

- `GET /sessions/recent`
  - recent live and ad hoc sessions

- `GET /api/replay/{session_id}`
  - full replay, summary, wiki proposals, replay audio, propaganda metadata

Snapshot fallback mirrors this split:

- `current.json`
- `archive.json`
- `recent.json`
- `replay/{session_id}.json`

## Propaganda-Lab In One Sentence

`propaganda-lab` is a dynamic propaganda-artifact mode where agents can produce posters, memes, TikTok-style stills, campaign ads, infographics, hostile remixes, and soft-power imagery rather than only long-form policy argument.

## Review Surfaces

If you want a compact operator reference:

- `wiki/ops/agent-prompts-only.md`
- `wiki/ops/agent-simulation-control-surface.md`
- `wiki/ops/propaganda-lab-mode.md`

## Future Wishlist

- add a second-stage `llama_index`-based document synthesis layer for deeper PDF/DOCX parsing, chunking, extraction, and semi-automatic wiki update assistance after raw ingestion

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

## News Ingest

Manual-first news ingest is available for geopolitics, China, U.S., EU, regulation, industry actors, and open-source/open-weight model coverage.

Run:

```powershell
python scripts/run_news_ingest.py --days 3 --max-per-query 5 --build-manifest
```

This will:

1. search recent web results using Tavily and SerpAPI
2. save normalized files directly into `raw/articles/` or `raw/reg-documents/`
3. write `sessions/news-ingest-report.md`
4. optionally rebuild `sessions/ingest-manifest.md`

Use `--topics` to narrow scope, for example:

```powershell
python scripts/run_news_ingest.py --topics open-models,policy,industry
```

Use `--focus` when there is a specific issue you care about that week, for example:

```powershell
python scripts/run_news_ingest.py --days 3 --focus "Manus Meta acquisition China security review" --build-manifest
```

The ingest now applies relevance filtering to reduce generic market and low-signal items.

When `--focus` is used, the matching focus-specific items are saved under:

- `raw/focus-issues/<focus-slug>/`

This makes it easier to track a special weekly issue that should influence the broader wiki update pass.

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
