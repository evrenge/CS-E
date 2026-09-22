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
}

# Documents CS-E cites and does not contain. A second tier on purpose: they are
# never a source of CS-E requirement content, and they are pinned to the version
# the vault was written against rather than tracked across amendments.
# See source/external/SOURCES.md.
EXTERNAL: dict[str, tuple[str, int]] = {
    "CS-27_Amendment_10.pdf": ("Easy Access Rules for Small Rotorcraft (CS-27)", 322),
    "CS-29_Amendment_12.pdf": ("CS-29 Amendment 12", 438),
    "CS-Definitions_Amendment_2.pdf": ("Decision 2010/014/R", 26),
    "CS-34_Amendment_4_repealed.pdf": ("CS-34 Amendment 4", 5),
    "EN_to_ED_Decision_2025-005-R_CS-34-repeal.pdf":
        ("EN to EDD 2025/005/R", 6),
    "AMC-20_Amendment_23.pdf": ("AMC-20 Amendment 23", 678),
    "Part-21_EAR_Reg-748-2012_Nov-2025.pdf":
        ("Easy Access Rules for Initial Airworthiness and Environmental "
         "Protection (Regulation (EU) No 748/2012)", 1041),
}

CHANGE_RE = re.compile(
    r"((?:CS-E|AMC E|GM E)\s*\d{2,4}[A-Za-z()0-9 ]{0,12}?)\s+is\s+"
    r"(amended|replaced|inserted|added|deleted|created)",
    re.IGNORECASE,
)


def checksums(directory: Path = SOURCE_DIR) -> dict[str, str]:
    path = directory / "CHECKSUMS.sha256"
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


# Pages that carry an image instead of text, and are meant to. The text-layer
# check exists to catch a scanned document with no OCR; a picture cover on an
# otherwise fully extractable file is not that. Declared per document so the
# check stays strict everywhere else.
IMAGE_ONLY: dict[str, frozenset[int]] = {
    # 1-based. Page 1 is the EASA eRules cover; pages 2 to 1041 all extract.
    "Part-21_EAR_Reg-748-2012_Nov-2025.pdf": frozenset({1}),
}


def check(name: str, expect_title: str, expect_pages: int, sums: dict[str, str],
          show_inventory: bool, directory: Path = SOURCE_DIR) -> list[str]:
    problems: list[str] = []
    path = directory / name
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

    # Extract once per page. Doing it twice doubled the cost of the slowest
    # step in the pipeline, which matters now that AMC-20 (678 pages) and
    # CS-29 (438) are checked too.
    texts = [p.extract_text() or "" for p in reader.pages]
    empty = [i + 1 for i, s in enumerate(texts) if not s.strip()]
    total = sum(len(s) for s in texts)
    allowed = IMAGE_ONLY.get(name, frozenset())
    unexpected = [i for i in empty if i not in allowed]
    note = f", {len(allowed & set(empty))} declared image-only" if allowed else ""
    print(f"  text     {total:,} chars, {len(empty)} page(s) without a text layer{note}")
    empty = unexpected
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

    ext_dir = SOURCE_DIR / "external"
    ext_sums = checksums(ext_dir)
    if EXTERNAL and ext_dir.exists():
        print("\n" + "=" * 70)
        print("External reference documents (not CS-E requirement content)")
        if not ext_sums:
            print("warning: source/external/CHECKSUMS.sha256 is missing")
        for name, (title, pages) in EXTERNAL.items():
            problems += check(name, title, pages, ext_sums, False, ext_dir)

    print("\n" + "-" * 70)
    if problems:
        print(f"{len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"All {len(EXPECTED)} source documents and {len(EXTERNAL)} external "
          "reference documents verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
