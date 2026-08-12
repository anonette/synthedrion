# Lovable update prompt — 2026-08-12 (The Critical Archivist)

Paste this whole block into Lovable in one go.

---

One new guest voice for the AI Cold War roundtable frontend: **The Critical Archivist**, a meta-agent that interrogates the archive the debate runs on. It really reorganizes the backend's knowledge corpus by a rotating "archival logic" (chronology, geography, threat-vocabulary, byte mass, absence of links, deterministic shuffle...) and confronts the room with what each new order foregrounds and buries. Three additions:

**1. Add a "Summon Archivist" control to the live session operator bar**, next to the existing Summon Halcyon / Summon James buttons. It calls `POST /session/{id}/summon-archivist` (operator token header, same as the other summons; optional `?logic=<key>` to force a specific logic — omit it and the backend rotates through the repertoire automatically). Render the returned message as an archivist turn (see 2). Suggested styling: parchment/amber accent (`#d4b26a` on dark), 🗂 icon, label "The Critical Archivist". On non-200, show a plain error state — never fabricate a line.

**2. Render archivist turns with their "reorganized shelf" card.** Archivist messages have `actor: "archivist"` and `metadata.format == "archivist-intervention"`, in both live turns and `/api/replay/{id}` events. Alongside the spoken `content`, use the metadata to render a small card:
- `metadata.logic_label` as the card title (e.g. "Absence, the least-linked and least-reachable pages first")
- if `metadata.experimental` is true, add a small badge: "experimental ordering — computational artifact, not revealed truth"
- `metadata.foreground` (array of strings) as a short "rises to the front" list
- `metadata.suppressed` (array of strings) as a "sinks out of reach" list
These lists are real measurements of the backend corpus, not flavor text — present them as data, not decoration.

**3. The roster updates itself.** `GET /roster` already includes the archivist entry (`type: "guest"`), so the Who's Who screen needs no changes if it renders from the endpoint.

Optional, only if it fits the design: an "Archive shelf" viewer using public `GET /archivist/catalog?logic=<key>` — it returns `logics` (the full repertoire with labels and notes, for a picker), `applied` (foreground/suppressed under the chosen logic), and `census` (one row per corpus page with folder, bytes, words, link counts). A simple two-panel layout — logic picker left, foreground/suppressed right — makes the archive's politics browsable between sessions. There is also an operator-only `POST /archivist/retrospective` where the Archivist reads the whole database of past sessions back (word counts per actor, recurring prompt vocabulary, sessions never summarized) and names a forgotten session to revive; render `reading` as a quote block above a small stats strip from `census` if you want a "state of the archive" screen.
