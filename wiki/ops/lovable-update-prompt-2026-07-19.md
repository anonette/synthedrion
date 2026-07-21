# Lovable update prompt — 2026-07-19 (mirror-world + James + who's who)

Paste this whole block into Lovable in one go.

---

Three updates to the AI Cold War roundtable frontend:

**1. Promote mirror-world to a normal main-menu mode.**
It's no longer experimental — a live feed of 205 real DPRK/Lazarus-attributed
crypto-theft incidents now powers its reality layer. Add `mirror-world` as a regular
option in the main mode menu, alongside the existing debate/negotiation/crisis/
propaganda-lab modes. Start it with `POST /session/start` `{mode:"mirror-world",
seed_incident:true}`. For each turn (`metadata.format == "mirror-turn"`) render a
three-row card: **Official line** / **Buried reality** / **Mirror (speculation)**, with
the `irony` field as a caption. Attribution is always a sourced claim, never asserted
fact — say so somewhere in the UI (e.g. a small "sourced claim, not fact" tag on the
reality row).

**2. Add the closing "tabloid + James" flow.**
When a mirror-world session ends, call `POST /session/{id}/mirror-card?tone=absurdist&visual=true`
and render the result as a tabloid front page: `headline` as a screaming banner, `perex`
as the standfirst, `visual.image_url` as the hero image, `dispatch` as the body, and
`reality` / `official_story` / `speculation` as three labeled strips below it. Then show
a **"Get James's take"** button that calls `POST /session/{id}/james-take` and renders
the returned `james_take` string as one cynical closing quote block, visually separated
from the tabloid card — James is not one of the debating actors, he's an uninvited 4th
voice who only shows up at the end. This call has **no fallback**: on a non-200 response,
show a plain error state ("James isn't available right now") — never fabricate or
hard-code a substitute line.

**3. Add a "Who's Who" roster screen**, reachable from the main menu, introducing every
voice a visitor might encounter — not just the three debaters. Fetch `GET /roster`
(public, no auth needed) and render one card per entry using its `name`, `archetype`,
`produces`, and `trigger` fields directly — don't hardcode the cast copy client-side, so
the screen stays in sync if a persona changes. Each entry has a `type` of `"core"`
(China/US/EU — always present, argue every mode) or `"guest"` (Halcyon, the satire
heads, James — each invoked on demand, off by default); group/visually separate the
roster screen by that field. Keep each card to the one-line `archetype` + one phrase
from `produces` — no lore dumps.

---

## Reference (not part of the paste-in — for whoever wires this up)

- `wiki/ops/mirror-world-mode.md` — mirror-turn shape, mirror-card shape, James section.
- `wiki/ops/lovable-roster-whos-who.md` — full roster copy and per-voice endpoint map.
- `wiki/ops/roundtable-frontend-contract.md` — full protected/public endpoint list
  (now includes `POST /session/{session_id}/james-take`).
