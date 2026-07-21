# Mirror-World Mode

> Updated: 2026-06-17

## What this is

`mirror-world` is a standalone session mode (a peer of `propaganda-lab`) that turns the simulation into a satirical **mirror**: it stages the gap between covert reality and the official story, then extrapolates a bizarre near-future. It runs in the "satirical-but-not-cynical / darkly optimistic" register of the AIwars `simulation_narrative_guide.md` — named ordinary protagonists, unexpected consequences, cultural detail, vivid imagery, ironic twists.

Three layers per debate:

1. **Reality (the underworld)** — a threat-intel incident (e.g. a DPRK/Russia/Iran-attributed crypto-exchange hack) from the feed.
2. **Official narrative** — what governments and regulations claim (media/regulatory coverage + the actors' own sanctioned lines).
3. **Speculative mirror** — a darkly funny extrapolation from the gap between layers 1 and 2.

The gap between covert reality and the official story is the irony engine. Attribution is always carried as a **sourced claim at a stated confidence**, never asserted as fact.

## End-to-end flow

```
threat-intel feed ──▶ raw/threat-intel/ (reality)         [see threat-intel-feed-integration.md]
        │
        └─ official coverage ──▶ raw/focus-issues/<incident>/
                                          │
        mirror-world session (seed_incident: true) ◀──────┘
                                          │
                          POST /session/{id}/mirror-card  ──▶ card + optional tabloid front page
```

## Each turn (the three-layer clash)

A mirror-world turn carries structured metadata (`metadata.format == "mirror-turn"`):

- `official_line` — the sanctioned framing the actor pushes
- `buried_reality` — the uncomfortable truth it has to spin
- `speculation` — a short bizarre near-future with a named protagonist + ironic twist
- `irony` — one line naming the contradiction

LLM path: `generate_openrouter_mirror_turn` (`app/llm.py`); heuristic fallback: `generate_actor_mirror_turn` (`app/agent_logic.py`); wired through the dedicated `mirror-world` branch in `_generate_session_turn` (`app/main.py`).

## Closing artifact: the mirror-card

`POST /session/{session_id}/mirror-card?tone=<tone>&visual=<bool>` returns:

- `headline` — screaming tabloid title
- `perex` — short sensational standfirst/lead blurb
- `reality` / `official_story` / `speculation` — the three layers, side by side
- `dispatch` — a 4-6 sentence satirical news dispatch from the near-future
- `visual` (when `visual=true`) — a generated **yellow-journalism tabloid front page** via the image pipeline, rendered by a GPT-image-class model (`MIRROR_VISUAL_MODEL`, default `openai/gpt-5.4-image-2`) because it renders legible headline text far better than photoreal diffusion; override per call with `&image_model=...`

### Tone dial

`tone` ∈ `grounded` | `grounded-absurdist` (default) | `absurdist`. `absurdist` goes fully surreal and laugh-out-loud while staying politically legible (e.g. office AC units turned into crypto-mining furnaces, "How I Got Owned By Lazarus" support groups, compliance-themed reality TV).

## Running it

```powershell
# seed the reality layer (sample today; live feed later — see threat-intel-feed-integration.md)
python scripts/run_threat_intel_ingest.py --sample docs/sample_incidents.json --no-official
# then start a session: mode=mirror-world, seed_incident=true, and call /mirror-card?tone=absurdist&visual=true
```

## Incident selection (2026-07-19)

`POST /session/start` seeds mirror-world from one incident in `raw/threat-intel/`, chosen by:

- `seed_incident: true` (no `incident_id`) — picks **randomly** across the whole dataset (208 incidents as of this feed), not always the same "latest" file. Each session draws a different case.
- `incident_id: "<id>"` — seeds that **specific** incident (e.g. `"CHA-Ronin-Network-149"`), for a chosen/repeatable case.

The seed prompt also carries a **dataset-context clause** (`app/threat_intel.py::dataset_stats()` + `prompt_from_incident()`): how this incident's attribution confidence and scale compare to the dataset's own median, how many incidents even have a known attack vector, and the most-named threat group across the set. This gives actors a pattern to contest, not just one isolated anecdote — e.g. an actor can argue a case is "a convenient outlier" versus "representative," using real dataset numbers, not vibes.

## Frontend rendering — live as of 2026-07-19

The live feed is connected (205 real DPRK/Lazarus-attributed incidents, see [Threat-Intel Feed Integration](threat-intel-feed-integration.md)), so `mirror-world` should move from a parked/experimental mode into the **main mode menu** alongside the standard debate and propaganda-lab modes. Paste prompt for Lovable:

> Add `mirror-world` as a normal, always-available mode option in the main mode menu (not hidden/experimental). Start it with `POST /session/start` `{mode:"mirror-world", seed_incident:true}`. For each turn (`metadata.format == "mirror-turn"`) render a three-row card: **Official line** / **Buried reality** / **Mirror (speculation)**, with the `irony` as a caption. On close, call `POST /session/{id}/mirror-card?tone=absurdist&visual=true` and render the result as a **tabloid front page**: the `headline` as a screaming banner, `perex` as the standfirst, the `visual.image_url` as the hero image, and `dispatch` as the body; show `reality` / `official_story` / `speculation` as three labeled strips. Then offer a **"Get James's take"** button that calls `POST /session/{id}/james-take` and renders `james_take` as a single cynical closing quote block, visually distinct from the state actors (he's not one of them — a 4th, uninvited voice). That call has no fallback: a non-200 response means show an error state ("James isn't available right now"), never fabricate a take client-side. Treat attribution as a sourced claim, never fact.

## James's closing take

`POST /session/{session_id}/james-take` (operator-token protected, see [James persona](#see-also) wiring in `app/llm.py::generate_james_take`) reads the finished transcript — including each mirror-turn's `official_line`/`buried_reality`/`speculation` metadata when present — and returns `{session_id, james_take}`: one grounded, contrarian counter-prediction from a Machiavellian crypto-native analyst-activist persona, naming a specific mechanism rather than a generic cynical aside. Works on any session transcript, not just mirror-world, though mirror-world sessions give him the richest material. Deliberately has **no heuristic fallback** — if `OPENROUTER_API_KEY` isn't set or the call fails, it returns a real error (503/502), never a canned line.

## See also

- [Threat-Intel Feed Integration](threat-intel-feed-integration.md) — the live feed powering the reality layer.
- [Roundtable Frontend Contract](roundtable-frontend-contract.md) — the Mirror-World Contract (endpoint shapes).
- [Propaganda Lab Mode](propaganda-lab-mode.md) — the sibling structured-artifact mode.
- [Roundtable Roster (Who's Who)](lovable-roster-whos-who.md) — introducing James, Halcyon, and the satire heads alongside china/us/eu.
