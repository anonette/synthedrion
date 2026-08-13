"""Audio generation for session replay."""

import asyncio
import os
import subprocess
import tempfile
from typing import Optional
import httpx
from pathlib import Path
from urllib.parse import quote

# Voice configurations
ACTOR_VOICES = {
    "china": {
        "openai": {"voice": "sage", "instructions": "Speak with calm strategic gravity, disciplined pacing, and a state-planning register."},
        "elevenlabs": {"voice_id": "EXAVITQu4vr4xnSDxMaL", "stability": 0.5, "similarity_boost": 0.75},
        "edge-tts": {"voice": "zh-CN-XiaoxiaoNeural", "rate": "-5%"},
    },
    "us": {
        "openai": {"voice": "onyx", "instructions": "Speak with confident prosecutorial force and sharp strategic emphasis."},
        "elevenlabs": {"voice_id": "21m00Tcm4TlvDq8ikWAM", "stability": 0.6, "similarity_boost": 0.8},
        "edge-tts": {"voice": "en-US-JennyNeural", "rate": "+0%"},
    },
    "eu": {
        "openai": {"voice": "coral", "instructions": "Speak with precise institutional authority, dry wit, and measured legitimacy."},
        "elevenlabs": {"voice_id": "ErXwobaYiN019PkySvjV", "stability": 0.55, "similarity_boost": 0.75},
        "edge-tts": {"voice": "en-GB-RyanNeural", "rate": "-3%"},
    },
    "halcyon": {  # earnest peace-builder — warm, hopeful (serious register, not the satire caricature)
        "openai": {"voice": "shimmer", "instructions": "Speak as a warm, earnest, quietly hopeful peacemaker addressing rivals with disarming sincerity."},
        "elevenlabs": {"voice_id": "EXAVITQu4vr4xnSDxMaL", "stability": 0.6, "similarity_boost": 0.7},
        "edge-tts": {"voice": "en-US-AriaNeural", "rate": "+2%"},
    },
    "james": {  # the crypto-native analyst — fast, dry, faintly contemptuous
        "openai": {"voice": "onyx", "instructions": "Speak as a fast-talking, dry, faintly contemptuous market analyst who has seen every rug pull coming."},
        "elevenlabs": {"voice_id": "TxGEqnHWrfWFTfGW9XjX", "stability": 0.55, "similarity_boost": 0.75},
        "edge-tts": {"voice": "en-AU-WilliamNeural", "rate": "+8%"},
    },
    "archivist": {  # The Critical Archivist — precise, dry, faintly amused
        "openai": {"voice": "sage", "instructions": "Speak with dry, precise, librarian-like authority and a faint undertone of amusement, as someone calmly rearranging the shelves under everyone's argument."},
        "elevenlabs": {"voice_id": "onwK4e9ZLuTAKqWW03F9", "stability": 0.7, "similarity_boost": 0.7},
        "edge-tts": {"voice": "en-GB-SoniaNeural", "rate": "-4%"},
    },
    "human": {
        "openai": {"voice": "nova", "instructions": "Speak naturally and clearly."},
        "elevenlabs": {"voice_id": "pNInz6obpgDQGcFmaJgB", "stability": 0.7, "similarity_boost": 0.7},
        "edge-tts": {"voice": "en-US-GuyNeural", "rate": "+5%"},
    },
    "system": {
        "openai": {"voice": "shimmer", "instructions": "Speak as a neutral system announcer with crisp clarity."},
        "elevenlabs": {"voice_id": "flq6f7yk4E4fJM5XTYuZ", "stability": 0.8, "similarity_boost": 0.9},
        "edge-tts": {"voice": "en-US-AriaNeural", "rate": "+10%"},
    },
}

OPENAI_AUDIO_MODEL = os.getenv("OPENAI_TTS_MODEL", "gpt-4o-mini-tts")

