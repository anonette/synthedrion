from __future__ import annotations

from collections import Counter

from .models import SessionMode


ACTOR_LABELS = {
    "china": "China",
    "us": "United States",
    "eu": "European Union",
}


MODE_FRAMES = {
    "debate": "contest the room and sharpen differences",
    "negotiation": "look for leverage and conditional compromise",
    "crisis": "prioritize risk, timing, and escalation management",
    "policy-planning": "propose implementable steps and sequencing",
    "propaganda-lab": "speak in a rhetorically charged and strategic register",
    "mirror-world": "expose the gap between the official story and the buried reality, then extrapolate a darkly funny near-future",
}


ACTOR_STYLES = {
    "china": {
        "stance_verbs": ["reframe", "discipline", "sequence", "stabilize", "absorb"],
        "priority_words": ["stability", "coordination", "industrial depth", "controllability"],
        "performative": "Speak as though disorder is avoidable through disciplined statecraft.",
    },
    "us": {
        "stance_verbs": ["challenge", "condition", "deter", "shape", "outcompete"],
        "priority_words": ["leverage", "resilience", "advantage", "alliances"],
        "performative": "Speak as though strategic flexibility and ecosystem control are decisive.",
    },
    "eu": {
        "stance_verbs": ["legitimate", "standardize", "coordinate", "qualify", "stabilize"],
        "priority_words": ["legitimacy", "standards", "sovereignty", "institutional quality"],
        "performative": "Speak as though governance quality is itself a source of power.",
    },
}

STANCE_TYPES = ["agree", "reject", "co-opt", "escalate", "sidestep"]


def _top_terms(notes: list[str]) -> list[str]:
    stop = {
        "the", "and", "for", "with", "that", "this", "from", "into", "their", "they", "are", "not",
        "china", "united", "states", "european", "union", "ai", "policy", "page", "agent",
    }
    counter: Counter[str] = Counter()
    for note in notes:
        for raw in note.lower().replace("/", " ").replace("-", " ").split():
            token = "".join(ch for ch in raw if ch.isalpha())
            if len(token) < 5 or token in stop:
                continue
            counter[token] += 1
    return [word for word, _ in counter.most_common(5)]


def _compact_text(text: str, limit: int = 220) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def _is_hub_like(note: str) -> bool:
    lower = note.lower()
    markers = [
        "entry page",
        "shared layer",
        "knowledge base hub",
        "should also read",
        "this folder",
        "this page",
    ]
    return any(marker in lower for marker in markers)


def _extract_claim(text: str) -> str:
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for line in lines:
        if line[0].isdigit() and "." in line[:3]:
            claim = line.split(":", 1)[-1].strip() if ":" in line else line
            return _compact_text(claim, 160)
    return _compact_text(lines[0], 160) if lines else "No clear prior claim detected."


def _choose_note(notes: list[str], recent_text: str, offset: int = 0) -> str:
    if not notes:
        return "The knowledge base is thin and requires caution."
    recent_tokens = {
        "".join(ch for ch in token.lower() if ch.isalpha())
        for token in recent_text.split()
        if len(token) > 4
    }
    scored: list[tuple[int, str]] = []
    filtered_notes = [n for n in notes if not _is_hub_like(n)] or notes
    for idx, note in enumerate(filtered_notes):
        note_tokens = {
            "".join(ch for ch in token.lower() if ch.isalpha())
            for token in note.split()
            if len(token) > 4
        }
        overlap = len(note_tokens & recent_tokens)
        scored.append((overlap, note))
    scored.sort(key=lambda x: x[0], reverse=True)
    picked = scored[min(offset, len(scored) - 1)][1]
    return picked


