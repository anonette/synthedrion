from __future__ import annotations

import json
from typing import Any

import httpx

from .config import ACTOR_MODELS, OPENROUTER_API_KEY, OPENROUTER_APP_NAME, OPENROUTER_BASE_URL, OPENROUTER_SITE_URL


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


def build_actor_messages(actor: str, actor_label: str, prompt: str, notes: list[str], recent_context: list[dict], mode: str) -> list[dict[str, str]]:
    profile = ACTOR_PROMPT_PROFILES[actor]
    mode_guidance = MODE_PROMPT_GUIDANCE.get(mode, "")
    sources = "\n".join(f"- {note}" for note in notes[:14]) or "- No strong source notes available."
    recent = "\n".join(
        f"- {item.get('actor','unknown')} ({item.get('kind','agent')}): {item.get('content','')[:500]}"
        for item in recent_context[-4:]
    ) or "- No recent dialogue context."

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
    )

    user = (
        f"Session prompt:\n{prompt}\n\n"
        f"Source-grounded notes available to you:\n{sources}\n\n"
        f"Recent dialogue context:\n{recent}\n\n"
        "Now produce one natural spoken intervention for the roundtable.\n"
        "Requirements:\n"
        "- respond directly to the most recent speaker or intervention when there is one\n"
        "- use at least one concrete idea from the source notes\n"
        "- introduce one strategic twist, reframing, wedge move, or unexpected line of attack\n"
        "- press on a vulnerability, contradiction, dependency, or hypocrisy in what others are saying\n"
        "- try to gain argumentative advantage, not just summarize or sound balanced\n"
        "- let geopolitical interests, cultural-political style, and institutional identity shape the wording and cadence\n"
        "- keep it readable and persuasive, about 140 to 260 words\n"
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
    return data["choices"][0]["message"]["content"].strip()


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