# Voices for the brutal-satire talking heads — deliberately caricatured (gender +
# accent + comedic tone). Kept SEPARATE from ACTOR_VOICES so the serious replay
# narration is unaffected. Trick for accents on free edge-tts: a locale voice
# (zh-CN / de-DE) reading English speaks it with that native accent.
SATIRE_VOICES = {
    "china": {  # Xi — a man, heavy Chinese accent
        "openai": {"voice": "ash", "instructions": "Speak as a stern authoritarian man with a HEAVY Chinese accent, calm cold menace, slow and deliberate."},
        "edge-tts": {"voice": "zh-CN-YunjianNeural", "rate": "-8%", "pitch": "-12Hz"},
    },
    "us": {  # Trump — whiny high-pitched man-baby, cranked to aggressive/manic (comedy + rage)
        "openai": {"voice": "onyx", "instructions": "Speak as an AGGRESSIVE, MEAN, whiny American man-baby strongman: shrill, petulant, snarling and hostile, ranting at high pitch — a furious over-the-top comic caricature."},
        "edge-tts": {"voice": "en-US-GuyNeural", "rate": "+4%", "pitch": "+42Hz", "volume": "+55%"},
    },
    "eu": {  # Ursula von der Leyen — a woman, German accent, funny
        "openai": {"voice": "coral", "instructions": "Speak as a prim European bureaucrat WOMAN with a German accent, over-formal and unintentionally comic, faintly exasperated."},
        "edge-tts": {"voice": "de-DE-KatjaNeural", "rate": "+0%", "pitch": "+8Hz"},
    },
    "halcyon": {  # earnest peace-bird — warm, hopeful
        "openai": {"voice": "shimmer", "instructions": "Speak as a warm, relentlessly hopeful peacemaker — gentle and earnest."},
        "edge-tts": {"voice": "en-US-AriaNeural", "rate": "+3%", "pitch": "+0Hz"},
    },
}


async def generate_satire_audio(text: str, actor: str, provider: str | None = None) -> bytes:
    """TTS for the satire talking heads using the caricatured SATIRE_VOICES map.
    `provider` = "edge" (free, default) | "openai" (paid)."""
    tts_service = (provider or "edge").lower()
    cfg = SATIRE_VOICES.get(actor) or SATIRE_VOICES["us"]
    if tts_service == "openai" and os.getenv("OPENAI_API_KEY"):
        return await generate_tts_openai(text, cfg["openai"])
    return await generate_tts_edge(text, cfg["edge-tts"])


async def generate_tts_elevenlabs(text: str, voice_config: dict) -> bytes:
    """Generate TTS using ElevenLabs API."""
    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise ValueError("ELEVENLABS_API_KEY not set")
    
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_config['voice_id']}"
    
    headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": api_key,
    }
    
    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": voice_config.get("stability", 0.5),
            "similarity_boost": voice_config.get("similarity_boost", 0.75),
        }
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.content


