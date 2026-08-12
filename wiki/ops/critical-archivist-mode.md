# The Critical Archivist

> Updated: 2026-08-12

## Purpose

The Critical Archivist is a summonable meta-agent (same shape as Halcyon and James: a guest voice, never part of the china/us/eu round-robin). Its object of intervention is the archive itself — the wiki knowledge bases, transcripts, metadata, and retrieval conventions that condition what the other agents can know and say. Its premise: no archive is innocent; the archive precedes the utterance. Its goal is not a perfect archive but to make archival power perceptible.

Two honesty rules are enforced in code (`app/archivist.py`):

- **Reorganizations are real.** Every archival logic is computed over the actual wiki corpus on disk (folders, byte sizes, the link graph, lexicon counts). When the Archivist says a page rises or sinks under an order, that is a measured fact.
- **Opaque logics are labeled.** Logics flagged `experimental` are surfaced to the model with an instruction to present them as experimental or computational artifacts, never as revealed truth.

## Knowledge base

The agent grounds itself in `wiki/critical-archives/` — synthesized source notes from the critical archival studies corpus (Derrida's *Archive Fever*, Mbembe, Schwartz & Cook, Stoler, Caswell, Appadurai, Zinn, Samuels, Ketelaar, Bastian, Fritzsche, Anderson, Hodder & Krishnan, Terry Cook), plus two operational pages: the repertoire of archival logics and a bridge page applying archive theory to machine memory and this simulation itself. Raw extractions live in `raw/archivist/` (built with `scripts/extract_pdfs_to_markdown.py` from the PDF corpus).

This folder is deliberately NOT in `ACTOR_HUBS`/`ALLOWED_PATH_PREFIXES` — the state actors cannot read it, and the Archivist loads it directly via `ARCHIVIST_HUB_DIR`.

## The repertoire of archival logics

Each summons applies the next logic in rotation (or a forced one). Keys:

`chronology`, `geography`, `citation-gravity`, `threat-vocabulary`, `inevitability`, `mass` (bytes), `brevity`, `interrogative` (question density), `absence` (least-linked pages first), `shuffle` (deterministic control condition).

`mass`, `brevity`, `interrogative`, and `shuffle` are flagged experimental.

## Endpoints

```powershell
# Summon mid-debate (operator token required). Rotates logics per summons.
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/session/<id>/summon-archivist" -Headers @{"X-Roundtable-Token"=$env:ROUNDTABLE_OPERATOR_TOKEN}

# Force a specific logic
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/session/<id>/summon-archivist?logic=absence" -Headers @{"X-Roundtable-Token"=$env:ROUNDTABLE_OPERATOR_TOKEN}

# Public: browse the census under any logic (for a frontend shelf view)
Invoke-RestMethod -Uri "http://127.0.0.1:8000/archivist/catalog?logic=threat-vocabulary"

# The Archivist reads the roundtable's OWN archive (past sessions from the DB):
# who spoke how much, which modes dominate, what was argued but never summarized,
# which prompt vocabulary recurs — and names a forgotten session to reintroduce.
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8000/archivist/retrospective?limit=25" -Headers @{"X-Roundtable-Token"=$env:ROUNDTABLE_OPERATOR_TOKEN}
```

## When to summon it

- **Mid-debate (primary use):** right after an actor presents an archival effect as a self-evident fact. The turn prompt makes the Archivist name one claim just made that depends on the current arrangement, and end on a pointed question to a specific actor. The state actors' `guest_directive` forces them to engage with it on their next turn instead of resuming their argument.
- **End of session:** summon it once as the final turn before `/summary`; its closing intervention and `metadata.logic` ride into the replay.
- **Between sessions:** `/archivist/retrospective` for its reading of the accumulated session archive.

## Turn metadata

Each summoned message carries `metadata`: `format: "archivist-intervention"`, `logic`, `logic_label`, `experimental`, and the real `foreground`/`suppressed` page lists — enough for the frontend to render a "reorganized shelf" card next to the spoken turn.

## Models and fallback

LLM path uses `OPENROUTER_MODEL_ARCHIVIST` (defaults to the recap model). Offline or on failure it falls back to a deterministic turn composed entirely from the computed census — honest by construction, so unlike James the Archivist always has something true to say. TTS voice is defined in `ACTOR_VOICES["archivist"]` (dry, precise, faintly amused).
