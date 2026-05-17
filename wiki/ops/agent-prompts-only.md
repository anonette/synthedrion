# Agent Prompts Only

> Updated: 2026-05-17

## Knowledge Base Refresh

```text
Ingest these new raw files into the knowledge base.
Update the relevant actor and shared wiki pages.
Then start a fresh round so the new material is reflected in agent behavior.
```

## Knowledge Base Refresh With File List

```text
Ingest these new raw files into the knowledge base.
Update the relevant actor and shared wiki pages.
Then start a fresh round so the new material is reflected in agent behavior.

Files:
- raw/articles/...
- raw/reg-documents/...
- raw/rand/...
```

## Fastest Ingest Instruction

```text
Add these new raw files to the wiki knowledge base, update the affected actor/shared pages, and make sure the next rounds use them.
```

## China Evolution Prompt

```text
New source: [URL or file]
Source type: [policy / article / speech / translation / media / visual]
Why it matters: [1 sentence]
Please update:
- interests
- instruments
- strategy
- propaganda style
- agent cards
```

## Fast China Update Prompt

```text
Add this to the China agents and extract new strategy, rhetoric, and propaganda motifs: [URL]
```

## General Actor Update Prompt

```text
Update the [China / U.S. / EU] agent behavior based on these sources.
Change what the actor wants, fears, treats as legitimate action, and how it talks.
Also update propaganda motifs if relevant.
```

## Propaganda-Lab Tuning Prompt

```text
Make propaganda-lab less repetitive and more surprising.
Let each turn choose the most effective propaganda artifact type while preserving bloc-specific political identity.
```

## Featured Weekly Session Prompt

```text
Promote session <session_id> to this week's featured roundtable and regenerate snapshots.
```

## Lovable Build Prompt

```text
Build a page called Daily Roundtable for https://aicoldwar.lovable.app/.

This page is the interface for a live geopolitical AI simulation with three actors:
- China
- United States
- European Union

Important architecture rule:
- The frontend is only the interface layer.
- The backend is the source of truth for knowledge loading, actor context, turn orchestration, and session state.
- Do not hardcode actor personalities in the frontend.
- Do not simulate agent logic in the frontend.

Design goal:
- The page should feel like a live strategic control room, not a generic chatbot.
- It should be editorial, geopolitical, and high-stakes.
- Desktop first, but fully usable on mobile.
- Avoid bland SaaS dashboard aesthetics.

Visual direction:
- Dark, high-contrast interface with restrained accent colors.
- China uses a deep red accent.
- United States uses a cold blue accent.
- European Union uses a muted gold accent.
- System / shock events use amber.
- Human interventions use slate or gray.
- The transcript should feel like a live diplomatic theater rather than chat support software.

Page structure from top to bottom:

1. Header
- Title: Daily Roundtable
- Subtitle: Live wiki-grounded geopolitical AI session
- Right side status chips:
  - Backend connected / disconnected
  - Session mode
  - Turn count
  - Session ID

2. Session Setup Panel
- Prompt textarea
- Mode segmented control with:
  - debate
  - negotiation
  - crisis
  - policy-planning
  - propaganda-lab
- Actor toggle buttons for:
  - China
  - United States
  - European Union
- Include shared sources toggle, default on
- Primary CTA: Start Session

3. Knowledge Sources Panel
- Show loaded wiki pages after session start
- Group by actor
- Each group should show a count plus expandable file list
- This must visibly communicate that the agents are reading live wiki material, not hidden fixed personas

4. Live Roundtable Panel
- Main transcript area
- Distinct message cards by actor
- China aligned left
- United States aligned right
- European Union aligned left but visually distinct from China
- Human interventions aligned right in neutral styling
- System shocks centered and prominent
- Show actor name, timestamp, and message content
- Transcript should support long-form turns cleanly
- Add a persistent footer control bar with:
  - Next Turn button
  - Auto-advance toggle placeholder
  - Generate Summary button
  - Generate Wiki Proposals button

5. Intervention Panel
- Textarea for human intervention
- Type selector:
  - question
  - challenge
  - redirect
  - source
  - shock
- Button: Send Intervention

6. Shock Injection Panel
- Shock title
- Shock content
- Severity selector:
  - low
  - medium
  - high
- Button: Inject Shock

7. Strategic Tensions Panel
- A compact side panel that highlights:
  - current next speaker
  - most recent speaker
  - active actors
  - latest intervention or shock
- This can be mostly frontend state for now

8. Session Summary Panel
- Empty state before summary exists
- After generation, render:
  - headline
  - context
  - points of agreement
  - points of disagreement
  - strategic options
  - risks and unknowns
  - recommended follow-ups

9. Wiki Proposal Panel
- Empty state before proposals exist
- After generation, render candidate proposals with:
  - target path
  - reason
  - content preview if available
```