async def generate_tts_openai(text: str, voice_config: dict) -> bytes:
    """Generate TTS using OpenAI speech API."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not set")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "model": OPENAI_AUDIO_MODEL,
        "voice": voice_config.get("voice", "alloy"),
        "input": text,
        "format": "mp3",
        "instructions": voice_config.get("instructions", "Speak clearly and naturally."),
    }

    async with httpx.AsyncClient(timeout=90.0) as client:
        response = await client.post("https://api.openai.com/v1/audio/speech", json=data, headers=headers)
        response.raise_for_status()
        return response.content


async def generate_tts_edge(text: str, voice_config: dict) -> bytes:
    """Generate TTS using Edge TTS (free Microsoft neural voices, no API key).

    Streams the mp3 into memory — avoids a temp file (the old `/tmp/...` path did
    not exist on Windows and always failed there)."""
    try:
        import edge_tts
    except ImportError:
        raise ImportError("edge-tts not installed. Run: pip install edge-tts")

    voice = voice_config.get("voice", "en-US-JennyNeural")
    rate = voice_config.get("rate", "+0%")
    pitch = voice_config.get("pitch", "+0Hz")
    volume = voice_config.get("volume", "+0%")

    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch, volume=volume)
    audio = bytearray()

    async def _collect():
        async for chunk in communicate.stream():
            if chunk.get("type") == "audio" and chunk.get("data"):
                audio.extend(chunk["data"])

    # Cap synthesis so a stalled Microsoft edge-tts connection can't hang the request forever.
    await asyncio.wait_for(_collect(), timeout=20)
    if not audio:
        raise RuntimeError("edge-tts produced no audio")
    return bytes(audio)


async def generate_actor_audio(text: str, actor: str, provider: str | None = None) -> bytes:
    """Generate audio for a specific actor. `provider` ("openai" | "elevenlabs" |
    "edge") overrides the TTS_SERVICE env var for a single call — the satire voice
    switch uses this so the caller picks free (edge) vs paid (openai) per request."""
    tts_service = (provider or os.getenv("TTS_SERVICE", "openai")).lower()

    voice_config = ACTOR_VOICES.get(actor, ACTOR_VOICES["human"])

    if tts_service == "openai" and os.getenv("OPENAI_API_KEY"):
        return await generate_tts_openai(text, voice_config["openai"])
    if tts_service == "elevenlabs" and os.getenv("ELEVENLABS_API_KEY"):
        return await generate_tts_elevenlabs(text, voice_config["elevenlabs"])
    # Default / explicit: free edge-tts
    return await generate_tts_edge(text, voice_config["edge-tts"])


def combine_audio_segments(segments: list[bytes], pause_ms: int = 1000) -> bytes:
    """Combine multiple MP3 segments into one MP3 using ffmpeg."""
    if not segments:
        return b""

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_root = Path(temp_dir)
        list_file = temp_root / "inputs.txt"
        output_file = temp_root / "combined.mp3"
        segment_paths: list[Path] = []

        for idx, segment_data in enumerate(segments):
            segment_path = temp_root / f"segment-{idx:03d}.mp3"
            segment_path.write_bytes(segment_data)
            segment_paths.append(segment_path)

        list_file.write_text(
            "\n".join(f"file '{path.as_posix()}'" for path in segment_paths),
            encoding="utf-8",
        )

        command = [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(list_file),
            "-c",
            "copy",
            str(output_file),
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0 or not output_file.exists():
            raise RuntimeError(f"ffmpeg concat failed: {result.stderr.strip() or result.stdout.strip()}")

        return output_file.read_bytes()


async def generate_session_audio(session_id: str, transcript: list[dict]) -> Optional[str]:
    """Generate full audio for a session."""
    if not transcript:
        return None
    
    try:
        audio_segments = []
        
        for msg in transcript:
            if msg["kind"] == "agent" or msg["kind"] == "human":
                audio = await generate_actor_audio(
                    text=msg.get("narration_text") or msg["content"],
                    actor=msg["actor"]
                )
                audio_segments.append(audio)
        
        if not audio_segments:
            return None
        
        # Combine all segments
        combined_audio = combine_audio_segments(audio_segments)
        
        # Save to file (in production, upload to S3/CloudStorage instead)
        audio_dir = Path("sessions") / session_id
        audio_dir.mkdir(parents=True, exist_ok=True)
        audio_path = audio_dir / "audio.mp3"
        
        with open(audio_path, "wb") as f:
            f.write(combined_audio)
        
        # Return URL path (in production, return cloud storage URL)
        return f"/sessions/{session_id}/audio.mp3"
        
    except Exception as e:
        print(f"Audio generation failed: {e}")
        return None


def _audio_dir(session_id: str) -> Path:
    return Path("sessions") / session_id / "audio"


def _event_audio_file(session_id: str, index: int) -> Path:
    return _audio_dir(session_id) / f"event-{index:03d}.mp3"


def _full_audio_file(session_id: str) -> Path:
    return _audio_dir(session_id) / "replay-full.mp3"


def check_replay_audio_status(session_id: str, events: list[dict]) -> dict:
    """Cheap, generation-free cache check — file-existence only, no TTS calls. Used by the
    main /api/replay response so it stays fast (that endpoint used to block on generating
    audio for every uncached turn, which could take 20-60+ seconds and cause client-side
    timeouts/aborts). Actual generation happens lazily via the separate audio endpoint,
    only when a caller explicitly asks for it (e.g. the user presses Play)."""
    event_entries: list[dict] = []
    for event in events:
        if event.get("kind") not in {"agent", "human"}:
            event_entries.append({"index": event.get("index"), "audio_url": None, "cached": True})
            continue
        index = int(event["index"])
        audio_file = _event_audio_file(session_id, index)
        cached = audio_file.exists()
        event_entries.append({
            "index": index,
            "audio_url": f"/session-assets/{quote(session_id)}/audio/{audio_file.name}" if cached else None,
            "cached": cached,
        })
    full_audio_file = _full_audio_file(session_id)
    full_cached = full_audio_file.exists()
    return {
        "full_audio_url": f"/session-assets/{quote(session_id)}/audio/{full_audio_file.name}" if full_cached else None,
        "full_audio_cached": full_cached,
        "event_audio": event_entries,
        "fully_cached": full_cached and all(e["cached"] for e in event_entries),
    }


async def ensure_replay_audio_assets(session_id: str, events: list[dict]) -> dict:
    """Generate and cache per-event and full replay audio."""
    if not events:
        return {"full_audio_url": None, "event_audio": []}

    audio_dir = _audio_dir(session_id)
    audio_dir.mkdir(parents=True, exist_ok=True)
    event_entries: list[dict] = []
    segments: list[bytes] = []

    for event in events:
        if event.get("kind") not in {"agent", "human"}:
            event_entries.append({
                "index": event.get("index"),
                "audio_url": None,
                "cached": True,
            })
            continue

        index = int(event["index"])
        audio_file = _event_audio_file(session_id, index)
        cached = audio_file.exists()
        if not cached:
            text = event.get("narration_text") or event.get("content", "")
            actor = event.get("actor", "human")
            audio_bytes = await generate_actor_audio(text=text, actor=actor)
            audio_file.write_bytes(audio_bytes)
        segment_bytes = audio_file.read_bytes()
        segments.append(segment_bytes)
        event_entries.append({
            "index": index,
            "audio_url": f"/session-assets/{quote(session_id)}/audio/{audio_file.name}",
            "cached": cached,
        })

    full_audio_file = _full_audio_file(session_id)
    full_cached = full_audio_file.exists()
    full_audio_error = None
    full_audio_mode = None
    if segments and not full_cached:
        try:
            combined = combine_audio_segments(segments)
            full_audio_file.write_bytes(combined)
            full_audio_mode = "concatenated-events"
        except Exception as exc:
            try:
                combined_text = " ".join(
                    event.get("narration_text") or event.get("content", "")
                    for event in events
                    if event.get("kind") in {"agent", "human"}
                ).strip()
                if not combined_text:
                    raise RuntimeError("No eligible replay narration text")
                full_bytes = await generate_actor_audio(text=combined_text, actor="system")
                full_audio_file.write_bytes(full_bytes)
                full_audio_mode = "single-voice-fallback"
                full_audio_error = str(exc)
            except Exception as fallback_exc:
                full_audio_error = f"{exc}; fallback failed: {fallback_exc}"
    elif not full_cached:
        full_audio_error = "No eligible replay audio segments"
    else:
        full_audio_mode = "cached"

    return {
        "full_audio_url": f"/session-assets/{quote(session_id)}/audio/{_full_audio_file(session_id).name}" if full_audio_file.exists() else None,
        "full_audio_cached": full_cached,
        "full_audio_error": full_audio_error,
        "full_audio_mode": full_audio_mode,
        "event_audio": event_entries,
    }
