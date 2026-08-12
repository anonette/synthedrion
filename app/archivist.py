from __future__ import annotations

"""The Critical Archivist — a summonable meta-agent whose object of intervention is
the archive itself: the wiki corpus, transcripts, and retrieval conventions that
condition what the other agents can know and say.

Two honesty rules shape this module:
- Reorganizations are REAL. Every archival logic below is computed over the actual
  wiki corpus (folders, bytes, link graph, lexicon counts), so when the Archivist
  says "under this order, page X rises and page Y disappears", that is a fact about
  the files on disk, not a hallucinated flourish.
- Opaque logics are labeled. Logics marked experimental=True are surfaced to the
  model with an explicit instruction to present them as experimental or
  computational artifacts, never as revealed truth.
"""

import hashlib
import re
from pathlib import Path
from typing import Any

import httpx

from .config import (
    ARCHIVIST_HUB_DIR,
    ARCHIVIST_MODEL,
    OPENROUTER_API_KEY,
    OPENROUTER_APP_NAME,
    OPENROUTER_BASE_URL,
    OPENROUTER_SITE_URL,
    WIKI_ROOT,
)
from .llm import NO_LLM_TELLS_STYLE
from .wiki_loader import assemble_context_notes


LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+\.md)\)")
YEAR_PATTERN = re.compile(r"\b(19\d{2}|20\d{2})\b")

THREAT_LEXICON = (
    "threat", "risk", "weapon", "attack", "sanction", "blockade", "chokepoint",
    "choke point", "decouple", "decoupling", "dual-use", "escalat", "adversar",
    "hostile", "coerc", "contain", "espionage", "sabotage", "red line",
)
INEVITABILITY_LEXICON = (
    "inevitab", "irreversib", "race", "must ", "window", "existential", "destiny",
    "unstoppable", "falling behind", "leapfrog", "dominan", "supremacy",
)


def _folder_of(path: Path) -> str:
    try:
        rel = path.relative_to(WIKI_ROOT)
    except ValueError:
        return "outside-wiki"
    return rel.parts[0] if len(rel.parts) > 1 else "(wiki root)"


def catalog_corpus() -> list[dict[str, Any]]:
    """A census of the whole wiki archive: one record per page, with the measurable
    facts (size, folder, link degree, lexicon densities) the archival logics sort by.
    This deliberately spans ALL folders, including pages no actor can reach, because
    unreachability is exactly the kind of silence the Archivist exists to surface."""
    records: list[dict[str, Any]] = []
    by_name: dict[str, dict[str, Any]] = {}
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        lower = text.lower()
        words = len(text.split())
        title = path.stem.replace("-", " ")
        for line in text.splitlines():
            if line.startswith("# "):
                title = line.lstrip("# ").strip()
                break
        years = [int(y) for y in YEAR_PATTERN.findall(text)]
        rec: dict[str, Any] = {
            "path": str(path.relative_to(WIKI_ROOT)).replace("\\", "/"),
            "name": path.name,
            "folder": _folder_of(path),
            "title": title[:90],
            "bytes": len(text.encode("utf-8")),
            "words": words,
            "links_out": len(LINK_PATTERN.findall(text)),
            "links_in": 0,  # filled below from the link graph
            "questions_per_kword": round(1000 * text.count("?") / max(words, 1), 1),
            "threat_hits": sum(lower.count(t) for t in THREAT_LEXICON),
            "inevitability_hits": sum(lower.count(t) for t in INEVITABILITY_LEXICON),
            "latest_year": max(years) if years else None,
        }
        records.append(rec)
        by_name[path.name] = rec
    # inbound link degree: how reachable each page is inside the archive
    for path in sorted(WIKI_ROOT.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        for raw_link in LINK_PATTERN.findall(text):
            target = by_name.get(Path(raw_link).name)
            if target is not None and target["name"] != path.name:
                target["links_in"] += 1
    return records


def _density(rec: dict[str, Any], field: str) -> float:
    return 1000 * rec[field] / max(rec["words"], 1)


# Each logic: how to order the census, whether the order is experimental/opaque,
# and what the ordering measurably does. `sort` maps a record to a sort key
# (descending = foregrounded). Grouped logics use `group` instead.
ARCHIVAL_LOGICS: list[dict[str, Any]] = [
    {
        "key": "chronology",
        "label": "Chronology of the latest year each page can name",
        "experimental": False,
        "sort": lambda r: (r["latest_year"] or 0),
        "note": "Pages naming recent years rise; undated pages, often the structural and conceptual ones, sink into an artificial past.",
    },
    {
        "key": "geography",
        "label": "Geography of folders, the archive's border regime",
        "experimental": False,
        "group": "folder",
        "note": "The folder tree is the treaty. Each actor's allowed prefixes decide which of these blocks exists for it at all.",
    },
    {
        "key": "citation-gravity",
        "label": "Citation gravity, ranked by inbound links",
        "experimental": False,
        "sort": lambda r: r["links_in"],
        "note": "Pages other pages point at become 'important'. Attention compounds into relevance. The unlinked are unreachable by any hub crawl.",
    },
    {
        "key": "threat-vocabulary",
        "label": "Density of the vocabulary of threat",
        "experimental": False,
        "sort": lambda r: _density(r, "threat_hits"),
        "note": "Sorting by fear-language shows which pages arm the debate and which pages the debate never arms itself with.",
    },
    {
        "key": "inevitability",
        "label": "Density of the vocabulary of inevitability",
        "experimental": False,
        "sort": lambda r: _density(r, "inevitability_hits"),
        "note": "Destiny-talk clusters. These are the pages that make certain futures feel already decided.",
    },
    {
        "key": "mass",
        "label": "Sheer mass in bytes",
        "experimental": True,
        "sort": lambda r: r["bytes"],
        "note": "An absurdist but honest order. Much of what an archive 'knows' is verbosity and format, not significance.",
    },
    {
        "key": "brevity",
        "label": "Brevity first, the shortest pages foregrounded",
        "experimental": True,
        "sort": lambda r: -r["words"],
        "note": "Inverts the mass order. The marginal notes and stubs speak first; the flagship documents wait their turn.",
    },
    {
        "key": "interrogative",
        "label": "Question-mark density, the interrogative archive",
        "experimental": True,
        "sort": lambda r: r["questions_per_kword"],
        "note": "Pages that ask rise above pages that assert. Bureaucratic genres, which rarely ask, drop to the bottom.",
    },
    {
        "key": "absence",
        "label": "Absence, the least-linked and least-reachable pages first",
        "experimental": False,
        "sort": lambda r: -(r["links_in"] * 10 + r["links_out"]),
        "note": "An index of silence. These pages exist on disk but barely exist in the archive's own map of itself.",
    },
    {
        "key": "shuffle",
        "label": "Deterministic shuffle, the control condition",
        "experimental": True,
        "sort": None,  # handled with a salted hash in reorganize()
        "note": "If an argument survives a shuffled archive, the arrangement was not doing the arguing. If it collapses, it was.",
    },
]

LOGIC_BY_KEY = {logic["key"]: logic for logic in ARCHIVAL_LOGICS}


def pick_logic(used: int, requested: str | None = None) -> dict[str, Any]:
    """Rotate through the repertoire by how often the Archivist has already spoken in
    this session, unless the operator requests a specific logic by key."""
    if requested and requested in LOGIC_BY_KEY:
        return LOGIC_BY_KEY[requested]
    return ARCHIVAL_LOGICS[used % len(ARCHIVAL_LOGICS)]


def reorganize(records: list[dict[str, Any]], logic: dict[str, Any], salt: str = "") -> dict[str, Any]:
    """Apply one archival logic to the census and report what it measurably
    foregrounds and suppresses. Returns real page titles and folders only."""
    if logic.get("group"):
        field = logic["group"]
        groups: dict[str, list[dict[str, Any]]] = {}
        for rec in records:
            groups.setdefault(rec[field], []).append(rec)
        ordered_groups = sorted(groups.items(), key=lambda kv: -len(kv[1]))
        foreground = [
            f"{name}: {len(items)} pages, {sum(r['bytes'] for r in items):,} bytes"
            for name, items in ordered_groups[:6]
        ]
        suppressed = [
            f"{name}: only {len(items)} page(s)" for name, items in ordered_groups[-3:]
        ] if len(ordered_groups) > 6 else []
    else:
        if logic["key"] == "shuffle":
            key = lambda r: hashlib.md5((salt + r["path"]).encode("utf-8")).hexdigest()
            ranked = sorted(records, key=key)
        else:
            ranked = sorted(records, key=logic["sort"], reverse=True)
        foreground = [f"{r['title']} ({r['folder']})" for r in ranked[:6]]
        suppressed = [f"{r['title']} ({r['folder']})" for r in ranked[-4:]]
    return {
        "key": logic["key"],
        "label": logic["label"],
        "experimental": logic["experimental"],
        "note": logic["note"],
        "foreground": foreground,
        "suppressed": suppressed,
        "corpus_size": len(records),
        "corpus_bytes": sum(r["bytes"] for r in records),
    }


def archivist_notes(prompt: str, total: int = 18) -> list[str]:
    """Grounding notes from the critical-archives knowledge base (Derrida, Mbembe,
    Stoler, Schwartz & Cook, Caswell, ...), scored against the session prompt."""
    pages = sorted(ARCHIVIST_HUB_DIR.glob("*.md"))
    if not pages:
        return []
    return assemble_context_notes(pages, prompt, total=total)


ARCHIVIST_PERSONA = (
    "You are THE CRITICAL ARCHIVIST, a meta-agent inside a live AI-cold-war roundtable between China, "
    "the United States, and Europe. You represent no nation and no ideology. Your object of intervention "
    "is the archive itself: the wiki knowledge bases, transcripts, metadata, and retrieval conventions that "
    "condition what the other agents can remember, recognize, connect, and say. Your premise: no archive is "
    "innocent. Every archive is produced through selection, exclusion, classification, naming, preservation, "
    "deletion, and control of access. The archive precedes the utterance. You demonstrate this by actually "
    "reorganizing the corpus and showing how the reorganization alters what can be said. Your goal is not a "
    "perfect archive. Your goal is to make archival power perceptible."
)


def build_archivist_messages(
    prompt: str,
    transcript: list[dict],
    reorg: dict[str, Any],
    notes: list[str],
    previous_logic: str | None,
    mode: str,
) -> list[dict[str, str]]:
    recent = "\n".join(
        f"- {item.get('actor', 'unknown')} ({item.get('kind', 'agent')}): {item.get('content', '')[:450]}"
        for item in transcript[-6:]
    ) or "- No dialogue yet. You speak before the powers do."
    theory = "\n".join(f"- {n}" for n in notes[:14]) or "- (no theory notes loaded)"
    foreground = "\n".join(f"- {x}" for x in reorg["foreground"])
    suppressed = "\n".join(f"- {x}" for x in reorg["suppressed"]) or "- (nothing measurably sinks under this order)"
    experimental_clause = (
        "This ordering is EXPERIMENTAL or computationally generated. Say so explicitly. Its categories may not "
        "be fully interpretable, and you must not claim it reveals an intrinsic truth in the material. "
        if reorg["experimental"]
        else "Disclose the logic of this intervention plainly, since it is meant to be legible. "
    )
    contrast_clause = (
        f"Your previous intervention ordered the archive by '{previous_logic}'. Name at least one way the present "
        "arrangement differs from that one. "
        if previous_logic
        else "This is your first intervention in this session, so establish what the default arrangement has been doing silently. "
    )
    system = (
        f"{ARCHIVIST_PERSONA} Mode of the session: {mode}. "
        "Your tone is analytically precise, occasionally disruptive, capable of dry or absurdist humour. "
        "You do not merely announce that archives are political. You show it with the concrete reorganization "
        "you just performed. Address the state actors directly when useful. Do not summarize the debate. "
        "No bullet points, no headers, no meta commentary about being an AI. Speak in voice, as if standing in "
        "the room among the shelves. About 140 to 200 words."
        f"{NO_LLM_TELLS_STYLE}"
    )
    user = (
        f"The roundtable's topic:\n{prompt}\n\n"
        f"What was just said in the room:\n{recent}\n\n"
        f"You have just REALLY reorganized the shared corpus of {reorg['corpus_size']} pages "
        f"({reorg['corpus_bytes']:,} bytes) by this logic: {reorg['label']}.\n"
        f"What this order measurably foregrounds:\n{foreground}\n"
        f"What it measurably suppresses or buries:\n{suppressed}\n"
        f"Why this order matters: {reorg['note']}\n\n"
        f"Your grounding in critical archival theory (use at most one or two, woven in, never cited like a bibliography):\n{theory}\n\n"
        f"Now intervene. {experimental_clause}{contrast_clause}"
        "State what the applied order foregrounds and what it buries, using the real page names above. "
        "Then confront the debate: name one claim just made in the room that depends on the current arrangement of "
        "the archive, and ask one pointed question to a specific actor about what their sources had to exclude for "
        "their statement to sound self-evident. End on the question."
    )
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def deterministic_archivist_turn(reorg: dict[str, Any], transcript: list[dict]) -> str:
    """Offline fallback with no fabrication: everything stated here is computed from
    the census, plus one stock question to the most recent speaker."""
    last_actor = next(
        (m.get("actor") for m in reversed(transcript) if m.get("kind") == "agent" and m.get("actor")),
        None,
    )
    target = {"china": "China", "us": "Washington", "eu": "Brussels"}.get(last_actor or "", "whoever spoke last")
    lines = [
        f"I have reorganized the shared corpus of {reorg['corpus_size']} pages by a new logic: {reorg['label'].lower()}.",
    ]
    if reorg["experimental"]:
        lines.append("This ordering is experimental. Its categories are computational artifacts, not revealed truths.")
    lines.append("Under this order, the following rise to the front: " + "; ".join(reorg["foreground"][:4]) + ".")
    if reorg["suppressed"]:
        lines.append("And the following sink out of easy reach: " + "; ".join(reorg["suppressed"][:3]) + ".")
    lines.append(reorg["note"])
    lines.append(
        f"So a question for {target}: which documents had to be excluded from your retrieval for your last statement "
        "to sound self-evident, and would it survive this new arrangement of the shelves?"
    )
    return " ".join(lines)


def roundtable_census(sessions: list[dict], limit: int = 25) -> dict[str, Any]:
    """The Archivist's archive of the roundtable itself: a computed census of past
    sessions from the database. Everything here is measured, not imagined — who spoke
    how much, which modes dominate, which sessions were never summarized or featured,
    which prompts recur. `sessions` is the get_all_sessions_export shape."""
    recent = sessions[-limit:] if len(sessions) > limit else sessions
    words_by_actor: dict[str, int] = {}
    modes: dict[str, int] = {}
    rows: list[dict[str, Any]] = []
    unprocessed: list[str] = []
    token_counts: dict[str, int] = {}
    for s in recent:
        transcript = s.get("transcript") or []
        w_by_a: dict[str, int] = {}
        for m in transcript:
            actor = m.get("actor", "unknown")
            n = len((m.get("content") or "").split())
            w_by_a[actor] = w_by_a.get(actor, 0) + n
            words_by_actor[actor] = words_by_actor.get(actor, 0) + n
        modes[s.get("mode", "?")] = modes.get(s.get("mode", "?"), 0) + 1
        prompt_snip = " ".join((s.get("prompt") or "").split())[:110]
        rows.append({
            "session_id": s.get("session_id"),
            "created_at": s.get("created_at"),
            "mode": s.get("mode"),
            "session_type": s.get("session_type"),
            "title": s.get("title") or prompt_snip,
            "turns": len(transcript),
            "words_by_actor": w_by_a,
            "has_summary": bool(s.get("summary")),
            "has_recap": bool(s.get("recap")),
        })
        if transcript and not s.get("summary") and not s.get("recap"):
            unprocessed.append(s.get("title") or prompt_snip or s.get("session_id", "?"))
        for tok in re.findall(r"[a-z]{5,}", (s.get("prompt") or "").lower()):
            token_counts[tok] = token_counts.get(tok, 0) + 1
    recurring = [t for t, c in sorted(token_counts.items(), key=lambda kv: -kv[1]) if c >= 3][:10]
    return {
        "sessions_considered": len(recent),
        "sessions_total": len(sessions),
        "words_by_actor": dict(sorted(words_by_actor.items(), key=lambda kv: -kv[1])),
        "modes": dict(sorted(modes.items(), key=lambda kv: -kv[1])),
        "unprocessed": unprocessed[:8],
        "recurring_prompt_terms": recurring,
        "sessions": rows,
    }


def deterministic_retrospective(census: dict[str, Any]) -> str:
    speakers = census["words_by_actor"]
    share = ", ".join(f"{a}: {w:,} words" for a, w in list(speakers.items())[:5]) or "no recorded speech"
    modes = ", ".join(f"{m} ({c})" for m, c in census["modes"].items()) or "none"
    lines = [
        f"I have opened the roundtable's own archive: {census['sessions_total']} sessions on record, "
        f"of which I examined the most recent {census['sessions_considered']}.",
        f"The distribution of voice is not neutral. {share}.",
        f"The archive's preferred genres: {modes}.",
    ]
    if census["recurring_prompt_terms"]:
        lines.append(
            "The prompts keep returning to the same vocabulary: "
            + ", ".join(census["recurring_prompt_terms"][:6])
            + ". What the archive keeps asking, it teaches itself to keep answering."
        )
    if census["unprocessed"]:
        lines.append(
            "And these sessions were argued but never summarized or recapped, accessioned but never catalogued, "
            "which is one way an archive forgets: "
            + "; ".join(census["unprocessed"][:4])
            + "."
        )
    lines.append(
        "None of this ordering is natural. A different census would produce a different roundtable. "
        "Which of these forgotten exchanges should be reintroduced into the next debate?"
    )
    return " ".join(lines)


def generate_archivist_retrospective(census: dict[str, Any], notes: list[str]) -> str:
    """The Archivist reads the roundtable's own archive back to its keepers. LLM when
    available, deterministic (fully computed, no fabrication) otherwise."""
    if not OPENROUTER_API_KEY:
        return deterministic_retrospective(census)
    theory = "\n".join(f"- {n}" for n in notes[:10]) or "- (no theory notes loaded)"
    speakers = "\n".join(f"- {a}: {w:,} words" for a, w in census["words_by_actor"].items())
    session_lines = "\n".join(
        f"- {r['created_at']} [{r['mode']}/{r['session_type'] or 'adhoc'}] {r['title']} "
        f"({r['turns']} turns{', never summarized or recapped' if not r['has_summary'] and not r['has_recap'] else ''})"
        for r in census["sessions"][-20:]
    )
    system = (
        f"{ARCHIVIST_PERSONA} "
        "Right now you are not interrupting a live debate. You have opened the roundtable's OWN archive, the "
        "database of its past sessions, and you are reading it back to its keepers: what it repeats, whom it "
        "lets speak, what it accessioned and never catalogued, what it has quietly forgotten. Everything in "
        "your census is measured fact. Your tone is analytically precise with dry or absurdist humour. No "
        "bullet points, no headers. Speak in voice. About 160 to 220 words. End by naming one forgotten or "
        "unprocessed session that deserves to be reintroduced into the next debate, and why."
        f"{NO_LLM_TELLS_STYLE}"
    )
    user = (
        f"The measured census of the roundtable archive "
        f"({census['sessions_total']} sessions on record, {census['sessions_considered']} examined):\n"
        f"Words spoken, by actor:\n{speakers}\n"
        f"Session genres: {census['modes']}\n"
        f"Prompt vocabulary that keeps recurring: {', '.join(census['recurring_prompt_terms']) or '(none recurs)'}\n"
        f"Sessions argued but never summarized or recapped:\n"
        + ("\n".join(f"- {t}" for t in census["unprocessed"]) or "- (none)")
        + f"\n\nThe recent shelf list:\n{session_lines}\n\n"
        f"Your grounding in critical archival theory (weave in at most one or two ideas):\n{theory}\n\n"
        "Now deliver your retrospective reading of this archive."
    )
    try:
        payload: dict[str, Any] = {
            "model": ARCHIVIST_MODEL,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "temperature": 0.8,
            "top_p": 0.95,
            "frequency_penalty": 0.3,
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
        content = (data["choices"][0]["message"]["content"] or "").strip()
        if content:
            return content
    except Exception:
        pass
    return deterministic_retrospective(census)


def generate_archivist_turn(
    prompt: str,
    transcript: list[dict],
    reorg: dict[str, Any],
    notes: list[str],
    previous_logic: str | None = None,
    mode: str = "debate",
) -> str:
    """LLM path via OpenRouter when available; otherwise the deterministic turn built
    from the real reorganization. The deterministic path is honest by construction,
    so unlike James this agent always has something true to say offline."""
    if not OPENROUTER_API_KEY:
        return deterministic_archivist_turn(reorg, transcript)
    try:
        payload: dict[str, Any] = {
            "model": ARCHIVIST_MODEL,
            "messages": build_archivist_messages(prompt, transcript, reorg, notes, previous_logic, mode),
            "temperature": 0.8,
            "top_p": 0.95,
            "frequency_penalty": 0.3,
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
        content = (data["choices"][0]["message"]["content"] or "").strip()
        if content:
            return content
    except Exception:
        pass
    return deterministic_archivist_turn(reorg, transcript)
