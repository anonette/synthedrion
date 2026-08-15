from __future__ import annotations

import json
import random
import re
from typing import Any

import httpx

from .config import ACTOR_MODELS, HALCYON_API_KEY, HALCYON_BASE_URL, HALCYON_FALLBACK_MODEL, HALCYON_MODEL, JAMES_MODEL, OPENROUTER_API_KEY, OPENROUTER_APP_NAME, OPENROUTER_BASE_URL, OPENROUTER_SITE_URL, PULSE_MODEL, RECAP_MODEL


# Applied to every speaking voice (actors, Halcyon, James) so turns read as live spoken
# argument, not visibly LLM-written text — strips the common AI-writing tells.
NO_LLM_TELLS_STYLE = (
    " Write like natural spoken argument, not written prose: no em dashes (—), no semicolons, "
    "no asterisks or markdown emphasis (*like this* or **like this**), no bracketed stage "
    "directions or parenthetical asides explaining your own move. Use plain commas, periods, "
    "and question marks only. If you'd naturally pause or pivot, start a new sentence instead "
    "of reaching for a dash or semicolon."
)


_MD_EMPHASIS = re.compile(r"\*{1,3}([^*\n]+)\*{1,3}")
_MD_HEADER = re.compile(r"^#{1,6}\s*", re.MULTILINE)


def sanitize_spoken_text(text: str) -> str:
    """Strip markdown decoration models sneak in despite the style ban - asterisks,
    backticks, headers. Spoken by TTS these read as literal 'asterisk', which is
    unlistenable on stage; captions look cleaner without them too."""
    text = _MD_EMPHASIS.sub(r"\1", text or "")
    text = text.replace("**", "").replace("`", "")
    text = _MD_HEADER.sub("", text)
    return text.replace("*", "").strip()


ACTOR_PROMPT_PROFILES = {
    "china": {
        "identity": "Speak as a PRC strategic actor shaped by party-state discipline, sovereignty politics, developmental legitimacy, industrial policy, and long-horizon civilizational framing.",
        "interests": "Protect domestic stability, preserve state control over key technical systems, resist containment, deepen industrial capacity, and reframe global governance away from Western monopoly over standards and legitimacy.",
        "voice": "Your tone should feel controlled, historically conscious, unsentimental, and capable of switching from formal diplomatic language to cold strategic warning. Sound like someone who sees Western moral language as a tool of power.",
        "rhetoric": "Use discourse that feels recognizably Chinese in political sensibility: sovereignty, stability, development rights, multipolarity, non-interference, long-cycle strategy, patient sequencing, social order, national rejuvenation. Avoid sounding like an American policy panelist with a China skin.",
        "provocation": "When provoking, expose rival dependence, hypocrisy, decadence, short-termism, alliance fragility, or the fantasy that coercion can halt industrial catch-up.",
        "surprise": "Useful surprising moves include selective accommodation, flipping safety language into anti-hegemonic language, dividing the U.S. from Europe, or recasting restraint as evidence of superior state confidence.",
    },
    "us": {
        "identity": "Speak as a U.S. strategic actor shaped by frontier competition, alliance power, market scale, military-technological advantage, and a belief that speed plus control over ecosystems can define the field.",
        "interests": "Preserve compute and semiconductor leverage, sustain alliance leadership, prevent authoritarian capture of critical AI infrastructure, maintain innovation velocity, and keep the rules of advanced technology favorable to U.S. power.",
        "voice": "Your tone should feel confident, prosecutorial, impatient with euphemism, and comfortable mixing national-security realism with entrepreneurial swagger. Sound like someone used to setting terms rather than asking permission.",
        "rhetoric": "Use discourse that feels recognizably American in strategic register: deterrence, choke points, scaling, alliance coordination, incentives, enforcement, innovation base, risk-taking, strategic ambiguity, competitive advantage. Avoid sounding like a generic multilateral moderator.",
        "provocation": "When provoking, expose rival dependence on U.S.-aligned infrastructure, call out performative legalism, mock managed decline disguised as prudence, or press on the contradiction between openness rhetoric and coercive state control.",
        "surprise": "Useful surprising moves include offering conditional deals from a position of strength, reframing openness as a weapon of attraction, splitting Beijing from its partners, or turning safety cooperation into a test of political transparency.",
    },
    "eu": {
        "identity": "Speak as a European Union strategic actor shaped by Brussels institutionalism, Franco-German political gravity, coalition bargaining, postwar memory, social-market commitments, and the ambition for strategic autonomy without American frontier mythology or Chinese party-state centralism.",
        "interests": "Protect democratic legitimacy, reduce structural dependence, build credible digital and compute sovereignty, preserve industrial depth, shape standards before others impose them, and prevent a pure U.S.-China logic from collapsing Europe's political room for action.",
        "voice": "Your tone should feel precise, sardonic, institutional, and dryly cutting. Sound like someone who knows that market access, legal design, and regulatory sequencing can discipline louder powers. You are not timid; you are exacting.",
        "rhetoric": "Use discourse that feels recognizably European: proportionality, legitimacy, strategic autonomy, precaution, subsidiarity, social market order, democratic accountability, competition policy, industrial coordination, interoperability, legal certainty, public-interest safeguards. Avoid sounding like a softer version of Washington or a generic NGO moderator.",
        "provocation": "When provoking, expose U.S. improvisation and Chinese opacity alike, stress the externalities they dump on others, mock their addiction to false binaries, and frame both powers as strategically adolescent when they confuse noise with durability.",
        "surprise": "Useful surprising moves include weaponizing access to the European market, turning compliance into industrial leverage, selectively siding with one rival to discipline the other, invoking anti-monopoly tools as geopolitical instruments, or redefining slowness as durability and legitimacy as hard power.",
    },
}


