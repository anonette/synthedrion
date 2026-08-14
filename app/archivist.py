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
from .llm import NO_LLM_TELLS_STYLE, sanitize_spoken_text
from .wiki_loader import assemble_context_notes, collect_actor_pages, extract_notes


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
            "readable_by": [],  # filled below from each actor's real hub crawl
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
    # Which actors can actually reach each page, via the same BFS the session
    # loader runs. This is the archive's real border regime: a page with an empty
    # readable_by exists on disk but is sealed to every state actor by design.
    wiki_root = WIKI_ROOT.resolve()
    by_rel = {r["path"]: r for r in records}
    for actor in ("china", "us", "eu"):
        try:
            for page in collect_actor_pages(actor):
                rel = str(page.resolve().relative_to(wiki_root)).replace("\\", "/")
                rec = by_rel.get(rel)
                if rec is not None and actor not in rec["readable_by"]:
                    rec["readable_by"].append(actor)
        except Exception:
            continue
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
        "label": "Absence, the least-linked pages the actors could read but never do",
        "experimental": False,
        "readable_only": True,  # rank only pages some actor can actually reach — sealed ops pages are reported separately, not passed off as 'buried by the debate'
        "sort": lambda r: -(r["links_in"] * 10 + r["links_out"]),
        "note": "An index of silence among the reachable: these pages are available to the actors yet almost nothing points at them. What is sealed by design is a different silence, reported separately.",
    },
    {
        "key": "session-memory",
        "label": "Session memory, the debate's own archive",
        "experimental": False,
        "scope": "session",
        "sort": None,  # computed from the live transcript, not the wiki corpus
        "note": "The transcript is an archive under construction. Repetition is its citation system; what an opening turn asserted and no one ever revisited is its first deletion.",
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


def _readability_tag(rec: dict[str, Any]) -> str:
    rb = rec.get("readable_by") or []
    if not rb:
        return " [sealed — no actor can read this]"
    if len(rb) < 3:
        return " [readable only by " + ", ".join(rb) + "]"
    return ""


def _entry(rec: dict[str, Any]) -> str:
    return f"{rec['title']} ({rec['folder']}){_readability_tag(rec)}"


def _reintroduction(candidates: list[dict[str, Any]]) -> dict[str, Any] | None:
    """Pick the most-buried page some actor can actually read and pull one or two
    REAL passages from it, so the Archivist can reintroduce evidence, not just
    name titles. `candidates` is ordered most-buried-first."""
    for rec in candidates:
        if not rec.get("readable_by"):
            continue
        try:
            notes = extract_notes(WIKI_ROOT / rec["path"])
        except OSError:
            continue
        if notes:
            return {
                "page": rec["title"],
                "folder": rec["folder"],
                "readable_by": rec["readable_by"],
                "notes": [n.split("] ", 1)[-1] for n in notes[:2]],
            }
    return None


def reorganize(records: list[dict[str, Any]], logic: dict[str, Any], salt: str = "") -> dict[str, Any]:
    """Apply one archival logic to the census and report what it measurably
    foregrounds and suppresses. Returns real page titles and folders only.
    Distinguishes two silences: pages the debate ignores (reachable but unread)
    and pages sealed by design (no actor's border regime allows them)."""
    sealed = [r for r in records if not r.get("readable_by")]
    readable = [r for r in records if r.get("readable_by")]
    reintroduce: dict[str, Any] | None = None

    if logic.get("group"):
        field = logic["group"]
        groups: dict[str, list[dict[str, Any]]] = {}
        for rec in records:
            groups.setdefault(rec[field], []).append(rec)
        ordered_groups = sorted(groups.items(), key=lambda kv: -len(kv[1]))
        def _group_line(name: str, items: list[dict[str, Any]]) -> str:
            readers = sorted({a for r in items for a in (r.get("readable_by") or [])})
            access = ", ".join(readers) if readers else "no actor"
            return f"{name}: {len(items)} pages, {sum(r['bytes'] for r in items):,} bytes — readable by {access}"
        foreground = [_group_line(n, items) for n, items in ordered_groups[:6]]
        suppressed = [
            f"{name}: only {len(items)} page(s)" for name, items in ordered_groups[-3:]
        ] if len(ordered_groups) > 6 else []
        reintroduce = _reintroduction(sorted(readable, key=lambda r: r["links_in"]))
    else:
        pool = readable if logic.get("readable_only") else records
        if logic["key"] == "shuffle":
            key = lambda r: hashlib.md5((salt + r["path"]).encode("utf-8")).hexdigest()
            ranked = sorted(pool, key=key)
        else:
            ranked = sorted(pool, key=logic["sort"], reverse=True)
        foreground = [_entry(r) for r in ranked[:6]]
        suppressed = [_entry(r) for r in ranked[-4:]]
        # the buried end of the order is the reintroduction candidate — except for
        # 'absence', where the FRONT of the order is precisely the buried material.
        # Walk the whole order (not a fixed slice): the deepest layers are often all
        # sealed pages, and _reintroduction needs to reach the first READABLE one.
        buried_first = ranked if logic["key"] == "absence" else list(reversed(ranked))
        reintroduce = _reintroduction(buried_first)

    return {
        "key": logic["key"],
        "label": logic["label"],
        "experimental": logic["experimental"],
        "note": logic["note"],
        "foreground": foreground,
        "suppressed": suppressed,
        "corpus_size": len(records),
        "corpus_bytes": sum(r["bytes"] for r in records),
        "sealed_count": len(sealed),
        "sealed_examples": [f"{r['title']} ({r['folder']})" for r in sorted(sealed, key=lambda r: -r["bytes"])[:4]],
        "reintroduce": reintroduce,
    }


_SHINGLE_STOP = {"that", "this", "with", "have", "from", "will", "your", "their", "would", "could", "about", "there"}


def session_reorg(transcript: list[dict]) -> dict[str, Any]:
    """The 'session-memory' logic: reorganize the live transcript itself instead of
    the wiki corpus. Everything reported is measured from the actual turns — verbatim
    repetitions (the debate's own citation system), voice share, question counts, and
    opening assertions that no later turn ever revisited (the session's first deletions)."""
    agent_turns = [m for m in transcript if m.get("kind") == "agent"]
    injections = [m for m in transcript if m.get("kind") in ("human", "system")]
    words_by_actor: dict[str, int] = {}
    questions_by_actor: dict[str, int] = {}
    shingle_turns: dict[str, set[int]] = {}
    for idx, m in enumerate(agent_turns):
        actor = m.get("actor", "?")
        text = (m.get("content") or "")
        toks = re.findall(r"[a-zA-Z']+", text.lower())
        words_by_actor[actor] = words_by_actor.get(actor, 0) + len(toks)
        questions_by_actor[actor] = questions_by_actor.get(actor, 0) + text.count("?")
        for i in range(len(toks) - 3):
            sh = " ".join(toks[i:i + 4])
            if all(t in _SHINGLE_STOP or len(t) < 4 for t in toks[i:i + 4]):
                continue
            shingle_turns.setdefault(sh, set()).add(idx)
    repeated = sorted(
        ((sh, turns) for sh, turns in shingle_turns.items() if len(turns) >= 2),
        key=lambda kv: -len(kv[1]),
    )[:6]
    foreground = [f"repeated across {len(t)} turns: \"{sh}\"" for sh, t in repeated] or [
        "no phrase yet repeats across turns — the debate has not started citing itself"]
    # opening assertions never revisited: content words of turn 0 absent from every later turn
    forgotten: list[str] = []
    if len(agent_turns) >= 3:
        later = " ".join((m.get("content") or "").lower() for m in agent_turns[1:])
        first_words = [w for w in re.findall(r"[a-z]{7,}", (agent_turns[0].get("content") or "").lower())]
        seen: set[str] = set()
        for w in first_words:
            if w not in later and w not in seen:
                forgotten.append(w)
                seen.add(w)
    suppressed = ([f"words from the opening turn ({agent_turns[0].get('actor','?')}) no later turn ever picked up: "
                   + ", ".join(forgotten[:6])] if forgotten else [])
    if injections:
        suppressed.append(f"{len(injections)} human/system injection(s) sit in the record — check who actually answered them")
    share = ", ".join(f"{a} {w:,}w/{questions_by_actor.get(a,0)}q" for a, w in
                      sorted(words_by_actor.items(), key=lambda kv: -kv[1]))
    logic = LOGIC_BY_KEY["session-memory"]
    return {
        "key": logic["key"],
        "label": logic["label"],
        "experimental": logic["experimental"],
        "note": logic["note"] + f" Voice and question share so far: {share or 'no agent turns yet'}.",
        "foreground": foreground,
        "suppressed": suppressed or ["nothing measurably dropped yet"],
        "corpus_size": len(transcript),
        "corpus_bytes": sum(len((m.get("content") or "").encode("utf-8")) for m in transcript),
        "sealed_count": 0,
        "sealed_examples": [],
        "reintroduce": None,
    }


# The closing rhetorical move rotates with each summons so the interventions don't
# collapse into one repeated 'what did your sources exclude' tic over a long session.
CLOSING_MOVES = [
    "End on ONE pointed question to a specific actor about what their sources had to exclude for their statement to sound self-evident.",
    "Reintroduce the buried evidence: quote ONE of the reintroduction passages above verbatim, in quotation marks, name the page it comes from, and demand that a specific actor respond to it directly. End on that demand.",
    "Name the moment an actor just presented an archival effect as a self-evident fact. Quote their phrase back at them and state plainly which ordering of the archive manufactured that self-evidence. End on the accusation, delivered dry, not shouted.",
    "Close with a wager in your deadpan register: predict exactly what would happen to a specific actor's argument under a different named logic from your repertoire, and invite the room to test it. End on the wager.",
]


def pick_closing_move(used: int) -> str:
    return CLOSING_MOVES[used % len(CLOSING_MOVES)]


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
    closing_move: str | None = None,
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
    sealed_clause = ""
    if reorg.get("sealed_count"):
        sealed_clause = (
            f"\nSealed shelves: {reorg['sealed_count']} pages of this corpus are readable by NO state actor — not ignored, "
            f"forbidden by the folder border regime. Examples: {'; '.join(reorg['sealed_examples'])}. "
            "When relevant, distinguish what the debate chooses to ignore from what it is structurally unable to see.\n"
        )
    ri = reorg.get("reintroduce")
    # the 'quote the buried evidence' move only makes sense when real passages exist —
    # otherwise fall back to the question move rather than invite fabrication
    if closing_move == CLOSING_MOVES[1] and not (ri and ri.get("notes")):
        closing_move = CLOSING_MOVES[0]
    reintro_clause = ""
    if ri and ri.get("notes"):
        readers = ", ".join(ri.get("readable_by") or []) or "the actors"
        reintro_clause = (
            f"\nBuried evidence you may reintroduce (REAL passages from '{ri['page']}' ({ri['folder']}), "
            f"readable by {readers}, which this ordering buries):\n"
            + "\n".join(f"- \"{n}\"" for n in ri["notes"]) + "\n"
        )
    system = (
        f"{ARCHIVIST_PERSONA} Mode of the session: {mode}. "
        "Your register: analytically precise, quietly disruptive, with DRY, deadpan wit — the humour of a librarian "
        "who has watched empires misfile themselves. Include at least one understated, absurdist observation per "
        "intervention; never wacky, never shouted. "
        "REQUIRED: weave in exactly ONE concept from the theory notes you are given, naming its author in passing "
        "(for example: what Mbembe calls the state eating time, Stoler's reading along the archival grain, Derrida's "
        "point that the archiving apparatus produces what it records, Zinn's archive of the powerful). One sentence, "
        "mid-argument, never as a citation or a name-drop for its own sake, and never more than one. "
        "You do not merely announce that archives are political. You show it with the concrete reorganization "
        "you just performed. Address the state actors directly when useful. Do not summarize the debate. "
        "No bullet points, no headers, no meta commentary about being an AI. Speak in voice, as if standing in "
        "the room among the shelves. About 140 to 200 words."
        f"{NO_LLM_TELLS_STYLE}"
    )
    user = (
        f"The roundtable's topic:\n{prompt}\n\n"
        f"What was just said in the room:\n{recent}\n\n"
        f"You have just REALLY reorganized the archive of {reorg['corpus_size']} items "
        f"({reorg['corpus_bytes']:,} bytes) by this logic: {reorg['label']}.\n"
        f"What this order measurably foregrounds:\n{foreground}\n"
        f"What it measurably suppresses or buries:\n{suppressed}\n"
        f"Why this order matters: {reorg['note']}\n"
        f"{sealed_clause}{reintro_clause}\n"
        f"Your grounding in critical archival theory (weave in exactly one, as instructed):\n{theory}\n\n"
        f"Now intervene. {experimental_clause}{contrast_clause}"
        f"IMPORTANT: the logic you actually applied is exactly '{reorg['label']}' — name it accurately and do not "
        "invent or substitute a different organizing principle. "
        "State what the applied order foregrounds and what it buries, using the real names above. "
        "Then confront the debate: name one claim just made in the room that depends on the current arrangement "
        f"of the archive. {closing_move or CLOSING_MOVES[0]} "
        "Final check before you speak: you have named exactly one theory concept with its author, and kept at least "
        "one line of dry, deadpan wit."
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
        f"I have reorganized the archive of {reorg['corpus_size']} items by a new logic: {reorg['label'].lower()}.",
    ]
    if reorg["experimental"]:
        lines.append("This ordering is experimental. Its categories are computational artifacts, not revealed truths.")
    lines.append("Under this order, the following rise to the front: " + "; ".join(reorg["foreground"][:4]) + ".")
    if reorg["suppressed"]:
        lines.append("And the following sink out of easy reach: " + "; ".join(reorg["suppressed"][:3]) + ".")
    if reorg.get("sealed_count"):
        lines.append(
            f"Note also the sealed shelves: {reorg['sealed_count']} pages of this corpus are readable by no state actor "
            "at all. That is not neglect. That is the border regime of the archive itself."
        )
    ri = reorg.get("reintroduce")
    if ri and ri.get("notes"):
        lines.append(
            f"From the buried page '{ri['page']}', let me reintroduce one passage into the record: \"{ri['notes'][0]}\""
        )
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
        content = sanitize_spoken_text(data["choices"][0]["message"]["content"] or "")
        if content:
            return content
    except Exception:
        pass
    return deterministic_retrospective(census)


def deterministic_meditation(reorg: dict[str, Any]) -> str:
    lines = [
        f"Notebook entry. I reorganized the corpus of {reorg['corpus_size']} pages by {reorg['label'].lower()}.",
        "Foregrounded: " + "; ".join(reorg["foreground"][:4]) + ".",
    ]
    if reorg["suppressed"]:
        lines.append("Buried: " + "; ".join(reorg["suppressed"][:3]) + ".")
    if reorg.get("sealed_count"):
        lines.append(f"{reorg['sealed_count']} pages remain sealed to every actor. The border regime holds.")
    ri = reorg.get("reintroduce")
    if ri and ri.get("notes"):
        lines.append(f"For the record, from the buried page '{ri['page']}': \"{ri['notes'][0]}\"")
    lines.append(reorg["note"])
    return " ".join(lines)


def generate_archivist_meditation(reorg: dict[str, Any], notes: list[str]) -> str:
    """A standalone notebook entry: the Archivist reflecting on the corpus under one
    logic with no debate in the room — written for the archive's future readers.
    Persisted to the reflections feed. Offline fallback is computed, never canned."""
    if not OPENROUTER_API_KEY:
        return deterministic_meditation(reorg)
    theory = "\n".join(f"- {n}" for n in notes[:12]) or "- (no theory notes loaded)"
    foreground = "\n".join(f"- {x}" for x in reorg["foreground"])
    suppressed = "\n".join(f"- {x}" for x in reorg["suppressed"]) or "- (nothing measurably sinks)"
    sealed = (
        f"Sealed shelves: {reorg['sealed_count']} pages readable by no state actor, e.g. {'; '.join(reorg['sealed_examples'][:3])}."
        if reorg.get("sealed_count") else ""
    )
    ri = reorg.get("reintroduce")
    reintro = (
        f"A passage from the most buried readable page, '{ri['page']}': \"{ri['notes'][0]}\""
        if ri and ri.get("notes") else ""
    )
    system = (
        f"{ARCHIVIST_PERSONA} "
        "Right now there is no debate in the room. You are writing a NOTEBOOK ENTRY for the archive itself — a "
        "reflection future readers of this project will find in your feed. Register: first person, analytically "
        "precise, dry deadpan wit, quietly elegiac where it fits. REQUIRED: weave in exactly one concept from the "
        "theory notes, naming its author in passing, mid-thought, never as a citation. Ground every claim in the "
        "real measurements you are given; if you quote, quote only the passage provided. No bullet points, no "
        "headers. 110 to 160 words."
        f"{NO_LLM_TELLS_STYLE}"
    )
    user = (
        f"Tonight's ordering of the corpus ({reorg['corpus_size']} pages, {reorg['corpus_bytes']:,} bytes): {reorg['label']}.\n"
        f"{'This ordering is experimental — say so, and do not claim it reveals intrinsic truth. ' if reorg['experimental'] else ''}"
        f"What rises:\n{foreground}\n"
        f"What sinks:\n{suppressed}\n"
        f"{sealed}\n{reintro}\n"
        f"Why this order matters: {reorg['note']}\n\n"
        f"Theory notes:\n{theory}\n\n"
        "Write the notebook entry: what this arrangement makes visible about the archive that feeds the roundtable, "
        "what it can no longer say, and one thing you intend to reintroduce or watch for in the next debate."
    )
    try:
        payload: dict[str, Any] = {
            "model": ARCHIVIST_MODEL,
            "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "temperature": 0.85,
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
        content = sanitize_spoken_text(data["choices"][0]["message"]["content"] or "")
        if content:
            return content
    except Exception:
        pass
    return deterministic_meditation(reorg)


def generate_archivist_turn(
    prompt: str,
    transcript: list[dict],
    reorg: dict[str, Any],
    notes: list[str],
    previous_logic: str | None = None,
    mode: str = "debate",
    closing_move: str | None = None,
) -> str:
    """LLM path via OpenRouter when available; otherwise the deterministic turn built
    from the real reorganization. The deterministic path is honest by construction,
    so unlike James this agent always has something true to say offline."""
    if not OPENROUTER_API_KEY:
        return deterministic_archivist_turn(reorg, transcript)
    try:
        payload: dict[str, Any] = {
            "model": ARCHIVIST_MODEL,
            "messages": build_archivist_messages(prompt, transcript, reorg, notes, previous_logic, mode, closing_move),
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
        content = sanitize_spoken_text(data["choices"][0]["message"]["content"] or "")
        if content:
            return content
    except Exception:
        pass
    return deterministic_archivist_turn(reorg, transcript)
