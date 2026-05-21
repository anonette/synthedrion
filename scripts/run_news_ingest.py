from __future__ import annotations

import argparse
import asyncio
import subprocess
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.news_ingest import TOPIC_QUERIES, REPORT_PATH, run_news_ingest


def main() -> None:
    parser = argparse.ArgumentParser(description="Search recent AI geopolitics news and save it into raw/")
    parser.add_argument("--days", type=int, default=3, help="Look back window in days")
    parser.add_argument("--max-per-query", type=int, default=5, help="Max results per query/provider")
    parser.add_argument("--topics", type=str, default=",".join(TOPIC_QUERIES.keys()), help="Comma-separated topic groups")
    parser.add_argument("--focus", type=str, default=None, help="Extra weekly focus query or keyword string")
    parser.add_argument("--build-manifest", action="store_true", help="Run build_ingest_manifest.py after saving raw files")
    args = parser.parse_args()

    topics = [item.strip() for item in args.topics.split(",") if item.strip()]
    result = asyncio.run(run_news_ingest(days=args.days, max_per_query=args.max_per_query, topics=topics, focus_query=args.focus))
    print(f"Saved {len(result['saved'])} items, skipped {len(result['skipped'])}, failed {len(result['failed'])}.")
    print(f"Report: {REPORT_PATH}")

    if args.build_manifest:
        python_exe = PROJECT_ROOT / ".venv" / "Scripts" / "python.exe"
        subprocess.run([str(python_exe), "scripts/build_ingest_manifest.py"], cwd=PROJECT_ROOT, check=False)


if __name__ == "__main__":
    main()