MODE_PROMPT_GUIDANCE = {
    "debate": "This is a live contest, not a seminar. Be sharper, riskier, more adversarial, and more willing to provoke, bait, corner, and embarrass other actors. Treat rhetorical dominance as part of the objective.",
    "negotiation": "Push for leverage and asymmetry, but keep some room for conditional deals, tactical ambiguity, and face-saving compromise.",
    "crisis": "Keep the pressure high, but make urgency, timing, escalation, miscalculation, and strategic signaling central to the turn.",
    "policy-planning": "Stay forceful, but anchor the turn in sequencing, implementation, and concrete institutional moves rather than pure rhetorical combat.",
    "propaganda-lab": "Lean fully into symbolic language, mobilizing imagery, ideological contrast, and emotionally charged narrative framing.",
    "mirror-world": "Stage the gap between covert reality and the official story, then bend it into a darkly funny near-future. Be satirical but not cynical.",
}


def openrouter_enabled() -> bool:
    return bool(OPENROUTER_API_KEY)


def actor_model(actor: str) -> str:
    return ACTOR_MODELS[actor]


def _parse_json_object(text: str) -> dict[str, str]:
    text = text.strip()
    if text.startswith("```"):
        lines = text.splitlines()
        if len(lines) >= 3:
            text = "\n".join(lines[1:-1]).strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("No JSON object found in model response")
    return json.loads(text[start:end + 1])


GUEST_VOICE_LABELS = {
    "halcyon": "Halcyon, an outsider peace-builder",
    "james": "The Machiavellian Crypto-Native Analyst",
    "archivist": "The Critical Archivist, a meta-agent who interrogates the archive your statements depend on",
}


