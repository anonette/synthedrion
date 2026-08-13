# Lovable update prompt — 2026-08-13 (b): participants, future work, event banner, layout cleanup

Paste this whole block into Lovable in one go. Skip any item already done.

---

Six updates for the AI Cold War roundtable site. All content is served by the backend — render from the endpoints, never hardcode copy.

**1. Main page: event banner with status.** Remove the Call for Proposals block from the main page. In its place render a prominent banner from public `GET /event`: "📅 **Roundtable — Thursday 10 September 2026, 9:00–10:30** (Europe/Warsaw) · C-7, room 3.09, Kraków, Poland", with the `status` field visibly underneath as its own line: "Program confirmed — accepted papers and participants are set; no open call". Search the site for any other hardcoded date/venue/CfP copy and replace or remove it.

**2. About: Call for Proposals archived.** Keep the CfP's original text (Kraków, Poland, 8–11 September) on the About page as a historical record titled "Call for Proposals (closed)", with a small closed-note at the top rendered from `GET /event`'s `status`.

**3. About / Who's Who: Participants section.** `GET /roster` now returns a `participants` array — the researchers whose work inspired the agents (9 entries). Render one profile card each: `name`, `affiliation`, `paper` in italics (skip the line if empty — some entries are bio/contribution cards), `abstract`, `research_interests` (smaller text, labeled "Research interests", skip if empty), and `notes` as a highlighted connector line. Each entry's `inspired` array holds roster agent ids (`james`, `halcyon`, `archivist`, `satire-heads`) — render as clickable chips linking/scrolling to the matching agent card, with a reciprocal "inspired by" link on the agent's card. An empty `inspired` array means the research informs the shared knowledge base — show a chip reading "the knowledge layer" instead.

**4. About: Future Work section** (after participants). Fetch public `GET /future-work`: each entry has `title`, `author`, `format`, `description`, `finding`, `images` (paths relative to the API base — prepend the backend URL), and `image_captions` (same order). Render title + author, the description, the images as wide comic panels with captions underneath, and `finding` in a highlighted callout labeled "What the experiment found".

**5. Archive: de-duplicate the Archivist's Notebook.** It currently renders twice (main page and Archive). Keep it ONLY under Archive, fed by `GET /archivist/reflections`. On the main page at most a small teaser card ("🗂 The Archivist's Notebook", optionally showing `reflections[0].content` truncated) linking to the Archive page.

**6. Richer archivist cards.** Archivist message metadata (live turns, replay events, and notebook entries' `meta`) now also carries: `sealed_count` + `sealed_examples` (pages readable by NO state actor — render "sealed shelves: N" with examples in a tooltip/collapsible), and `reintroduced` (`{page, folder, readable_by, notes}` — render the first note as an indented "buried evidence" quote block sourced to the page name). In the notebook, `kind: "intervention"` entries should link `meta.session_id` to that session's replay. The logic picker from `GET /archivist/catalog` includes a `scope` field: include `session-memory` (scope `"session"`) in the live summon picker but exclude it from the standalone archive-shelf viewer.

Final layout: **Main page** = event banner + status + session entry points (+ notebook teaser). **About** = Who's Who roster + Participants + closed CfP + Future Work. **Archive** = weekly sessions, satire takes, Archivist's Notebook.
