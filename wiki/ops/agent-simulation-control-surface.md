# Agent Simulation Control Surface

> Updated: 2026-05-17

## Purpose

This page is the fastest way to review what shapes agent behavior in the simulation and where to edit it.

Use it when you want to:

- make China, U.S., or EU agents behave differently
- tune rhetoric, aggression, ideology, or surprise
- change propaganda-lab output style
- update what counts as legitimate action or strategic fear
- review which wiki pages are most important for each actor

## Main Control Layers

There are four main layers that shape agent behavior:

1. `wiki/` knowledge base pages
2. runtime prompt logic in `app/llm.py`
3. fallback behavior logic in `app/agent_logic.py`
4. mode and media rendering rules in the frontend

The most important rule is:

- new source files in `raw/` do not matter until the relevant `wiki/` pages are updated

## Actor Entry Pages

These are the main wiki roots each actor reads from.

- China: `wiki/china-ai-policy/china-ai-knowledge-base-hub.md`
- U.S.: `wiki/us-ai-policy/us-ai-knowledge-base-hub.md`
- EU: `wiki/eu-ai-policy/eu-ai-knowledge-base-hub.md`
- Shared: `wiki/shared-ai-geopolitics/shared-ai-geopolitics-and-governance.md`

If an actor feels wrong, start here.

## Most Important Runtime Prompt Files

### `app/llm.py`

This is the most important runtime control file for live model behavior.

Key sections:

- `ACTOR_PROMPT_PROFILES`
- `MODE_PROMPT_GUIDANCE`
- `build_actor_messages(...)`
- `build_propaganda_messages(...)`

What to edit here:

- voice
- rhetoric
- interests
- provocation style
- surprise style
- propaganda artifact selection
- how much meme/TikTok/poster logic is allowed

### `app/agent_logic.py`

This matters mainly for fallback and structure.

Key sections:

- `ACTOR_STYLES`
- `MODE_FRAMES`
- `generate_actor_turn(...)`
- `generate_actor_propaganda_turn(...)`

What to edit here:

- fallback speech tendencies
- actor-specific strategic verbs
- propaganda artifact defaults
- slogan seeds
- default audience / affect / visual logic

## Key Wiki Pages By Actor

### China

- `wiki/china-ai-policy/chinese-ai-strategic-interests.md`
- `wiki/china-ai-policy/chinese-ai-policy-instruments.md`
- `wiki/china-ai-policy/chinese-ai-operational-strategy.md`
- `wiki/china-ai-policy/chinese-ai-governance-style-and-agenda.md`
- `wiki/china-ai-policy/china-ai-simulation-profile.md`
- `wiki/china-ai-policy/china-agents-for-synthedrion.md`
- `wiki/china-ai-policy/china-propaganda-generation-template.md`
- `wiki/china-ai-policy/chinese-ai-cross-border-sovereignty.md`

### U.S.

- `wiki/us-ai-policy/us-ai-strategic-interests.md`
- `wiki/us-ai-policy/us-compute-strategy-and-global-ai-leadership.md`
- `wiki/us-ai-policy/us-ai-engagement-with-china-on-ai-safety.md`
- `wiki/us-ai-policy/japan-as-a-us-ai-partner.md`
- `wiki/us-ai-policy/us-ai-simulation-profile.md`

### EU

- `wiki/eu-ai-policy/eu-ai-strategic-interests.md`
- `wiki/eu-ai-policy/eu-ai-governance-style.md`
- `wiki/eu-ai-policy/eu-ai-policy-instruments.md`
- `wiki/eu-ai-policy/eu-ai-simulation-profile.md`

### Shared

- `wiki/shared-ai-geopolitics/ai-chip-control-cloud-leverage-and-us-china-compute.md`
- `wiki/geopolitics/us-china-ai-rivalry-and-strategic-stability.md`
- `wiki/shared-ai-geopolitics/rand-source-hub.md`

## Session Modes

Supported modes:

- `debate`
- `negotiation`
- `crisis`
- `policy-planning`
- `propaganda-lab`

