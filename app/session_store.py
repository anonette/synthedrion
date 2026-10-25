from __future__ import annotations

import threading
import time
from typing import Dict

from .models import SessionState

# Live working copies of sessions. Every mutation is also persisted to the database,
# and an evicted session is resurrected from it on next touch (main._live_session),
# so this cache only needs recently active sessions. Unbounded growth here is what
# used to balloon the process to 1.6 GB and OOM the 2 GB production box.
SESSIONS: Dict[str, SessionState] = {}

_LAST_TOUCHED: Dict[str, float] = {}
_PRUNE_GUARD = threading.Lock()

SESSION_IDLE_TTL_SECONDS = 2 * 60 * 60  # evict sessions idle longer than this
MAX_LIVE_SESSIONS = 32  # hard cap; longest-idle evicted first


def touch_session(session_id: str) -> None:
    """Mark a session as recently used so pruning spares it."""
    _LAST_TOUCHED[session_id] = time.monotonic()


def prune_sessions() -> list[str]:
    """Evict idle and over-cap sessions from memory; returns the evicted ids.

    Safe to call from any request path: only sessions idle past the TTL (or the
    longest-idle ones over the cap) are dropped, and every mutation persists to
    the DB first, so nothing is lost — the session just 404-proofs itself back
    in via _live_session on its next use.
    """
    now = time.monotonic()
    with _PRUNE_GUARD:
        for sid in SESSIONS:
            _LAST_TOUCHED.setdefault(sid, now)
        evicted = {
            sid
            for sid, ts in _LAST_TOUCHED.items()
            if sid in SESSIONS and now - ts > SESSION_IDLE_TTL_SECONDS
        }
        overflow = len(SESSIONS) - len(evicted) - MAX_LIVE_SESSIONS
        if overflow > 0:
            survivors = sorted(
                (sid for sid in SESSIONS if sid not in evicted),
                key=lambda s: _LAST_TOUCHED.get(s, now),
            )
            evicted.update(survivors[:overflow])
        for sid in evicted:
            SESSIONS.pop(sid, None)
            _LAST_TOUCHED.pop(sid, None)
        # drop touch stamps for sessions no longer in memory (e.g. cleared elsewhere)
        for sid in [s for s in _LAST_TOUCHED if s not in SESSIONS]:
            _LAST_TOUCHED.pop(sid, None)
        return sorted(evicted)
