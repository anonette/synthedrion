# Lovable Connection Guide

> Updated: 2026-05-11

## Overview

This guide explains how to connect the Lovable frontend to the local runtime so that Lovable acts as the interface while the local backend reads the wiki directly and runs the agents.

## Assumptions

- The local backend is running at `http://127.0.0.1:8000`
- Lovable is used as the UI layer
- The local backend owns all knowledge-base reading and session logic

## What Lovable Should Do

Lovable should:

- collect the prompt
- collect selected actors
- show the session transcript
- allow human intervention
- allow shock injection
- display summaries and wiki proposals

Lovable should not:

- build actor context itself
- hardcode actor personalities
- persist hidden actor memory outside approved wiki updates

## Minimum Calls

Lovable should call:

1. `POST /session/start`
2. `POST /session/message`
3. `POST /session/intervene`
4. `POST /session/shock`
5. `POST /session/{id}/summary`
6. `POST /session/{id}/wiki-proposals`

## Basic Flow

1. User enters prompt and selects actors
2. Lovable sends data to `POST /session/start`
3. Lovable stores `session_id`
4. Lovable calls `POST /session/message` whenever the next turn should occur
5. User can intervene at any time using `POST /session/intervene`
6. User can inject shocks using `POST /session/shock`
7. When ready, Lovable calls `POST /session/{id}/summary`
8. Optionally, Lovable calls `POST /session/{id}/wiki-proposals`

## During Local Testing

If Lovable cannot directly call `127.0.0.1` from its environment, use Lovable only as a design/reference layer at first and test interaction through:

- `http://127.0.0.1:8000/docs`
- `http://127.0.0.1:8000/test`

## Recommended Lovable Page Structure

- `Today's Prompt`
- `Active Agents`
- `Knowledge Sources`
- `Live Roundtable`
- `Human Intervention`
- `Strategic Tensions`
- `Session Summary`
- `Promote to Wiki`

## Important Constraint

The local runtime must remain the source of truth for:

- actor reading rules
- context assembly
- session state
- long-term memory discipline

## See Also

- [Local Agent Runtime Architecture](local-agent-runtime-architecture.md)
- [Lovable Local API Specification](lovable-local-api-spec.md)
