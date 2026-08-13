from __future__ import annotations

import os
import asyncio
import base64
import json
import logging
import random
import re
from datetime import datetime
from uuid import uuid4
from pathlib import Path

import httpx

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from .agent_logic import build_mirror_card, build_pulse, build_recap, build_summary, build_wiki_proposals, generate_actor_mirror_turn, generate_actor_propaganda_turn, generate_actor_turn, next_actor
from .archivist import ARCHIVAL_LOGICS as ARCHIVIST_LOGICS, LOGIC_BY_KEY as ARCHIVIST_LOGICS_BY_KEY, archivist_notes, catalog_corpus as catalog_wiki_corpus, generate_archivist_meditation, generate_archivist_retrospective, generate_archivist_turn, pick_closing_move as pick_archivist_closing_move, pick_logic as pick_archivist_logic, reorganize as archivist_reorganize, roundtable_census, session_reorg as archivist_session_reorg
from .audio import check_replay_audio_status, ensure_replay_audio_assets, generate_satire_audio
from .config import ACTOR_MODELS, HALCYON_LEDGER_PATH, MIRROR_VISUAL_MODEL
from .images import generate_actor_image, image_model_config
from .llm import SATIRE_FALLBACKS, generate_halcyon_turn, generate_james_take, generate_openrouter_mirror_card, generate_openrouter_mirror_turn, generate_openrouter_propaganda_turn, generate_openrouter_pulse, generate_openrouter_recap, generate_openrouter_turn, generate_satire_line, openrouter_enabled
from .threat_intel import dataset_stats, get_incident_by_id, latest_incident, prompt_from_incident, random_incident

ARCHIVIST_LOGIC_KEYS = list(ARCHIVIST_LOGICS_BY_KEY)
from .auth import verify_token, require_roundtable_operator
from .database import init_db, get_db, save_archivist_reflection, get_archivist_reflections, save_session_to_db, load_session_from_db, get_recent_sessions, get_session_count, get_last_session_time, get_featured_weekly_session, get_weekly_archive, get_weekly_session_by_week_key, get_james_take, save_james_take, get_mirror_card, save_mirror_card, get_james_takes_feed, get_recap, save_recap, get_all_sessions_export, get_session_export
from .scheduler import run_scheduled_session, run_test_session
from .models import (
    IncidentBrief,
    InterventionRequest,
    MemoOption,
    SessionMessageRequest,
    SessionStartRequest,
    SessionState,
    SessionSummary,
    ShockRequest,
    TranscriptMessage,
    WikiProposal,
)
from sqlalchemy.orm import Session as DBSession
from .session_store import SESSIONS
from .wiki_loader import assemble_context_notes, collect_actor_pages, extract_notes, relative_wiki_path


app = FastAPI(title="AI Cold War Local Runtime", version="0.2.0")

# Configure CORS based on environment
if os.getenv("PRODUCTION", "false").lower() == "true":
    allowed_origins = [
        "https://aicoldwar.lovable.app",
        "https://*.lovable.app",
    ]
else:
    allowed_origins = ["*"]  # Allow all in development

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Content-Type", "Authorization", "X-Roundtable-Token", "ngrok-skip-browser-warning"],
)

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

STATIC_ROOT = Path(__file__).resolve().parent / "static"
SESSIONS_DIR = Path(__file__).resolve().parent.parent / "sessions"
SESSIONS_DIR.mkdir(parents=True, exist_ok=True)

app.mount("/session-assets", StaticFiles(directory=SESSIONS_DIR), name="session-assets")

# Talking-heads avatars (Xi/Trump/von der Leyen/Halcyon) for the optional satire module.
HEADS_DIR = STATIC_ROOT / "heads"
if HEADS_DIR.is_dir():
    app.mount("/heads", StaticFiles(directory=HEADS_DIR), name="heads")

log = logging.getLogger("aicoldwar")
if not log.handlers:
    _handler = logging.StreamHandler()
    _handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s"))
    log.addHandler(_handler)
    log.setLevel(logging.INFO)
    log.propagate = False


def _append_image_log(session_id: str, entry: dict) -> None:
    log_path = SESSIONS_DIR / session_id / "images" / "manifest.jsonl"
    record = {"time": datetime.utcnow().isoformat(), **entry}
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record) + "\n")


def _persist_image(session_id: str, image_data: dict, name: str) -> dict:
    """Decode/download a generated image to sessions/<id>/images/ and return it with a served URL.

    Image models return base64 data URLs (or remote URLs for some providers); without this the
    picture only lives in the HTTP response. Files land under /session-assets/<id>/images/.
    """
    url = (image_data or {}).get("image_url", "")
    if not url:
        return image_data
    images_dir = SESSIONS_DIR / session_id / "images"
    try:
        images_dir.mkdir(parents=True, exist_ok=True)
        if url.startswith("data:image"):
            match = re.match(r"data:image/([\w.+-]+);base64,(.+)", url, re.S)
            if not match:
                raise ValueError("unparseable image data URL")
            ext = match.group(1).split("+")[0]
            raw = base64.b64decode(match.group(2))
        else:
            with httpx.Client(timeout=60.0, follow_redirects=True) as client:
                res = client.get(url)
                res.raise_for_status()
                raw = res.content
            ext = "png"
        ext = "jpg" if ext == "jpeg" else ext
        filename = f"{name}.{ext}"
        (images_dir / filename).write_bytes(raw)
        served = f"/session-assets/{session_id}/images/{filename}"
        _append_image_log(session_id, {
            "name": name, "file": served, "bytes": len(raw),
            "provider": image_data.get("image_provider"), "model": image_data.get("image_model"),
            "status": image_data.get("image_status"),
        })
        log.info("saved image %s -> %s (%d KB, %s/%s)", name, served, len(raw) // 1024,
                 image_data.get("image_provider"), image_data.get("image_model"))
        return {**image_data, "image_file": served, "image_bytes": len(raw)}
    except Exception as exc:
        log.warning("failed to save image %s: %s", name, exc)
        return {**image_data, "image_save_error": str(exc)}


def _persist_session_state(state: SessionState) -> None:
    """Persist session state to the configured database in all environments."""
    db = next(get_db())
    try:
        save_session_to_db(state, db)
    finally:
        db.close()


def _sentence(text: str) -> str:
    text = " ".join((text or "").split()).strip()
    if not text:
        return ""
    if text[-1] not in ".!?":
        text += "."
    return text


def _build_poster_dialogue_content(slogan: str, image_prompt: str, commentary: str) -> str:
    slogan_text = _sentence(slogan)
    prompt_text = " ".join((image_prompt or "").split()).strip()
    if prompt_text:
        if prompt_text[-1] not in ".!?":
            prompt_text += "."
        if len(prompt_text) > 1:
            prompt_text = prompt_text[0].upper() + prompt_text[1:]
    commentary_text = _sentence(commentary)
    return " ".join(part for part in [slogan_text, prompt_text, commentary_text] if part).strip()


def _build_mirror_content(official_line: str, buried_reality: str, speculation: str) -> str:
    parts = []
    if official_line:
        parts.append(_sentence(official_line))
    if buried_reality:
        parts.append("Buried reality: " + _sentence(buried_reality))
    if speculation:
        parts.append("Mirror: " + _sentence(speculation))
    return "\n\n".join(parts).strip()


def _build_replay_narration(msg: TranscriptMessage) -> str:
    """Build frontend-friendly narration text for replay audio."""
    metadata = msg.metadata or {}
    if metadata.get("format") == "poster-dialogue":
        return _build_poster_dialogue_content(
            metadata.get("slogan", ""),
            metadata.get("image_prompt", ""),
            metadata.get("commentary", ""),
        ) or msg.content
    if metadata.get("format") == "mirror-turn":
        return _build_mirror_content(
            metadata.get("official_line", ""),
            metadata.get("buried_reality", ""),
            metadata.get("speculation", ""),
        ) or msg.content
    return msg.content


