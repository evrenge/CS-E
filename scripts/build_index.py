#!/usr/bin/env python3
"""Phase 1b — build work/paragraph_index.csv from the Phase 1a sidecar.

Columns:
    id                  CS-E 740, AMC E 740(c)(3), ...
    title               heading text after the id
    subpart             A-F ('' for front matter)
    start_page          PDF page of the heading banner
    end_page            page before the next heading (document end for the last)
    has_figure_or_table 'yes' when any page in the span carries a real figure,
                        a detected table, or a Figure/Table caption
    changed_in          Amdt7 / Amdt8 / Amdt7;Amdt8 / none
    changed_refs        the verbatim redline declarations behind changed_in

Every page carries the EASA logo as an image, so a real figure is images > 1.

Usage:
    python3 scripts/build_index.py
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
SIDECAR = ROOT / "work" / "pages.json"
INDEX = ROOT / "work" / "paragraph_index.csv"
CI = {
    "Amdt7": ROOT / "source" / "Change_Information_CS-E_Amdt_7.pdf",
    "Amdt8": ROOT / "source" / "Change_Information_CS-E_Amdt_8.pdf",
}

# 'CS-E 740', 'AMC E 740(c)(2)(i)', 'AMC E 20(f)'
ID = r"(?:AMC to CS-E|CS-E|AMC E|GM E)\s*\d{1,4}(?:\([^)\s]{1,6}\))*"
HEAD_ID = re.compile(rf"^({ID})\s*(.*)$")

# Redline declarations. Anchored so body prose such as "... when imbalances are
# added to ..." cannot match; that sentence has no leading id.
DECLARATIONS = [
    re.compile(rf"^\s*({ID})\s+is\s+(?:amended|created|added|deleted|replaced)\b[^\n]*", re.M),
    re.compile(rf"^\s*The following\s+({ID})\s+is\s+(?:added|created)\b[^\n]*", re.M),
    re.compile(rf"^\s*Point[^\n]{{0,40}}?\s+is\s+added\s+in\s+({ID})\b[^\n]*", re.M),
    # Renames bind to the NEW id: 'AMC E 740(h)(2) is renamed as AMC E 740(i)(2)
    # and its content is amended' is a change to AMC E 740(i)(2), which is the
    # heading that exists in Amendment 8.
    re.compile(rf"^\s*{ID}\s+is\s+renamed\s+as\s+({ID})[^\n]*", re.M),
]


def redline_changes(path: Path) -> dict[str, list[str]]:
    """Return {paragraph id: [verbatim declaration, ...]} for one redline PDF."""
    doc = pymupdf.open(path)
    text = "\n".join(page.get_text("text") for page in doc)
    text = re.sub(r"[ \t]+", " ", text)
    found: dict[str, list[str]] = {}
    for pattern in DECLARATIONS:
        for m in pattern.finditer(text):
            ref = re.sub(r"\s+", " ", m.group(1)).strip()
            line = " ".join(m.group(0).split())
            found.setdefault(ref, [])
            if line not in found[ref]:
                found[ref].append(line)
    return found


def resolve(ref: str, ids: list[str]) -> str | None:
    """Map a redline reference onto an index id.

    Exact first, so 'AMC E 20(f)' binds to its own heading rather than to
    'AMC E 20'. Otherwise the longest heading id that prefixes the reference,
    so 'AMC E 740(c)(3)' binds to 'AMC E 740'.
    """
    if ref in ids:
        return ref
    candidates = [i for i in ids if ref.startswith(i)]
    return max(candidates, key=len) if candidates else None


def main() -> int:
    if not SIDECAR.exists():
        sys.exit("run scripts/extract_text.py first")
    pages = json.loads(SIDECAR.read_text())
    by_page = {p["page"]: p for p in pages}
    last_page = max(by_page)

    # Ordered heading list.
    entries: list[dict] = []
    for p in pages:
        for heading in p["headings"]:
            m = HEAD_ID.match(heading)
            if m:
                pid, title = " ".join(m.group(1).split()), m.group(2).strip()
            else:
                pid, title = heading.split("  ")[0].strip(), heading
            entries.append({
                "id": pid,
                "title": title,
                "subpart": p["subpart"],
                "start_page": p["page"],
            })

    for i, e in enumerate(entries):
        nxt = entries[i + 1]["start_page"] if i + 1 < len(entries) else last_page + 1
        e["end_page"] = max(e["start_page"], nxt - 1)
        span = range(e["start_page"], e["end_page"] + 1)
        e["has_figure_or_table"] = "yes" if any(
            by_page[n]["images"] > 1 or by_page[n]["tables"] > 0 or by_page[n]["captions"]
            for n in span
        ) else "no"

    ids = [e["id"] for e in entries]
    tags: dict[str, set[str]] = {}
    refs: dict[str, list[str]] = {}
    unresolved: list[tuple[str, str]] = []

    for amdt, path in CI.items():
        changes = redline_changes(path)
        print(f"{path.name}: {len(changes)} declared changes")
        for ref, lines in sorted(changes.items()):
            target = resolve(ref, ids)
            if target is None:
                unresolved.append((amdt, ref))
                continue
            tags.setdefault(target, set()).add(amdt)
            refs.setdefault(target, []).extend(f"[{amdt}] {ln}" for ln in lines)

    for e in entries:
        got = sorted(tags.get(e["id"], []))
        e["changed_in"] = ";".join(got) if got else "none"
        e["changed_refs"] = " | ".join(refs.get(e["id"], []))

    INDEX.parent.mkdir(parents=True, exist_ok=True)
    cols = ["id", "title", "subpart", "start_page", "end_page",
            "has_figure_or_table", "changed_in", "changed_refs"]
    with INDEX.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(entries)

    print(f"wrote {INDEX.relative_to(ROOT)}: {len(entries)} paragraphs")
    if unresolved:
        print("UNRESOLVED redline references (no matching heading):")
        for amdt, ref in unresolved:
            print(f"  {amdt}: {ref}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
