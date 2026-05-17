from __future__ import annotations

import re
from pathlib import Path
import re

from .config import ACTOR_HUBS, ALLOWED_PATH_PREFIXES, SHARED_HUB, WIKI_ROOT


LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+")


def _read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def _resolve_link(base_path: Path, raw_link: str) -> Path | None:
    candidate = (base_path.parent / raw_link).resolve()
    if not candidate.exists() or not candidate.is_file():
        return None
    return candidate


def _is_allowed(actor: str, path: Path) -> bool:
    allowed_prefixes = ALLOWED_PATH_PREFIXES[actor]
    return any(path.is_relative_to(prefix) for prefix in allowed_prefixes)


def collect_actor_pages(actor: str, include_shared: bool = True) -> list[Path]:
    hub = ACTOR_HUBS[actor].resolve()
    stack = [hub]
    if include_shared:
        stack.append(SHARED_HUB.resolve())

    seen: set[Path] = set()
    ordered: list[Path] = []

    while stack:
        path = stack.pop(0)
        if path in seen or not path.exists():
            continue
        if path != SHARED_HUB.resolve() and not _is_allowed(actor, path):
            continue
        seen.add(path)
        ordered.append(path)

        text = _read_text(path)
        for raw_link in LINK_PATTERN.findall(text):
            resolved = _resolve_link(path, raw_link)
            if not resolved:
                continue
            if resolved == SHARED_HUB.resolve() or _is_allowed(actor, resolved):
                stack.append(resolved)

    return ordered


def extract_notes(path: Path) -> list[str]:
    text = _read_text(path)
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    notes: list[str] = []

    heading = path.stem.replace("-", " ")
    for line in lines:
        if line.startswith("#") or line.startswith(">"):
            continue
        if line.startswith("Raw:") or line.startswith("Sources:") or line.startswith("Updated:"):
            continue
        if line.startswith("`") and line.endswith("`"):
            continue
        if line.count("/") >= 2 and len(line) < 140:
            continue
        if line.startswith("-"):
            candidate = line.lstrip("- ")
            if candidate.startswith("[") and "](" in candidate:
                continue
            if len(candidate) > 35:
                notes.append(f"[{heading}] {candidate}")
        elif len(line) > 60:
            if line.startswith("[") and "](" in line:
                continue
            if not HEADING_PATTERN.match(line):
                notes.append(f"[{heading}] {line}")
        if len(notes) >= 12:
            break

    return notes


def relative_wiki_path(path: Path) -> str:
    return str(path.relative_to(WIKI_ROOT.parent)).replace("\\", "/")