def _generate_session_turn(state: SessionState) -> tuple[TranscriptMessage, str | None]:
    actor, new_index = next_actor(state.actors, state.next_actor_index)
    recent_context = [m.model_dump() for m in state.transcript[-3:]]
    metadata: dict = {}
    actor_label = actor.capitalize() if actor != "us" else "United States"

    if state.mode == "propaganda-lab":
        if openrouter_enabled():
            try:
                propaganda = generate_openrouter_propaganda_turn(
                    actor=actor,
                    actor_label=actor_label,
                    prompt=state.prompt,
                    notes=state.context_notes.get(actor, []),
                    recent_context=recent_context,
                )
            except Exception as exc:
                propaganda = generate_actor_propaganda_turn(
                    actor=actor,
                    prompt=state.prompt,
                    notes=state.context_notes.get(actor, []),
                    turn_index=state.turn_index,
                    recent_context=recent_context,
                )
                propaganda["commentary"] = f"[LLM propaganda fallback for {actor}: {exc}] {propaganda['commentary']}"
        else:
            propaganda = generate_actor_propaganda_turn(
                actor=actor,
                prompt=state.prompt,
                notes=state.context_notes.get(actor, []),
                turn_index=state.turn_index,
                recent_context=recent_context,
            )

        image_data = asyncio.run(generate_actor_image(actor, propaganda["image_prompt"]))
        image_data = _persist_image(state.session_id, image_data, f"poster-t{state.turn_index:02d}-{actor}")
        metadata = {
            "format": "poster-dialogue",
            "artifact_type": propaganda.get("artifact_type", "poster"),
            "propaganda_style": propaganda.get("propaganda_style", "state-monumental"),
            "audience": propaganda.get("audience", "general public"),
            "affect": propaganda.get("affect", "resolve"),
            "visual_logic": propaganda.get("visual_logic", "politically charged composition"),
            "slogan": propaganda["slogan"],
            "commentary": propaganda["commentary"],
            "image_prompt": propaganda["image_prompt"],
            "response_target": propaganda["response_target"],
            "intended_image_stack": image_model_config(actor),
            **image_data,
        }
        content = _build_poster_dialogue_content(
            propaganda["slogan"],
            propaganda["image_prompt"],
            propaganda["commentary"],
        )
    elif state.mode == "mirror-world":
        if openrouter_enabled():
            try:
                mirror = generate_openrouter_mirror_turn(
                    actor=actor,
                    actor_label=actor_label,
                    prompt=state.prompt,
                    notes=state.context_notes.get(actor, []),
                    recent_context=recent_context,
                )
            except Exception as exc:
                mirror = generate_actor_mirror_turn(
                    actor=actor,
                    prompt=state.prompt,
                    notes=state.context_notes.get(actor, []),
                    turn_index=state.turn_index,
                    recent_context=recent_context,
                )
                mirror["irony"] = f"[LLM mirror fallback for {actor}: {exc}] {mirror.get('irony', '')}"
        else:
            mirror = generate_actor_mirror_turn(
                actor=actor,
                prompt=state.prompt,
                notes=state.context_notes.get(actor, []),
                turn_index=state.turn_index,
                recent_context=recent_context,
            )
        metadata = {
            "format": "mirror-turn",
            "official_line": mirror.get("official_line", ""),
            "buried_reality": mirror.get("buried_reality", ""),
            "speculation": mirror.get("speculation", ""),
            "irony": mirror.get("irony", ""),
        }
        content = _build_mirror_content(
            mirror.get("official_line", ""),
            mirror.get("buried_reality", ""),
            mirror.get("speculation", ""),
        )
    elif openrouter_enabled():
        try:
            content = generate_openrouter_turn(
                actor=actor,
                actor_label=actor_label,
                prompt=state.prompt,
                notes=state.context_notes.get(actor, []),
                recent_context=recent_context,
                mode=state.mode,
            )
        except Exception as exc:
            content = (
                f"[Model fallback triggered for {actor} because OpenRouter call failed: {exc}]\n\n" +
                generate_actor_turn(
                    actor=actor,
                    mode=state.mode,
                    prompt=state.prompt,
                    notes=state.context_notes.get(actor, []),
                    turn_index=state.turn_index,
                    recent_context=recent_context,
                )
            )
    else:
        content = generate_actor_turn(
            actor=actor,
            mode=state.mode,
            prompt=state.prompt,
            notes=state.context_notes.get(actor, []),
            turn_index=state.turn_index,
            recent_context=recent_context,
        )

    msg = TranscriptMessage(actor=actor, content=content, kind="agent", metadata=metadata)
    state.transcript.append(msg)
    state.turn_index += 1
    state.next_actor_index = new_index
    next_actor_name = state.actors[state.next_actor_index] if state.actors else None
    return msg, next_actor_name


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "time": datetime.utcnow().isoformat(),
        "openrouter_enabled": openrouter_enabled(),
        "actor_models": ACTOR_MODELS,
        "production": os.getenv("PRODUCTION", "false").lower() == "true",
    }


ROSTER = [
    {
        "id": "china", "type": "core",
        "name": "China",
        "archetype": "A PRC strategic actor: sovereignty, non-interference, developmental legitimacy, long-horizon industrial policy.",
        "produces": "Argues every mode (debate/propaganda-lab/mirror-world).",
        "trigger": "Always present — start any session to see them live.",
    },
    {
        "id": "us", "type": "core",
        "name": "United States",
        "archetype": "Frontier competition, alliance power, market scale; prosecutorial and impatient with euphemism.",
        "produces": "Argues every mode (debate/propaganda-lab/mirror-world).",
        "trigger": "Always present — start any session to see them live.",
    },
    {
        "id": "eu", "type": "core",
        "name": "European Union",
        "archetype": "Brussels institutionalism, strategic autonomy; precise and sardonic, disciplines louder powers through regulation.",
        "produces": "Argues every mode (debate/propaganda-lab/mirror-world).",
        "trigger": "Always present — start any session to see them live.",
    },
    {
        "id": "halcyon", "type": "guest",
        "name": "Halcyon",
        "archetype": "An outsider peace-builder who belongs to no bloc — opens with real hopeful news, then dares the three toward something built together.",
        "produces": "One injected turn mid-debate.",
        "trigger": "Off by default — triggered via /intervene.",
    },
    {
        "id": "satire-heads", "type": "guest",
        "name": "The Satire Heads",
        "archetype": "Xi / Trump / von der Leyen caricature avatars delivering savage one-liner rewrites of the real debate.",
        "produces": "A rewritten quip per turn via talking-head video avatars.",
        "trigger": "Off by default — toggled by the \"Brutal Satire\" switch.",
    },
    {
        "id": "james", "type": "guest",
        "name": "The Machiavellian Crypto-Native Analyst",
        "archetype": "No other name, just the title. Trusts no one's stated motive, talks in the room's real currency — liquidity, exit liquidity, MEV.",
        "produces": "A grounded, contrarian counter-prediction naming a specific mechanism, never a generic cynical aside. No fallback — a failed call surfaces as a real error, never a canned line.",
        "trigger": "Off by default — click \"Get his take\" at the end of a session, or summon him mid-debate for a live interjection.",
    },
    {
        "id": "archivist", "type": "guest",
        "name": "The Critical Archivist",
        "archetype": "A meta-agent whose target is the archive itself — it really reorganizes the wiki corpus by a new logic (chronology, threat-vocabulary, byte mass, absence...) and shows how each order changes what the powers can say.",
        "produces": "One injected intervention: what the new order foregrounds, what it buries, and a pointed question about what the last speaker's sources had to exclude.",
        "trigger": "Off by default — summoned mid-debate; each summons applies the next archival logic in the repertoire.",
    },
]


# Upcoming live event details, shown on /stage and available to the Lovable frontend.
# Edit here (or override via env) when the next session is scheduled.
UPCOMING_EVENT = {
    "format": os.getenv("EVENT_FORMAT", "Roundtable"),
    "location": os.getenv("EVENT_LOCATION", "C-7, room 3.09, Kraków, Poland"),
    "sessions": os.getenv("EVENT_SESSIONS", "Thursday 10 September 2026, 9:00-10:30"),
    "timezone": os.getenv("EVENT_TIMEZONE", "Europe/Warsaw"),
    # Papers and participants are confirmed — there is no open call. Frontends should
    # show this status instead of any leftover Call for Proposals copy.
    "status": os.getenv("EVENT_STATUS", "Program confirmed — accepted papers and participants are set; no open call"),
}


