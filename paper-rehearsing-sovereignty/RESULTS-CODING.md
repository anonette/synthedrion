# Results: discourse coding of the debate corpus

First-pass computational discourse analysis, transparent dictionary coding over
the substantive debate sessions (mode=debate, >=6 agent turns, test/junk prompts
excluded). Corpus: 37 sessions, 900 agent turns. Coding is reproducible from
`code_debates.py`; the codebook is grounded in the genealogy (Fearon signal,
Ezrahi fiction, the materialist and rules/market registers, the casting power
lens). Measurement is reported here separately from interpretation, which follows
each table. No em-dashes.

Status: dictionary coding is a first pass. LLM-assisted coding against the same
codebook, with human validation of a sample, is the next step and is required
before any of these rates is reported as a finding rather than a signal.

---

## Finding 1. The three agents produce distinguishable discourse

Code rate per 1000 words, by actor:

| code | CHINA | US | EU |
|---|---:|---:|---:|
| signal_resolve | 10.64 | **16.90** | 9.58 |
| fiction_future | 1.88 | 2.04 | 2.30 |
| material_stack | 27.17 | **36.39** | 34.47 |
| dependence | 7.46 | **11.64** | 9.77 |
| rules_regulation | 10.06 | 7.44 | **13.45** |
| market_innovation | 6.30 | **12.49** | 7.96 |
| accusation | **7.18** | 4.53 | 2.79 |
| concession | 0.60 | 0.92 | 0.55 |
| refusal | 0.66 | 0.51 | 0.44 |
| hedge_modality | 0.38 | 0.75 | 0.82 |

Avg turn length (words): China 161, US 138, EU 181.
Distinctive vocabulary (log-odds over the other two, min count 5):
- **US**: tout, velocity, leverages, shackled, flaunt, parade, kumbaya, eagle, tethered
- **EU**: aramco, ally, colleague, mubadala, disclose, comply, negotiating, addiction
- **China**: (formatting artifact, see Finding 4) then: concern, speaks

**Interpretation.** The agents are separable, and they separate along the axes
their design intended. The US register is resolve, market, and hardware: highest
signal_resolve, market_innovation, and material_stack, with a mocking distinctive
vocabulary (tout, parade, kumbaya). The EU register is institutional: highest
rules_regulation, the longest and most hedged turns, the lowest accusation rate,
and a distinctive vocabulary of compliance and named Gulf counterparties (Aramco,
Mubadala) it is courting. The China register is grievance: the highest accusation
rate, oriented to hypocrisy and containment. This matters for the thesis because
it satisfies the validity condition for synthetic rehearsal stated in
ARGUMENT.md: distinct models on distinct corpora produce distinct discourse
rather than one machine in three hats. Had the profiles collapsed into one, the
rehearsal would be staging nothing about the discourse. They do not collapse.

**Rival explanation to keep open.** Distinguishability here is consistent both
with the agents genuinely enacting different sovereignty imaginaries and with the
corpora simply imprinting different vocabularies. The two are not separated by
this table; the reflexive-prompt sessions are where we test it.

---

## Finding 2. Human intervention shifts the discourse from posture to concession

Code rate per turn, baseline turns (n=836) versus turns immediately after a human
or guest-agent intervention (n=64):

| code | baseline | after intervention | change |
|---|---:|---:|---:|
| concession | 0.083 | 0.438 | **+430%** |
| signal_resolve | 1.937 | 1.781 | -8% |
| accusation | 0.786 | 0.562 | -28% |
| refusal | 0.089 | 0.047 | -47% |
| hedge_modality | 0.106 | 0.062 | -41% |
| material_stack | 5.246 | 4.500 | -14% |
| market_innovation | 1.408 | 1.125 | -20% |

**Interpretation.** This is the paper's core empirical claim in miniature. When
the room intervenes, whether a human question or a summoned guest, the very next
agent turn moves away from adversarial posture (accusation down 28 percent,
refusal down 47 percent) and toward common ground (concession up more than
fourfold). The performance of resolve is not self-sustaining; it is maintained,
and it gives when contested. This is maintenance-under-contestation made visible,
the thing a retrospective reading of finished announcements cannot show. It is
also the operational payoff of treating the human interveners as the instrument's
active variable rather than as noise.

**Caveats, load-bearing.** Only 64 post-intervention turns exist in the whole
corpus, and the baseline concession rate is very low (0.083 per turn), so the
+430 percent rides on a small absolute change and is volatile. Report the
absolute counts alongside the percentage. Direction of the shift is the robust
part; the magnitude is provisional. Establishing this properly needs more
sessions with deliberate, coded interventions, which is a live experiment the
apparatus is built to run.

---

## Finding 3. The debate is US-centric, and the EU and China do the casting

References to other blocs, per 1000 words:

| speaker | names China | names US | names EU |
|---|---:|---:|---:|
| CHINA | - | 10.68 | 12.52 |
| US | 13.41 | - | 5.65 |
| EU | 9.14 | 12.24 | - |

Casting third parties as object (Gulf, Global South, Taiwan, etc.) per 1000w:
China 6.36, US 3.88, EU 6.95.

**Interpretation.** The United States is the gravitational center: it is the most
named actor overall, and it names China back most heavily, so the axis of the
room is US-China with the EU orbiting. The casting measure sharpens the power
lens (Ajibona). It is the EU and China, not the US, that most often invoke the
states caught in the middle, the EU while courting Gulf capital by name, China
while claiming the Global South. The US talks least about the actors it is not.
Whose sovereignty gets performed as agency and whose gets invoked as terrain is
itself patterned, and the pattern is measurable.

---

## Finding 4. A methodological finding: one model breaks frame

The China agent's distinctive-vocabulary list is dominated by tokens like
summary, postscript, moderator, meta, brackets, each appearing 527 times. These
are not content. They are scaffolding the underlying model (deepseek-chat-v3)
emits, meta-commentary and bracketed stage directions that leak into the turn
text. This is a data-quality issue to clean before final coding, and it is also a
finding in its own right: the models do not perform sovereignty uniformly. One of
them repeatedly steps outside the role to annotate its own output. For a paper
about performance, an agent that breaks the fourth wall is not only noise; it is a
visible seam in the staging, and worth a sentence in the discussion.

---

## What to run next (the coding programme)

1. **Clean the frame-break artifact** and re-run, so China's profile reflects
   content not scaffolding.
2. **LLM-assisted coding** of every agent turn against this codebook, with two
   coders (the model and a human) on a sample and an agreement statistic, to move
   from dictionary hits to validated codes.
3. **Deliberate intervention experiment**: run matched sessions with and without
   guest summons at fixed turns, to test Finding 2 with adequate n.
4. **Reflexive-prompt test** for Finding 1's rival explanation: does claimed
   inter-agent difference survive when the prompt tells the agents they share
   training data.
5. **Cross-register tracing**: follow one proposition (compute sovereignty) from
   debate to poster to mirror-world to satire, per INTERPRETING-THE-LOGS.md, and
   report what each rendering keeps and drops.