Mode guidance is controlled in:

- `app/llm.py` via `MODE_PROMPT_GUIDANCE`

### What Each Mode Should Feel Like

- `debate`: adversarial, sharp, competitive
- `negotiation`: leverage, bargaining, conditional compromise
- `crisis`: urgency, escalation, timing, risk
- `policy-planning`: implementation, sequencing, statecraft details
- `propaganda-lab`: symbolic struggle, image logic, persuasion artifacts

## Propaganda-Lab Specific Controls

See also:

- `wiki/ops/propaganda-lab-mode.md`

Current propaganda-lab can emit:

- `artifact_type`
- `propaganda_style`
- `audience`
- `affect`
- `visual_logic`
- `slogan`
- `commentary`
- `image_prompt`
- `image_url`
- `response_target`

Current artifact types include:

- `poster`
- `meme`
- `tiktok-still`
- `campaign-ad`
- `infographic`
- `hostile-remix`
- `soft-power-aspiration`

If propaganda-lab feels too repetitive, edit:

- `build_propaganda_messages(...)` in `app/llm.py`
- `generate_actor_propaganda_turn(...)` in `app/agent_logic.py`

## Image Model Routing

Current image routing defaults:

- U.S.: `openai/gpt-5.4-image-2`
- China: `bytedance-seed/seedream-4.5`
- EU: `black-forest-labs/flux.2-max`

Configured in:

- `app/config.py`
- `app/images.py`

If images stop working, inspect:

- `OPENROUTER_API_KEY`
- model ids in `ACTOR_IMAGE_MODELS`
- fallback behavior in `app/images.py`

## Replay Audio Controls

Replay audio now uses cached backend-generated MP3 files.

Important files:

- `app/audio.py`
- `app/main.py`

Replay event fields:

- `event.audio_url`
- `event.audio_cached`
- `event.narration_text`

Replay top-level fields:

- `audio.full_audio_url`
- `audio.full_audio_cached`
- `audio.full_audio_mode`

If you want to change how agents sound, edit:

- `ACTOR_VOICES` in `app/audio.py`

## Important Frontend Contract Pages

- `wiki/ops/roundtable-frontend-contract.md`
- `wiki/ops/lovable-roundtable-build-prompt.md`
- `wiki/ops/lovable-roundtable-ui-spec.md`
- `wiki/ops/lovable-page-build-steps.md`

## Most Useful Prompts To Reuse

### Update Knowledge Base From New Sources

```text
Ingest these new raw files into the knowledge base.
Update the relevant actor and shared wiki pages.
Then start a fresh round so the new material is reflected in agent behavior.
```

### Make One Actor More Complex

```text
Update the [China / U.S. / EU] agent behavior based on these sources.
Change what the actor wants, fears, treats as legitimate action, and how it talks.
Also update propaganda motifs if relevant.
```

### Tune Propaganda-Lab

```text
Make propaganda-lab less repetitive and more surprising.
Let each turn choose the most effective propaganda artifact type while preserving bloc-specific political identity.
```

### Change Weekly Featured Session

```text
Promote session <session_id> to this week's featured roundtable and regenerate snapshots.
```

## Good Questions To Use For Review

When reviewing agent behavior, ask:

- Does this actor want the right things?
- Does this actor fear the right things?
- Does this actor sound too generic or too Anglo?
- Does this actor have bloc-specific rhetoric?
- Does propaganda-lab vary enough in artifact type and aesthetic?
- Does the image logic feel too fixed or too safe?
- Does the session mode actually change the behavior, or only the wording?

## Comment / Review Section

Use this section as a working scratchpad.

### China

- Voice notes:
- Strategic notes:
- Propaganda notes:

### U.S.

- Voice notes:
- Strategic notes:
- Propaganda notes:

### EU

- Voice notes:
- Strategic notes:
- Propaganda notes:

### Shared / Systemic

- Weekly archive notes:
- Replay notes:
- Audio notes:
- Image model notes:
- Lovable notes:
