# Summary for the feed's collaborator — how your DPRK incident data is being used

Quick writeup of what we did with the `sandbox.hacksleuths.com/feed` data, exactly how it's used, and the
prompts touching it — so you can tell us if anything should change.

## What we built

Your feed (~208 DPRK-attributed crypto-theft incidents, 2020–2026, `id`/`attribution{state,group,confidence}`/
`target`/`amount_usd`/`vector`/`summary`/`references`) is the "reality layer" for a mode called **mirror-world**
in an AI-geopolitics roundtable simulator. Each mirror-world session:

1. Picks one incident from your feed (see "Incident selection" below).
2. Seeds a debate between three AI-persona actors (China / US / EU) with that incident.
3. Each actor generates a **three-part turn**: their *official line* (the sanctioned denial/spin), the
   *buried reality* (what actually happened, grounded in your data), and a satirical *speculation* about where
   it goes next.
4. On close, a "mirror-card" renders a tabloid-style summary (headline, dispatch, the three layers side by side).
5. Optionally, a 4th persona ("James," a Machiavellian crypto-native analyst) reads the finished transcript and
   adds one closing counter-take — 3-4 punchy sentences, calibrated to your feed's own stated confidence score,
   forced to name a specific crypto/blockchain mechanism (laundering pathway, DeFi exploit, exit liquidity,
   custody failure) rather than staying at the level of generic geopolitics.

Everything downstream treats attribution as a **sourced claim at a stated confidence, never asserted fact** —
that framing is baked into every prompt below.

## Incident selection (as of 2026-07-19)

Originally every session used whatever file was "latest" by date — which meant only 1 of your 208 records was
ever actually used, since our pre-existing sample incident happened to be dated after all of yours. Fixed:

- Default now picks **randomly** across the whole set, so sessions actually sample your data instead of one file.
- `incident_id` can also be passed to pin a specific case (e.g. `"CHA-Ronin-Network-149"`).

## The exact seed prompt (this is the part that touches your data directly)

`app/threat_intel.py::prompt_from_incident()` — built straight from your fields:

```
MIRROR-WORLD INTELLIGENCE (reality layer — sourced claim at {confidence} confidence): {target} lost
{amount_usd} in a {state}-attributed operation ({group}) via {vector}. {summary}

DATASET CONTEXT: this is one of {N} tracked incidents (combined modeled losses over ${total}); its
{confidence} attribution confidence is [notably more solid than / roughly in line with / notably weaker
than] the dataset's own median of {median_confidence}, and only {vector_known}/{N} incidents in the set
even have a known attack vector. The most-named group across the set is {top_group}.

The official story and the regulations will say something cleaner. Stage the clash between what actually
happened and what each actor claims — including whether this case is representative of the pattern or a
convenient outlier — then extrapolate where this absurdly goes next.
```

The "DATASET CONTEXT" paragraph is new — it's computed live across all your records
(`app/threat_intel.py::dataset_stats()`) so each session isn't just reacting to one anecdote, it's reacting to
where that anecdote sits in your actual dataset.

## What we found digging into the full 208 records (you may want to know this)

- **Attribution confidence skews low**: median is **0.14** across records with a numeric confidence score; only
  ~11 sit at 0.80+ ("high"). Most of the dataset is contested/low-confidence, even though the framing (and the
  region label) reads as a settled "DPRK crypto-theft programme." Not a criticism of the data — just worth
  knowing it's driving a lot of the narrative tension we're generating from it.
- **Group breakdown**: APT38 is actually your most-named group (92 records), ahead of "Lazarus Group" (63) —
  interesting since Lazarus is the popularly-known name but APT38 dominates your attribution field.
- **`vector` is "unknown" on ~192/208 records** (confirmed via the live API response itself, not an ingestion
  bug on our end) — if attack-technique categorization is something you're still filling in, that's the field
  with the most room to grow; right now it's the weakest-populated field we use.
- **`state` has two spellings** — "DPRK" and "North Korea" — same country, inconsistent label. Harmless for us
  (we treat them the same), but flagging in case it's an easy normalize on your end.
- **Total modeled losses across the set: ~$10.4B**, median per-incident ~$7.5M, max ~$1.44B (ByBit, Feb 2025 —
  checks out against public reporting).

## James's prompt (the part most likely to need your input) — updated 2026-07-20

`app/llm.py` — persona + the instruction that uses your confidence score directly:

> "The feed's own attribution confidence here is {confidence} — [genuinely solid / genuinely contested /
> barely more than a guess]. [Calibrated instruction: don't manufacture fake doubt about a solid attribution;
> vs. explicitly call out anyone treating a low-confidence claim as settled fact.]"

This is the one place your `confidence` field directly steers tone, not just content — so if you'd rather we
not editorialize on confidence at all (e.g. if low scores mean "still investigating" rather than "weak
evidence"), that's a one-line change on our side, just tell us.

He's also now forced to translate whatever's being discussed into a concrete crypto/blockchain mechanism (a
rotating pool: laundering pathway, DeFi exploit, exit liquidity, custody failure, etc.) rather than staying at
the level of generic policy language — and capped at 3-4 sentences, no throat-clearing. Real example, generated
against one of your actual records (a $54.3M CoinEx incident, 0.12 confidence):

> "CoinEx's $54.3M hit isn't a DPRK magic trick; it's the liquidity vacuum left when global compute sovereignty
> is a house of cards... That 0.12 attribution confidence is smoke and mirrors laundering narrative certainty
> for compliance vendors and EU regulators' theater — they sell control by selling the illusion of control...
> CoinEx's users and LPs are the real bagholders in this cross-border compute power play."

So your `confidence` number isn't just informing his tone anymore — it's the specific number he calls out by
name when he thinks an actor is overstating certainty your own data doesn't support.

## Open questions for you

1. Is `vector` something you plan to backfill, or is "unknown" often the honest answer from your sources?
2. Should "DPRK" vs "North Korea" be normalized on your end, or should we just keep normalizing on ours?
3. Any incidents in the 208 you'd flag as *wrong* attribution rather than *uncertain* — i.e. should be pulled
   rather than just carrying a low confidence score?
4. Anything about how we're using `confidence` (see James's prompt above) that misrepresents how confident you
   actually are in the underlying analysis?

Happy to adjust any of the above — this doc mirrors exactly what's live right now, not a proposal.
