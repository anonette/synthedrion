# Lovable Frontend Package

This folder is a frontend-ready scaffold for the weekly roundtable fallback files.

## What This Is

The actual generated snapshot data currently lives in:

- `public/roundtable-archive/current.json`
- `public/roundtable-archive/archive.json`
- `public/roundtable-archive/replay/*.json`

This package exists so you have a clear target structure for the real Lovable/frontend repo, even though that repo is not present in this workspace.

## Folder Structure The Frontend Needs

```text
public/
  roundtable-archive/
    current.json
    archive.json
    replay/
      <session_id>.json
```

## What To Copy Later

When you identify or create the actual frontend repo used by Lovable, copy:

- `C:\dev\AIcoldWar2026\public\roundtable-archive`

into:

- `<frontend-repo>\public\roundtable-archive`

## Current Status

The snapshot files already exist in this backend workspace.
What does not yet exist is the separate frontend repo that should publish them.
