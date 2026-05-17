# Lovable Roundtable UI Spec

> Updated: 2026-05-16

## Goal

This spec translates the current local `app/static/roundtable.html` prototype into a cleaner interface that Lovable can reproduce with stronger product structure and less prototype feel.

## Product Position

The page is not a chatbot. It is a live geopolitical simulation console.

The emotional frame should be:
- strategic
- editorial
- high-stakes
- legible under long-form output

The page should make it obvious that:
- agents are grounded in live wiki sources
- multiple actors are in contention
- the human can redirect the exchange
- summaries and wiki proposals are second-order products of the session

## Information Architecture

Use a 2-column layout on desktop and a single-column stacked layout on mobile.

Desktop layout:
- Left: main interaction column
- Right: supporting intelligence column

Left column sections:
1. Header
2. Session Setup
3. Live Roundtable
4. Intervention and Shock controls

Right column sections:
1. Connection and session status
2. Knowledge Sources
3. Strategic Tensions
4. Session Summary
5. Wiki Proposals

## Visual Language

### Overall
- Dark interface
- Dense but readable
- Strong typographic hierarchy
- Avoid consumer-chat styling
- Use spacing and panel depth to distinguish strategic layers

### Accent Colors
- China: deep red
- United States: cold blue
- European Union: muted gold
- Human: slate
- System / shock: amber

### Typography
- Use one serious display face for headings if available
- Use a highly readable sans-serif for body copy
- Transcript body should optimize for 140-260 word turns

## Core Components

## 1. Header

Contents:
- `Daily Roundtable`
- subtitle: `Live wiki-grounded geopolitical AI session`
- compact status rail on the right:
  - backend status
  - mode
  - turn count
  - current session id

## 2. Session Setup Card

Contents:
- prompt textarea
- mode selector
- actor toggle chips
- include shared toggle
- primary start button

Behavior:
- Disabled while a start request is in flight
- After successful start, persist form state visibly

## 3. Live Roundtable Panel

This is the dominant visual element.

Requirements:
- vertically scrolling transcript
- message cards, not plain text blocks
- support very long responses without collapsing readability
- preserve timestamps
- show actor name prominently

Message alignment:
- China left
- U.S. right
- EU left
- Human right
- System centered

Message behavior:
- New turns append at the end in chronological order
- Do not reverse the visual order in a way that feels unnatural
- Auto-scroll only if the user is near the bottom

Footer action bar:
- Next Turn
- Generate Summary
- Generate Wiki Proposals
- optional future Auto mode toggle

## 4. Knowledge Sources Panel

Purpose:
- prove source-grounding visibly

Display:
- actor group heading
- source count
- collapsed by default
- expand to show file paths

Use pills for compact counts and an accordion for details.

## 5. Intervention Panel

Contents:
- multiline text input
- intervention type selector
- send button

Behavior:
- After successful send, append the human message to transcript immediately

## 6. Shock Panel

Contents:
- title
- content
- severity
- inject button

Behavior:
- After successful send, append a system event card to transcript immediately
- System cards should be visually louder than normal turns

## 7. Strategic Tensions Panel

Contents:
- next speaker
- last speaker
- active actors
- latest intervention
- latest shock

This panel is allowed to be a lightweight derived summary of frontend state.

## 8. Session Summary Panel

Render fields from backend summary:
- headline
- context
- points of agreement
- points of disagreement
- strategic options
- risks and unknowns
- recommended follow-ups

Use strong section dividers. Avoid giant uninterrupted text walls.

## 9. Wiki Proposals Panel

Render fields from backend proposals:
- target
- reason
- content preview when available

These should read like candidate intelligence memos, not generic list items.

## API Integration Rules

Frontend must call the backend for all live behavior.

Required calls:
- `POST /session/start`
- `GET /session/{session_id}`
- `POST /session/message`
- `POST /session/intervene`
- `POST /session/shock`
- `POST /session/{session_id}/summary`
- `POST /session/{session_id}/wiki-proposals`

Frontend must not:
- generate actor content itself
- invent actor memory
- build actor knowledge context

## State Model

Minimum frontend state:
- `apiBaseUrl`
- `sessionId`
- `mode`
- `actors`
- `loadedPages`
- `transcript`
- `summary`
- `wikiProposals`
- `isStarting`
- `isAdvancing`
- `isGeneratingSummary`
- `isGeneratingProposals`
- `error`

## Error States

Must handle:
- backend unreachable
- invalid session id
- failed turn generation
- failed summary generation
- empty source list

Use a persistent error banner near the header for connection failures.

## Mobile Behavior

On mobile:
- stack all panels vertically
- keep transcript first after session setup
- move Knowledge Sources below transcript
- pin the Next Turn button within easy thumb reach

## Notes On Porting From Current Prototype

Keep from `roundtable.html`:
- actor-specific transcript styling
- visible knowledge sources
- direct intervention and shock controls
- summary and proposals in-page

Change from `roundtable.html`:
- remove prototype-like plain form stacking
- stop hardcoding `http://127.0.0.1:8000` in the UI
- promote backend status into the header
- move to chronological transcript rendering
- make the layout feel like a strategic interface rather than a dev test page
