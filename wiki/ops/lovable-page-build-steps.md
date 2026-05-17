# Lovable Page Build Steps

> Updated: 2026-05-12

## Overview

This is the concrete step-by-step translation of the local runtime flow into a Lovable page. The page should remain only the interface layer. The local backend should continue to own actor reading, context assembly, turn logic, and wiki-memory discipline.

## Goal

Build a `Daily Roundtable` page that lets a human run live, synchronous sessions with China, U.S., and EU agents whose positions are derived from the wiki at runtime.

## Step 1: Create the Page Shell

Create a page called `Daily Roundtable`.

Add these sections in order:

1. `Today's Prompt`
2. `Session Type`
3. `Active Agents`
4. `Knowledge Sources`
5. `Live Roundtable`
6. `Human Intervention`
7. `Strategic Tensions`
8. `Session Summary`
9. `Promote to Wiki`

## Step 2: Build the Session Setup Form

Inputs:

- prompt text area
- mode selector with:
  - debate
  - negotiation
  - crisis
  - policy-planning
  - propaganda-lab
- actor toggles:
  - china
  - us
  - eu
- start session button

On submit, call:

- `POST /session/start`

Store:

- `session_id`
- `mode`
- `actors`
- `loaded_pages`

## Step 3: Show the Knowledge Sources Panel

After session start, render `loaded_pages` as a visible source list.

This matters because users need to see that:

- the agents are reading the wiki live
- the agents are not relying on hidden fixed personas

## Step 4: Build the Live Roundtable Area

Add:

- transcript container
- `Next Turn` button

When clicked, call:

- `POST /session/message`

Append returned agent messages to the transcript.

## Step 5: Add Human Intervention

Add:

- intervention text area
- intervention type selector:
  - question
  - challenge
  - redirect
  - source
  - shock
- submit button

Call:

- `POST /session/intervene`

The intervention should become part of the live session state but should not become hidden long-term memory.

## Step 6: Add Shock Injection

Add:

- shock title
- shock content
- severity selector
- inject button

Call:

- `POST /session/shock`

## Step 7: Build Summary Section

Add a `Generate Summary` button.

Call:

- `POST /session/{id}/summary`

Render the returned summary into:

- agreements
- disagreements
- strategies explored
- candidate wiki updates

## Step 8: Build Promote to Wiki Section

Add a `Generate Wiki Proposals` button.

Call:

- `POST /session/{id}/wiki-proposals`

Display proposals clearly, but do not auto-write them.

## Step 9: Preserve the Memory Rule

The page should respect the agreed memory contract:

- sessions are synchronous and live
- humans can intervene
- long-term memory only changes through approved wiki updates

Do not add hidden persona persistence.

## Step 10: Nice-to-Have Enhancements

After the basic page works, add:

- actor color-coding in transcript
- timer / round count
- collapsible knowledge sources panel
- transcript export
- archive view using `GET /session/{id}`

## See Also

- [Lovable Connection Guide](lovable-connection-guide.md)
- [Lovable Local API Specification](lovable-local-api-spec.md)
- [Local Agent Runtime Architecture](local-agent-runtime-architecture.md)
- [Propaganda Lab Mode](propaganda-lab-mode.md)