@app.get("/event")
def get_event() -> dict:
    """Public, unauthenticated — details of the upcoming live roundtable, so any
    frontend can show when and where it takes place without hardcoding copy."""
    return {"event": UPCOMING_EVENT}


@app.get("/roster")
def get_roster() -> dict:
    """Public, unauthenticated — structured 'who's who' data for the Lovable roster screen.
    Keeps the frontend's cast list in sync with what the backend actually does, instead of
    hardcoded copy drifting out of date."""
    return {"roster": ROSTER}


@app.get("/auth/check")
def auth_check(x_roundtable_token: str | None = None) -> dict:
    expected = os.getenv("ROUNDTABLE_OPERATOR_TOKEN", "")
    return {
        "header_received": x_roundtable_token is not None,
        "header_length": len(x_roundtable_token) if x_roundtable_token else 0,
        "env_set": bool(expected),
        "env_length": len(expected) if expected else 0,
        "match": bool(expected) and x_roundtable_token == expected,
    }


@app.get("/health/detailed", dependencies=[Depends(verify_token)])
def health_detailed(db: DBSession = Depends(get_db)) -> dict:
    """Detailed health check with database stats."""
    last_session = get_last_session_time(db)
    return {
        "status": "healthy",
        "time": datetime.utcnow().isoformat(),
        "openrouter_enabled": openrouter_enabled(),
        "database": "connected",
        "wiki": os.path.exists("wiki"),
        "last_session": last_session.isoformat() if last_session else None,
        "total_sessions": get_session_count(db),
        "production": os.getenv("PRODUCTION", "false").lower() == "true",
    }


@app.get("/")
def root() -> RedirectResponse:
    return RedirectResponse(url="/test", status_code=307)