## Lovable Consolidated Update Prompt

```text
Update the Weekly Roundtable page so it matches the current backend contract exactly.

Do not redesign from scratch. Keep the existing dark editorial geopolitical visual language. Focus on runtime correctness, replay correctness, propaganda-lab support, and fallback resilience.

Backend base URL:
https://8ade-84-43-244-65.ngrok-free.app

Current backend capabilities you must support:

- public weekly/archive/replay endpoints
- operator-gated mutating POST endpoints
- live session start can auto-generate the opening turn
- replay payloads use `events`
- propaganda-lab emits poster-dialogue metadata
- read-only weekly content should support snapshot fallback

Implement all of the following:

1. Operator token on mutating requests
2. Start session must generate the opening turn immediately
3. Weekly current and archive
4. Replay rendering fix
5. Propaganda-lab special rendering
6. Snapshot fallback for read-only content
7. Live session studio
8. Knowledge Sources
9. Dev logging
10. Error and empty states
11. Preserve visual identity

Do not change backend assumptions.
Do not simulate content in the frontend.
Use backend response shapes exactly as returned.
```

## Lovable Recent Sessions Prompt

```text
Update the Weekly Roundtable frontend so recent live sessions are surfaced automatically and separately from the featured weekly archive.

Keep the current visual design. This is a data-flow and page-structure correction.

Backend base URL:
https://8ade-84-43-244-65.ngrok-free.app

Important backend contract:

There are now three distinct public read feeds:

1. Featured weekly session
- `GET /weekly/current`

2. Curated weekly archive
- `GET /weekly/archive?limit=12&offset=0`

3. Recent live sessions
- `GET /sessions/recent?limit=50`

Do not confuse them.
```

## Lovable Propaganda Replay Prompt

```text
Update the `/weekly-roundtable` page so that `propaganda-lab` is rendered as a multimodal poster-dialogue mode instead of a normal transcript.

Keep the existing dark geopolitical editorial design language, but add a special rendering path for propaganda sessions.

Backend base URL:
https://8ade-84-43-244-65.ngrok-free.app

Important:
The backend has already been updated.
For `mode = "propaganda-lab"`, agent messages now include structured metadata.

Implement propaganda artifact cards with image, slogan, commentary, and metadata-aware rendering.
```

## Lovable Replay Audio Prompt

```text
Update replay audio so it uses backend-generated MP3 files instead of browser speech synthesis.

Keep the current visual design and replay layout. This is an audio integration change.

Backend base URL:
https://8ade-84-43-244-65.ngrok-free.app

Important:
The backend now generates and caches replay audio files.

Replay API response now includes:

Top-level:
- `audio.full_audio_url`
- `audio.full_audio_cached`
- `audio.full_audio_mode`
- `audio.event_audio`

Per event:
- `event.audio_url`
- `event.audio_cached`
- `event.narration_text`
- `event.metadata`

Prefer backend audio over browser speech.
```

## Lovable Operator Token Prompt

```text
Update the Weekly Roundtable frontend to use the real operator token flow and stop relying on the hardcoded dev fallback.

Important:
- The backend now enforces `X-Roundtable-Token` on all mutating POST routes.
- The token value must match the backend’s `ROUNDTABLE_OPERATOR_TOKEN`.
- Do not assume mutating actions are available without operator access.
```
