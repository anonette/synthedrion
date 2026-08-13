# Lovable update prompt — 2026-08-13 (layout cleanup, event banner, notebook dedup, richer archivist cards)

Paste this whole block into Lovable in one go.

---

Four fixes and one enhancement for the AI Cold War roundtable site. Skip any item that is already done.

**1. Main page: replace the Call for Proposals with the live event banner.** Remove the Call for Proposals block from the main page. In its place, render a prominent event banner from public `GET /event` (no auth). It returns:

```json
{"event": {
  "format": "Roundtable",
  "location": "C-7, room 3.09, Kraków, Poland",
  "sessions": "Thursday 10 September 2026, 9:00-10:30",
  "timezone": "Europe/Warsaw",
  "status": "Program confirmed — accepted papers and participants are set; no open call"
}}
```

Render as: "📅 **Roundtable — Thursday 10 September 2026, 9:00–10:30** (Europe/Warsaw) · C-7, room 3.09, Kraków, Poland" with the `status` value as a smaller line underneath. Always render from the endpoint — never hardcode the date, venue, or status. Also search the whole site for other hardcoded date/venue copy (e.g. "8–11 September", "Call for Proposals") and replace with endpoint values or remove.

**2. Move the Call for Proposals under About, as history.** Do not delete its content. Place it on the About page/section titled "Call for Proposals (closed)", keeping the original text (Kraków, Poland, 8–11 September) intact as a historical record, with a small "closed" note at the top rendered from the `status` field of `GET /event`.

**3. De-duplicate the Archivist's Notebook.** It currently renders twice (main page and Archive). Keep it in ONE place only: under Archive, fed by `GET /archivist/reflections`. On the main page, at most a small link/card ("🗂 The Archivist's Notebook") navigating there — never the full feed. Optionally the card may show only the single latest entry (`reflections[0].content`, truncated) as a teaser quote.

**4. Final layout check.** Main page = live event banner + session entry points (+ notebook teaser link at most). About = Who's Who roster (from `GET /roster`) + closed CfP. Archive = weekly sessions, satire takes, and the Archivist's Notebook.

**5. Richer archivist cards (enhancement, if not already applied).** Archivist message metadata (live turns and `/api/replay/{id}` events) now also carries:
- `sealed_count` and `sealed_examples`: pages readable by NO state actor — render a small "sealed shelves: N" line on the shelf card, with the examples in a tooltip or collapsible list;
- `reintroduced`: `{page, folder, readable_by, notes}` — render the first note as an indented "buried evidence" quote block under the shelf card, sourced to the page name.

The notebook feed's entries carry the same fields inside `meta` — render them the same way there (`meta.foreground`/`meta.suppressed` as collapsible rises/sinks lists, `meta.reintroduced.notes` as the quote block, and for `kind: "intervention"` link `meta.session_id` to that session's replay). The logic picker fed from `GET /archivist/catalog` now includes a `scope` field: show `"session-memory"` (scope `"session"`) in the live-session summon picker like any other logic, but exclude it from the standalone Archive-shelf viewer since it needs a live transcript.
