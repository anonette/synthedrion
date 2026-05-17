from __future__ import annotations

import os
import asyncio
from datetime import datetime
from uuid import uuid4
from pathlib import Path

from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

from .agent_logic import build_summary, build_wiki_proposals, generate_actor_propaganda_turn, generate_actor_turn, next_actor
from .audio import ensure_replay_audio_assets
from .config import ACTOR_MODELS
from .images import generate_actor_image, image_model_config
from .llm import generate_openrouter_propaganda_turn, generate_openrouter_turn, openrouter_enabled
from .auth import verify_token, optional_token, require_roundtable_operator
from .database import init_db, get_db, save_session_to_db, load_session_from_db, get_recent_sessions, get_session_count, get_last_session_time, get_featured_weekly_session, get_weekly_archive, get_weekly_session_by_week_key
from .scheduler import run_scheduled_session, run_test_session
from .models import (
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
from .wiki_loader import collect_actor_pages, extract_notes, relative_wiki_path


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

app.mount("/sessions", StaticFiles(directory=SESSIONS_DIR), name="sessions-files")


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


def _build_replay_narration(msg: TranscriptMessage) -> str:
    """Build frontend-friendly narration text for replay audio."""
    metadata = msg.metadata or {}
    if metadata.get("format") == "poster-dialogue":
        return _build_poster_dialogue_content(
            metadata.get("slogan", ""),
            metadata.get("image_prompt", ""),
            metadata.get("commentary", ""),
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


@app.get("/minimal-test")
def minimal_test_page() -> FileResponse:
    return FileResponse(STATIC_ROOT / "minimal-test.html", headers={"Cache-Control": "no-cache, no-store, must-revalidate"})


@app.post("/session/start", dependencies=[Depends(require_roundtable_operator)])
def start_session(request: SessionStartRequest) -> dict:
    session_id = f"sess_{uuid4().hex[:12]}"
    loaded_pages: dict[str, list[str]] = {}
    context_notes: dict[str, list[str]] = {}

    for actor in request.actors:
        pages = collect_actor_pages(actor, include_shared=request.include_shared)
        loaded_pages[actor] = [relative_wiki_path(page) for page in pages]
        notes: list[str] = []
        for page in pages:
            notes.extend(extract_notes(page))
        context_notes[actor] = notes[:40]

    state = SessionState(
        session_id=session_id,
        mode=request.mode,
        actors=request.actors,
        prompt=request.prompt,
        loaded_pages=loaded_pages,
        context_notes=context_notes,
    )
    SESSIONS[session_id] = state

    opening_messages: list[dict] = []
    next_actor_name = state.actors[0] if state.actors else None

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


@app.post("/session/intervene", dependencies=[Depends(require_roundtable_operator)])
def intervene(request: InterventionRequest) -> dict:
    state = SESSIONS.get(request.session_id)
    if not state:
        raise HTTPException(status_code=404, detail="session not found")
    state.transcript.append(
        TranscriptMessage(actor="human", content=request.content, kind="human")
    )
    state.prompt = f"{state.prompt}\nHuman intervention ({request.type}): {request.content}"
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
    token: str | None = Depends(optional_token),
    db: DBSession = Depends(get_db)
) -> dict:
    """Get list of recent sessions."""
    sessions = get_recent_sessions(db, limit=limit)
    return {
        "sessions": sessions,
        "total": len(sessions),
    }


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

    audio = None
    try:
        audio = await ensure_replay_audio_assets(session_id, events)
        by_index = {item["index"]: item for item in audio.get("event_audio", []) if item.get("audio_url")}
        for event in events:
            event_audio = by_index.get(event["index"])
            if event_audio:
                event["audio_url"] = event_audio["audio_url"]
                event["audio_cached"] = event_audio["cached"]
    except Exception as exc:
        audio = {"error": str(exc), "full_audio_url": None, "event_audio": []}
    
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
    }
