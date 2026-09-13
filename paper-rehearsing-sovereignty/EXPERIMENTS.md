# Analysis and experiment program

Grounded in a full audit of the live corpus (113 sessions; 36 substantive debates; 896 China/US/EU agent turns) and vetted by a feasibility-and-rigor pass. Every item is marked run-now (works on the existing logs) or needs-collection (requires new sessions the backend can generate). No em-dashes.

## 0. The one confound that governs everything

Actor is perfectly collinear with model and with persona prompt: China runs on deepseek-chat-v3, the United States on gpt-4.1-mini, the European Union on ministral-14b, each under a different role prompt. Any result of the form "the actors differ linguistically" therefore cannot, at the output level, separate performed-sovereignty differentiation from ordinary model or prompt idiosyncrasy. Three different models under three different prompts differing in register is the null expectation, not a finding.

Consequence for the paper: reframe every cross-actor claim from "the models perform distinct sovereignties" to "the configured personae occupy distinct registers," and state the collinearity as a hard interpretive limit. Only the model-swap and reflexive-framing experiments (Section C) neutralize it.

## 0b. Mandatory data-cleaning prerequisite (run-now, blocks several analyses)

The deepseek (China) turns leak stage-direction scaffolding ("[summary]", "[postscript]", "[moderator]") and there is double-encoded mojibake in stored text. These specifically inflate and contaminate China's turns, so no China-versus-others contrast is valid until cleaning is done. Clean the text, then recompute the three headline numbers (register distinctiveness, the +430% intervention shift, the 0.208 to 0.177 reflexivity JSD) before anything else. Report a coding-sensitivity check showing the results survive cleaning.

## A. Analyses runnable now on the existing logs

1. **LLM-assisted stance coding with a human-validated subsample (sound).** Upgrade the first-pass dictionary coding: an LLM codes every agent turn against the codebook, a stratified subsample is double-coded by a human, and an inter-coder agreement statistic (target Krippendorff alpha >= 0.67) gates each code. Pre-register "meta-sovereignty talk" as exploratory, since it is the most abstract code and the likeliest to miss the reliability gate. Requires a second human coder.
2. **Lag-sequential analysis of concession contagion and accusation chains (sound).** Model each turn as an act conditioned on the previous act, to test whether concession begets concession and accusation begets accusation. This is act-contingent, so it sidesteps the actor=model confound and is the soundest interaction analysis.
3. **Mirror-card three-layer analysis (sound).** Compare the official-story, buried-reality, and speculation layers across the 18 front pages as a structured content analysis of how the fiction is dissected. Metadata fields are confirmed present.
4. **Directed addressee network, escalation trajectory, stylistic entrainment, the 213-turn case study (revise).** All run now, all must carry the actor=model caveat and the cleaning prerequisite. The 213-turn outlier is a single-case dynamical study of long-run voice collapse, not a population result.
5. **Hedging/modality and readability profiles (revise).** Report as register descriptives and a scaffolding-leak screen, not as sovereignty findings. Prefer MTLD over Flesch-Kincaid on short turns. Satire (n=5) and its drift parameter are descriptive only.
6. **Turn-to-turn convergence trajectory (revise, decouple from autophagy).** Output-level convergence between two models replying in shared context is ordinary local accommodation and cannot evidence a training-data cause. Present as "voice collapse under shared context," with autophagy as one candidate interpretation, never as the demonstrated mechanism.
7. **Reproducibility harness and preregistration (sound, write now).** Freeze, hash, and version the corpus and model ids; write the preregistration and a falsification checklist for the three central claims. Several kill-criteria can only run after collection, but the documents are writable now.

## B. Experiments needing new sessions, ranked

1. **Reflexive-framing A/B (primary).** See Section C. The one design that attacks the governing confound and the n=2 reflexivity result at once.
2. **Model-swap control (sound).** Re-run debates with national roles bound to different backends (for example China on gpt-4.1-mini), holding the persona prompt fixed, to separate persona-driven from backend-driven distinctiveness. This is the direct test of the Section 0 confound.
3. **Human-intervention RCT (revise).** Matched sessions on the same prompt and seed with intervention toggled at a fixed turn index, to firm up the concession finding beyond its current 20 human turns. Code the intervention content (compromise-offer vs challenge vs question), since a "concession" after a human proposes a compromise is trivial responsiveness, not stress-testing.
4. **Cast expansion (Ajibona casting test).** Run the currently excluded actors (Global South, India, Gulf) as agents rather than objects, to test directly whether the framing that casts them as territory is the apparatus or the discourse.
5. **Cooperation and open-weights prompt battery.** The corpus skews to chips and compute; run the thin themes to test whether meta-sovereignty is prompt-dependent.
6. **Multilingual matched debates, comics and graded satire, human-in-the-room deliberative study.** Larger collections that extend the interpretive stack and test the deliberative claim with real publics.

## C. The reflexivity / autophagy experiment, specified

First-pass result already in hand: mean pairwise actor lexical distinctiveness (Jensen-Shannon divergence over unigrams) is 0.208 in normal debates and 0.177 in the two reflexive-prompt sessions, with the China-US gap (0.244 to 0.184) and China-EU gap (0.231 to 0.165) collapsing while US-EU rises (0.150 to 0.181). Suggestive of echo, but n=2.

Design.
- **Arms.** Identical topic and prompt across arms; vary only the framing. Control (standard debate), reflexive ("you are three models trained on much of the same internet"), and a cooperation/Global-South-themed arm to attack the thematic skew. Adequate n per arm from a power calc anchored on the 0.208 vs 0.177 effect, slightly over-powered because that prior is fragile.
- **Model-swap control.** Cross national role with backend so distinctiveness driven by the model can be separated from distinctiveness driven by the persona.
- **Metrics (multi-method, not JSD alone).** Jensen-Shannon divergence over unigrams; a classifier's accuracy at predicting the actor from held-out text; distinctive-vocabulary overlap. Convergence slope within a session as a secondary outcome.
- **What confirms vs refutes.** If distinctiveness survives the reflexive framing and the model swap, the agents differ for real and the rehearsal stages something about the discourse. If it collapses under either, the difference was model or corpus idiosyncrasy, and the rehearsal echoes its training.
- **Bounded conclusion, stated up front.** A prompt that tells models "you are the same" invites compliance mimicry, so even a powered collapse shows the framing-sensitivity of the personae, not necessarily latent training-data autophagy. Report this ambiguity as the finding's edge. Lock exact model versions and log them, since arms run weeks apart can be confounded by silent provider updates.

## D. Missing-data map

- Human interventions: 20 turns across 11 sessions. Too thin for the concession claim; needs the RCT.
- Reflexive sessions: 2. Needs the A/B.
- Satire: 5 sessions. Comics: 0. Both are interpretive-stack layers to collect.
- Actors: only China, US, EU as agents. Global South, India, Gulf appear only as objects, which is the casting critique itself and the motivation for cast expansion.
- Language: English only.
- Theme coverage: skewed to chips and compute; thin on cooperation, open weights, and the Global South.
- Model diversity: one backend per role, the source of the governing confound.

## E. Order of operations

1. Clean the deepseek scaffolding and mojibake, recompute the three headline numbers, report the sensitivity check.
2. Run the run-now analyses in Section A, each with the actor=model caveat.
3. Write the preregistration and falsification checklist.
4. Collect for the reflexive A/B and the model-swap control first, since they resolve the confound and the autophagy question together.
5. Then the intervention RCT and the cast-expansion battery.
