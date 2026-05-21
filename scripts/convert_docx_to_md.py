from __future__ import annotations

import argparse
import html
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


WORD_NAMESPACE = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def extract_docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as archive:
        xml_bytes = archive.read("word/document.xml")

    root = ET.fromstring(xml_bytes)
    paragraphs: list[str] = []

    for paragraph in root.findall(".//w:p", WORD_NAMESPACE):
        texts: list[str] = []
        for node in paragraph.iterfind(".//w:t", WORD_NAMESPACE):
            if node.text:
                texts.append(node.text)
        para_text = "".join(texts).strip()
        if para_text:
            paragraphs.append(para_text)

    return "\n\n".join(paragraphs).strip()


def title_from_text(path: Path, text: str) -> str:
    first_line = next((line.strip() for line in text.splitlines() if line.strip()), "")
    return first_line or path.stem


def render_markdown(path: Path, text: str) -> str:
    title = title_from_text(path, text)
    safe_title = html.escape(title)
    body = text.strip()
    return f"# {safe_title}\n\n> Converted from: `{path.name}`\n\n{body}\n"


def convert_file(path: Path, overwrite: bool = False) -> Path:
    text = extract_docx_text(path)
    out_path = path.with_suffix(".md")
    if out_path.exists() and not overwrite:
        raise FileExistsError(f"Refusing to overwrite existing file: {out_path}")
    out_path.write_text(render_markdown(path, text), encoding="utf-8")
    return out_path


def iter_docx_files(target: Path) -> list[Path]:
    if target.is_file():
        return [target]
    return sorted(target.rglob("*.docx"))


def main() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description="Convert DOCX files to simple Markdown")
    parser.add_argument("target", help="DOCX file or folder to convert")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing markdown files")
    args = parser.parse_args()

    target = Path(args.target).resolve()
    if not target.exists():
        raise SystemExit(f"Target not found: {target}")

    converted = 0
    skipped = 0
    for path in iter_docx_files(target):
        try:
            out_path = convert_file(path, overwrite=args.overwrite)
            print(f"converted: {path} -> {out_path}")
            converted += 1
        except FileExistsError as exc:
            print(f"skipped: {exc}")
            skipped += 1

    print(f"done: converted={converted} skipped={skipped}")


if __name__ == "__main__":
    main()
