# Lovable Roundtable Build Prompt

Paste the prompt below into Lovable when generating the interface.

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

Functional requirements:
- Use fetch to call a backend base URL from a config constant or environment variable.
- Do not hardcode localhost directly inside components.
- Maintain session_id in component state.
- Append each new returned message into transcript state.
- After starting a session, immediately fetch full session state to populate loaded wiki pages.
- Handle loading, disabled, empty, and error states.
- Show a connection error banner when the backend is unreachable.

Backend API contract:

POST /session/start
Request:
{
  "prompt": "China, US, and EU debate AI chip controls, compute dependence, and industrial strategy.",
  "actors": ["china", "us", "eu"],
  "mode": "debate",
  "include_shared": true
}

POST /session/message
Request:
{
  "session_id": "sess_123"
}

POST /session/intervene
Request:
{
  "session_id": "sess_123",
  "content": "Reassess from the perspective of labor stability.",
  "type": "question"
}

POST /session/shock
Request:
{
  "session_id": "sess_123",
  "title": "Compute outage",
  "content": "A major allied cloud region goes down.",
  "severity": "high"
}

GET /session/{session_id}

POST /session/{session_id}/summary

POST /session/{session_id}/wiki-proposals

Data notes:
- transcript messages include actor, content, timestamp, and kind
- actors are china, us, eu, human, or system
- kinds are agent, human, or system

Implementation preference:
- Build this as reusable React components.
- Create a small API helper module.
- Keep state management simple and local unless a shared store is clearly necessary.
- Preserve a strong editorial visual identity.
- Avoid generic chatbot tropes.
```
