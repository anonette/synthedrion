# Lovable Local API Specification

> Updated: 2026-05-11

## Overview

This document defines the minimal API contract between the Lovable frontend and the local agent runtime.

The API should support:

- synchronous live sessions
- actor-specific runtime reading
- human intervention during sessions
- summaries and archive retrieval
- proposed wiki updates

## General Rules

- The frontend does not build the actor context itself.
- The backend reads the wiki directly from the local filesystem.
- The frontend sends scenario instructions and user interventions.
- The backend returns agent turns, session state, summaries, and wiki proposals.
- The backend may use actor-specific model routing internally, but the frontend should treat that as an implementation detail.

## Session Object

Each session should minimally track:

- `session_id`
- `created_at`
- `mode`
- `actors`
- `prompt`
- `status`
- `turn_index`
- `transcript`
- `loaded_pages`
- `summary`
- `wiki_proposals`

## Endpoints

### `POST /session/start`

Starts a live session.

Request body:

```json
{
  "prompt": "Today's geopolitical question or scenario.",
  "actors": ["china", "us", "eu"],
  "mode": "debate",
  "include_shared": true
}
```

Response body:

```json
{
  "session_id": "sess_123",
  "status": "running",
  "actors": ["china", "us", "eu"],
  "mode": "debate",
  "loaded_pages": {
    "china": ["wiki/china-ai-policy/china-ai-knowledge-base-hub.md"],
    "us": ["wiki/us-ai-policy/us-ai-knowledge-base-hub.md"],
    "eu": ["wiki/eu-ai-policy/eu-ai-knowledge-base-hub.md"],
    "shared": ["wiki/shared-ai-geopolitics/shared-ai-geopolitics-and-governance.md"]
  }
}
```

### `POST /session/message`

Advances the session by one step or requests the next set of agent turns.

Request body:

```json
{
  "session_id": "sess_123"
}
```

Response body:

```json
{
  "session_id": "sess_123",
  "turn_index": 4,
  "messages": [
    {
      "actor": "china",
      "content": "..."
    },
    {
      "actor": "us",
      "content": "..."
    }
  ],
  "status": "running"
}
```

### `POST /session/intervene`

Allows a human to intervene during the live session.

Request body:

```json
{
  "session_id": "sess_123",
  "content": "You are ignoring labor instability. Reassess from that angle.",
  "type": "question"
}
```

Possible `type` values:

- `question`
- `challenge`
- `redirect`
- `source`
- `shock`

Response body:

```json
{
  "session_id": "sess_123",
  "accepted": true,
  "status": "running"
}
```

### `POST /session/shock`

Injects an explicit scenario shock.

Request body:

```json
{
  "session_id": "sess_123",
  "title": "Compute outage",
  "content": "A major allied cloud region experiences an unexpected disruption.",
  "severity": "high"
}
```

### `GET /session/{session_id}`

Returns the full current state of a session.

Response body:

```json
{
  "session_id": "sess_123",
  "status": "running",
  "mode": "debate",
  "actors": ["china", "us", "eu"],
  "prompt": "...",
  "turn_index": 4,
  "transcript": [],
  "loaded_pages": {},
  "summary": null,
  "wiki_proposals": []
}
```

### `POST /session/{session_id}/summary`

Generates a session summary.

Response body:

```json
{
  "session_id": "sess_123",
  "summary": {
    "agreements": [],
    "disagreements": [],
    "strategies_explored": [],
    "candidate_wiki_updates": []
  }
}
```

### `POST /session/{session_id}/wiki-proposals`

Generates candidate wiki updates, but does not write them automatically.

Response body:

```json
{
  "session_id": "sess_123",
  "wiki_proposals": [
    {
      "target": "wiki/china-ai-policy/chinese-ai-labor-and-social-stability.md",
      "reason": "New argument about staged adoption under labor risk",
      "content": "..."
    }
  ]
}
```

## Frontend Requirements

The Lovable page should surface:

- selected actors
- session mode
- current prompt
- currently loaded wiki pages
- live transcript
- human intervention box
- summary box
- proposed wiki updates

## Session Modes

Supported mode values:

- `debate`
- `negotiation`
- `crisis`
- `policy-planning`
- `propaganda-lab`

The backend should slightly alter turn behavior based on mode, but not change the core reading rules.

## Reading Scope Reporting

Each session should expose which pages were actually loaded so the frontend can show a `Knowledge Sources` panel. This helps users trust that the agents are reading from the wiki rather than from hidden fixed persona prompts.

## Memory Contract

- No hidden long-term memory outside session state
- No fixed persona cards required for baseline operation
- Long-term change only through approved wiki updates

## Failure Handling

The backend should gracefully report when:

- an actor hub is missing
- no readable pages were found under an actor scope
- a page link resolves outside allowed reading paths
- a summary or wiki proposal could not be generated

## See Also

- [Local Agent Runtime Architecture](local-agent-runtime-architecture.md)
- [Shared AI Geopolitics and Governance](../shared-ai-geopolitics/shared-ai-geopolitics-and-governance.md)
