"""Speech-to-text for the live dialogue mode.

Provider-agnostic: any OpenAI-compatible /audio/transcriptions endpoint works.
Defaults to OpenAI's hosted Whisper using the existing OPENAI_API_KEY, so the
hall microphone works with zero new secrets. To use a different service (e.g. a
Super Whisper / hosted whisper deployment), set:

    STT_BASE_URL   (default https://api.openai.com/v1)
    STT_API_KEY    (default: falls back to OPENAI_API_KEY)
    STT_MODEL      (default whisper-1)
"""

from __future__ import annotations

import os

import httpx

STT_BASE_URL = os.getenv("STT_BASE_URL", "https://api.openai.com/v1").rstrip("/")
STT_MODEL = os.getenv("STT_MODEL", "whisper-1")


def _api_key() -> str:
    return os.getenv("STT_API_KEY", "") or os.getenv("OPENAI_API_KEY", "")


def stt_enabled() -> bool:
    return bool(_api_key())


def transcribe_audio(data: bytes, filename: str = "speech.webm", content_type: str = "audio/webm", language: str | None = None) -> str:
    """Send one recorded utterance to the transcription API and return its text.
    Raises on failure — the caller surfaces a real error, never a fabricated quote."""
    if not data:
        raise ValueError("empty audio")
    if not stt_enabled():
        raise RuntimeError("no STT credentials: set STT_API_KEY (or OPENAI_API_KEY)")
    form: dict = {"model": (None, STT_MODEL)}
    if language:
        form["language"] = (None, language)
    files = {"file": (filename, data, content_type or "application/octet-stream"), **form}
    headers = {"Authorization": f"Bearer {_api_key()}"}
    with httpx.Client(timeout=60.0) as client:
        res = client.post(f"{STT_BASE_URL}/audio/transcriptions", headers=headers, files=files)
        res.raise_for_status()
        payload = res.json()
    text = (payload.get("text") or "").strip()
    if not text:
        raise RuntimeError("transcription returned no text")
    return text
