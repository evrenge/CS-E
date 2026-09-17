#!/usr/bin/env python3
"""Verify the EASA source PDFs in source/ are intact and machine-readable.

Checks, per file:
  1. present, and SHA-256 matches source/CHECKSUMS.sha256;
  2. opens as a PDF and reports page count;
  3. /Author is EASA and the expected title fragment appears in PDF metadata;
  4. a text layer is present on every page (no OCR needed);
  5. for the Change Information files, the declared change inventory parses.

Requires pypdf (see requirements.txt). Exit status is 0 only if every check passes.

Usage:
    python3 scripts/verify_sources.py
    python3 scripts/verify_sources.py --inventory   # also print the change lists
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    sys.exit("pypdf is required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "source"

# filename -> (expected fragment in /Title, expected page count)
EXPECTED: dict[str, tuple[str, int]] = {
    "CS-E_Amendment_8.pdf": ("CS-E Amendment 8", 262),
    "CS-E_Amendment_7.pdf": ("CS-E Amendment 7", 228),
    "Change_Information_CS-E_Amdt_8.pdf": ("Change Information CS-E Amendment 8", 47),
    "Change_Information_CS-E_Amdt_7.pdf": ("Change information - CS-E Amendment 7", 30),
    "EN_to_ED_Decision_2025-003-R.pdf": ("Explanatory Note to ED Decision 2025/003/R", 11),
}

CHANGE_RE = re.compile(
    r"((?:CS-E|AMC E|GM E)\s*\d{2,4}[A-Za-z()0-9 ]{0,12}?)\s+is\s+"
    r"(amended|replaced|inserted|added|deleted|created)",
    re.IGNORECASE,
)


def checksums() -> dict[str, str]:
    path = SOURCE_DIR / "CHECKSUMS.sha256"
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text().splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1].lstrip("*")] = parts[0]
    return out


def change_inventory(reader: PdfReader) -> list[tuple[str, str]]:
    text = "\n".join((p.extract_text() or "") for p in reader.pages)
    seen: list[tuple[str, str]] = []
    for m in CHANGE_RE.finditer(text):
        entry = (" ".join(m.group(1).split()), m.group(2).lower())
        if entry not in seen:
            seen.append(entry)
    return seen


def check(name: str, expect_title: str, expect_pages: int, sums: dict[str, str],
          show_inventory: bool) -> list[str]:
    problems: list[str] = []
    path = SOURCE_DIR / name
    print(f"\n{name}")

    if not path.exists():
        print("  MISSING")
        return [f"{name}: missing"]

    payload = path.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    want = sums.get(name)
    if want is None:
        print(f"  sha256   {digest}  (not recorded in CHECKSUMS.sha256)")
        problems.append(f"{name}: no recorded checksum")
    elif want != digest:
        print(f"  sha256   {digest}  MISMATCH, expected {want}")
        problems.append(f"{name}: checksum mismatch")
    else:
        print(f"  sha256   {digest[:24]}...  OK")

    if not payload.startswith(b"%PDF"):
        print("  not a PDF")
        return problems + [f"{name}: not a PDF"]

    reader = PdfReader(str(path))
    meta = reader.metadata or {}
    pages = len(reader.pages)
    title = (meta.get("/Title") or "").strip()
    author = (meta.get("/Author") or "").strip()

    print(f"  pages    {pages}" + ("" if pages == expect_pages else f"  (expected {expect_pages})"))
    if pages != expect_pages:
        problems.append(f"{name}: {pages} pages, expected {expect_pages}")

    print(f"  title    {title!r}")
    if expect_title.lower() not in title.lower():
        problems.append(f"{name}: title {title!r} does not contain {expect_title!r}")

    print(f"  author   {author!r}")
    if "easa" not in author.lower():
        problems.append(f"{name}: /Author is {author!r}, expected EASA")

    empty = [i + 1 for i, p in enumerate(reader.pages) if not (p.extract_text() or "").strip()]
    total = sum(len(p.extract_text() or "") for p in reader.pages)
    print(f"  text     {total:,} chars, {len(empty)} page(s) without a text layer")
    if empty:
        head = ", ".join(str(i) for i in empty[:10])
        print(f"           pages: {head}{' ...' if len(empty) > 10 else ''}")
        problems.append(f"{name}: {len(empty)} page(s) with no extractable text")

    if name.startswith("Change_Information"):
        inv = change_inventory(reader)
        print(f"  changes  {len(inv)} declared")
        if not inv:
            problems.append(f"{name}: no change inventory parsed")
        if show_inventory:
            for item, verb in inv:
                print(f"             {item:<28} {verb}")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--inventory", action="store_true",
                    help="print the declared change list from each Change Information PDF")
    args = ap.parse_args()

    sums = checksums()
    if not sums:
        print("warning: source/CHECKSUMS.sha256 is missing; integrity is unverified")

    problems: list[str] = []
    for name, (title, pages) in EXPECTED.items():
        problems += check(name, title, pages, sums, args.inventory)

    print("\n" + "-" * 70)
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"All {len(EXPECTED)} source documents verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
