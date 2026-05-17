from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


FOLDER_ID_RE = re.compile(r"/folders/([a-zA-Z0-9_-]+)")


def extract_folder_id(value: str) -> str:
    match = FOLDER_ID_RE.search(value)
    if match:
        return match.group(1)
    if re.fullmatch(r"[a-zA-Z0-9_-]{10,}", value):
        return value
    raise ValueError("Could not extract a Google Drive folder id from the provided value")


def ensure_gdown(python_exe: str) -> None:
    result = subprocess.run(
        [python_exe, "-m", "gdown", "--version"],
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        return
    install = subprocess.run(
        [python_exe, "-m", "pip", "install", "gdown"],
        text=True,
    )
    if install.returncode != 0:
        raise RuntimeError("Failed to install gdown")


def main() -> None:
    parser = argparse.ArgumentParser(description="Download a public Google Drive folder into raw/")
    parser.add_argument("folder", help="Public Google Drive folder URL or folder id")
    parser.add_argument("target", nargs="?", default="raw/drive-import", help="Target directory")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    python_exe = str(project_root / ".venv" / "Scripts" / "python.exe")
    target = (project_root / args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)

    folder_id = extract_folder_id(args.folder)
    ensure_gdown(python_exe)

    command = [
        python_exe,
        "-m",
        "gdown",
        f"https://drive.google.com/drive/folders/{folder_id}",
        "--folder",
        "--remaining-ok",
        "-O",
        str(target),
    ]
    result = subprocess.run(command)
    if result.returncode != 0:
        raise SystemExit(result.returncode)

    print(f"Downloaded folder {folder_id} into {target}")
    print("Next step: run `python scripts/build_ingest_manifest.py`")


if __name__ == "__main__":
    main()
