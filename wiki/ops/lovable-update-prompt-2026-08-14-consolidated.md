# Lovable update prompt — 2026-08-14 (consolidated: archive performance, notebook clarity, layout, dialogue)

Paste this whole block into Lovable in one go. Skip any item already done.

---

Updates for the AI Cold War roundtable site. Backend base URL: `https://aicoldwar.ngrok.app` — all public endpoints need no auth, but always send header `ngrok-skip-browser-warning: true`. Render everything from endpoints; never hardcode copy.

**1. FIX: Archivist's Notebook — collapsed by default, lazy, user chooses what to open.** Fetch `GET /archivist/reflections?limit=10` (fast; do not fetch more initially, and never fetch session replays on page load). Render each entry as a **collapsed card**: kind badge (intervention / meditation / retrospective), date, logic label (`meta.logic_label` or `logic`), and the first ~140 characters of `content`. Clicking a card expands that card only (full text; rises/sinks lists from `meta.foreground`/`meta.suppressed`; "sealed shelves: N" from `meta.sealed_count`; buried-evidence quote from `meta.reintroduced.notes[0]`, sourced to `meta.reintroduced.page`). A single "Load more" button refetches with `limit=30`. For `kind: "intervention"` cards, a "view session replay" link built from `meta.session_id` — replay JSON loads only when clicked.

**2. FIX: Archive page must not preload sessions.** Any list of past sessions renders from lightweight `GET /sessions/recent` preview data only (title, date, turn count); full `/api/replay/{id}` loads only when the user opens that session. Remove any loop fetching all replays up front.

**3. Notebook header explains itself.** `GET /archivist/reflections` returns an `about` object: render `about.intro` as the page introduction under the title, `about.kinds` as a three-item legend, and `about.glossary` as tooltips on the matching card labels ("sealed shelves", "rises & sinks", "buried evidence") or a small glossary line under the legend.

**4. Main page cleanup.** Remove ALL Call-for-Proposals remnants from the main page — including the "What to Submit" block ("Contributors are invited to submit...") and any "historical record" note. Scan the main page for any sentence addressed to prospective submitters ("invited to submit", "proposals", "deadline", "call") and delete it. The main page shows: the event banner from `GET /event` ("📅 Roundtable — Thursday 10 September 2026, 9:00–10:30 (Europe/Warsaw) · C-7, room 3.09, Kraków, Poland"; the `status` field is empty — render nothing beneath when empty), session entry points, and at most a small teaser card linking to the Archivist's Notebook.

**5. About page composition.** In order: (a) Who's Who roster from `GET /roster`; (b) Participants from the same response's `participants` array — the `role: "Convener"` entry (Denisa Reshef Kera) first with a distinct badge, `paper` in italics (skip when empty), `abstract`, `research_interests` labeled "Research interests" (skip when empty), `notes` as a highlighted connector line; (c) "Call for Proposals (closed)" — the original CfP text kept as history; (d) "Future Work" from `GET /future-work` — title + author, description, the comic images (prefix paths with the backend URL) with captions, and `finding` in a callout labeled "What the experiment found".

**6. Collaboration chips.** Label all agent-participant links "Collaboration" (not "Inspired by"). Each agent card renders its own `collaboration` array from `GET /roster` in the given order (e.g. China: Denisa Reshef Kera, Avi Spitz, Merav Turgeman, Hila Ofek) as chips linking to participant profiles — never derive the list from participants' back-links. Participant cards keep reciprocal chips to agents.

**7. One line about live dialogue.** On the About page, near the roster intro, add: "At live events, the audience speaks directly to the agents — spoken questions are transcribed into the debate and the agents answer aloud." (Informational only; the microphone control lives on the operator stage, not the public site.)