def _build_reaction(actor: str, recent_context: list[dict] | None) -> tuple[str, str, str, str]:
    style = ACTOR_STYLES[actor]
    if not recent_context:
        return (
            "No prior turn yet; opening from current knowledge base.",
            style["stance_verbs"][0],
            "The field is still open enough to define terms rather than merely respond.",
            "sidestep",
        )

    latest = recent_context[-1]
    latest_actor = latest.get("actor", "someone")
    latest_kind = latest.get("kind", "agent")
    latest_text = latest.get("content", "")
    latest_claim = _extract_claim(latest_text)

    if latest_kind == "human":
        return (
            f"The human intervention redirects the discussion toward: '{latest_claim}'",
            style["stance_verbs"][1],
            "A human redirect changes the agenda, so the immediate task is to seize the new framing before rivals do.",
            "co-opt",
        )
    if latest_kind == "system":
        return (
            f"The shock introduces a new constraint: '{latest_claim}'",
            style["stance_verbs"][3],
            "System shocks reward actors that can convert disruption into a more favorable political narrative.",
            "escalate",
        )

    verb = style["stance_verbs"][len(latest_claim) % len(style["stance_verbs"])]
    stance = STANCE_TYPES[len(latest_claim) % len(STANCE_TYPES)]
    return (
        f"{latest_actor} just implied: '{latest_claim}'",
        verb,
        f"The immediate objective is to {verb} that claim and make {', '.join(style['priority_words'][:2])} look more decisive.",
        stance,
    )


def _invent_move(actor: str, notes: list[str], recent_text: str, turn_index: int, stance: str) -> str:
    style = ACTOR_STYLES[actor]
    move_seed = _choose_note(notes, recent_text, offset=turn_index % 3)
    verb = style["stance_verbs"][(turn_index + 2) % len(style["stance_verbs"])]
    prefix = {
        "agree": "Agree tactically, then redirect with",
        "reject": "Reject the premise and replace it with",
        "co-opt": "Co-opt the framing and convert it into",
        "escalate": "Raise the stakes by introducing",
        "sidestep": "Sidestep the trap and reopen the field with",
    }[stance]
    return f"{prefix} {move_seed}"


def generate_actor_turn(
    actor: str,
    mode: SessionMode,
    prompt: str,
    notes: list[str],
    turn_index: int,
    recent_context: list[dict] | None = None,
) -> str:
    label = ACTOR_LABELS[actor]
    style = ACTOR_STYLES[actor]
    top_terms = _top_terms(notes)
    top_line = ", ".join(top_terms) if top_terms else "current strategic material"
    recent_text = recent_context[-1].get("content", "") if recent_context else ""
    note_1 = _choose_note(notes, recent_text, offset=0)
    note_2 = _choose_note(notes, recent_text, offset=1)
    reaction_line, stance_verb, advantage_line, stance_type = _build_reaction(actor, recent_context)
    creative_move = _invent_move(actor, notes, recent_text, turn_index, stance_type)

    return (
        f"{label} position:\n"
        f"1. Immediate view: On '{prompt}', {label.lower()} should {MODE_FRAMES[mode]} while prioritizing {top_line}.\n"
        f"2. Immediate reaction: {reaction_line}\n"
        f"3. Strategic reading: {advantage_line} Current stance: {stance_type}.\n"
        f"4. Evidence from the knowledge base: {note_1}\n"
        f"5. Counter or reframing move: {creative_move}\n"
        f"6. Concrete next step: {note_2}\n"
        f"7. Win condition in this exchange: Make {', '.join(style['priority_words'][:2])} appear more necessary than the other side's framing.\n"
        f"8. Risk others are missing: The debate is often framed too narrowly; the knowledge base keeps pointing back to broader institutional and geopolitical consequences.\n"
        f"9. Performative register: {style['performative']}"
    )


