# China Agent Evolution Workflow

> Sources: RAND, 2025-06-26; State Council, 2017-07-20; Xinhua, 2025-04-26; State Council, 2025-08-21; MIIT et al., 2026-01-07; CSET, 2026-03-02
> Raw: [Full Stack: China's Evolving Industrial Policy for AI](../../raw/reg-documents/2025-06-26-full-stack-chinas-evolving-industrial-policy-for-ai.md); [A New Generation Artificial Intelligence Development Plan](../../raw/reg-documents/2017-07-20-new-generation-artificial-intelligence-development-plan.md); [Politburo Collective Study on AI](../../raw/reg-documents/2025-04-26-politburo-collective-study-on-ai.md); [Opinions of the State Council on Deepening the Implementation of the "Artificial Intelligence+" Initiative](../../raw/reg-documents/2025-08-21-ai-plus-initiative-gov-cn.md); [Implementation Opinions on the "AI + Manufacturing" Special Initiative](../../raw/reg-documents/t0667_ai_manufacturing_opinions_EN.pdf); [CSET AI + Manufacturing Initiative Opinions](../../raw/reg-documents/2026-03-02-cset-ai-plus-manufacturing-initiative-opinions.md)
> Updated: 2026-05-11

## Overview

This is the simplest repeatable pattern for making the China agents more complex whenever you send a new link or document.

## Workflow

1. Add the source to `raw/reg-documents/`.
2. Extract only the delta: what does this source add or change about interests, instruments, strategies, fears, narratives, and visual style.
3. Update one or more of these pages:
- `china-ai-strategic-interests.md`
- `chinese-ai-policy-instruments.md`
- `chinese-ai-operational-strategy.md`
- `china-ai-simulation-profile.md`
- `china-agents-for-synthedrion.md`
4. If the source adds rhetoric, symbolism, or public style, also update `china-propaganda-generation-template.md`.
5. Refresh `wiki/index.md` and `wiki/log.md`.

## What To Extract From Every New Source

- Interests: what goal is being pursued
- Instruments: what tools are being used
- Strategy: how deployment or coordination is supposed to happen
- Constraints: what bottlenecks, fears, or tradeoffs appear
- Rhetoric: what slogans, metaphors, legitimacy claims, or ideological language recur
- Visual motifs: what sectors, workers, machines, landscapes, enemies, or futures are being imagined
- Jurisdictional claims: what the source says counts as strategically Chinese even across borders

## Minimal Update Block

Use this block whenever you send me a new source:

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

## Fastest Possible Instruction

If you want speed over ceremony, just send:

```text
Add this to the China agents and extract new strategy, rhetoric, and propaganda motifs: [URL]
```

## Complexity Rule

The agents should not just accumulate facts. Each new source should change at least one of these:

- what an agent wants
- what an agent fears
- what an agent treats as legitimate action
- how an agent talks
- what imagery or affect the agent can generate

## See Also

- [China Agents for Synthedrion](china-agents-for-synthedrion.md)
- [China Agent Prompt Template](china-agent-prompt-template.md)
- [China Propaganda Generation Template](china-propaganda-generation-template.md)
