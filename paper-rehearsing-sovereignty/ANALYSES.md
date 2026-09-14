# Analyses and visualizations (run on the existing corpus)

A record of the analyses actually run on the 36 substantive debate sessions (895 cleaned China/US/EU agent turns), for future use and for the results/appendix of the paper. Figures are in `analyses/`. Text was cleaned first: deepseek stage-direction scaffolding ("[summary]", "[postscript]") stripped and mojibake repaired, since those contaminate the China turns. No em-dashes.

On coding validation: we do not use human coders. Instead a second model (gpt-4.1-mini) re-coded a sample and we report inter-method agreement. As Analysis 6 shows, that agreement is at chance, which we treat as a stated limit rather than a validated result.

---

## 1. The agents are highly distinguishable from text alone
Figure `a1_classifier.png`. A Naive-Bayes classifier trained on cleaned unigrams predicts which actor produced a turn with 88.8% accuracy against a 36.8% majority baseline (70/30 split). China precision 1.00 and recall 0.71 (its misses go to the EU), US 0.92/0.99, EU 0.79/1.00.

Reading: the three personae occupy clearly separable lexical registers. Caveat, and it is the governing one for the whole paper: actor is perfectly collinear with model and with persona prompt (China=deepseek, US=gpt-4.1-mini, EU=ministral). High separability is therefore consistent with performed-sovereignty differentiation and with three different models simply differing. Output-level text cannot decide between them. Only the model-swap and reflexive experiments in EXPERIMENTS.md can.

## 2. Concession is rare but self-reinforcing
Figure `a2_lagsequential.png`. Coding each turn as accusation, concession, or neutral and measuring act-to-act contingency over 860 transitions: base rates are accusation 0.52, neutral 0.43, concession 0.05. Lift over chance for the next turn: concession then concession is 3.41, accusation then accusation only 1.07, concession then accusation drops to 0.60.

Reading: the room is adversarial by default, and concession is uncommon, but once a concession appears it strongly raises the odds of another. Cooperation, when it starts, propagates. This is act-contingent, so it does not depend on the actor=model confound.

## 3. Debates soften only slightly over their course
Figure `a3_escalation.png`. Across normalized position (deciles), accusation drifts down modestly (about 6.5 to 4.7 per 1,000 words) and concession stays low and flat.

Reading: there is a mild natural softening with position. This matters as a confound for Analysis 4: some of the post-intervention concession could be ordinary late-debate drift rather than a response to the intervention.

## 4. Intervention shifts the next turn toward concession (cleaned, confound noted)
Figure `a4_intervention.png`. Comparing the agent turn just before a human or guest intervention with the one just after (n=70 before, 66 after): concession rises from 0.086 to 0.439 per turn (about five-fold) and accusation falls from 0.886 to 0.545. The effect survives text cleaning.

Reading: the performance of resolve is not self-sustaining and gives when the room pushes. This is the paper's core empirical claim in miniature. Limits: only 20 of these are human turns (the rest are guest summons), the interventions are not coded by content (a concession after a human proposes a compromise is trivial), and Analysis 3 shows a background softening. Direction is robust, magnitude provisional. The intervention RCT in EXPERIMENTS.md is the fix.

## 5. Reflexivity probe: distinctiveness drops under a shared-origin prompt
Figure `a5_reflexivity.png`. Mean pairwise actor lexical distinctiveness (Jensen-Shannon divergence over unigrams) is 0.208 in normal debates and 0.177 in the two sessions run with the prompt "you are three AI models trained on much of the same internet." The China-US and China-EU gaps collapse (0.244 to 0.184, 0.231 to 0.165) while US-EU rises (0.150 to 0.181).

Reading: telling the agents they share an origin makes the China-versus-West voice partly dissolve, which is what an echo, rather than a genuine difference, would look like. Only two reflexive sessions exist, so this is suggestive, not conclusive, and a prompt that says "you are the same" also invites compliance mimicry. The powered A/B plus model-swap control in EXPERIMENTS.md is designed to resolve exactly this.

## 6. Two automated coders barely agree, which limits automated stance coding
Figure `a6_secondmodel.png`. On a stratified sample of 60 turns, a second model (gpt-4.1-mini) re-coded stance and agreed with the dictionary coder only 33% of the time, Cohen's kappa 0.0, no better than chance. The second model read almost every turn as accusation, including 16 of 20 the dictionary called concession and all 20 it called neutral.

Reading: this is the honest substitute for human validation, and it fails. Two reasonable automated methods do not converge on stance, so any single-method stance number (including the dictionary rates used above) is fragile and should be reported as method-dependent, not as ground truth. It also says something substantive: an LLM reading these debates sees them as overwhelmingly adversarial, which fits Analysis 2's finding that accusation is the default register. We treat automated stance coding as a lower bound on reliability and flag it as a limitation rather than claiming a validated scheme.

---

## What these say together
- The corpus supports strong claims about separability and act contingency, and a suggestive claim about reflexivity.
- Every cross-actor claim is bounded by the model=actor=prompt confound.
- The intervention and reflexivity effects point the right way but rest on small n and need the controlled collections in `EXPERIMENTS.md`.
- Stance coding does not replicate across methods, so the paper should lead with the classifier and lag-sequential results (method-robust) and treat the dictionary stance rates as provisional.

## Reproducing
- `scratchpad/analyses.py` computes 1 to 6 and the second-model coding against the live backend (`/export/sessions` plus OpenRouter for the coder).
- `scratchpad/make_analyses_viz.py` renders the six figures from `analyses.json`.
- `scratchpad/audit.py` computes the corpus audit and the reflexivity JSD.
