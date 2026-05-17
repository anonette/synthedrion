# Local Agent Runtime Architecture

> Updated: 2026-05-11

## Overview

This document defines the preferred architecture for the AI Cold War simulation runtime. The agreed model is:

1. the knowledge base lives in this repository
2. agents read the knowledge base directly at runtime
3. Lovable is the interface layer, not the knowledge-reading engine
4. long-term agent memory exists only through approved wiki updates

The goal is to keep the agents autonomous, authentic, and dynamically grounded in the current wiki rather than in frozen persona templates.

## Core Design

The system should be split into two layers:

1. Local runtime/backend
2. Lovable frontend

The local runtime owns:

- filesystem access
- actor hub loading
- recursive page reading
- context assembly
- turn orchestration
- human intervention handling
- session summaries
- wiki update proposals

The runtime may optionally call external model APIs, but only after it has assembled actor context from the local wiki. Model choice should be actor-specific and runtime-configurable.

The Lovable frontend owns:

- session setup UI
- live roundtable display
- human intervention controls
- transcript display
- archive browsing
- wiki-promotion actions

## Actor Entry Points

The runtime should treat these pages as actor roots:

- China: `wiki/china-ai-policy/china-ai-knowledge-base-hub.md`
- U.S.: `wiki/us-ai-policy/us-ai-knowledge-base-hub.md`
- EU: `wiki/eu-ai-policy/eu-ai-knowledge-base-hub.md`
- Shared: `wiki/shared-ai-geopolitics/shared-ai-geopolitics-and-governance.md`

## Reading Rules

The runtime should enforce the following reading boundaries:

1. China agent may read:
- `wiki/china-ai-policy/`
- linked shared pages
- linked general pages such as `wiki/geopolitics/` and `wiki/ai-governance/` only when reached through allowed hub/shared links

2. U.S. agent may read:
- `wiki/us-ai-policy/`
- linked shared pages
- linked general pages only when reached through allowed hub/shared links

3. EU agent may read:
- `wiki/eu-ai-policy/`
- linked shared pages
- linked general pages only when reached through allowed hub/shared links

4. No agent may directly read rival actor folders unless an explicit future mode is added for comparative intelligence or adversarial reading.

## Runtime Context Assembly

For each session or turn:

1. load the actor hub
2. extract linked internal wiki pages
3. recursively follow allowed links
4. build a bounded working context from:
- actor-specific pages
- shared pages
- relevant linked general pages
5. assemble a live prompt from the currently loaded material

The runtime should prefer a small, relevant page set over dumping the entire wiki into context.

## Agent Behavior Contract

Agents should be derived from the wiki at runtime and should not rely on fixed persona cards.

Each agent should infer from its loaded pages:

- core goals
- fears
- legitimate actions
- strategic constraints
- preferred rhetoric
- internal contradictions

Each agent should sound like a mix of:

- realistic
- strategic
- ideological
- performative

This mix should vary with the scenario and source material rather than be hardcoded.

## Session Model

The agreed session model is synchronous live interaction.

Humans may:

- set the initial prompt
- intervene during the session
- inject new questions
- inject shocks or events

Agents should not retain hidden long-term memory outside the session.

Persistent memory should come only from:

- approved wiki updates
- optionally archived transcripts for human review, but not as direct hidden memory for the agents

## Turn Logic

Each substantive turn should internally do the following:

1. identify current goals from the loaded pages
2. identify constraints and red lines
3. identify multiple plausible strategies
4. evaluate tradeoffs
5. produce a position suited to the current round

The output should usually include:

- immediate position
- strategic reasoning
- preferred move
- what risk others are underestimating

## Human Intervention

The runtime should treat interventions as first-class events rather than normal chat messages.

Interventions may:

- redirect the topic
- force clarification
- introduce new evidence
- inject scenario shocks
- request narrower output modes such as memo, negotiation, or propaganda

## Wiki Update Discipline

Agents do not directly write to the wiki by default.

Instead, the runtime should produce proposed wiki deltas such as:

- changed assumptions
- new strategic disagreements
- new policy options
- new slogans or narratives
- unresolved tensions

Humans approve these before promotion into the knowledge base.

## Suggested Backend Stack

A practical local stack:

- Python + FastAPI
- filesystem access to this repository
- optional SQLite for session storage

Optional model integration:

- OpenRouter as the routing layer
- China -> DeepSeek
- U.S. -> OpenAI
- EU -> Mistral

Equivalent Node implementations are fine, but the most important requirement is reliable local file access and bounded link-following.

## Minimal Component Map

- `kb_loader`: load hub pages and linked markdown files
- `link_resolver`: enforce allowed read paths
- `context_builder`: assemble scenario-relevant context
- `agent_runner`: produce actor turns from current context
- `session_orchestrator`: manage turn order and timing
- `intervention_handler`: process human interventions
- `summary_builder`: generate end-of-session output
- `wiki_proposer`: create candidate wiki updates

## Success Criteria

The runtime is working correctly when:

1. agent outputs change as the wiki changes
2. agents stay inside their actor folder plus shared reading rules
3. agents feel authentic without relying on canned biographies
4. human interventions can redirect the session cleanly
5. only explicit wiki updates create long-term memory changes

## See Also

- [Lovable Local API Specification](lovable-local-api-spec.md)
- [China Agent Evolution Workflow](../china-ai-policy/china-agent-evolution-workflow.md)
- [Shared AI Geopolitics and Governance](../shared-ai-geopolitics/shared-ai-geopolitics-and-governance.md)
