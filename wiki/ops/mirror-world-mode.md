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

## Frontend rendering — PARKED until real data

Once the live feed is connected, wire this into Lovable. Paste prompt (kept here deliberately; do not build until there's real data):

> Add a `mirror-world` mode. For each turn (`metadata.format == "mirror-turn"`) render a three-row card: **Official line** / **Buried reality** / **Mirror (speculation)**, with the `irony` as a caption. Start it with `POST /session/start` `{mode:"mirror-world", seed_incident:true}`. On close, call `POST /session/{id}/mirror-card?tone=absurdist&visual=true` and render the result as a **tabloid front page**: the `headline` as a screaming banner, `perex` as the standfirst, the `visual.image_url` as the hero image, and `dispatch` as the body; show `reality` / `official_story` / `speculation` as three labeled strips. Treat attribution as a sourced claim, never fact.

## See also

- [Threat-Intel Feed Integration](threat-intel-feed-integration.md) — connecting the live feed when it arrives.
- [Roundtable Frontend Contract](roundtable-frontend-contract.md) — the Mirror-World Contract (endpoint shapes).
- [Propaganda Lab Mode](propaganda-lab-mode.md) — the sibling structured-artifact mode.