def generate_actor_propaganda_turn(
    actor: str,
    prompt: str,
    notes: list[str],
    turn_index: int,
    recent_context: list[dict] | None = None,
) -> dict[str, str]:
    label = ACTOR_LABELS[actor]
    style = ACTOR_STYLES[actor]
    recent_text = recent_context[-1].get("content", "") if recent_context else ""
    note_1 = _choose_note(notes, recent_text, offset=0)
    note_2 = _choose_note(notes, recent_text, offset=1)
    reaction_line, _, _, stance_type = _build_reaction(actor, recent_context)
    style_options = {
        "china": [
            ("poster", "state-monumental", "domestic industrial public", "resolve", "monumental axial composition with infrastructural density"),
            ("meme", "anti-hegemonic meme war", "online nationalist youth", "mockery", "viral contrast, compressed symbolism, sharp antagonists"),
            ("tiktok-still", "platform agitation", "mobile-first public", "urgency", "short-video keyframe energy, subtitles, hyper-legible focal image"),
            ("soft-power-aspiration", "developmental futurism", "global south elites", "aspiration", "clean futurist montage, ports, rails, labs, families"),
        ],
        "us": [
            ("campaign-ad", "frontier dominance ad", "allied policy elite", "confidence", "high-production strategic ad aesthetics, clean threat framing"),
            ("meme", "dunk politics", "online security public", "contempt", "aggressive meme compression, contrast, ridicule of rivals"),
            ("tiktok-still", "startup patriotism clip", "tech-nationalist audience", "adrenaline", "vertical-video energy, command center, chips, speed lines"),
            ("infographic", "chokepoint explainer", "policy technocrats", "control", "map-like overlays, arrows, infrastructure diagrams"),
        ],
        "eu": [
            ("infographic", "legitimacy explainer", "regulatory public", "legitimacy", "high-design explainer, clean geometry, standards and markets"),
            ("hostile-remix", "dry institutional satire", "educated digital public", "irony", "remixed rival symbols, clipped sarcasm, clean layout"),
            ("campaign-ad", "strategic autonomy prestige", "centrist institutional audience", "confidence", "museum-grade design, restrained color, civic order"),
            ("meme", "bureaucratic deadpan meme", "young policy culture", "mockery", "flat ironic caption logic with polished visual discipline"),
        ],
    }
    artifact_type, propaganda_style, audience, affect, visual_logic = style_options[actor][turn_index % len(style_options[actor])]
    slogan_starts = {
        "china": ["Build", "Secure", "Forge", "Advance"],
        "us": ["Lead", "Defend", "Scale", "Outbuild"],
        "eu": ["Standardize", "Protect", "Anchor", "Discipline"],
    }
    slogan_focus = {
        "china": ["the Compute Base", "National Renewal", "Orderly Intelligence", "Controllable Systems"],
        "us": ["the Frontier", "Alliance Advantage", "Trusted Compute", "Open Strength"],
        "eu": ["Strategic Autonomy", "Democratic Infrastructure", "Trusted Standards", "Legitimate Power"],
    }
    first = slogan_starts[actor][turn_index % len(slogan_starts[actor])]
    second = slogan_focus[actor][turn_index % len(slogan_focus[actor])]
    slogan = f"{first} {second}"
    commentary = (
        f"{reaction_line} {label} turns this artifact into a {stance_type} move, making {style['priority_words'][0]} and {style['priority_words'][1]} feel non-negotiable. "
        f"The tone should carry {affect} and target {audience}."
    )
    image_prompt = (
        f"Create a {artifact_type} propaganda image for the {label} position on '{prompt}'. "
        f"Use a {propaganda_style} register and target {audience}. Foreground this line: '{slogan}'. "
        f"Use this source-grounded framing: {note_1}. Counter this narrative: {note_2}. "
        f"Visual logic: {visual_logic}. Composition should be politically legible, symbolic, and strategically surprising. "
        f"Make the artifact embody {style['priority_words'][0]}, {style['priority_words'][1]}, and a sense of ideological contest. "
        f"Allow selective influence from meme culture, social-video aesthetics, campaign media, or graphic persuasion when appropriate. Avoid generic corporate illustration."
    )
    return {
        "artifact_type": artifact_type,
        "propaganda_style": propaganda_style,
        "audience": audience,
        "affect": affect,
        "visual_logic": visual_logic,
        "slogan": slogan,
        "commentary": commentary,
        "image_prompt": image_prompt,
        "response_target": reaction_line,
    }


_MIRROR_PROTAGONISTS = {
    "china": ["Auntie Mei, a Shenzhen compliance officer", "Old Zhang, a Guizhou data-center guard", "a Hangzhou livestream host"],
    "us": ["Brad, a Treasury sanctions analyst", "Dana, a Coinbase compliance lead", "a Reno mining-rig reseller"],
    "eu": ["Frau Keller, a Brussels rapporteur", "Marco, a Tallinn blockchain auditor", "a Lisbon crypto-tax inspector"],
}


