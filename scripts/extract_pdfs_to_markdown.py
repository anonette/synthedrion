from __future__ import annotations

"""Extract text from PDF (and DOCX) source files into normalized Markdown.

Mirrors the header style of scripts/convert_docx_to_md.py so extracted pages slot
into raw/ alongside hand-written notes. Heavy source PDFs can stay outside the repo;
only the extracted Markdown is committed.

Usage:
    python scripts/extract_pdfs_to_markdown.py <source_dir> <target_raw_dir> [--min-bytes 2000] [--overwrite]

URL-only .txt bookmarks in the source are collected into `<target>/_source-links.md`
rather than copied as many tiny files. Files smaller than --min-bytes (failed
downloads / stubs) are skipped and reported.
"""

import argparse
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import fitz  # PyMuPDF


WORD_NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
URL_RE = re.compile(r"https?://\S+")


def slugify(name: str) -> str:
    stem = Path(name).stem
    stem = stem.replace("&#8217;", "").replace("’", "")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", stem).strip("-").lower()
    slug = re.sub(r"-{2,}", "-", slug)
    return slug or "document"


def normalize_text(text: str) -> str:
    # collapse runaway whitespace while preserving paragraph breaks
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    lines = [ln.rstrip() for ln in text.split("\n")]
    return "\n".join(lines).strip()


def pdf_to_text(path: Path) -> str:
    parts: list[str] = []
    with fitz.open(path) as doc:
        for page in doc:
            parts.append(page.get_text("text"))
    return normalize_text("\n\n".join(parts))


def docx_to_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("word/document.xml"))
    paragraphs: list[str] = []
    for paragraph in root.findall(".//w:p", WORD_NS):
        texts = [node.text for node in paragraph.iterfind(".//w:t", WORD_NS) if node.text]
        para = "".join(texts).strip()
        if para:
            paragraphs.append(para)
    return normalize_text("\n\n".join(paragraphs))


def title_from(text: str, fallback: str) -> str:
    for line in text.splitlines():
        line = line.strip()
        if len(line) > 8:
            return line[:160]
    return fallback


def render_markdown(source_name: str, text: str) -> str:
    title = title_from(text, Path(source_name).stem)
    return f"# {title}\n\n> Extracted from: `{source_name}`\n\n{text}\n"


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    ap = argparse.ArgumentParser(description="Extract PDFs/DOCX to normalized Markdown")
    ap.add_argument("source")
    ap.add_argument("target")
    ap.add_argument("--min-bytes", type=int, default=2000, help="Skip files smaller than this (stubs)")
    ap.add_argument("--overwrite", action="store_true")
    args = ap.parse_args()

    source = Path(args.source).resolve()
    target = Path(args.target).resolve()
    target.mkdir(parents=True, exist_ok=True)

    converted = skipped = empty = 0
    links: list[str] = []

    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        suffix = path.suffix.lower()

        if suffix == ".txt" and path.stat().st_size < args.min_bytes:
            body = path.read_text(encoding="utf-8", errors="ignore")
            for url in URL_RE.findall(body):
                links.append(f"- [{path.stem}]({url})")
            continue

        if path.stat().st_size < args.min_bytes:
            print(f"skip stub ({path.stat().st_size}B): {path.name}")
            skipped += 1
            continue

        if suffix == ".pdf":
            text = pdf_to_text(path)
        elif suffix == ".docx":
            text = docx_to_text(path)
        elif suffix == ".txt":
            text = normalize_text(path.read_text(encoding="utf-8", errors="ignore"))
        else:
            continue

        out = target / f"{slugify(path.name)}.md"
        if out.exists() and not args.overwrite:
            print(f"skip exists: {out.name}")
            skipped += 1
            continue

        if len(text.strip()) < 200:
            print(f"WARNING near-empty (scanned image?): {path.name} -> {out.name} ({len(text)} chars)")
            empty += 1

        out.write_text(render_markdown(path.name, text), encoding="utf-8")
        print(f"ok: {path.name} -> {out.name} ({len(text):,} chars)")
        converted += 1

    if links:
        links_path = target / "_source-links.md"
        header = "# Imported source links\n\n> URL bookmarks from the imported corpus (fetch on demand).\n\n"
        existing = links_path.read_text(encoding="utf-8") if links_path.exists() else ""
        seen = set(existing.splitlines())
        new = [ln for ln in links if ln not in seen]
        if new:
            links_path.write_text((existing or header) + "\n".join(new) + "\n", encoding="utf-8")
            print(f"links: +{len(new)} -> {links_path.name}")

    print(f"\ndone: converted={converted} skipped={skipped} near_empty={empty}")


if __name__ == "__main__":
    main()
