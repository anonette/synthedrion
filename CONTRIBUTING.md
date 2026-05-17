# Contributing

## Project Layout

- `app/` - FastAPI runtime, session logic, model routing, image and audio generation
- `wiki/` - actor and shared knowledge base used at runtime
- `raw/` - source materials that must be synthesized into `wiki/` before they affect agents
- `scripts/` - local helper scripts for snapshots, Drive downloads, and ingest manifests
- `public/roundtable-archive/` - static fallback JSON for the frontend
- `sessions/` - local generated artifacts and ingest manifests

## Important Rules

1. Adding files to `raw/` does not change agent behavior by itself.
2. Update `wiki/` pages to make new source material active in future rounds.
3. Use `python scripts/build_ingest_manifest.py` to prepare ingest work.
4. Use `node scripts/snapshot-roundtable.mjs` to refresh frontend fallback snapshots.

## Local Runtime

Start the backend with:

```powershell
.venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

If operator-gated frontend actions are needed:

```powershell
$env:ROUNDTABLE_OPERATOR_TOKEN="your-token"
```

## Git Hygiene

The repo ignores:

- `.env`
- `.venv/`
- local databases
- generated session folders
- audio artifacts

Useful generated files that remain trackable:

- `public/roundtable-archive/`
- `sessions/ingest-manifest.md`
- `sessions/ingest-manifest-state.json`