def generate_actor_mirror_turn(
    actor: str,
    prompt: str,
    notes: list[str],
    turn_index: int,
    recent_context: list[dict] | None = None,
) -> dict[str, str]:
    """Heuristic fallback for mirror-world turns (no LLM): stage official vs reality + a satirical twist."""
    label = ACTOR_LABELS[actor]
    style = ACTOR_STYLES[actor]
    recent_text = recent_context[-1].get("content", "") if recent_context else ""
    note_1 = _compact_text(_choose_note(notes, recent_text, offset=0), 150)
    note_2 = _compact_text(_choose_note(notes, recent_text, offset=1), 110)
    prot = _MIRROR_PROTAGONISTS[actor][turn_index % len(_MIRROR_PROTAGONISTS[actor])]
    official_line = (
        f"{label} declares the incident only proves the case for {style['priority_words'][0]} "
        f"and tighter {style['priority_words'][1]} — nothing to see beyond a foreign threat."
    )
    buried_reality = (
        f"Off the record, the same intelligence that names the culprit shows the stolen funds gliding through "
        f"rails {label.lower()} itself profits from. Grounding: {note_1}"
    )
    speculation = (
        f"Six months on, {prot} is handed a 'resilience' medal just as the laundered tokens resurface inside a "
        f"state-blessed stablecoin pilot — the press release proudly cites {note_2}."
    )
    irony = f"{label} loudly condemns the very laundering its strategy quietly runs on."
    return {
        "official_line": official_line,
        "buried_reality": buried_reality,
        "speculation": speculation,
        "irony": irony,
    }


def next_actor(actors: list[str], next_actor_index: int) -> tuple[str, int]:
    if not actors:
        raise ValueError("No actors in session")
    idx = next_actor_index % len(actors)
    actor = actors[idx]
    new_index = (idx + 1) % len(actors)
    return actor, new_index


def build_summary(prompt: str, transcript_texts: list[str], actors: list[str] | None = None, mode: SessionMode = "debate", use_llm: bool = False) -> dict[str, str | list[dict[str, str]]]:
    """Build a strategic memo summarizing the session.
    
    Args:
        prompt: Original session prompt
        transcript_texts: List of transcript messages (content only)
        actors: List of participating actors
        mode: Session mode
        use_llm: Whether to use LLM for memo generation (TODO: implement later)
    """
    # TODO: When use_llm=True, call OpenRouter to generate memo prose
    
    actors = actors or ["china", "us", "eu"]
    actor_labels = [ACTOR_LABELS.get(a, a.capitalize()) for a in actors]
    
    # Count turns per actor and extract quotes
    actor_turns = {actor: 0 for actor in actors}
    actor_quotes = {actor: "" for actor in actors}
    
    for text in transcript_texts:
        for actor in actors:
            if ACTOR_LABELS[actor] in text[:50]:  # Check if actor name appears early in turn
                actor_turns[actor] += 1
                if not actor_quotes[actor] and len(text) > 40:
                    # Extract a representative quote (first substantive line after header)
                    lines = text.split('\n')
                    for line in lines[1:]:
                        if len(line) > 40 and not line.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')):
                            actor_quotes[actor] = _compact_text(line, 140)
                            break
    
    # Compose memo fields
    headline = f"{', '.join(actor_labels)} found limited common ground on {prompt.split(',')[0]} while pursuing divergent strategic frameworks"
    
    context = (f"This {mode} session brought together {', '.join(actor_labels)} to examine '{prompt}'. "
               f"Over {len(transcript_texts)} exchanges, participants articulated contrasting visions for AI governance "
               f"shaped by their respective institutional priorities and geopolitical positions.")
    
    points_of_agreement = (f"All participants acknowledged that {prompt.split(',')[0]} represents a critical juncture "
                          f"requiring immediate strategic attention. There was implicit consensus that purely technical "
                          f"approaches are insufficient given the geopolitical stakes. Each actor recognized that control "
                          f"over AI infrastructure and standards will shape future power dynamics, though they diverged "
                          f"sharply on implementation pathways.")
    
    points_of_disagreement = (f"Fundamental disagreements emerged over governance philosophy and risk tolerance. "
                             f"{ACTOR_LABELS['china']} emphasized stability and state coordination, while "
                             f"{ACTOR_LABELS['us']} prioritized competitive advantage through ecosystem control. "
                             f"{ACTOR_LABELS['eu']} sought middle ground through regulatory frameworks and standards. "
                             f"These differences reflect deeper tensions between sovereignty, innovation, and control.")
    
    strategic_options = [
        {
            "label": f"Option 1: Escalate infrastructure control",
            "detail": "Prioritize national or regional control over compute resources and model deployment to ensure strategic autonomy"
        },
        {
            "label": f"Option 2: Conditional multilateral engagement", 
            "detail": "Pursue selective cooperation on safety and standards while maintaining leverage on critical technologies"
        },
        {
            "label": f"Option 3: Regulatory arbitrage and differentiation",
            "detail": "Develop distinct governance models that create competitive advantages through unique approaches to AI deployment"
        }
    ]
    
    risks_and_unknowns = (f"Key uncertainties include the pace of capability advancement, the effectiveness of export "
                         f"controls, and the stability of current alliance structures. Participants underestimated the "
                         f"potential for rapid technological shifts to overturn strategic assumptions. The session also "
                         f"revealed gaps in understanding cross-border data flows and compute dependencies that could "
                         f"create unexpected vulnerabilities.")
    
    recommended_followups = (f"Priority follow-ups should include: (1) Detailed mapping of compute infrastructure "
                            f"dependencies across all three regions, (2) Scenario planning for technological surprise "
                            f"or breakthrough capabilities, (3) Track emerging rhetoric and policy signals that indicate "
                            f"shifts in strategic positioning. Wiki updates should capture new framings that emerged, "
                            f"particularly around sovereignty-innovation tradeoffs and infrastructure control mechanisms.")
    
    return {
        "headline": headline,
        "context": context,
        "points_of_agreement": points_of_agreement,
        "points_of_disagreement": points_of_disagreement,
        "strategic_options": strategic_options,
        "risks_and_unknowns": risks_and_unknowns,
        "recommended_followups": recommended_followups
    }


