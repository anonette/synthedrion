from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_ROOT = PROJECT_ROOT / "raw"
OUT_PATH = PROJECT_ROOT / "sessions" / "ingest-manifest.md"
STATE_PATH = PROJECT_ROOT / "sessions" / "ingest-manifest-state.json"
RECENT_DAYS = 7
IGNORED_FILENAMES = {"desktop.ini", ".ds_store"}
IGNORED_SUFFIXES = {".tmp", ".bak"}


def target_bucket(path: Path) -> str:
    raw_parts = set(path.parts)
    if "china-ai-policy" in raw_parts or "reg-documents" in raw_parts:
        return "China / policy-state material"
    if "us-ai-policy" in raw_parts:
        return "U.S. / actor-specific material"
    if "eu-ai-policy" in raw_parts:
        return "EU / actor-specific material"
    if "rand" in raw_parts:
        return "Shared compute-governance / RAND"
    if "shared-ai-geopolitics" in raw_parts:
        return "Shared geopolitics"
    if "articles" in raw_parts:
        return "Shared articles / cross-actor framing"
    return "Manual review"


def bucket_hint(path: Path) -> str:
    raw_parts = set(path.parts)
    if "reg-documents" in raw_parts:
        return "Likely update actor policy pages and governance/instruments pages."
    if "articles" in raw_parts:
        return "Likely update shared geopolitics pages and actor strategic framing pages."
    if "rand" in raw_parts:
        return "Likely update shared compute/governance pages and U.S./EU strategic pages."
    if "eu-ai-policy" in raw_parts:
        return "Likely update EU-specific wiki pages."
    if "us-ai-policy" in raw_parts:
        return "Likely update U.S.-specific wiki pages."
    if "china-ai-policy" in raw_parts:
        return "Likely update China-specific wiki pages."
    return "Review manually and decide which actor/shared wiki pages should cite it."


def should_ignore(path: Path) -> bool:
    name = path.name.lower()
    if name in IGNORED_FILENAMES:
        return True
    if path.suffix.lower() in IGNORED_SUFFIXES:
        return True
    return False


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {}
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_state(timestamp: datetime) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    STATE_PATH.write_text(
        json.dumps({"last_run": timestamp.isoformat()}, indent=2) + "\n",
        encoding="utf-8",
    )


def clear_state() -> None:
    if STATE_PATH.exists():
        try:
            STATE_PATH.unlink()
        except PermissionError:
            STATE_PATH.write_text("", encoding="utf-8")


def collect_files(cutoff: datetime) -> list[Path]:
    files = [
        path for path in RAW_ROOT.rglob("*")
        if path.is_file()
        and not should_ignore(path)
        and datetime.fromtimestamp(path.stat().st_mtime) >= cutoff
    ]
    files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return files


def main() -> None:
    parser = argparse.ArgumentParser(description="Build an ingest manifest from recent raw files")
    parser.add_argument("--days", type=int, default=None, help="Include files modified in the last N days")
    parser.add_argument("--since", type=str, default=None, help="Include files modified since YYYY-MM-DD or ISO datetime")
    parser.add_argument("--reset-state", action="store_true", help="Clear the saved last-run state before computing the window")
    args = parser.parse_args()

    now = datetime.now()

    if args.reset_state:
        clear_state()

    state = load_state()

    if args.since:
        try:
            cutoff = datetime.fromisoformat(args.since)
        except ValueError:
            cutoff = datetime.fromisoformat(f"{args.since}T00:00:00")
        window_label = f"since explicit date: {cutoff.strftime('%Y-%m-%d %H:%M')}"
    elif args.days is not None:
        cutoff = now - timedelta(days=args.days)
        window_label = f"last {args.days} days"
    elif state.get("last_run"):
        try:
            cutoff = datetime.fromisoformat(state["last_run"])
            window_label = f"since last run: {cutoff.strftime('%Y-%m-%d %H:%M')}"
        except Exception:
            cutoff = now - timedelta(days=RECENT_DAYS)
            window_label = f"last {RECENT_DAYS} days"
    else:
        cutoff = now - timedelta(days=RECENT_DAYS)
        window_label = f"last {RECENT_DAYS} days"

    files = collect_files(cutoff)
    grouped: dict[str, list[Path]] = {}
    for path in files:
        grouped.setdefault(target_bucket(path), []).append(path)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    lines: list[str] = []
    lines.append("# Ingest Manifest")
    lines.append("")
    lines.append(f"> Generated: {now.strftime('%Y-%m-%d %H:%M')} local")
    lines.append(f"> Window: {window_label}")
    lines.append("")

    if not files:
        lines.append("No new raw files found for the current window.")
    else:
        lines.append("## New Raw Files")
        lines.append("")
        for bucket, bucket_files in grouped.items():
            lines.append(f"### {bucket}")
            lines.append("")
            for path in bucket_files:
                rel = path.relative_to(PROJECT_ROOT).as_posix()
                modified = datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M")
                lines.append(f"- `{rel}`")
                lines.append(f"  Modified: {modified}")
                lines.append(f"  Hint: {bucket_hint(path)}")
                lines.append("")

        lines.append("## Suggested Instruction")
        lines.append("")
        lines.append("```text")
        lines.append("Ingest these new raw files into the knowledge base.")
        lines.append("Update the relevant actor and shared wiki pages.")
        lines.append("Then start a fresh round so the new material is reflected in agent behavior.")
        lines.append("")
        lines.append("Files:")
        for path in files:
            rel = path.relative_to(PROJECT_ROOT).as_posix()
            lines.append(f"- {rel}")
        lines.append("```")

    OUT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")
    save_state(now)
    print(f"Wrote ingest manifest to {OUT_PATH}")


if __name__ == "__main__":
    main()
