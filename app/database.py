"""Database models and connection for session persistence."""

import json
import os
from datetime import date, datetime
from typing import Optional

import sqlalchemy as sa
from sqlalchemy import create_engine, Column, String, DateTime, Text, JSON, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session as DBSession

from .models import SessionState, TranscriptMessage, SessionSummary, WikiProposal, IncidentBrief

# Database URL from environment or default to SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./sessions.db")

# Handle Heroku-style postgres:// URLs
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class SessionDB(Base):
    """Database model for persistent session storage."""
    
    __tablename__ = "sessions"
    
    id = Column(String, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    mode = Column(String(50), nullable=False)
    actors = Column(JSON, nullable=False)
    prompt = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)
    transcript = Column(JSON, nullable=True)
    summary = Column(JSON, nullable=True)
    wiki_proposals = Column(JSON, nullable=True)
    loaded_pages = Column(JSON, nullable=True)
    context_notes = Column(JSON, nullable=True)
    turn_index = Column(sa.Integer, default=0)
    next_actor_index = Column(sa.Integer, default=0)
    audio_url = Column(Text, nullable=True)
    replay_metadata = Column(JSON, nullable=True)
    session_type = Column(String(50), nullable=False, default="live")
    week_key = Column(String(20), nullable=True, index=True)
    week_start = Column(Date, nullable=True, index=True)
    is_featured_weekly = Column(Boolean, nullable=False, default=False)
    title = Column(String(255), nullable=True)
    theme = Column(String(255), nullable=True)
    james_take = Column(Text, nullable=True)
    mirror_card = Column(JSON, nullable=True)
    incident = Column(JSON, nullable=True)
    recap = Column(JSON, nullable=True)