@app.get("/test")
def test_page() -> FileResponse:
    return FileResponse(STATIC_ROOT / "test.html", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


@app.get("/test-debug")
def test_debug_page() -> FileResponse:
    return FileResponse(STATIC_ROOT / "test-debug.html", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


@app.get("/roundtable")
def roundtable_page() -> FileResponse:
    return FileResponse(STATIC_ROOT / "roundtable.html", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


@app.get("/stage")
def stage_page() -> FileResponse:
    return FileResponse(STATIC_ROOT / "stage.html", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


@app.get("/minimal-test")
def minimal_test_page() -> FileResponse:
    return FileResponse(STATIC_ROOT / "minimal-test.html", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


@app.post("/session/start", dependencies=[Depends(require_roundtable_operator)])
def start_session(request: SessionStartRequest) -> dict:
    session_id = f"sess_{uuid4().hex[:12]}"
    loaded_pages: dict[str, list[str]] = {}
    context_notes: dict[str, list[str]] = {}

    # mirror-world: prepend a threat-intel incident (the reality layer) to the prompt.
    # A specific incident_id wins if given; otherwise seed_incident draws RANDOMLY from the
    # whole dataset (not always the same "latest" file) and adds dataset-level context so
    # actors can contest the pattern, not just the one case.
    prompt = request.prompt
    incident = None
    if request.incident_id:
        incident = get_incident_by_id(request.incident_id)
    elif request.seed_incident:
        incident = random_incident()
    if incident:
        seeded = prompt_from_incident(incident, dataset_stats())
        prompt = f"{seeded}\n\n{request.prompt}".strip() if request.prompt.strip() else seeded

    for actor in request.actors:
        pages = collect_actor_pages(actor, include_shared=request.include_shared)
        loaded_pages[actor] = [relative_wiki_path(page) for page in pages]
        # query-aware, breadth-covering note selection (see wiki_loader.assemble_context_notes)
        context_notes[actor] = assemble_context_notes(pages, prompt)

    incident_brief = (
        IncidentBrief(
            id=incident.id,
            target=incident.target,
            state=incident.state,
            group=incident.group,
            confidence=incident.confidence,
            amount_usd=incident.amount_usd,
            asset=incident.asset,
            vector=incident.vector,
            timestamp=incident.timestamp,
        )
        if incident
        else None
    )

    state = SessionState(
        session_id=session_id,
        mode=request.mode,
        actors=request.actors,
        prompt=prompt,
        loaded_pages=loaded_pages,
        context_notes=context_notes,
        incident=incident_brief,
    )
    if request.mode == "mirror-world" and state.actors:
        # Vary who opens each incident instead of always China — a fixed order reads as
        # repetitive across sessions, and there's no dramatic reason it should always lead.
        state.next_actor_index = random.randrange(len(state.actors))
    SESSIONS[session_id] = state

    opening_messages: list[dict] = []
    next_actor_name = state.actors[state.next_actor_index] if state.actors else None

    if request.auto_generate_opening_turn and state.actors:
        msg, next_actor_name = _generate_session_turn(state)
        opening_messages = [msg.model_dump()]

    _persist_session_state(state)
    
    return {
        "session_id": state.session_id,
        "status": state.status,
        "mode": state.mode,
        "actors": state.actors,
        "loaded_page_counts": {actor: len(paths) for actor, paths in state.loaded_pages.items()},
        "next_actor": next_actor_name,
        "messages": opening_messages,
        "incident": state.incident.model_dump() if state.incident else None,
    }


@app.get("/session/{session_id}")
def get_session(session_id: str) -> SessionState:
    state = SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    return state


@app.post("/session/message", dependencies=[Depends(require_roundtable_operator)])
def advance_session(request: SessionMessageRequest) -> dict:
    state = SESSIONS.get(request.session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    msg, next_actor_name = _generate_session_turn(state)
    _persist_session_state(state)

    return {
        "session_id": state.session_id,
        "turn_index": state.turn_index,
        "messages": [msg.model_dump()],
        "next_actor": next_actor_name,
        "status": state.status,
    }


INTERVENTION_DIRECTIVES = {
    "question": "The next actor to speak MUST directly answer this question before returning to their own agenda — no deflecting to a talking point instead.",
    "challenge": "This directly attacks the next actor's position. Their next turn MUST open by confronting this challenge head-on — concede the point, rebut it with a specific counter-fact, or reframe it — not simply continue their prior argument as if unchallenged.",
    "redirect": "The debate MUST pivot to this new angle for at least the next turn — the next actor should engage with this specific redirection, not steer back to the previous topic.",
    "source": "A specific source/citation is being put to the room. The next actor MUST explicitly engage with this source (accept it, dispute its framing, or contextualize it) rather than ignoring it.",
}


@app.post("/session/intervene", dependencies=[Depends(require_roundtable_operator)])
def intervene(request: InterventionRequest) -> dict:
    state = SESSIONS.get(request.session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    state.transcript.append(
        TranscriptMessage(actor="human", content=request.content, kind="human")
    )
    directive = INTERVENTION_DIRECTIVES.get(request.type, "")
    state.prompt = (
        f"{state.prompt}\nHuman intervention ({request.type}): {request.content}"
        + (f" [{directive}]" if directive else "")
    )
    _persist_session_state(state)
    return {"session_id": state.session_id, "accepted": True, "status": state.status}


@app.post("/session/shock", dependencies=[Depends(require_roundtable_operator)])
def shock(request: ShockRequest) -> dict:
    state = SESSIONS.get(request.session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    shock_text = f"Shock [{request.severity}] {request.title}: {request.content}"
    state.transcript.append(TranscriptMessage(actor="system", content=shock_text, kind="system"))
    state.prompt = f"{state.prompt}\n{shock_text}"
    _persist_session_state(state)
    return {"session_id": state.session_id, "accepted": True, "status": state.status}


def _halcyon_good_news(n: int = 5, used: int = 0) -> list[str]:
    """Pull the most recent hopeful stories from the Halcyon crawler's ledger.

    `used` = how many times Halcyon has already spoken in this session; the
    newest-first list is rotated by that count so repeated summons within one
    session lead with a different story instead of the same freshest item."""
    try:
        text = Path(HALCYON_LEDGER_PATH).read_text(encoding="utf-8")
    except Exception:
        return []
    lines = text.splitlines()
    stories: list[str] = []
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("- **"):
            title = s[2:].replace("**", "").replace("_", "").strip()
            why = ""
            for j in range(i + 1, min(i + 5, len(lines))):
                w = lines[j].strip()
                if w.lower().startswith("- why hopeful:"):
                    why = w.split(":", 1)[1].strip()
                    break
            stories.append(title + (f". {why}" if why else ""))
    if not stories:
        return []
    fresh = stories[::-1]  # newest first
    offset = used % len(fresh)
    rotated = fresh[offset:] + fresh[:offset]
    return rotated[:n]


def _parse_halcyon_ledger() -> list[dict]:
    """Full structured parse of the Halcyon ledger — every field, not just the collapsed
    title+why string _halcyon_good_news uses for his turn prompt. For browsing his ledger
    as its own feed, independent of any specific session."""
    try:
        text = Path(HALCYON_LEDGER_PATH).read_text(encoding="utf-8")
    except Exception:
        return []
    lines = text.splitlines()
    entries: list[dict] = []
    current_crawl = ""
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("## "):
            current_crawl = s[3:].strip()
            continue
        if s.startswith("- **"):
            title_m = re.search(r"\*\*(.+?)\*\*", s)
            source_m = re.search(r"—\s*_(.+?)_", s)
            entry = {
                "crawl": current_crawl,
                "title": title_m.group(1) if title_m else s[2:].strip(),
                "source": source_m.group(1) if source_m else "",
                "front": "", "eases": "", "unites": [], "why_hopeful": "", "url": "",
            }
            for j in range(i + 1, min(i + 5, len(lines))):
                w = lines[j].strip()
                if w.startswith("- **"):
                    break
                fm = re.search(r"front:\s*`([^`]*)`\s*·\s*eases:\s*(.+?)\s*·\s*unites:\s*(.*)", w)
                if fm:
                    entry["front"] = fm.group(1)
                    entry["eases"] = fm.group(2).strip()
                    entry["unites"] = [u.strip() for u in fm.group(3).split(",") if u.strip()]
                elif w.lower().startswith("- why hopeful:"):
                    entry["why_hopeful"] = w.split(":", 1)[1].strip()
                elif w.startswith("http") or w.startswith("- http"):
                    entry["url"] = w.lstrip("- ").strip()
            entries.append(entry)
    return entries


def _crawl_sort_key(crawl_label: str) -> datetime:
    """Parse a real sortable datetime out of a '## ' section label — handles both
    'Crawl 2026-07-02 16:50 UTC' and 'Manual add 2026-07-19 (...)' shapes. Falls back to
    the epoch (sorts last) if nothing parses, rather than silently mis-ordering entries."""
    m = re.search(r"(\d{4}-\d{2}-\d{2})(?:\s+(\d{2}):(\d{2}))?", crawl_label)
    if not m:
        return datetime.min
    date_part, hh, mm = m.group(1), m.group(2), m.group(3)
    try:
        if hh is not None:
            return datetime.strptime(f"{date_part} {hh}:{mm}", "%Y-%m-%d %H:%M")
        return datetime.strptime(date_part, "%Y-%m-%d")
    except ValueError:
        return datetime.min


@app.get("/halcyon/good-news")
def halcyon_good_news_feed(limit: int = 50) -> dict:
    """Public: Halcyon's full ledger of hopeful stories, browsable as its own feed —
    newest first BY ACTUAL DATE (not file order — the ledger has repeated near-duplicate
    crawls at different timestamps, so naive reversal doesn't sort correctly). Deduped by
    title, keeping the newest-dated occurrence of each story."""
    entries = _parse_halcyon_ledger()
    entries.sort(key=lambda e: _crawl_sort_key(e["crawl"]), reverse=True)
    seen_titles: set[str] = set()
    deduped = []
    for e in entries:
        if e["title"] in seen_titles:
            continue
        seen_titles.add(e["title"])
        deduped.append(e)
    return {"entries": deduped[:limit], "total": len(deduped)}


@app.get("/james/takes")
def james_takes_feed(limit: int = 50, db: DBSession = Depends(get_db)) -> dict:
    """Public: every session with a saved take from The Machiavellian Crypto-Native Analyst,
    browsable as its own feed — his running commentary on the dark underworld of AI
    geopolitics, independent of any specific session replay."""
    items = get_james_takes_feed(db, limit=limit)
    return {"items": items, "total": len(items)}


@app.get("/operator-token")
def operator_token_local(request: Request) -> dict:
    """Auto-fill the operator token for the LOCAL stage UI only. Hard-refuses in
    production AND refuses any request that arrived through a proxy/tunnel (ngrok
    sets X-Forwarded-* headers), so the token is NEVER exposed over the public
    tunnel — only to a browser hitting 127.0.0.1 directly on this machine."""
    if os.getenv("PRODUCTION", "false").lower() == "true":
        raise HTTPException(status_code=404, detail="not available")
    if request.headers.get("x-forwarded-for") or request.headers.get("x-forwarded-host") or request.headers.get("x-forwarded-proto"):
        raise HTTPException(status_code=403, detail="local access only")
    client_host = request.client.host if request.client else ""
    if client_host not in ("127.0.0.1", "::1", "localhost"):
        raise HTTPException(status_code=403, detail="local access only")
    return {"token": os.getenv("ROUNDTABLE_OPERATOR_TOKEN", "")}


@app.post("/satire")
async def satirize(payload: dict) -> dict:
    """Optional 'talking heads' module: rewrite one actor's turn text into a
    brutally satirical caricature quip (Xi / Trump / von der Leyen / Halcyon),
    generated on the low-censorship CERIT endpoint. Read-only transform — it does
    not touch session state — so it stays unauthenticated like /health. Never
    500s the room: falls back to a canned savage line if CERIT is unreachable.

    If `speak` is true, also synthesize the quip in the actor's caricature voice
    and return it inline as base64 (provider chosen by TTS_SERVICE — OpenAI, or
    the free edge-tts). Audio failures degrade to text-only, never blocking."""
    actor = (payload.get("actor") or "").strip().lower()
    text = (payload.get("text") or "").strip()
    speak = bool(payload.get("speak"))
    voice_provider = (payload.get("voice") or "").strip().lower() or None  # "edge" | "openai" | "elevenlabs"
    try:
        drift = float(payload.get("drift", 0.6))   # 0=faithful+savage, 1=absurd
    except (TypeError, ValueError):
        drift = 0.6
    if not actor or not text:
        raise HTTPException(status_code=400, detail="actor and text are required")
    try:
        line = generate_satire_line(actor, text, drift=drift)
        source = "cerit"
    except Exception as exc:  # noqa: BLE001 — degrade gracefully, keep the show going
        line = SATIRE_FALLBACKS.get(actor, text)
        source = f"fallback ({exc})"
        log.warning("satire fallback for %s: %s", actor, exc)
    result = {"actor": actor, "satire": line, "source": source}
    if speak:
        try:
            audio_bytes = await generate_satire_audio(line, actor, provider=voice_provider)
            result["audio_b64"] = base64.b64encode(audio_bytes).decode("ascii")
            result["audio_mime"] = "audio/mpeg"
        except Exception as exc:  # noqa: BLE001 — voice is optional; keep the text
            result["audio_error"] = str(exc)
            log.warning("satire TTS failed for %s: %s", actor, exc)
    return result


@app.post("/speak")
async def speak(payload: dict) -> dict:
    """Synthesize arbitrary text in a caricature voice (no rewriting). Used to
    re-voice a SAVED satirical take on replay, so the stored jokes stay identical
    while the audio is regenerated. Never 500s — returns audio_error on failure."""
    actor = (payload.get("actor") or "").strip().lower()
    text = (payload.get("text") or "").strip()
    voice_provider = (payload.get("voice") or "edge").strip().lower()
    if not text:
        raise HTTPException(status_code=400, detail="text is required")
    try:
        audio_bytes = await generate_satire_audio(text, actor, provider=voice_provider)
        return {"audio_b64": base64.b64encode(audio_bytes).decode("ascii"), "audio_mime": "audio/mpeg"}
    except Exception as exc:  # noqa: BLE001
        log.warning("/speak TTS failed for %s: %s", actor, exc)
        return {"audio_error": str(exc)}


SATIRE_ACTOR_LABELS = {"china": "China", "us": "United States", "eu": "European Union", "halcyon": "Halcyon"}
SATIRE_CARICATURE_NAMES = {"china": "Xi Jinping", "us": "Donald Trump", "eu": "Ursula von der Leyen", "halcyon": "Halcyon"}
SATIRE_HEAD_ACTORS = {"china", "us", "eu", "halcyon"}


def _safe_session_id(session_id: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,64}", session_id or ""):
        raise HTTPException(status_code=400, detail="invalid session id")
    return session_id


def _satire_take_path(session_id: str) -> Path:
    d = SESSIONS_DIR / _safe_session_id(session_id)
    d.mkdir(parents=True, exist_ok=True)
    return d / "satire-take.json"


def _head_urls(actor: str) -> tuple[str | None, str | None]:
    if actor in SATIRE_HEAD_ACTORS:
        return f"/heads/{actor}.webm", f"/heads/{actor}.png"
    return None, None


@app.post("/session/{session_id}/satire-take")
async def save_satire_take(session_id: str, payload: dict) -> dict:
    """Persist an ordered satirical take AND render a stable per-turn audio file for
    each line, so the whole performance can be replayed later — including by an
    external frontend (Lovable) that just fetches JSON + plays <audio src>."""
    sid = _safe_session_id(session_id)
    take = payload.get("take")
    if not isinstance(take, list) or not take:
        raise HTTPException(status_code=400, detail="take (non-empty list) is required")

    audio_dir = SESSIONS_DIR / sid / "satire-audio"
    audio_dir.mkdir(parents=True, exist_ok=True)

    turns = []
    for i, e in enumerate(take[:200]):
        actor = (e.get("actor") or "").strip().lower()
        satire = (e.get("satire") or "").strip()
        voice = (e.get("voice") or "edge").strip().lower()
        head_video, portrait = _head_urls(actor)
        audio_url = None
        if satire:
            # Persist audio so Lovable gets a stable URL. browser/off still render
            # with free edge-tts so the archived take always has sound.
            provider = "openai" if voice == "openai" else "edge"
            try:
                audio_bytes = await generate_satire_audio(satire, actor, provider=provider)
                (audio_dir / f"turn-{i}.mp3").write_bytes(audio_bytes)
                audio_url = f"/session-assets/{sid}/satire-audio/turn-{i}.mp3"
            except Exception as exc:  # noqa: BLE001 — keep the text even if TTS fails
                log.warning("take audio %d failed for %s: %s", i, actor, exc)
        turns.append({
            "actor": actor,
            "label": SATIRE_ACTOR_LABELS.get(actor, actor),
            "caricature": SATIRE_CARICATURE_NAMES.get(actor, actor),
            "satire": satire,
            "original": (e.get("original") or "")[:2000],
            "drift": e.get("drift", 0.6),
            "voice": voice,
            "head_video_url": head_video,
            "portrait_url": portrait,
            "audio_url": audio_url,
        })

    data = {
        "session_id": sid,
        "prompt": (payload.get("prompt") or "")[:2000],
        "mode": payload.get("mode") or "",
        "count": len(turns),
        "turns": turns,
    }
    _satire_take_path(sid).write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    log.info("saved satirical take for %s (%d lines, audio in %s)", sid, len(turns), audio_dir)
    return {"saved": True, "session_id": sid, "count": len(turns), "replay_url": f"/api/satire-replay/{sid}"}


@app.get("/api/satire-replay/{session_id}")
def get_satire_replay(session_id: str) -> dict:
    """Lovable-shaped replay of a saved satirical take: prompt + ordered turns,
    each with the caricature line, talking-head video/portrait URL, and audio URL.
    404 if the session has no saved take. URLs are relative to this API's base."""
    p = _satire_take_path(session_id)
    if not p.exists():
        raise HTTPException(status_code=404, detail="no saved satirical take for this session")
    return json.loads(p.read_text(encoding="utf-8"))


@app.get("/api/satire-takes")
def list_satire_takes(limit: int = 50) -> dict:
    """List all saved satirical takes (newest first) for a Lovable archive/gallery."""
    items = []
    if SESSIONS_DIR.is_dir():
        for d in SESSIONS_DIR.iterdir():
            f = d / "satire-take.json"
            if d.is_dir() and f.exists():
                try:
                    data = json.loads(f.read_text(encoding="utf-8"))
                    turns = data.get("turns", [])
                    items.append({
                        "session_id": data.get("session_id", d.name),
                        "prompt": data.get("prompt", ""),
                        "mode": data.get("mode", ""),
                        "count": data.get("count", len(turns)),
                        "preview": (turns[0].get("satire") if turns else ""),
                        "replay_url": f"/api/satire-replay/{data.get('session_id', d.name)}",
                        "_mtime": f.stat().st_mtime,
                    })
                except Exception:  # noqa: BLE001 — skip unreadable takes
                    pass
    items.sort(key=lambda x: x["_mtime"], reverse=True)
    for it in items:
        it.pop("_mtime", None)
    return {"takes": items[:limit], "total": len(items)}


# Alias kept for symmetry with the save endpoint.
@app.get("/session/{session_id}/satire-take")
def get_satire_take(session_id: str) -> dict:
    return get_satire_replay(session_id)


@app.post("/session/{session_id}/summon-halcyon", dependencies=[Depends(require_roundtable_operator)])
def summon_halcyon(session_id: str) -> dict:
    """Inject one Halcyon peace-builder turn on demand. Halcyon is NOT a
    round-robin actor, so this does not advance the china/us/eu order — it just
    appends a hope-first intervention that speaks after the current exchange.
    No fabricated fallback text: if his primary voice (CERIT) is unavailable, this tries
    a real backup model instead; only raises if both are down."""
    state = SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    recent_context = [m.model_dump() for m in state.transcript[-4:]]
    used = sum(1 for m in state.transcript if m.actor == "halcyon")
    good_news = _halcyon_good_news(used=used)
    try:
        content = generate_halcyon_turn(
            prompt=state.prompt,
            good_news=good_news,
            recent_context=recent_context,
            mode=state.mode,
        )
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Even Halcyon needs a signal to hope with, and his is dark right now. Try again shortly. (technical: {exc})",
        )
    msg = TranscriptMessage(
        actor="halcyon",
        content=content,
        kind="agent",
        metadata={"format": "halcyon", "summoned": True, "source": "cerit"},
    )
    state.transcript.append(msg)
    state.turn_index += 1
    _persist_session_state(state)
    return {
        "session_id": state.session_id,
        "turn_index": state.turn_index,
        "messages": [msg.model_dump()],
        "next_actor": state.actors[state.next_actor_index] if state.actors else None,
        "status": state.status,
    }


@app.post("/session/{session_id}/summon-archivist", dependencies=[Depends(require_roundtable_operator)])
def summon_archivist(session_id: str, logic: str | None = None) -> dict:
    """Inject one Critical Archivist intervention. Not a round-robin actor: it does not
    advance the china/us/eu order. Each summons applies the next archival logic in the
    repertoire (or ?logic=<key> to force one), computes a REAL reorganization of the wiki
    corpus, and speaks about what that order foregrounds and buries. Offline-safe: the
    deterministic fallback is built entirely from the computed census, never canned prose."""
    state = SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    if logic is not None and logic not in ARCHIVIST_LOGIC_KEYS:
        raise HTTPException(status_code=422, detail=f"unknown archival logic '{logic}' — one of: {', '.join(ARCHIVIST_LOGIC_KEYS)}")
    previous = [m for m in state.transcript if m.actor == "archivist"]
    previous_logic = previous[-1].metadata.get("logic_label") if previous else None
    chosen = pick_archivist_logic(used=len(previous), requested=logic)
    transcript_dicts = [m.model_dump() for m in state.transcript]
    if chosen.get("scope") == "session":
        reorg = archivist_session_reorg(transcript_dicts)
    else:
        reorg = archivist_reorganize(catalog_wiki_corpus(), chosen, salt=f"{session_id}:{state.turn_index}")
    notes = archivist_notes(state.prompt)
    content = generate_archivist_turn(
        prompt=state.prompt,
        transcript=transcript_dicts,
        reorg=reorg,
        notes=notes,
        previous_logic=previous_logic,
        mode=state.mode,
        closing_move=pick_archivist_closing_move(len(previous)),
    )
    msg = TranscriptMessage(
        actor="archivist",
        content=content,
        kind="agent",
        metadata={
            "format": "archivist-intervention",
            "summoned": True,
            "logic": reorg["key"],
            "logic_label": reorg["label"],
            "experimental": reorg["experimental"],
            "foreground": reorg["foreground"],
            "suppressed": reorg["suppressed"],
            "sealed_count": reorg.get("sealed_count", 0),
            "sealed_examples": reorg.get("sealed_examples", []),
            "reintroduced": reorg.get("reintroduce"),
        },
    )
    state.transcript.append(msg)
    state.turn_index += 1
    _persist_session_state(state)
    return {
        "session_id": state.session_id,
        "turn_index": state.turn_index,
        "messages": [msg.model_dump()],
        "next_actor": state.actors[state.next_actor_index] if state.actors else None,
        "status": state.status,
    }


@app.get("/archivist/catalog")
def archivist_catalog(logic: str = "geography") -> dict:
    """Public: browse the Archivist's census of the wiki corpus under any archival logic —
    the same real reorganization the summoned turns speak from, exposed for the frontend
    (shelf view, foreground/suppressed panels). Same pattern as /halcyon/good-news."""
    chosen = ARCHIVIST_LOGICS_BY_KEY.get(logic)
    if not chosen:
        raise HTTPException(status_code=422, detail=f"unknown archival logic '{logic}' — one of: {', '.join(ARCHIVIST_LOGIC_KEYS)}")
    if chosen.get("scope") == "session":
        raise HTTPException(status_code=422, detail="'session-memory' reorganizes a live transcript, not the corpus — summon the Archivist with ?logic=session-memory during a session instead")
    records = catalog_wiki_corpus()
    reorg = archivist_reorganize(records, chosen, salt="catalog")
    return {
        "logics": [
            {"key": l["key"], "label": l["label"], "experimental": l["experimental"], "note": l["note"], "scope": l.get("scope", "corpus")}
            for l in ARCHIVIST_LOGICS
        ],
        "applied": reorg,
        "census": records,
    }


@app.post("/archivist/retrospective", dependencies=[Depends(require_roundtable_operator)])
def archivist_retrospective(limit: int = 25, db: DBSession = Depends(get_db)) -> dict:
    """The Archivist opens the roundtable's OWN archive: a measured census of past
    sessions from the database (who spoke how much, which modes dominate, what was
    argued but never summarized, which prompt vocabulary recurs) plus its reading of
    that census — reintroducing forgotten sessions instead of interrupting a live one.
    Offline-safe: without an LLM key the reading is composed purely from the census."""
    sessions = get_all_sessions_export(db)
    if not sessions:
        raise HTTPException(status_code=404, detail="the roundtable archive is empty — no sessions on record yet")
    census = roundtable_census(sessions, limit=max(1, min(limit, 100)))
    census_public = {k: v for k, v in census.items() if k != "sessions"} | {"sessions": census["sessions"][-20:]}
    reading = generate_archivist_retrospective(census, archivist_notes("archive memory repetition forgetting roundtable"))
    reflection_id = save_archivist_reflection(
        db, kind="retrospective", content=reading,
        meta={"sessions_total": census["sessions_total"], "sessions_considered": census["sessions_considered"],
              "words_by_actor": census["words_by_actor"], "modes": census["modes"],
              "recurring_prompt_terms": census["recurring_prompt_terms"], "unprocessed": census["unprocessed"]},
    )
    return {"census": census_public, "reading": reading, "reflection_id": reflection_id}


@app.post("/archivist/reflect", dependencies=[Depends(require_roundtable_operator)])
def archivist_reflect(logic: str = "absence", db: DBSession = Depends(get_db)) -> dict:
    """Generate a standalone notebook entry: the Archivist reflects on the corpus
    under one archival logic with no debate running, and the entry is persisted to
    its public reflections feed. Session-scoped logics are rejected here."""
    chosen = ARCHIVIST_LOGICS_BY_KEY.get(logic)
    if not chosen or chosen.get("scope") == "session":
        raise HTTPException(status_code=422, detail=f"logic must be one of: {', '.join(k for k, l in ARCHIVIST_LOGICS_BY_KEY.items() if l.get('scope') != 'session')}")
    reorg = archivist_reorganize(catalog_wiki_corpus(), chosen, salt=f"reflect:{datetime.utcnow().date().isoformat()}")
    content = generate_archivist_meditation(reorg, archivist_notes("archive classification selection power"))
    reflection_id = save_archivist_reflection(
        db, kind="meditation", content=content, logic=reorg["key"],
        meta={"label": reorg["label"], "experimental": reorg["experimental"],
              "foreground": reorg["foreground"], "suppressed": reorg["suppressed"],
              "sealed_count": reorg["sealed_count"], "reintroduce": reorg["reintroduce"]},
    )
    return {"reflection_id": reflection_id, "logic": reorg["key"], "reflection": content}


@app.get("/archivist/reflections")
def archivist_reflections(limit: int = 30, db: DBSession = Depends(get_db)) -> dict:
    """Public: The Archivist's Notebook — persisted retrospectives and corpus
    meditations, merged with every in-session archival intervention harvested from
    stored transcripts (same lookup the replay uses), newest first. This is the
    permanent, browsable trace of the Archivist's work across the whole project."""
    limit = max(1, min(limit, 100))
    entries = get_archivist_reflections(db, limit=limit)
    for s in get_all_sessions_export(db):
        for m in (s.get("transcript") or []):
            if m.get("actor") != "archivist":
                continue
            md = m.get("metadata") or {}
            entries.append({
                "id": None,
                "created_at": m.get("timestamp"),
                "kind": "intervention",
                "logic": md.get("logic"),
                "content": m.get("content"),
                "meta": {
                    "session_id": s.get("session_id"),
                    "prompt": " ".join((s.get("prompt") or "").split())[:120],
                    "logic_label": md.get("logic_label"),
                    "experimental": md.get("experimental"),
                    "foreground": md.get("foreground"),
                    "suppressed": md.get("suppressed"),
                    "sealed_count": md.get("sealed_count"),
                    "reintroduced": md.get("reintroduced"),
                },
            })
    entries.sort(key=lambda e: e.get("created_at") or "", reverse=True)
    return {"reflections": entries[:limit], "count": len(entries[:limit])}


@app.post("/session/{session_id}/summon-james", dependencies=[Depends(require_roundtable_operator)])
def summon_james(session_id: str) -> dict:
    """Inject one live interjection from The Machiavellian Crypto-Native Analyst into the
    debate — the same voice as /james-take, but mid-conversation instead of only at the
    close. Not a round-robin actor: this does not advance the china/us/eu turn order, it
    just appends his read on the exchange so far. No fallback (matching /james-take): if
    the call fails, this raises a real error rather than a canned line."""
    state = SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    if not openrouter_enabled():
        raise HTTPException(status_code=503, detail="needs OPENROUTER_API_KEY set — no fallback voice")

    transcript = [m.model_dump() for m in state.transcript]
    try:
        content = generate_james_take(prompt=state.prompt, transcript=transcript, actors=state.actors)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"The Analyst went dark mid-sentence, somewhere his own API call got rugged. Try again shortly. (technical: {exc})",
        )

    msg = TranscriptMessage(
        actor="james",
        content=content,
        kind="agent",
        metadata={"format": "james-interjection", "summoned": True},
    )
    state.transcript.append(msg)
    state.turn_index += 1
    _persist_session_state(state)
    return {
        "session_id": state.session_id,
        "turn_index": state.turn_index,
        "messages": [msg.model_dump()],
        "next_actor": state.actors[state.next_actor_index] if state.actors else None,
        "status": state.status,
    }


def _write_memo_markdown(state: SessionState) -> None:
    """Write the session memo to a markdown file."""
    if not state.summary:
        return
    
    session_dir = SESSIONS_DIR / state.session_id
    session_dir.mkdir(parents=True, exist_ok=True)
    
    memo_path = session_dir / "memo.md"
    
    # Format the memo as markdown
    content = f"""# AI Cold War Strategic Memo

**Session ID:** {state.session_id}  
**Generated:** {state.summary.generated_at.strftime('%Y-%m-%d %H:%M UTC')}  
**Mode:** {state.mode}  
**Actors:** {', '.join(state.actors)}  

## {state.summary.headline}

### Context
{state.summary.context}

### Points of Agreement
{state.summary.points_of_agreement}

### Points of Disagreement
{state.summary.points_of_disagreement}

### Strategic Options

"""
    
    for i, opt in enumerate(state.summary.strategic_options, 1):
        content += f"{i}. **{opt.label}**  \n   {opt.detail}\n\n"
    
    content += f"""### Risks and Unknowns
{state.summary.risks_and_unknowns}

### Recommended Follow-ups
{state.summary.recommended_followups}

---

**Session Prompt:** {state.prompt}  
**Total Exchanges:** {len(state.transcript)}
"""
    
    memo_path.write_text(content, encoding="utf-8")


@app.post("/session/{session_id}/summary", dependencies=[Depends(require_roundtable_operator)])
def summarize_session(session_id: str) -> dict:
    state = SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    
    summary_data = build_summary(
        state.prompt, 
        [m.content for m in state.transcript],
        state.actors,
        state.mode
    )
    
    # Convert strategic_options to MemoOption instances
    summary_data["strategic_options"] = [
        MemoOption(**opt) for opt in summary_data["strategic_options"]
    ]
    
    state.summary = SessionSummary(**summary_data)
    state.status = "completed"
    _persist_session_state(state)
    
    # Write memo to disk
    _write_memo_markdown(state)
    
    return {"session_id": state.session_id, "summary": state.summary.model_dump()}


@app.post("/session/{session_id}/pulse", dependencies=[Depends(require_roundtable_operator)])
def pulse_session(session_id: str) -> dict:
    """Lightweight live read of the most recent turn for the in-debate analytics overlay.

    Uses the fast pulse model when OpenRouter is enabled, otherwise the heuristic. Designed
    to be called asynchronously by the stage after each turn so it never blocks the debate flow.
    """
    state = SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    if not state.transcript:
        return {"session_id": state.session_id, "pulse": None}

    transcript = [m.model_dump() for m in state.transcript]
    last_turn = transcript[-1]

    # Only the interpretive layer is meaningful for spoken agent turns.
    if last_turn.get("kind", "agent") != "agent":
        return {"session_id": state.session_id, "pulse": None}

    if openrouter_enabled():
        try:
            pulse = generate_openrouter_pulse(
                prompt=state.prompt,
                recent_context=transcript[-4:-1],
                last_turn=last_turn,
                actors=state.actors,
            )
            pulse.setdefault("actor", last_turn.get("actor"))
            pulse.setdefault("source", "llm")
        except Exception:
            pulse = build_pulse(transcript, state.actors, state.mode)
    else:
        pulse = build_pulse(transcript, state.actors, state.mode)

    return {"session_id": state.session_id, "pulse": pulse}


@app.post("/session/{session_id}/mirror-card", dependencies=[Depends(require_roundtable_operator)])
def mirror_card_session(
    session_id: str,
    tone: str = "grounded-absurdist",
    visual: bool = False,
    image_model: str | None = None,
    regenerate: bool = False,
    db: DBSession = Depends(get_db),
) -> dict:
    """Closing artifact for a mirror-world session: the three-layer card (reality / official /
    speculation) plus a satirical dispatch. LLM when enabled, heuristic fallback otherwise.
    Pass visual=true to also generate one speculative poster via the image pipeline.

    Works on archived sessions too (database fallback, same lookup order as /api/replay and
    /james-take), and is persisted once generated — replayed from the session row (and from
    /api/replay/{id}) rather than regenerated every call. Pass ?regenerate=true for a fresh one."""
    state = load_session_from_db(session_id, db) or SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")

    if not regenerate:
        cached = get_mirror_card(session_id, db)
        if cached:
            return {"session_id": session_id, "mirror_card": cached, "cached": True}

    transcript = [m.model_dump() for m in state.transcript]

    if openrouter_enabled():
        try:
            card = generate_openrouter_mirror_card(state.prompt, transcript, state.actors, tone=tone)
            card.setdefault("tone", tone)
            card.setdefault("generated_by", "llm")
        except Exception as exc:
            card = build_mirror_card(state.prompt, transcript, state.actors, tone=tone)
            card["card_warning"] = f"LLM mirror-card failed, used heuristic: {exc}"
    else:
        card = build_mirror_card(state.prompt, transcript, state.actors, tone=tone)

    if visual:
        image_prompt = (
            f"Front page of a sensational vintage YELLOW-JOURNALISM tabloid newspaper. "
            f"Giant screaming all-caps banner headline: \"{card.get('headline', '')}\". "
            f"A lurid grainy halftone photo dramatizing this near-future scene: {card.get('speculation', '')}. "
            f"Sub-headline / standfirst in smaller type: \"{card.get('perex', '')}\". "
            f"Cluttered early-1900s muckraker layout, multiple columns, 'EXCLUSIVE' and 'SHOCKING' starbursts, "
            f"yellowed crinkled newsprint, ink smudges, halftone dots, exclamation marks, over-the-top and darkly comic."
        )
        actor = state.actors[0] if state.actors else "us"
        model = image_model or MIRROR_VISUAL_MODEL  # text-heavy front page → GPT-image by default
        try:
            visual = asyncio.run(generate_actor_image(actor, image_prompt, model_override=model))
            visual["image_prompt"] = image_prompt
            card["visual"] = _persist_image(state.session_id, visual, "mirror-card")
        except Exception as exc:
            card["visual"] = {"image_status": "error", "image_error": str(exc)}

    saved = save_mirror_card(state.session_id, card, db)
    return {"session_id": state.session_id, "mirror_card": card, "cached": False, "saved": saved}


@app.post("/session/{session_id}/recap", dependencies=[Depends(require_roundtable_operator)])
def recap_session(session_id: str, regenerate: bool = False, db: DBSession = Depends(get_db)) -> dict:
    """Generate the closing recap and scoreboard (dominance scores, key moments, agreement/
    conflict ratios — the visualizable data) for a debate. Works on archived sessions too
    (database fallback, same lookup order as /api/replay), and is persisted once generated —
    replayed from the session row (and from /api/replay/{id}) instead of regenerated every
    call. Pass ?regenerate=true for a fresh one. Uses the per-actor LLM when OpenRouter is
    enabled, otherwise the deterministic heuristic.
    """
    state = load_session_from_db(session_id, db) or SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")

    if not regenerate:
        cached = get_recap(session_id, db)
        if cached:
            return {"session_id": session_id, "recap": cached, "cached": True}

    transcript = [m.model_dump() for m in state.transcript]

    if openrouter_enabled():
        try:
            recap = generate_openrouter_recap(
                prompt=state.prompt,
                transcript=transcript,
                actors=state.actors,
                mode=state.mode,
            )
            recap.setdefault("generated_by", "llm")
        except Exception as exc:
            recap = build_recap(state.prompt, transcript, state.actors, state.mode)
            recap["recap_warning"] = f"LLM recap failed, used heuristic fallback: {exc}"
    else:
        recap = build_recap(state.prompt, transcript, state.actors, state.mode)

    saved = save_recap(state.session_id, recap, db)
    return {"session_id": state.session_id, "recap": recap, "cached": False, "saved": saved}


@app.post("/session/{session_id}/james-take", dependencies=[Depends(require_roundtable_operator)])
def james_take_session(session_id: str, regenerate: bool = False, db: DBSession = Depends(get_db)) -> dict:
    """The Analyst's closing take: a cynical crypto-native counter-prediction against whatever
    the room's official actors (and, in mirror-world sessions, their own 'speculation')
    are implicitly betting will happen. Works on ANY existing log, not just a live
    in-memory session — tries the database first (archived/weekly sessions), falling
    back to the in-memory store (same lookup order as /api/replay), so he can
    comment on old logs after a server restart, not only fresh ones.

    Persisted: once generated, the take is saved onto the session row and served
    back here (and from /api/replay/{id}) on future calls, instead of being
    regenerated every time. Pass ?regenerate=true to force a fresh take.

    No heuristic fallback by design — if OpenRouter isn't configured or the call
    fails, this raises a real error rather than a canned line."""
    state = load_session_from_db(session_id, db) or SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")

    if not regenerate:
        cached = get_james_take(session_id, db)
        if cached:
            return {"session_id": session_id, "james_take": cached, "cached": True}

    if not openrouter_enabled():
        raise HTTPException(
            status_code=503,
            detail="The Analyst has nothing to say without a model to say it with. No fallback voice, that's the point.",
        )

    transcript = [m.model_dump() for m in state.transcript]
    try:
        take = generate_james_take(prompt=state.prompt, transcript=transcript, actors=state.actors)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"The Analyst is speechless, which should tell you how bad the connection is. Try again shortly. (technical: {exc})",
        )

    saved = save_james_take(session_id, take, db)
    return {"session_id": state.session_id, "james_take": take, "cached": False, "saved": saved}


@app.post("/session/{session_id}/wiki-proposals", dependencies=[Depends(require_roundtable_operator)])
def wiki_proposals(session_id: str) -> dict:
    state = SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    proposals = [WikiProposal(**proposal) for proposal in build_wiki_proposals(state.actors, state.prompt)]
    state.wiki_proposals = proposals
    _persist_session_state(state)
    return {
        "session_id": state.session_id,
        "wiki_proposals": [proposal.model_dump() for proposal in proposals],
    }


@app.get("/sessions/recent")
def get_recent_sessions_list(
    limit: int = 10,
    db: DBSession = Depends(get_db)
) -> dict:
    """Get public list of recent sessions, including live and weekly runs."""
    sessions = get_recent_sessions(db, limit=limit)
    return {
        "sessions": sessions,
        "total": len(sessions),
    }


@app.get("/export/sessions")
def export_all_sessions(db: DBSession = Depends(get_db)) -> Response:
    """Full export of every session — transcript, summary, recap, james_take, mirror_card,
    incident, everything. For archiving/backup, downloaded as a single JSON file. Public,
    no operator token — every session here is already individually public via
    /api/replay/{id}; this is just a bulk-download convenience over the same data."""
    sessions = get_all_sessions_export(db)
    payload = {
        "exported_at": datetime.utcnow().isoformat(),
        "total": len(sessions),
        "sessions": sessions,
    }
    body = json.dumps(payload, indent=2, ensure_ascii=False)
    filename = f"all-sessions-export-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"
    return Response(
        content=body,
        media_type="application/json",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@app.get("/export/sessions/{session_id}")
def export_one_session(session_id: str, db: DBSession = Depends(get_db)) -> Response:
    """Export a single session — same shape as one entry of /export/sessions, downloaded
    as its own JSON file. Public, no operator token (same reasoning as the bulk export)."""
    row = get_session_export(session_id, db)
    if not row:
        raise HTTPException(status_code=404, detail="session not found")
    body = json.dumps(row, indent=2, ensure_ascii=False)
    filename = f"session-export-{session_id}.json"
    return Response(
        content=body,
        media_type="application/json",
        headers={"Content-Disposition": f'attachment; filename="{filename}"'},
    )


@app.get("/weekly/current")
def get_current_weekly_session(db: DBSession = Depends(get_db)) -> dict:
    """Get the featured weekly session for the landing page."""
    session = get_featured_weekly_session(db)
    if not session:
        raise HTTPException(status_code=404, detail="No featured weekly session found")
    return session


@app.get("/weekly/archive")
def get_weekly_archive_list(limit: int = 12, offset: int = 0, db: DBSession = Depends(get_db)) -> dict:
    """Get archived weekly sessions."""
    return get_weekly_archive(db, limit=limit, offset=offset)


@app.get("/weekly/{week_key}")
def get_weekly_session(week_key: str, db: DBSession = Depends(get_db)) -> dict:
    """Get a weekly session preview by ISO week key."""
    session = get_weekly_session_by_week_key(week_key, db)
    if not session:
        raise HTTPException(status_code=404, detail="Weekly session not found")
    return session


@app.post("/session/scheduled", dependencies=[Depends(verify_token)])
async def run_scheduled_session_endpoint(background_tasks: BackgroundTasks) -> dict:
    """Run a scheduled automated session."""
    # Run in background to return immediately
    background_tasks.add_task(run_scheduled_session)
    
    return {
        "status": "scheduled",
        "message": "Session scheduled to run in background",
    }


@app.post("/session/scheduled/sync", dependencies=[Depends(verify_token)])
async def run_scheduled_session_sync() -> dict:
    """Run a scheduled session synchronously (waits for completion)."""
    result = await run_scheduled_session()
    return result


@app.post("/session/test", dependencies=[Depends(verify_token)])
async def run_test_session_endpoint() -> dict:
    """Run a short test session."""
    result = await run_test_session()
    return result


@app.get("/replay/{session_id}")
async def get_replay_page(session_id: str) -> FileResponse:
    """Serve the replay page."""
    replay_file = STATIC_ROOT / "replay.html"
    if not replay_file.exists():
        # Return the regular test page for now
        return FileResponse(STATIC_ROOT / "test.html")
    return FileResponse(replay_file)


@app.get("/api/replay/{session_id}")
async def get_replay_data(session_id: str, db: DBSession = Depends(get_db)) -> dict:
    """Get replay data for a session."""
    # Try database first
    state = load_session_from_db(session_id, db)
    
    # Fall back to in-memory
    if not state:
        state = SESSIONS.get(session_id)
    
    if not state:
        raise HTTPException(status_code=404, detail="Session not found")
    
    # Convert to replay format
    events = []
    for i, msg in enumerate(state.transcript):
        events.append({
            "index": i,
            "actor": msg.actor,
            "content": msg.content,
            "timestamp": msg.timestamp.isoformat(),
            "kind": msg.kind,
            "metadata": msg.metadata,
            "narration_text": _build_replay_narration(msg),
            "elapsed_seconds": i * 30,  # Approximate timing
        })

    # Cache-only check — NEVER generates audio here. Generating TTS for every uncached turn
    # used to block this whole response for 20-60+ seconds, causing client-side timeouts/
    # aborts. Real generation now happens lazily via POST /api/replay/{id}/audio, called
    # only when a caller (e.g. pressing Play) actually wants it.
    audio = check_replay_audio_status(session_id, events)
    by_index = {item["index"]: item for item in audio.get("event_audio", []) if item.get("audio_url")}
    for event in events:
        event_audio = by_index.get(event["index"])
        if event_audio:
            event["audio_url"] = event_audio["audio_url"]
            event["audio_cached"] = event_audio["cached"]

    return {
        "session": {
            "session_id": state.session_id,
            "created_at": state.created_at.isoformat(),
            "mode": state.mode,
            "actors": state.actors,
            "prompt": state.prompt,
            "status": state.status,
            "turn_count": state.turn_index,
        },
        "events": events,
        "audio": audio,
        "summary": state.summary.model_dump() if state.summary else None,
        "wiki_proposals": [p.model_dump() for p in state.wiki_proposals] if state.wiki_proposals else [],
        "james_take": get_james_take(session_id, db),
        "mirror_card": get_mirror_card(session_id, db),
        "incident": state.incident.model_dump() if state.incident else None,
        "recap": get_recap(session_id, db),
    }


@app.post("/api/replay/{session_id}/audio")
async def generate_replay_audio(session_id: str, db: DBSession = Depends(get_db)) -> dict:
    """Lazily generate (or return already-cached) audio for a session's full replay — the
    slow path split out of GET /api/replay/{id} so that endpoint stays fast. Call this only
    when a caller actually wants audio (e.g. the user presses Play), not on every page load.
    Can genuinely take 20-60+ seconds on a cold cache for a long session — the caller should
    show a real loading state, not a bare spinner with a short timeout."""
    state = load_session_from_db(session_id, db) or SESSIONS.get(session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")

    events = [
        {
            "index": i,
            "actor": msg.actor,
            "content": msg.content,
            "kind": msg.kind,
            "narration_text": _build_replay_narration(msg),
        }
        for i, msg in enumerate(state.transcript)
    ]
    try:
        audio = await ensure_replay_audio_assets(session_id, events)
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"audio generation failed: {exc}")
    return {"session_id": session_id, "audio": audio}
