# Lovable integration — "Who's Who" roster / about screen

The roundtable has grown past three debaters. This is the copy + wiring for an intro
screen that introduces every voice a visitor might encounter, what each one actually
produces, and which live endpoint/mode surfaces them — so it reads as a cast list, not
just documentation.

## Live data source

`GET /roster` (public, unauthenticated, like `/health`) returns `{"roster": [...]}` — one
object per voice: `id`, `type` (`"core"` or `"guest"`), `name`, `archetype` (one
sentence), `produces` (what it actually outputs), `trigger` (how a visitor sees it).
**Fetch this instead of hardcoding the copy below** — it's the same content, but staying
data-driven means the roster screen won't drift out of sync if a persona changes.

## The core three (the actual debaters)

These load real wiki-grounded policy positions (`ACTOR_PROMPT_PROFILES` in `app/llm.py`)
and argue every mode. They are the only entries in `SessionState.actors` / `next_actor`
turn order.

- **China** — a PRC strategic actor: sovereignty, non-interference, developmental
  legitimacy, long-horizon industrial policy. Produces: debate/negotiation/crisis turns,
  propaganda-lab artifacts, one voice in every mirror-world "official line."
- **United States** — frontier competition, alliance power, market scale, prosecutorial
  and impatient with euphemism. Same production surface as China.
- **European Union** — Brussels institutionalism, strategic autonomy, precise and
  sardonic, disciplines louder powers through regulation rather than force. Same
  production surface.

All three: `POST /session/start`, `POST /session/message`, `/recap` scoreboard,
`/mirror-card` official line.

## Halcyon — the outsider peace-builder

Belongs to no bloc. Enters mid-debate with one real, cited, hopeful development on the
fronts they're fighting over, then dares the three toward one bold thing they could
build together. Not cynical, not neutral mush — warm and sharp. Produces: an
`/intervene`-style turn injected into the live transcript (see `generate_halcyon_turn`,
`app/llm.py`). Optional — off unless invoked.

## The satire heads — caricature avatars (optional toggle)

When "🎭 Brutal satire" is on, each state actor's earnest turn is rewritten into a short,
savage caricature line and delivered by a talking-head avatar of the real-world leader
they represent: **Xi Jinping** (China), **Donald Trump** (US), **Ursula von der Leyen**
(EU) — plus **Halcyon the peace-bird** for the optimist voice. A `drift` slider (0=tight
savage fidelity → 1=full signature-catchphrase rant) controls register. Produces:
`POST /satire`, rendered via `/heads/{actor}.webm` avatars. See
[Lovable satire integration](lovable-satire-integration.md).

## James — the uninvited closing voice

Not a debater — he never appears in the transcript itself. A Machiavellian
crypto-native analyst-activist who reads the *finished* transcript (any mode, richest in
mirror-world) and delivers one grounded, contrarian counter-prediction: he doesn't
believe anyone's stated motive, talks in the room's real currency (liquidity, exit
liquidity, MEV), and always names a specific mechanism instead of a vague cynical aside.
Produces: `POST /session/{id}/james-take` → `{james_take: "..."}`, called once at the
close of a session, never mid-debate. **No fallback**: a non-200 response means show an
honest error state ("James isn't available right now"), never fabricate a take
client-side. See [Mirror-World Mode](mirror-world-mode.md#jamess-closing-take).

## Suggested roster screen shape

A card per voice: name, one-line archetype, and a "what he/she/it produces" chip linking
to where you'll actually see it (a live debate, a satire toggle, a closing button) —
not a wall of lore. James and Halcyon should visually read as *guests*, not participants,
since they sit outside the china/us/eu turn order.

## Paste-in prompt for Lovable

> Add a "Who's Who" roster screen, reachable from the main menu, introducing every voice
> in the roundtable — not just the three debaters. For each entry show: name, a one-line
> archetype description, and what they actually produce with a link/button to see it live
> (China/US/EU → "see them debate", start a session; Halcyon → "hear the outsider's case",
> shown only when triggered; the satire heads → link to the 🎭 Brutal Satire toggle; James
> → "get his take", shown as a closing-button explainer since he only appears via
> `POST /session/{id}/james-take` at the end of a session, never mid-debate). Visually
> separate the three core debaters (always present, argue every mode) from the three
> optional guest voices (Halcyon, the satire heads, James — each off by default / invoked
> on demand). Keep copy short — one sentence of archetype, one phrase of "what they do."

## See also

- [Roundtable Frontend Contract](roundtable-frontend-contract.md) — full endpoint list.
- [Mirror-World Mode](mirror-world-mode.md) — James's home endpoint and the reality layer.
- [Lovable satire integration](lovable-satire-integration.md) — the caricature avatars.
