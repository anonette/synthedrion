# Knowledge Base Refresh Workflow

> Updated: 2026-05-16

## Core Rule

Adding PDFs, markdown files, or other sources under `raw/` does **not** automatically change agent behavior.

The runtime reads:

- actor hub pages in `wiki/`
- linked wiki pages reachable from those hubs
- extracted notes from those wiki pages at session start

So the actual path is:

1. add source to `raw/`
2. update or create wiki pages that cite and synthesize that source
3. start a new session
4. the agents then pick up the updated wiki material automatically

## What Changes Behavior Immediately

The following changes affect the next new round automatically:

- editing actor hub pages
- editing linked actor-specific wiki pages
- editing linked shared wiki pages
- adding newly linked wiki pages inside the allowed actor/shared read graph

No backend rebuild is required for this. A new session is enough, because session start reloads the wiki live.

## What Does Not Change Behavior By Itself

These actions alone do not change the agents:

- dropping a PDF into `raw/`
- adding an article into `raw/articles/`
- adding a regulation into `raw/reg-documents/`
- adding a file into `raw/rand/`

Those files only become behaviorally active after wiki pages are updated to incorporate them.

## Recommended Manual Instruction

When you add new source files, use an instruction like this:

```text
Ingest these new raw files into the knowledge base.
Update the relevant actor and shared wiki pages.
Then start a fresh round so the new material is reflected in agent behavior.

Files:
- raw/articles/...
- raw/reg-documents/...
- raw/rand/...
```

## Recommended Fast Instruction

If you want the shortest working instruction, use:

```text
Add these new raw files to the wiki knowledge base, update the affected actor/shared pages, and make sure the next rounds use them.
```

## Repeatable Refresh Loop

1. Place new sources into the correct `raw/` folder.
2. Run the ingest manifest helper:

```powershell
python scripts/build_ingest_manifest.py
```

3. Review the generated manifest:

- `sessions/ingest-manifest.md`

4. Use that manifest as the instruction payload for a wiki update pass.
5. Start a new live or weekly session.
6. If needed, regenerate snapshots:

```powershell
node scripts/snapshot-roundtable.mjs
```

## Automatable Parts

Automatable now:

- detecting new files in `raw/`
- generating an ingest manifest
- starting a fresh weekly round
- regenerating archive snapshots

Not fully automated yet:

- interpreting the new documents correctly
- deciding which wiki pages need substantive changes
- writing the new synthesis into the wiki with judgment

That synthesis step still needs an explicit update pass, whether done by a human or by me.

## Suggested Future Automation

The best long-term workflow is:

1. `raw/inbox/` or normal `raw/` folders receive new files
2. helper script builds an ingest manifest
3. an ingest pass updates wiki pages
4. a scheduled or manual run creates a fresh session
5. snapshots are regenerated for the frontend

## See Also

- [Roundtable Frontend Contract](roundtable-frontend-contract.md)
- [Local Agent Runtime Architecture](local-agent-runtime-architecture.md)
- [China Agent Evolution Workflow](../china-ai-policy/china-agent-evolution-workflow.md)
- [Manual Upload Needed](../manual-upload-needed.md)