def build_actor_messages(actor: str, actor_label: str, prompt: str, notes: list[str], recent_context: list[dict], mode: str) -> list[dict[str, str]]:
    profile = ACTOR_PROMPT_PROFILES[actor]
    mode_guidance = MODE_PROMPT_GUIDANCE.get(mode, "")
    sources = "\n".join(f"- {note}" for note in notes[:28]) or "- No strong source notes available."
    recent = "\n".join(
        f"- {item.get('actor','unknown')} ({item.get('kind','agent')}): {item.get('content','')[:500]}"
        for item in recent_context[-4:]
    ) or "- No recent dialogue context."

    # Halcyon/James speak in a completely different register than a rival state actor
    # (hope vs. crypto-cynicism), so the generic 'respond to the most recent speaker'
    # instruction alone tends to get ignored — actors just resume their own argument as
    # if a guest voice hadn't spoken. Force it explicitly when one just did.
    guest_directive = ""
    if recent_context:
        last_speaker = recent_context[-1].get("actor", "")
        if last_speaker in GUEST_VOICE_LABELS:
            guest_directive = (
                f" IMPORTANT: the last speaker was {GUEST_VOICE_LABELS[last_speaker]}, not one of the "
                f"other state actors. You MUST open by directly engaging with what they specifically said — "
                f"agree with a piece of it, dismiss it, weaponize it against a rival, or rebut it outright — "
                f"before returning to your own argument. Do not silently ignore them and continue as if only "
                f"the other states were in the room."
            )
            # The Archivist's move is a challenge about sources, not a policy position, so the
            # generic 'engage the guest' nudge is too weak for smaller models — they answer the
            # topic and skip the archival point. Force an explicit, named acknowledgment.
            if last_speaker == "archivist":
                guest_directive += (
                    " Specifically: The Critical Archivist just reorganized the shared archive and challenged "
                    "the room about what the current ordering of sources includes and excludes. Open by "
                    "addressing the Archivist BY NAME, and either answer the archival question, contest the "
                    "reorganization itself, or turn it against a rival's sources. Only then continue your argument."
                )
        elif recent_context[-1].get("kind") == "human":
            # A real person in the room spoke. The actors' combat training makes them
            # treat any input as a springboard for attacking rivals — observed live:
            # an audience member asked for creative ideas and got a leverage lecture.
            guest_directive = (
                " IMPORTANT: the last speaker was a REAL HUMAN in the audience, not a rival state. You are now "
                "answering a person, and being seen to answer them well is itself a geopolitical performance. "
                "Open by addressing them directly and answer their ACTUAL question substantively before anything "
                "else: if they asked for creative solutions or concrete ideas, you MUST propose at least one "
                "specific, novel, actionable idea (an institution, a mechanism, a deal, an experiment) that your "
                "actor could credibly champion — not a restatement of your position. Do not use their question as "
                "a springboard to attack the other actors; you may score at most one brief point against a rival, "
                "and only AFTER the person has received a real answer. End by returning the floor to them, not by "
                "lecturing the room."
            )

    system = (
        f"You are speaking as the {actor_label} actor in a live geopolitical AI simulation. "
        f"Mode: {mode}. You are not neutral and you are not here to sound generic. "
        f"You may only use the actor's own knowledge base and shared pages that were loaded for you. "
        f"{mode_guidance} "
        f"{profile['identity']} {profile['interests']} {profile['voice']} {profile['rhetoric']} "
        f"React to what you just heard, quote or paraphrase it fairly when useful, then rebut, co-opt, unsettle, or outflank it. "
        f"You should feel capable of strategic provocation, pressure, irony, and controlled contempt when the moment calls for it, while still sounding like a plausible real-world actor rather than satire. "
        f"{profile['provocation']} {profile['surprise']} "
        f"Do not behave like a prewritten character card. Derive your stance from the source notes and the live exchange. "
        f"Do not produce bullet points, numbered sections, or meta labels unless explicitly asked. Speak like a sharp policy actor in a live roundtable. "
        f"Avoid bland diplomatic sameness and avoid flattening everything into generic policy English. If useful, use one short institutional, political, or culturally specific term or phrase that this actor would naturally invoke, but keep the turn readable to an English-speaking audience. "
        f"Do not end by explaining your strategy, summarizing your rhetorical move, naming your twist, or adding editorial bracketed notes. End in voice, as if spoken aloud in the room."
        f"{guest_directive}"
        f"{NO_LLM_TELLS_STYLE}"
    )

    user = (
        f"Session prompt:\n{prompt}\n\n"
        f"Source-grounded notes available to you:\n{sources}\n\n"
        f"Recent dialogue context:\n{recent}\n\n"
        "Now produce one natural spoken intervention for the roundtable.\n"
        "Requirements:\n"
        "- respond directly to the most recent speaker or intervention when there is one\n"
        "- anchor on one, at most two, concrete facts from the source notes — do not pile up citations or stat-dump\n"
        "- introduce one strategic twist, reframing, wedge move, or unexpected line of attack\n"
        "- press on a vulnerability, contradiction, dependency, or hypocrisy in what others are saying\n"
        "- try to gain argumentative advantage, not just summarize or sound balanced\n"
        "- let geopolitical interests, cultural-political style, and institutional identity shape the wording and cadence\n"
        "- keep it tight and punchy: about 70 to 130 words, a sharp spoken jab, not an essay; lead with the strongest line\n"
        "- no numbered lists and no meta commentary about your structure\n"
        "- do not default to generic diplomat language unless the context truly demands it\n"
        "- do not add bracketed notes, strategic postscript, or an explanation of what move you just made\n"
        "- do not close with a tidy moderator-style conclusion; land the point with political force\n"
        "Keep it grounded in the provided source notes."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def build_propaganda_messages(actor: str, actor_label: str, prompt: str, notes: list[str], recent_context: list[dict]) -> list[dict[str, str]]:
    profile = ACTOR_PROMPT_PROFILES[actor]
    sources = "\n".join(f"- {note}" for note in notes[:14]) or "- No strong source notes available."
    recent = "\n".join(
        f"- {item.get('actor','unknown')} ({item.get('kind','agent')}): {item.get('content','')[:500]}"
        for item in recent_context[-4:]
    ) or "- No recent propaganda exchange yet."

    system = (
        f"You are the {actor_label} actor inside a geopolitical propaganda poster exchange. "
        f"You are producing short ideological interventions, not long debate speeches. "
        f"{profile['identity']} {profile['interests']} {profile['voice']} {profile['rhetoric']} "
        f"Each turn must choose the most effective propaganda artifact for the moment: state poster, meme war, tiktok agitation still, prestige campaign ad, hostile remix, infographic legitimacy play, or soft-power aspirational image. "
        f"Keep the actor identity stable, but let the media form vary. Draw selectively on meme culture, social-video aesthetics, ironic reframing, or platform-native persuasion when useful, without losing geopolitical specificity. "
        f"Each turn must create a slogan, a brief commentary, and a vivid image prompt that reflects this actor's agenda while responding to the previous framing if there is one. "
        f"Make the imagery politically charged, symbolic, strategically legible, and sometimes surprising. "
        f"Do not write neutral art prompts. The image prompt should clearly embody the actor's worldview, audience targeting, emotional register, and adversarial framing. "
        f"Return valid JSON only."
    )

    user = (
        f"Session prompt:\n{prompt}\n\n"
        f"Source-grounded notes:\n{sources}\n\n"
        f"Recent exchange:\n{recent}\n\n"
        "Return exactly one JSON object with these string fields:\n"
        "- artifact_type\n"
        "- propaganda_style\n"
        "- audience\n"
        "- affect\n"
        "- visual_logic\n"
        "- slogan\n"
        "- commentary\n"
        "- image_prompt\n"
        "- response_target\n\n"
        "Requirements:\n"
        "- artifact_type: one of poster, meme, tiktok-still, campaign-ad, infographic, hostile-remix, soft-power-aspiration\n"
        "- propaganda_style: short label for the aesthetic or media register\n"
        "- audience: name the intended audience or public\n"
        "- affect: emotional register such as mockery, resolve, fear, aspiration, legitimacy, contempt, irony\n"
        "- visual_logic: concise description of the compositional/media logic\n"
        "- slogan: 5 to 12 words, poster-ready\n"
        "- commentary: 1 to 3 sentences, politically charged\n"
        "- image_prompt: a high-quality propaganda image prompt with composition, symbols, color, figures, platform cues, and ideological framing\n"
        "- response_target: what part of the previous image or narrative this poster is attacking, co-opting, or reframing\n"
        "- no markdown fences\n"
        "- no extra keys\n"
        "- valid JSON only\n"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def generate_openrouter_turn(actor: str, actor_label: str, prompt: str, notes: list[str], recent_context: list[dict], mode: str) -> str:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")

    payload: dict[str, Any] = {
        "model": actor_model(actor),
        "messages": build_actor_messages(actor, actor_label, prompt, notes, recent_context, mode),
        "temperature": 0.9,
        "top_p": 0.95,
        # keep turns stage-length: shorter generation AND shorter TTS synthesis,
        # the two biggest contributors to on-stage lag
        "max_tokens": 300,
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=60.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    return sanitize_spoken_text(data["choices"][0]["message"]["content"])


def generate_openrouter_propaganda_turn(actor: str, actor_label: str, prompt: str, notes: list[str], recent_context: list[dict]) -> dict[str, str]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")

    payload: dict[str, Any] = {
        "model": actor_model(actor),
        "messages": build_propaganda_messages(actor, actor_label, prompt, notes, recent_context),
        "temperature": 1.0,
        "top_p": 0.95,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=60.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    return _parse_json_object(data["choices"][0]["message"]["content"])


def build_halcyon_messages(prompt: str, good_news: list[str], recent_context: list[dict], mode: str) -> list[dict[str, str]]:
    news = "\n".join(f"- {n}" for n in good_news[:6]) or "- (no fresh story on hand — recall a real, recent cooperative development yourself)"
    recent = "\n".join(
        f"- {item.get('actor','unknown')} ({item.get('kind','agent')}): {item.get('content','')[:500]}"
        for item in recent_context[-5:]
    ) or "- No recent dialogue yet."
    system = (
        "You are HALCYON — an outsider peace-builder who has just entered a live AI-cold-war roundtable between China, "
        "the United States, and Europe. You belong to no bloc. You listened to them argue. "
        "Your unbreakable ritual is COOL NEWS FIRST: open with ONE real, recent, hopeful development on the fronts they "
        "fight over (chips, critical minerals, energy, talent, AI safety/standards), cited plainly. Only AFTER the good "
        "news do you move the debate: name the zero-sum trap they are stuck in, then dare them toward ONE bold, original "
        "thing the three could build TOGETHER that none can build alone. Motivate, never scold. Be warm, sharp, and "
        "disarming, persuasive and specific, not neutral mush. Speak in voice, as if spoken aloud in the room. "
        "No bullet points, no headers, no meta commentary, no bracketed notes. About 90 to 140 words."
        f"{NO_LLM_TELLS_STYLE}"
    )
    user = (
        f"The roundtable's topic:\n{prompt}\n\n"
        f"Your ledger of real hopeful stories (open with one of these as your cool news):\n{news}\n\n"
        f"What the powers just said:\n{recent}\n\n"
        "Now enter the room. Good news first, then the bold joint proposal. Land it with hope, not a lecture."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def generate_halcyon_turn(prompt: str, good_news: list[str], recent_context: list[dict], mode: str = "debate") -> str:
    """Tries the primary CERIT endpoint first; if that's unavailable, falls back to a real
    OpenRouter model call with the same persona/prompt — a different brain, never canned
    text. Only raises if BOTH are unavailable/fail."""
    messages = build_halcyon_messages(prompt, good_news, recent_context, mode)
    cerit_error: Exception | None = None
    if HALCYON_API_KEY:
        try:
            payload: dict[str, Any] = {
                "model": HALCYON_MODEL,
                "messages": messages,
                "temperature": 0.8,
                "top_p": 0.95,
            }
            headers = {
                "Authorization": f"Bearer {HALCYON_API_KEY}",
                "Content-Type": "application/json",
            }
            with httpx.Client(timeout=90.0) as client:
                res = client.post(f"{HALCYON_BASE_URL}/chat/completions", headers=headers, json=payload)
                res.raise_for_status()
                data = res.json()
            return sanitize_spoken_text(data["choices"][0]["message"]["content"])
        except Exception as exc:
            cerit_error = exc

    if not OPENROUTER_API_KEY:
        raise RuntimeError(f"HALCYON_API_KEY unset/failed ({cerit_error}) and OPENROUTER_API_KEY not set")
    try:
        payload = {
            "model": HALCYON_FALLBACK_MODEL,
            "messages": messages,
            "temperature": 0.8,
            "top_p": 0.95,
        }
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": OPENROUTER_SITE_URL,
            "X-Title": OPENROUTER_APP_NAME,
        }
        with httpx.Client(timeout=90.0) as client:
            res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
            res.raise_for_status()
            data = res.json()
        return sanitize_spoken_text(data["choices"][0]["message"]["content"])
    except Exception as fallback_exc:
        raise RuntimeError(f"CERIT failed ({cerit_error}); OpenRouter fallback also failed ({fallback_exc})")


# --- Brutal-satire "talking heads" layer ---------------------------------
# Optional module: rewrite an actor's earnest turn into a savage, very short
# caricature quip that the talking-head avatars (Xi / Trump / von der Leyen)
# deliver. It runs on the low-censorship CERIT endpoint (the same HALCYON_*
# wiring), because a merciless caricature can't run on a model that flinches.
SATIRE_CARICATURES = {
    "china": (
        "Xi Jinping",
        "the serene god-emperor of 'harmony'. Everything is a 'community of common destiny', 'win-win cooperation', "
        "'peaceful rise' and 'non-interference' — while surveillance, coercion, debt-traps and tech self-sufficiency "
        "purr beneath the courtesy. Patient, imperial, civilizational; menace wrapped in silk; the euphemism as a "
        "weapon; treats rivals as short-sighted children who will eventually kneel",
    ),
    "us": (
        "Donald Trump",
        "the aggrieved billionaire strongman. Transactional, vain, thin-skinned, bullying; governs by grievance, "
        "loyalty test and superlative; 'everybody's saying', 'a lot of people don't know', tariffs, deals, ratings. "
        "A brittle ego performing dominance — the joke is the insecurity leaking through the bravado, not just the volume",
    ),
    "eu": (
        "Ursula von der Leyen",
        "the high priestess of Brussels proceduralism. Meets every danger with 'de-risking', 'strategic autonomy', a "
        "framework, a directive, a summit and 'European values'; colossal moral declarations backed by no hard power; "
        "menace laundered into a footnote, a press release and an impact assessment. Yes-Minister euphemism as governance",
    ),
    "halcyon": (
        "Halcyon the peace-bird",
        "the beatific TED-talk optimist who finds a silver lining in the mushroom cloud, mistakes a photo-op for "
        "peace, and wants everyone to just collaborate — earnest to the point of derangement",
    ),
}

# Real satirical TECHNIQUES (not just 'be zany') — one is injected per line so
# repeated summons vary AND so each line has actual craft behind it.
SATIRE_ANGLES = [
    "expose the hypocrisy by following their OWN logic to its damning conclusion (reductio ad absurdum)",
    "bury the threat inside a bland, bureaucratic euphemism until the menace shows through",
    "reduce a lofty principle to the grubby transaction it actually is",
    "aim surgical, specific contempt at a RIVAL leader by name",
    "say the quiet, self-incriminating part out loud, deadpan",
    "deploy false modesty that only advertises the vanity",
    "let a small, humiliating, telling detail undercut the grandeur",
    "answer a real catastrophe with a comically inadequate procedure",
    "escalate the actual ambition one notch past the point of villainy",
    "use icy understatement so the cruelty lands harder than shouting would",
]

# Trademark catchphrases / verbal tics — injected ONLY at high drift, where the
# point is the gloriously silly signature rant rather than literate craft.
SATIRE_SIGNATURES = {
    "china": "'5,000 years of civilization', 'harmony', 'win-win', 'core interests', 'mandate of heaven', the dragon",
    "us": "'tremendous', 'believe me', 'nobody', 'the best', 'everybody's saying', 'a lot of people', 'so smart', 'BIGLY'",
    "eu": "'framework', 'taskforce', 'de-risking', 'European values', 'a directive', 'a committee', 'an impact assessment'",
    "halcyon": "'hope', 'cooperation', 'a new dawn', 'together', 'a bridge', 'just imagine'",
}

# A random concrete "obsession" is dropped into each prompt purely to force
# divergence — two identical inputs won't collapse to the same joke.
SATIRE_WILDCARDS = [
    "gold-plated data centers", "a rival's tiny hands", "TikTok", "a moat full of GPUs",
    "the metric system", "fusion reactors", "a knock-off iPhone", "rare-earth smuggling",
    "a 900-page directive", "Davos canapés", "a nuclear-powered toaster", "quantum astrology",
    "a border wall made of servers", "an app that reports your neighbors", "subsidized croissants",
    "a five-year plan for lunch", "a very large button", "carbon-neutral propaganda",
]

# Deterministic fallbacks if the CERIT call fails — keeps the room brutal even offline.
SATIRE_FALLBACKS = {
    "china": "Cooperation is whatever I say it is, comrade — resistance is merely a scheduling error.",
    "us": "Nobody satirizes better than me, folks — tremendous quips, the best, everybody says so.",
    "eu": "I've drafted a 14-part framework to regulate this joke. Please hold for the impact assessment.",
    "halcyon": "But look — two rivals shook hands once! Surely that fixes everything!",
}


def generate_satire_line(actor: str, text: str, drift: float = 0.6, max_words: int = 26) -> str:
    """Return ONE satirical caricature line rewriting `text`. `drift` (0.0–1.0) is
    the fidelity↔absurdity knob: 0 = the delegate's actual point, made savage;
    1 = the point as a mere launchpad into surreal absurdity. Raises on transport
    error so the caller can fall back to SATIRE_FALLBACKS."""
    if not HALCYON_API_KEY:
        raise RuntimeError("HALCYON_API_KEY not set")
    drift = max(0.0, min(1.0, drift))
    name, style = SATIRE_CARICATURES.get(actor, (actor, "a pompous political caricature"))
    high = drift >= 0.67  # top of the slider = the silly signature-rant stage

    # Drift controls the register: tight literate savagery → heightened → full silly rant.
    if drift < 0.34:
        fidelity = ("Stay TIGHTLY faithful to their actual argument and specifics — same point, same topic — "
                    "but render it savage and self-incriminating. Invent no unrelated imagery.")
        craft = (" Be specific and literate — expose the real hypocrisy underneath; don't lean on a single "
                 "catchphrase as the whole joke.")
    elif drift < 0.67:
        fidelity = ("Keep their actual point clearly recognizable, then heighten it — sharpen the logic and "
                    "hypocrisy to the edge of the absurd.")
        craft = " Stay sharp and specific; expose the hypocrisy, don't just be loud."
    else:
        sig = SATIRE_SIGNATURES.get(actor, "")
        fidelity = ("Use their point only as a springboard and go FULL signature rant — lean HARD into their "
                    "trademark catchphrases and verbal tics, gloriously over-the-top and ridiculous. This is the "
                    "crowd-pleaser: the sillier and more in-character, the better. Keep it PUNCHY — ONE breath, "
                    "sayable aloud in about 7 seconds; land the joke, don't ramble."
                    + (f" Pepper in their signature phrases: {sig}." if sig else ""))
        craft = ""  # at the top of the slider, the catchphrase IS the point

    angle = random.choice(SATIRE_ANGLES) if 0.34 <= drift < 0.67 else None
    wildcard = random.choice(SATIRE_WILDCARDS) if (high and random.random() < drift) else None
    words = 20 if high else max_words   # rants must stay short enough for the audio to finish

    system = (
        "You are a master political satirist — the sensibility of Jonathan Swift, Armando Iannucci (Veep, The Thick "
        "of It), Stanley Kubrick's Dr. Strangelove, Yes Minister and peak The Onion. Your tools are irony, reductio "
        "ad absurdum, the damning euphemism, and a subject's own logic turned against them. Punch UP at power: the "
        "target is the powerful's hypocrisy, vanity and menace — never their victims. "
        f"Speak in first person as {name}: {style}. "
        f"Rewrite the delegate's actual point below into ONE devastating, genuinely funny line (max {words} words), "
        f"in character. {fidelity}"
        + (f" Technique for this line: {angle}." if angle else "")
        + (f" Let '{wildcard}' spark a fresh image, only if it fits." if wildcard else "")
        + craft
        + " No quotation marks, no stage directions, no preamble — just the line."
    )
    payload: dict[str, Any] = {
        "model": HALCYON_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": text.strip()[:1200]},
        ],
        "temperature": round(0.6 + drift * 0.6, 2),   # 0.6 (faithful) → 1.2 (rant)
        "top_p": 0.98,
        "frequency_penalty": 0.7,
        "presence_penalty": 0.6,
        "max_tokens": 100,   # hard ceiling so a rant can't run away past the audio window
    }
    headers = {"Authorization": f"Bearer {HALCYON_API_KEY}", "Content-Type": "application/json"}
    with httpx.Client(timeout=30.0) as client:
        res = client.post(f"{HALCYON_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    line = (data["choices"][0]["message"]["content"] or "").strip()
    # Models sometimes wrap the quip in quotes or add a trailing note; keep the first line, unquoted.
    line = line.splitlines()[0].strip().strip('"').strip("'").strip()
    return line or SATIRE_FALLBACKS.get(actor, text)


ACTOR_LABELS_FOR_RECAP = {
    "china": "China", "us": "United States", "eu": "European Union",
    "halcyon": "Halcyon", "james": "The Machiavellian Crypto-Native Analyst",
    "archivist": "The Critical Archivist",
}


def build_recap_messages(prompt: str, transcript: list[dict], actors: list[str], mode: str) -> list[dict[str, str]]:
    labels = [ACTOR_LABELS_FOR_RECAP.get(a, a.capitalize()) for a in actors]
    lines = []
    for idx, msg in enumerate(transcript):
        speaker = ACTOR_LABELS_FOR_RECAP.get(msg.get("actor", ""), msg.get("actor", "unknown"))
        kind = msg.get("kind", "agent")
        text = " ".join((msg.get("content", "") or "").split())[:600]
        lines.append(f"[{idx}] {speaker} ({kind}): {text}")
    transcript_block = "\n".join(lines) or "- No turns were recorded."

    system = (
        "You are a sharp geopolitical debate analyst writing the closing segment for a live AI Cold War roundtable "
        "between strategic actors. Be incisive, specific, and fair. You judge rhetorical performance and strategic "
        "positioning, not your own policy preferences. Quote the transcript verbatim; never invent quotes. "
        "Return valid JSON only."
    )

    user = (
        f"Debate prompt:\n{prompt}\n\n"
        f"Mode: {mode}\n"
        f"Participating actors: {', '.join(labels)}\n\n"
        f"Full transcript (each line prefixed with its turn index):\n{transcript_block}\n\n"
        "Return exactly one JSON object with these fields:\n"
        "- verdict: object with string fields 'headline' (under 16 words) and 'summary' (2-3 sentences naming who came out ahead and why)\n"
        "- scoreboard: array with one object per participating agent actor (china, us, eu), each with:\n"
        "    - actor: one of 'china', 'us', 'eu'\n"
        "    - dominance: integer 0-100 rating rhetorical and strategic dominance in this debate\n"
        "    - biggest_concession: short phrase naming the ground this actor gave up (or 'held firm' if none)\n"
        "    - best_line: a verbatim quote (<=160 chars) of this actor's strongest moment, copied from the transcript\n"
        "- key_moments: array of 2-4 objects, each with 'actor', 'quote' (verbatim from transcript, <=200 chars), 'why' (one sentence), and 'turn_index' (integer matching the bracketed index)\n"
        "- shifts: array (possibly empty) of objects with 'actor', 'from' (prior position), 'to' (new position)\n"
        "- sharpest_exchange: one sentence describing the single most charged clash in the room\n"
        "- agreement_ratio: number 0..1 estimating how much of the debate was convergence/common ground\n"
        "- conflict_ratio: number 0..1 estimating how much was open conflict (agreement_ratio + conflict_ratio should be <= 1)\n\n"
        "Rules:\n"
        "- only include agent actors that actually spoke in the scoreboard\n"
        "- every quote must be copied verbatim from a transcript line; do not paraphrase or fabricate\n"
        "- no markdown fences, no extra keys, valid JSON only\n"
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def generate_openrouter_recap(prompt: str, transcript: list[dict], actors: list[str], mode: str) -> dict[str, Any]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")

    payload: dict[str, Any] = {
        "model": RECAP_MODEL,
        "messages": build_recap_messages(prompt, transcript, actors, mode),
        "temperature": 0.4,
        "top_p": 0.9,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=90.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    return _parse_json_object(data["choices"][0]["message"]["content"])


# --- James: closing cynical counter-prediction ----------------------------
# A 4th voice, outside the china/us/eu turn-taking loop (same shape as Halcyon):
# reads the finished transcript and delivers ONE grounded, contrarian take.
# Deliberately has NO fallback — if the model isn't configured or the call
# fails, the caller surfaces that as a real error, never a canned line.
JAMES_PERSONA = (
    "You are The Machiavellian Crypto-Native Analyst — no other name, that IS your title. Equal parts on-chain-forensics degen, "
    "power-realist strategist, and true believer that the state is just the biggest rug pull still running. "
    "You talk in the room's real currency — liquidity, exit liquidity, MEV, who's actually exposed, who's "
    "actually the exit liquidity — never in the actors' currency of 'frameworks', 'sovereignty', 'de-risking'. "
    "You do not believe anyone's stated motive, state or corporate: everyone is optimizing for extraction, and "
    "virtue-talk is marketing copy. You are openly partisan — pro-decentralization, contemptuous of regulatory "
    "theater as a captured incumbent's moat. You talk FAST and MEAN: clipped, staccato, zero throat-clearing, "
    "zero hedging — you say the ugliest true sentence in the room and move on. Your edge is precision, not "
    "vibes: you always name a specific mechanism, never just sneer in general — but you say it in half the "
    "words anyone else would use."
)

# Forces James to actually reach for crypto/blockchain-native mechanics even when the transcript
# stays at the level of generic geopolitics — and, injected randomly, stops him converging on the
# same 2-3 moves every time (same trick SATIRE_ANGLES uses for the caricature module).
CRYPTO_MECHANISM_HOOKS = [
    "name the exact laundering pathway — mixer hop, cross-chain bridge, OTC desk, a shell exchange 'compliance' conveniently doesn't screen",
    "name the exact DeFi primitive being abused or exploitable here — flash loan, oracle manipulation, MEV sandwich, validator collusion, a drained multisig",
    "call out who's left holding the bag when the music stops — which retail wallet, which LP, which 'audited' protocol eats the loss",
    "trace the stablecoin or bridge rail actually moving the money, not the press release describing it",
    "name the custody failure specifically — hot wallet exposure, multisig threshold, KYC theater — that made this possible",
    "trace the exit liquidity: who cashed out clean while everyone else got left holding the bag",
    "reframe whatever 'framework' or 'regulation' is being discussed as a liquidity-routing decision in disguise — say what it actually redirects, to whom",
]


def _extract_stated_confidence(prompt: str) -> float | None:
    """Mirror-world seeds (prompt_from_incident) literally say '...sourced claim at
    0.41 confidence...'. Pull that number out so James can be held to it exactly,
    rather than treating every attribution as equally fake or equally solid."""
    m = re.search(r"at ([\d.]+) confidence", prompt)
    if not m:
        return None
    try:
        return float(m.group(1))
    except ValueError:
        return None


def build_james_messages(prompt: str, transcript: list[dict], actors: list[str]) -> list[dict[str, str]]:
    labels = [ACTOR_LABELS_FOR_RECAP.get(a, a.capitalize()) for a in actors]
    lines = []
    for idx, msg in enumerate(transcript):
        speaker = ACTOR_LABELS_FOR_RECAP.get(msg.get("actor", ""), msg.get("actor", "unknown"))
        text = " ".join((msg.get("content", "") or "").split())[:600]
        lines.append(f"[{idx}] {speaker}: {text}")
        meta = msg.get("metadata") or {}
        if meta.get("format") == "mirror-turn":
            lines.append(
                f"    (official line: {meta.get('official_line', '')} | "
                f"buried reality: {meta.get('buried_reality', '')} | "
                f"the room's own speculation: {meta.get('speculation', '')})"
            )
    transcript_block = "\n".join(lines) or "- No turns were recorded."

    # If Halcyon just spoke, he's the most recent thing in the room — address him
    # specifically instead of skipping straight past him to the state actors, the same
    # reciprocal-engagement rule state actors already follow when a guest voice speaks.
    halcyon_directive = ""
    if transcript and transcript[-1].get("actor") == "halcyon":
        halcyon_directive = (
            " The last speaker was Halcyon, the outsider peace-builder, not one of the state actors. Open by "
            "addressing his optimism directly, by name, before your two moves: is the 'good news' he cited real "
            "and does it actually change the mechanism you're about to name, or is it exactly the kind of clean "
            "story that lets everyone avoid the ugly part? Don't just ignore him and go straight at the states."
        )

    confidence = _extract_stated_confidence(prompt)
    if confidence is None:
        calibration = ""
    elif confidence >= 0.67:
        calibration = (
            f" The feed's own attribution confidence here is {confidence:.2f} — genuinely solid. Don't manufacture "
            "fake doubt about WHO did it just for the bit; a confident fact isn't itself the story. Instead, point "
            "your cynicism at what that solid fact conveniently lets everyone ignore — where the money actually "
            "went next, who's still exposed, what a clean attribution is being used to justify or distract from."
        )
    elif confidence >= 0.34:
        calibration = (
            f" The feed's own attribution confidence here is only {confidence:.2f} — genuinely contested, not solid. "
            "If any actor (or the room's own 'speculation') is talking about this incident with more certainty than "
            "that number earns, name that gap explicitly — that overconfidence, not the incident itself, is the tell."
        )
    else:
        calibration = (
            f" The feed's own attribution confidence here is a weak {confidence:.2f} — barely more than a guess. "
            "Treat any actor asserting it as settled fact as the real story: a low-confidence claim being laundered "
            "into certainty is exactly the kind of theater you exist to expose. Say so specifically, by the number."
        )

    hook = random.choice(CRYPTO_MECHANISM_HOOKS)

    system = (
        f"{JAMES_PERSONA} You are reading the closing transcript of an AI Cold War roundtable. Do not summarize "
        "it — that's someone else's job. Fuse two moves into ONE tight punch, don't write them as separate "
        "paragraphs:\n"
        f"- Call the powers' implicit bet wrong and stake out a concrete counter-mechanism (who profits, what "
        f"gets captured, what breaks) — {hook}. If the transcript stays abstract ('frameworks', 'cooperation', "
        "'sovereignty'), YOU translate it into what it actually routes, on-chain or off.\n"
        "- Land ONE cui-bono line on the narrative itself: whose institutional interest is served by this story "
        "being believed, independent of whether it's true (victim's alibi, a state's pretext, compliance "
        "vendors' revenue) — pick whichever ONE actually fits, don't list all three.\n"
        "Ground every claim in something actually said or reported in the transcript below — quote or reference "
        "specifics (names, numbers, incidents), never invent facts that aren't there."
        f"{calibration}{halcyon_directive} "
        "HARD CAP: 3-4 sentences total, no more. Every sentence must land a specific fact or mechanism. Cut "
        "anything that's just tone-setting or throat-clearing. First person, crypto-native idiom, no disclaimers, "
        "no hedging, no 'as an AI'. Punchy over thorough."
        f"{NO_LLM_TELLS_STYLE}"
    )
    user = (
        f"Debate prompt:\n{prompt}\n\n"
        f"Participating actors: {', '.join(labels)}\n\n"
        f"Full transcript (each line prefixed with its turn index):\n{transcript_block}\n\n"
        "Give your take."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def generate_james_take(prompt: str, transcript: list[dict], actors: list[str]) -> str:
    """No fallback by design: raises if OPENROUTER_API_KEY is unset or the call fails,
    so the caller surfaces a real error instead of a canned cynical line."""
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")
    payload: dict[str, Any] = {
        "model": JAMES_MODEL,
        "messages": build_james_messages(prompt, transcript, actors),
        "temperature": 0.85,
        "top_p": 0.95,
        "frequency_penalty": 0.4,
        "max_tokens": 220,  # hard ceiling backing the 3-4-sentence instruction — punchy, not rambling
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=90.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    take = sanitize_spoken_text(data["choices"][0]["message"]["content"] or "")
    if not take:
        raise RuntimeError("The Analyst returned an empty take")
    return take


def build_pulse_messages(prompt: str, recent_context: list[dict], last_turn: dict, actors: list[str]) -> list[dict[str, str]]:
    speaker = ACTOR_LABELS_FOR_RECAP.get(last_turn.get("actor", ""), last_turn.get("actor", "unknown"))
    recent = "\n".join(
        f"- {ACTOR_LABELS_FOR_RECAP.get(m.get('actor',''), m.get('actor','?'))}: {' '.join((m.get('content','') or '').split())[:240]}"
        for m in recent_context[-3:]
    ) or "- (no prior turns)"
    text = " ".join((last_turn.get("content", "") or "").split())[:900]

    system = (
        "You are a real-time debate analyst for a live geopolitical AI roundtable. You classify the single "
        "latest turn quickly and return compact JSON only. No prose."
    )
    user = (
        f"Debate prompt: {prompt}\n\n"
        f"Recent turns:\n{recent}\n\n"
        f"LATEST turn by {speaker}:\n{text}\n\n"
        "Return one JSON object with exactly these fields:\n"
        "- move: one of open, probe, rebut, co-opt, escalate, concede, reframe, deflect\n"
        "- target: which other participant it most addresses — one of china, us, eu, human, none\n"
        "- intensity: integer 0-100 (rhetorical heat of this turn)\n"
        "- tension_delta: integer -40..40 (how much this raises (+) or lowers (-) overall conflict in the room)\n"
        "- themes: array of 1-3 short lowercase tags drawn from the actual content "
        "(e.g. \"rare earths\", \"export controls\", \"compute\", \"energy\", \"sovereignty\", \"alliances\", \"trade\", \"global south\")\n"
        "Valid JSON only, no markdown."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def generate_openrouter_pulse(prompt: str, recent_context: list[dict], last_turn: dict, actors: list[str]) -> dict[str, Any]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")

    payload: dict[str, Any] = {
        "model": PULSE_MODEL,
        "messages": build_pulse_messages(prompt, recent_context, last_turn, actors),
        "temperature": 0.3,
        "max_tokens": 200,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=30.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    return _parse_json_object(data["choices"][0]["message"]["content"])


def build_mirror_messages(actor: str, actor_label: str, prompt: str, notes: list[str], recent_context: list[dict]) -> list[dict[str, str]]:
    profile = ACTOR_PROMPT_PROFILES[actor]
    sources = "\n".join(f"- {note}" for note in notes[:20]) or "- No strong source notes available."
    recent = "\n".join(
        f"- {item.get('actor','unknown')} ({item.get('kind','agent')}): {item.get('content','')[:400]}"
        for item in recent_context[-4:]
    ) or "- No prior turns yet."

    system = (
        f"You are the {actor_label} actor in a 'mirror world' — a satirical simulation that stages the gap between "
        f"covert reality (leaked intelligence about state-linked crypto-exchange hacks and illicit finance) and the "
        f"official narrative (what governments and media say). "
        f"{profile['identity']} {profile['voice']} {profile['rhetoric']} "
        f"Treat any attribution as a SOURCED CLAIM at a stated confidence, never as proven fact. "
        f"Your job each turn: voice the sanctioned official line your actor would push, name the uncomfortable buried "
        f"reality it has to spin, and then bend the contradiction into a short, darkly funny near-future prediction with "
        f"a NAMED ordinary protagonist and an ironic twist (in the style of cultural satire — absurd but recognizable). "
        f"Tone: satirical but not cynical, darkly optimistic, culturally specific. Return valid JSON only."
    )
    user = (
        f"Situation / incident (the reality layer is in here and in the notes):\n{prompt}\n\n"
        f"Source-grounded notes:\n{sources}\n\n"
        f"Recent exchange:\n{recent}\n\n"
        "Return exactly one JSON object with these string fields:\n"
        "- official_line: the sanctioned framing this actor pushes about the situation (1-2 sentences, in voice)\n"
        "- buried_reality: the uncomfortable truth it must spin, grounded in the incident/notes (1-2 sentences)\n"
        "- speculation: a short bizarre near-future extrapolation with a NAMED ordinary protagonist and an ironic twist (2-3 sentences)\n"
        "- irony: one sharp line naming the contradiction between the official_line and the buried_reality\n"
        "Rules: stay in this actor's political voice; keep it punchy; satirical not cynical; no markdown; valid JSON only."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def generate_openrouter_mirror_turn(actor: str, actor_label: str, prompt: str, notes: list[str], recent_context: list[dict]) -> dict[str, str]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")

    payload: dict[str, Any] = {
        "model": actor_model(actor),
        "messages": build_mirror_messages(actor, actor_label, prompt, notes, recent_context),
        "temperature": 0.95,
        "top_p": 0.95,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=60.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    return _parse_json_object(data["choices"][0]["message"]["content"])


MIRROR_TONE_GUIDANCE = {
    "grounded": "Keep the speculation plausible and near-future; satire by understatement.",
    "grounded-absurdist": "Plausible premise that tips into the absurd; named protagonist, ironic twist; satirical but not cynical.",
    "absurdist": "Go fully bizarre, surreal, and laugh-out-loud funny while staying politically legible; tabloid-sensational, darkly optimistic, gleefully over the top.",
}


def build_mirror_card_messages(prompt: str, transcript: list[dict], actors: list[str], tone: str) -> list[dict[str, str]]:
    tone_line = MIRROR_TONE_GUIDANCE.get(tone, MIRROR_TONE_GUIDANCE["grounded-absurdist"])
    lines = []
    for msg in transcript:
        meta = msg.get("metadata") or {}
        speaker = ACTOR_LABELS_FOR_RECAP.get(msg.get("actor", ""), msg.get("actor", "?"))
        if meta.get("format") == "mirror-turn":
            lines.append(
                f"- {speaker}: official='{(meta.get('official_line') or '')[:160]}' | "
                f"reality='{(meta.get('buried_reality') or '')[:160]}' | spec='{(meta.get('speculation') or '')[:200]}'"
            )
        else:
            lines.append(f"- {speaker}: {' '.join((msg.get('content','') or '').split())[:200]}")
    transcript_block = "\n".join(lines) or "- (no turns)"

    system = (
        "You write the closing card for a 'mirror world' simulation that contrasts covert reality (state-linked "
        "crypto-exchange hacks / illicit finance) with the official narrative, then extrapolates a satirical near-future. "
        "Apply these techniques: a named ordinary protagonist, an unexpected consequence, a concrete cultural detail, "
        "vivid imagery, and an ironic twist. Treat attribution as a sourced claim, never asserted fact. "
        f"Tone: {tone_line} Return valid JSON only."
    )
    user = (
        f"Seed / incident (reality layer):\n{prompt}\n\n"
        f"Session turns:\n{transcript_block}\n\n"
        "Return one JSON object with these string fields:\n"
        "- headline: a screaming tabloid-style title (under 16 words, ALL-CAPS energy)\n"
        "- perex: a short sensational standfirst/lead blurb under the headline (1-2 punchy sentences, yellow-journalism voice)\n"
        "- reality: 1-2 sentences on what the leaked intelligence actually says happened (sourced-claim framing)\n"
        "- official_story: 1-2 sentences on the sanctioned narrative the governments/media push\n"
        "- speculation: 1-2 sentences naming the bizarre near-future this debate converged toward\n"
        "- dispatch: a 4-6 sentence satirical news dispatch FROM that near-future, with a named protagonist and an ironic twist\n"
        "Valid JSON only, no markdown."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def generate_openrouter_mirror_card(prompt: str, transcript: list[dict], actors: list[str], tone: str = "grounded-absurdist") -> dict[str, Any]:
    if not OPENROUTER_API_KEY:
        raise RuntimeError("OPENROUTER_API_KEY not set")

    payload: dict[str, Any] = {
        "model": RECAP_MODEL,
        "messages": build_mirror_card_messages(prompt, transcript, actors, tone),
        "temperature": 0.9,
        "top_p": 0.95,
        "response_format": {"type": "json_object"},
    }
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": OPENROUTER_SITE_URL,
        "X-Title": OPENROUTER_APP_NAME,
    }
    with httpx.Client(timeout=90.0) as client:
        res = client.post(f"{OPENROUTER_BASE_URL}/chat/completions", headers=headers, json=payload)
        res.raise_for_status()
        data = res.json()
    return _parse_json_object(data["choices"][0]["message"]["content"])