class ArchivistReflectionDB(Base):
    """The Critical Archivist's notebook: persisted reflections that outlive any one
    session — retrospectives over the session archive and standalone corpus
    meditations. In-session interventions are NOT stored here (they live in session
    transcripts); the reflections feed harvests those at read time."""

    __tablename__ = "archivist_reflections"

    id = Column(sa.Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    kind = Column(String(30), nullable=False)  # "retrospective" | "meditation"
    logic = Column(String(50), nullable=True)  # archival logic key for meditations
    content = Column(Text, nullable=False)
    meta = Column(JSON, nullable=True)  # census stats / reorg summary backing the text


def save_archivist_reflection(db: DBSession, kind: str, content: str, logic: Optional[str] = None, meta: Optional[dict] = None, created_at: Optional[datetime] = None) -> int:
    row = ArchivistReflectionDB(kind=kind, logic=logic, content=content, meta=meta)
    if created_at is not None:
        row.created_at = created_at  # backfill keeps the original turn timestamp
    db.add(row)
    db.commit()
    db.refresh(row)
    return row.id


def get_archivist_reflections(db: DBSession, limit: int = 50) -> list[dict]:
    rows = (
        db.query(ArchivistReflectionDB)
        .order_by(ArchivistReflectionDB.created_at.desc())
        .limit(limit)
        .all()
    )
    return [
        {
            "id": r.id,
            "created_at": r.created_at.isoformat(),
            "kind": r.kind,
            "logic": r.logic,
            "content": r.content,
            "meta": r.meta,
        }
        for r in rows
    ]


class WeeklyPromptDB(Base):
    """Database model for weekly prompt storage."""
    
    __tablename__ = "weekly_prompts"
    
    id = Column(sa.Integer, primary_key=True, autoincrement=True)
    week_date = Column(sa.Date, nullable=False)
    prompt = Column(Text, nullable=False)
    theme = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


def get_db():
    """Get database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """Initialize database tables."""
    Base.metadata.create_all(bind=engine)
    _ensure_session_columns()


def _ensure_session_columns() -> None:
    """Backfill additive session columns for existing databases."""
    inspector = sa.inspect(engine)
    if "sessions" not in inspector.get_table_names():
        return

    existing = {column["name"] for column in inspector.get_columns("sessions")}
    additions = {
        "session_type": "ALTER TABLE sessions ADD COLUMN session_type VARCHAR(50) NOT NULL DEFAULT 'live'",
        "week_key": "ALTER TABLE sessions ADD COLUMN week_key VARCHAR(20)",
        "week_start": "ALTER TABLE sessions ADD COLUMN week_start DATE",
        "is_featured_weekly": "ALTER TABLE sessions ADD COLUMN is_featured_weekly BOOLEAN NOT NULL DEFAULT 0",
        "title": "ALTER TABLE sessions ADD COLUMN title VARCHAR(255)",
        "theme": "ALTER TABLE sessions ADD COLUMN theme VARCHAR(255)",
        "james_take": "ALTER TABLE sessions ADD COLUMN james_take TEXT",
        "mirror_card": "ALTER TABLE sessions ADD COLUMN mirror_card TEXT",
        "incident": "ALTER TABLE sessions ADD COLUMN incident TEXT",
        "recap": "ALTER TABLE sessions ADD COLUMN recap TEXT",
    }

    with engine.begin() as conn:
        for name, statement in additions.items():
            if name not in existing:
                conn.execute(sa.text(statement))


def _session_title(prompt: str) -> str:
    head = prompt.split(".", 1)[0].strip()
    return head[:252] + "..." if len(head) > 255 else head


_STEERING_MARKERS = ("\nHuman intervention (", "\nSpoken from the floor (", "\nShock [")


def public_prompt(prompt: str) -> str:
    """The prompt field doubles as LLM steering: interventions, floor questions, and
    shocks are appended to it so the next turn must engage them. Public reads show
    only the original question — the appended material already lives in the
    transcript, and the bracketed directives are internal instructions."""
    for marker in _STEERING_MARKERS:
        idx = prompt.find(marker)
        if idx != -1:
            prompt = prompt[:idx]
    return prompt.strip()


def _session_preview(s: SessionDB) -> dict:
    summary_headline = None
    if s.summary and isinstance(s.summary, dict):
        summary_headline = s.summary.get("headline")

    return {
        "session_id": s.id,
        "created_at": s.created_at.isoformat(),
        "completed_at": s.completed_at.isoformat() if s.completed_at else None,
        "mode": s.mode,
        "actors": s.actors,
        "prompt": (public_prompt(s.prompt)[:100] + "...") if len(public_prompt(s.prompt)) > 100 else public_prompt(s.prompt),
        "status": s.status,
        "turn_count": s.turn_index,
        "has_audio": bool(s.audio_url),
        "has_james_take": bool(s.james_take),
        "has_mirror_card": bool(s.mirror_card),
        "has_recap": bool(s.recap),
        "session_type": s.session_type or "live",
        "week_key": s.week_key,
        "week_start": s.week_start.isoformat() if s.week_start else None,
        "is_featured": bool(s.is_featured_weekly),
        "title": s.title or _session_title(s.prompt),
        "theme": s.theme,
        "summary_headline": summary_headline,
    }


def save_session_to_db(session_state: SessionState, db: DBSession, metadata: Optional[dict] = None) -> None:
    """Save or update a session in the database."""
    metadata = metadata or {}
    db_session = db.query(SessionDB).filter(SessionDB.id == session_state.session_id).first()
    
    if not db_session:
        db_session = SessionDB(id=session_state.session_id)
    
    # Update fields
    db_session.mode = session_state.mode
    db_session.actors = session_state.actors
    db_session.prompt = session_state.prompt
    db_session.status = session_state.status
    db_session.turn_index = session_state.turn_index
    db_session.next_actor_index = session_state.next_actor_index
    db_session.loaded_pages = session_state.loaded_pages
    db_session.context_notes = session_state.context_notes
    db_session.session_type = metadata.get("session_type", db_session.session_type or "live")
    db_session.week_key = metadata.get("week_key", db_session.week_key)
    db_session.week_start = metadata.get("week_start", db_session.week_start)
    db_session.is_featured_weekly = metadata.get("is_featured_weekly", db_session.is_featured_weekly or False)
    db_session.title = metadata.get("title", db_session.title or _session_title(session_state.prompt))
    db_session.theme = metadata.get("theme", db_session.theme)
    
    # Serialize complex objects
    if session_state.transcript:
        db_session.transcript = [msg.model_dump(mode="json") for msg in session_state.transcript]
    
    if session_state.summary:
        db_session.summary = session_state.summary.model_dump(mode="json")
    
    if session_state.wiki_proposals:
        db_session.wiki_proposals = [prop.model_dump(mode="json") for prop in session_state.wiki_proposals]

    if session_state.incident:
        db_session.incident = session_state.incident.model_dump(mode="json")

    if session_state.status == "completed" and not db_session.completed_at:
        db_session.completed_at = datetime.utcnow()
    
    db.add(db_session)
    db.commit()


def load_session_from_db(session_id: str, db: DBSession) -> Optional[SessionState]:
    """Load a session from the database."""
    db_session = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    
    if not db_session:
        return None
    
    # Reconstruct SessionState
    state = SessionState(
        session_id=db_session.id,
        created_at=db_session.created_at,
        mode=db_session.mode,
        actors=db_session.actors,
        prompt=db_session.prompt,
        status=db_session.status,
        turn_index=db_session.turn_index or 0,
        next_actor_index=db_session.next_actor_index or 0,
        loaded_pages=db_session.loaded_pages or {},
        context_notes=db_session.context_notes or {},
    )
    
    # Deserialize complex objects
    if db_session.transcript:
        state.transcript = [TranscriptMessage(**msg) for msg in db_session.transcript]
    
    if db_session.summary:
        # Import here to avoid circular import
        from .models import MemoOption
        summary_data = db_session.summary.copy()
        if "strategic_options" in summary_data:
            summary_data["strategic_options"] = [
                MemoOption(**opt) for opt in summary_data["strategic_options"]
            ]
        state.summary = SessionSummary(**summary_data)
    
    if db_session.wiki_proposals:
        state.wiki_proposals = [WikiProposal(**prop) for prop in db_session.wiki_proposals]

    if db_session.incident:
        state.incident = IncidentBrief(**db_session.incident)

    return state


def get_james_take(session_id: str, db: DBSession) -> Optional[str]:
    """Return a previously-saved James take for this session, if any."""
    row = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    return row.james_take if row else None


def save_james_take(session_id: str, take: str, db: DBSession) -> bool:
    """Persist James's take onto an existing session row so it survives restarts
    and shows up in replay. Returns False if the session has no DB row yet
    (e.g. a brand-new in-memory-only session) — the take is still returned to
    the caller, it just won't be saved until the session itself is persisted."""
    row = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    if not row:
        return False
    row.james_take = take
    db.add(row)
    db.commit()
    return True


def get_mirror_card(session_id: str, db: DBSession) -> Optional[dict]:
    """Return a previously-saved mirror-card for this session, if any."""
    row = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    return row.mirror_card if row else None


def save_mirror_card(session_id: str, card: dict, db: DBSession) -> bool:
    """Persist the mirror-card onto an existing session row, same pattern as
    save_james_take. Returns False if the session has no DB row yet."""
    row = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    if not row:
        return False
    row.mirror_card = card
    db.add(row)
    db.commit()
    return True


def get_james_takes_feed(db: DBSession, limit: int = 50) -> list[dict]:
    """Every session with a saved James take, newest first — browsable as its own feed,
    independent of any specific session replay."""
    rows = (
        db.query(SessionDB)
        .filter(SessionDB.james_take.isnot(None))
        .order_by(SessionDB.created_at.desc())
        .limit(limit)
        .all()
    )
    return [
        {
            "session_id": r.id,
            "title": r.title or _session_title(r.prompt),
            "mode": r.mode,
            "created_at": r.created_at.isoformat(),
            "james_take": r.james_take,
        }
        for r in rows
    ]


def get_recap(session_id: str, db: DBSession) -> Optional[dict]:
    """Return a previously-saved recap/scoreboard for this session, if any."""
    row = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    return row.recap if row else None


def save_recap(session_id: str, recap: dict, db: DBSession) -> bool:
    """Persist the recap onto an existing session row, same pattern as save_james_take
    and save_mirror_card. Returns False if the session has no DB row yet."""
    row = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    if not row:
        return False
    row.recap = recap
    db.add(row)
    db.commit()
    return True


def _session_export_row(r: SessionDB) -> dict:
    return {
        "session_id": r.id,
        "created_at": r.created_at.isoformat(),
        "completed_at": r.completed_at.isoformat() if r.completed_at else None,
        "mode": r.mode,
        "actors": r.actors,
        "prompt": public_prompt(r.prompt),
        "status": r.status,
        "title": r.title,
        "theme": r.theme,
        "session_type": r.session_type,
        "week_key": r.week_key,
        "transcript": r.transcript,
        "summary": r.summary,
        "wiki_proposals": r.wiki_proposals,
        "recap": r.recap,
        "james_take": r.james_take,
        "mirror_card": r.mirror_card,
        "incident": r.incident,
    }


def get_all_sessions_export(db: DBSession) -> list[dict]:
    """Full data for every session — transcript, summary, recap, james_take, mirror_card,
    incident, everything. For archiving/backup, not for the live UI (use the lighter preview
    endpoints for that)."""
    rows = db.query(SessionDB).order_by(SessionDB.created_at).all()
    return [_session_export_row(r) for r in rows]


def get_session_export(session_id: str, db: DBSession) -> Optional[dict]:
    """Same shape as one entry of get_all_sessions_export, for a single session — so a
    per-session export file is structurally identical to an entry in the bulk one."""
    row = db.query(SessionDB).filter(SessionDB.id == session_id).first()
    return _session_export_row(row) if row else None


def get_recent_sessions(db: DBSession, limit: int = 10) -> list[dict]:
    """Get recent sessions for display."""
    sessions = db.query(SessionDB).order_by(SessionDB.created_at.desc()).limit(limit).all()
    return [_session_preview(s) for s in sessions]


def clear_featured_weekly(db: DBSession) -> None:
    """Ensure only one weekly session is featured at a time."""
    db.query(SessionDB).filter(SessionDB.is_featured_weekly.is_(True)).update(
        {SessionDB.is_featured_weekly: False},
        synchronize_session=False,
    )
    db.commit()


def get_featured_weekly_session(db: DBSession) -> Optional[dict]:
    """Return the currently featured weekly session."""
    session = (
        db.query(SessionDB)
        .filter(SessionDB.session_type == "weekly")
        .filter(SessionDB.status == "completed")
        .filter(SessionDB.is_featured_weekly.is_(True))
        .order_by(SessionDB.created_at.desc())
        .first()
    )
    if not session:
        return None
    return _session_preview(session)


def get_weekly_archive(db: DBSession, limit: int = 12, offset: int = 0) -> dict:
    """Return weekly sessions for archive display."""
    query = (
        db.query(SessionDB)
        .filter(SessionDB.session_type == "weekly")
        .filter(SessionDB.status == "completed")
        .order_by(SessionDB.week_start.desc().nullslast(), SessionDB.created_at.desc())
    )
    total = query.count()
    items = query.offset(offset).limit(limit).all()
    return {
        "items": [_session_preview(item) for item in items],
        "total": total,
        "limit": limit,
        "offset": offset,
    }


def get_weekly_session_by_week_key(week_key: str, db: DBSession) -> Optional[dict]:
    """Return a weekly session preview by ISO week key."""
    session = (
        db.query(SessionDB)
        .filter(SessionDB.session_type == "weekly")
        .filter(SessionDB.status == "completed")
        .filter(SessionDB.week_key == week_key)
        .order_by(SessionDB.created_at.desc())
        .first()
    )
    if not session:
        return None
    return _session_preview(session)


def get_session_count(db: DBSession) -> int:
    """Get total session count."""
    return db.query(SessionDB).count()


def get_last_session_time(db: DBSession) -> Optional[datetime]:
    """Get the timestamp of the last session."""
    last_session = db.query(SessionDB).order_by(SessionDB.created_at.desc()).first()
    return last_session.created_at if last_session else None