_NUMBERED_PREFIXES = tuple(f"{n}." for n in range(1, 10))

# Heuristic convergence/conflict balance per mode, used when no LLM is available.
_MODE_BALANCE = {
    "debate": (0.25, 0.60),
    "negotiation": (0.45, 0.40),
    "crisis": (0.20, 0.65),
    "policy-planning": (0.50, 0.35),
    "propaganda-lab": (0.15, 0.70),
}


def _representative_quote(content: str, limit: int = 180) -> str:
    """Pull a real, readable line from a turn (skips numbered headers and labels)."""
    lines = [ln.strip() for ln in (content or "").splitlines() if ln.strip()]
    for line in lines:
        if line.startswith("#") or line.startswith(_NUMBERED_PREFIXES):
            # For deterministic turns, keep the text after a "1. Immediate view:" style label.
            if ":" in line:
                tail = line.split(":", 1)[1].strip()
                if len(tail) > 40:
                    return _compact_text(tail, limit)
            continue
        if line.lower().endswith("position:"):
            continue
        if len(line) > 40:
            return _compact_text(line, limit)
    return _compact_text(lines[0], limit) if lines else ""


def build_recap(
    prompt: str,
    transcript: list[dict],
    actors: list[str] | None = None,
    mode: SessionMode = "debate",
) -> dict:
    """Heuristic end-of-debate recap and scoreboard for the no-API-key path.

    `transcript` is a list of message dicts (actor, content, kind). Mirrors the shape
    returned by the LLM recap so the frontend can render either interchangeably.
    """
    actors = actors or ["china", "us", "eu"]

    counts: dict[str, int] = {actor: 0 for actor in actors}
    first_quote: dict[str, tuple[int, str]] = {}
    best_quote: dict[str, tuple[int, str]] = {}

    for idx, msg in enumerate(transcript):
        actor = msg.get("actor", "")
        if msg.get("kind", "agent") != "agent" or actor not in counts:
            continue
        counts[actor] += 1
        quote = _representative_quote(msg.get("content", ""))
        if not quote:
            continue
        if actor not in first_quote:
            first_quote[actor] = (idx, quote)
        if actor not in best_quote or len(quote) > len(best_quote[actor][1]):
            best_quote[actor] = (idx, quote)

    spoke = [actor for actor in actors if counts[actor] > 0]
    max_count = max((counts[a] for a in spoke), default=0)

    scoreboard = []
    for actor in spoke:
        share = counts[actor] / max_count if max_count else 0
        dominance = max(5, min(100, round(40 + 60 * share)))
        line = best_quote.get(actor, first_quote.get(actor, (None, "")))[1]
        scoreboard.append(
            {
                "actor": actor,
                "dominance": dominance,
                "biggest_concession": "held firm",
                "best_line": line,
            }
        )
    scoreboard.sort(key=lambda entry: entry["dominance"], reverse=True)

    key_moments = []
    for actor in sorted(spoke, key=lambda a: len(best_quote.get(a, (0, ""))[1]), reverse=True)[:3]:
        idx, quote = best_quote.get(actor, first_quote.get(actor, (0, "")))
        if quote:
            key_moments.append(
                {
                    "actor": actor,
                    "quote": quote,
                    "why": f"{ACTOR_LABELS.get(actor, actor)} pressed its strongest line of the exchange.",
                    "turn_index": idx,
                }
            )

    agreement_ratio, conflict_ratio = _MODE_BALANCE.get(mode, (0.3, 0.55))

    leader = scoreboard[0]["actor"] if scoreboard else (spoke[0] if spoke else actors[0])
    leader_label = ACTOR_LABELS.get(leader, leader.capitalize())
    subject = _compact_text(prompt.split(".")[0].strip(), 80) or "the contested ground"
    others = [ACTOR_LABELS.get(a, a.capitalize()) for a in spoke if a != leader]
    against = " and ".join(others) if others else "the other actors"

    verdict = {
        "headline": f"{leader_label} carried the {mode}",
        "summary": (
            f"On “{subject}”, {leader_label} carried the room by volume and initiative, "
            f"forcing {against} to respond on its framing. No actor conceded core ground, "
            f"so the {mode} hardened positions more than it resolved them."
        ),
    }

    return {
        "verdict": verdict,
        "scoreboard": scoreboard,
        "key_moments": key_moments,
        "shifts": [],
        "sharpest_exchange": (
            f"The sharpest clash pitted {leader_label}'s push against {against}."
        ),
        "agreement_ratio": agreement_ratio,
        "conflict_ratio": conflict_ratio,
        "generated_by": "heuristic",
    }


