from __future__ import annotations

"""Ingest the threat-intel incident feed (the mirror-world "reality" layer).

Works against a sample file today and a live API when THREAT_INTEL_BASE_URL/
THREAT_INTEL_API_KEY are set in .env.

Examples:
    python scripts/run_threat_intel_ingest.py --check                                     # connectivity only
    python scripts/run_threat_intel_ingest.py --sample docs/sample_incidents.json --no-official
    python scripts/run_threat_intel_ingest.py --no-official                                # full initial sync (paginated)
    python scripts/run_threat_intel_ingest.py --since 2026-06-01T00:00:00Z --no-official    # incremental
"""

import argparse
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.threat_intel import check_feed_health, fetch_all_incidents, ingest, load_sample, pull_official_coverage


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description="Ingest threat-intel incidents into raw/threat-intel/")
    ap.add_argument("--check", action="store_true", help="Just check feed connectivity (GET /health) and exit")
    ap.add_argument("--sample", help="Path to a sample JSON file instead of the live API")
    ap.add_argument("--since", help="Only pull incidents updated since this ISO timestamp (live API, incremental)")
    ap.add_argument("--limit", type=int, default=100, help="Page size per request (live API)")
    ap.add_argument("--max-per-query", type=int, default=4, help="Official-coverage results per incident")
    ap.add_argument("--no-official", action="store_true", help="Skip pulling media/regulatory coverage")
    args = ap.parse_args()

    if args.check:
        print(check_feed_health())
        return

    if args.sample:
        raws = load_sample(args.sample)
        source = f"sample: {args.sample}"
    else:
        raws = fetch_all_incidents(since=args.since, limit=args.limit)
        source = "live feed (THREAT_INTEL_BASE_URL)" + (f", since={args.since}" if args.since else ", full sync")

    if not raws:
        print("No incidents found. Provide --sample <file>, or set THREAT_INTEL_BASE_URL / THREAT_INTEL_API_KEY in .env.")
        return

    res = ingest(raws)
    print(f"Source: {source}")
    print(f"Ingested: saved={len(res['saved'])} skipped={len(res['skipped'])}")
    for s in res["saved"]:
        print(f"  + {s['path']}")
    for s in res["skipped"]:
        print(f"  - skipped {s['id']} ({s['reason']})")

    if not args.no_official and res["saved"]:
        print("\nPulling official-narrative coverage per incident (needs TAVILY/SERPAPI keys)...")
        records = [s["record"] for s in res["saved"]]
        official = asyncio.run(pull_official_coverage(records, max_per_query=args.max_per_query))
        for o in official["official"]:
            print(f"  official: {o}")

    print("\nNext: python scripts/build_ingest_manifest.py")


if __name__ == "__main__":
    main()
