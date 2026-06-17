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


_NOTE_STOPWORDS = {
    "this", "that", "with", "from", "into", "their", "they", "page", "agent", "actor",
    "should", "which", "while", "because", "these", "those", "there", "than", "then",
    "also", "such", "more", "most", "when", "what", "over", "about", "would", "could",
    "have", "this", "your", "will", "both", "each", "other", "shared", "policy",
}


def _note_tokens(text: str) -> set[str]:
    return {t for t in re.findall(r"[a-z]{4,}", (text or "").lower()) if t not in _NOTE_STOPWORDS}


def assemble_context_notes(pages: list[Path], prompt: str, total: int = 60) -> list[str]:
    """Build the per-actor grounding notes for a session.

    Two goals at once:
    - relevance: notes are scored by keyword overlap with the session prompt, so a
      debate about rare earths surfaces the minerals pages and a debate about compute
      surfaces the chip pages.
    - breadth: round-robin across every loaded page (best note from each page first,
      then the second-best, ...) so no single early page can monopolize the budget and
      every page — including newly linked ones — contributes.

    The final list is sorted most-relevant-first, so downstream slices take the notes
    that matter for the question being debated.
    """
    query = _note_tokens(prompt)

    def score(note: str) -> int:
        return len(_note_tokens(note) & query)

    per_page: list[list[str]] = []
    for page in pages:
        notes = extract_notes(page)
        notes.sort(key=score, reverse=True)  # best note within the page leads
        per_page.append(notes)

    selected: list[str] = []
    rank = 0
    while len(selected) < total and any(rank < len(notes) for notes in per_page):
        for notes in per_page:
            if rank < len(notes):
                selected.append(notes[rank])
                if len(selected) >= total:
                    break
        rank += 1

    selected.sort(key=score, reverse=True)  # most prompt-relevant first (stable keeps breadth order on ties)
    return selected[:total]
