# Lovable update prompt — 2026-08-13 (The Critical Archivist + clearer summon controls)

Paste this whole block into Lovable in one go.

---

One new guest voice for the AI Cold War roundtable frontend, plus a clearer summon UX: **The Critical Archivist**, a meta-agent that interrogates the archive the debate runs on. It really reorganizes the backend's knowledge corpus by a rotating "archival logic" (chronology, geography, threat-vocabulary, byte mass, absence of links, deterministic shuffle...) and confronts the room with what each new order foregrounds and buries. Four additions:

**0. Group the live-session operator controls** so it's obvious what summons a guest vs. what controls the flow: a labeled **Summon** group holding 🕊 Halcyon, 🗂 Archivist, 🃏 James (each with a tooltip: guests speak once and do not consume the actors' turn order), separate from pause/skip and from the Human point / Shock injections. If James has no mid-debate button yet, add one calling `POST /session/{id}/summon-james` (operator token; no fallback — on error show a plain error state, never a canned line).

**1. Add the "Summon Archivist" control with a logic picker.** Clicking 🗂 Archivist opens a small picker: default option "Auto — next logic in rotation (recommended)" plus the full repertoire fetched from public `GET /archivist/catalog` (`logics`: array of `{key, label, note, experimental}` — mark experimental ones 🧪 and show the note under the picker; never hardcode the list client-side). Summon calls `POST /session/{id}/summon-archivist` (operator token header; append `?logic=<key>` only when a specific logic was chosen). Render the returned message as an archivist turn (see 2). Suggested styling: parchment/amber accent (`#d4b26a` on dark), 🗂 icon, label "The Critical Archivist". On non-200, show a plain error state — never fabricate a line.

**2. Render archivist turns with their "reorganized shelf" card.** Archivist messages have `actor: "archivist"` and `metadata.format == "archivist-intervention"`, in both live turns and `/api/replay/{id}` events. Alongside the spoken `content`, use the metadata to render a small card:
- `metadata.logic_label` as the card title (e.g. "Absence, the least-linked and least-reachable pages first")
- if `metadata.experimental` is true, add a small badge: "experimental ordering — computational artifact, not revealed truth"
- `metadata.foreground` (array of strings) as a short "rises to the front" list
- `metadata.suppressed` (array of strings) as a "sinks out of reach" list
These lists are real measurements of the backend corpus, not flavor text — present them as data, not decoration.

**3. The roster updates itself.** `GET /roster` already includes the archivist entry (`type: "guest"`), so the Who's Who screen needs no changes if it renders from the endpoint.

**4. Add an upcoming-event banner.** Fetch public `GET /event` (no auth; returns `{event: {format, location, sessions, timezone}}`) and render it prominently in the site header or hero, e.g. "📅 Roundtable — Thursday 10 September, 9:00–10:30 (Europe/Warsaw) · C-7, room 3.09". Always render from the endpoint, never hardcode the copy — the backend is the single source of truth and the next event updates automatically.

Optional, only if it fits the design: an "Archive shelf" viewer using public `GET /archivist/catalog?logic=<key>` — it returns `logics` (the full repertoire with labels and notes, for a picker), `applied` (foreground/suppressed under the chosen logic), and `census` (one row per corpus page with folder, bytes, words, link counts). A simple two-panel layout — logic picker left, foreground/suppressed right — makes the archive's politics browsable between sessions. There is also an operator-only `POST /archivist/retrospective` where the Archivist reads the whole database of past sessions back (word counts per actor, recurring prompt vocabulary, sessions never summarized) and names a forgotten session to revive; render `reading` as a quote block above a small stats strip from `census` if you want a "state of the archive" screen.