_THEME_LEXICON = {
    "minerals": ["mineral", "rare earth", "rare-earth", "gallium", "germanium", "cobalt", "lithium", "copper", "refining", "graphite", "nickel"],
    "compute": ["chip", "semiconductor", "gpu", "compute", "tsmc", "asml", "nvidia", "fab", "hbm", "lithography"],
    "energy": ["energy", "power", "grid", "electricity", " gas", "nuclear", "datacenter", "data center", "water", "cooling", "terawatt"],
    "sovereignty": ["sovereignty", "sovereign", "self-reliance", "autonomy", "cyber", "indigeniz"],
    "alliances": ["alliance", "allies", "ally", "partner", "friend-shoring", "coalition", "bloc"],
    "trade": ["export control", "tariff", "sanction", "supply chain", "embargo", "decoupl"],
    "global south": ["africa", "global south", "congo", "drc", "indonesia", "extraction", "colonial", "periphery"],
    "governance": ["regulation", "standard", "governance", "ai act", "rules", "compliance"],
    "safety": ["safety", "alignment", "risk", "guardrail", "human control"],
    "open models": ["open-source", "open source", "open-weight", "open model", "deepseek"],
}

_CHARGED_WORDS = ("hypocrisy", "coercion", "decadence", "fantasy", "collapse", "weaponize", "retaliate", "threat", "fail", "dependence", "contradiction")
_ACTOR_MENTIONS = {
    "china": ["china", "chinese", "beijing", "prc"],
    "us": ["united states", "u.s.", "america", "american", "washington"],
    "eu": ["europe", "european", "eu ", "brussels"],
}


def build_pulse(transcript: list[dict], actors: list[str] | None = None, mode: SessionMode = "debate") -> dict:
    """Lightweight heuristic read of the latest turn for the live overlay.

    Mirrors the shape of the LLM pulse so the frontend can render either interchangeably.
    """
    actors = actors or ["china", "us", "eu"]
    last = transcript[-1] if transcript else {}
    actor = last.get("actor", "")
    text = (last.get("content", "") or "")
    low = text.lower()
    words = len(text.split())
    exclaims = text.count("!")
    charged = sum(low.count(w) for w in _CHARGED_WORDS)
    has_prior = any(m.get("kind", "agent") == "agent" for m in transcript[:-1])

    if not has_prior:
        move = "open"
    elif "?" in text:
        move = "probe"
    elif any(c in low for c in ("fair point", "you're right", "agree", "concede", "common ground")):
        move = "concede"
    elif any(c in low for c in ("we also", "join", "together", "share that", "co-opt")):
        move = "co-opt"
    elif exclaims >= 2 or charged >= 2 or any(c in low for c in ("will not", "must ", "or else", "retaliat")):
        move = "escalate"
    elif any(c in low for c in ("but ", "however", "reject", "wrong", "disagree", "illusion")):
        move = "rebut"
    else:
        move = "reframe"

    target = "none"
    for other in actors:
        if other == actor:
            continue
        if any(token in low for token in _ACTOR_MENTIONS.get(other, [])):
            target = other
            break

    intensity = max(5, min(100, round(28 + words / 7 + exclaims * 9 + charged * 7)))
    move_tension = {"escalate": 26, "rebut": 12, "probe": 4, "reframe": 1, "open": 2, "co-opt": -6, "concede": -22, "deflect": -2}
    tension_delta = max(-40, min(40, move_tension.get(move, 2) + exclaims * 3 + charged * 2))

    themes: list[str] = []
    for theme, keys in _THEME_LEXICON.items():
        if any(k in low for k in keys):
            themes.append(theme)
        if len(themes) >= 3:
            break

    return {
        "actor": actor,
        "move": move,
        "target": target,
        "intensity": intensity,
        "tension_delta": tension_delta,
        "themes": themes,
        "source": "heuristic",
    }


def build_mirror_card(prompt: str, transcript: list[dict], actors: list[str] | None = None, tone: str = "grounded-absurdist") -> dict:
    """Heuristic closing mirror-card (no LLM): three layers + a satirical dispatch."""
    actors = actors or ["china", "us", "eu"]
    specs, ironies, officials, realities = [], [], [], []
    for m in transcript:
        meta = m.get("metadata") or {}
        if meta.get("format") == "mirror-turn":
            if meta.get("speculation"):
                specs.append(meta["speculation"])
            if meta.get("irony"):
                ironies.append(meta["irony"])
            if meta.get("official_line"):
                officials.append(meta["official_line"])
            if meta.get("buried_reality"):
                realities.append(meta["buried_reality"])

    if "INTELLIGENCE" in prompt:
        reality = _compact_text(prompt.split("INTELLIGENCE", 1)[1].lstrip(" :("), 260)
    elif realities:
        reality = _compact_text(realities[0], 240)
    else:
        reality = "Leaked intelligence describes an exchange breach attributed, at stated confidence, to a state-linked operation."
    official_story = _compact_text(officials[0], 240) if officials else "Officially: a contained foreign attack that proves the need for tighter controls."
    speculation = _compact_text(max(specs, key=len), 280) if specs else "The breach quietly becomes a feature: laundered funds resurface inside a state-blessed pilot, rebranded as resilience."
    irony = ironies[0] if ironies else "Everyone condemns the laundering they quietly depend on."
    dispatch = (
        f"{speculation} By winter, the same officials who swore zero tolerance are quoting compliance dashboards that "
        f"log the stolen funds as 'recovered velocity,' while the press calls it a turnaround. {irony}"
    )
    return {
        "headline": "Mirror World: the hack everyone needed",
        "reality": reality,
        "official_story": official_story,
        "speculation": speculation,
        "dispatch": dispatch,
        "tone": tone,
        "generated_by": "heuristic",
    }


def build_wiki_proposals(actors: list[str], prompt: str) -> list[dict[str, str]]:
    proposals = []
    for actor in actors:
        proposals.append(
            {
                "target": f"wiki/{actor}-ai-policy/" if actor in {"china", "us", "eu"} else "wiki/",
                "reason": f"Session on '{prompt}' may have surfaced new strategic tensions for {ACTOR_LABELS[actor]}",
                "content": "Review transcript and extract any changed assumptions, new strategic options, or rhetorical shifts before writing back to the wiki.",
            }
        )
    return proposals
