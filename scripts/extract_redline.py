#!/usr/bin/env python3
"""Recover before/after wording from the Change Information PDFs.

Both redlines mark changes the same way, verified by rendering pages and by
reading the content stream:

    inserted   black text sitting on a cyan highlight - a filled rectangle with
               non-stroking colour (0, 1, 1) behind the run
    deleted    red text, #ff0000, with a strikethrough rule
    unchanged  plain black with nothing behind it

`extract_text()` alone drops both markers and runs deleted and inserted words
together, producing sentences that read as normative but exist in no amendment.
This classifies every span instead, then reconstructs:

    before = unchanged + deleted      (the wording as it stood)
    after  = unchanged + inserted     (the wording as amended)

Runs are grouped under the paragraph each Change Information document declares
them against ("CS-E 740 is amended as follows:").

Writes work/redline.json and one readable file per paragraph in work/redline/.

Usage:
    python3 scripts/extract_redline.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    import pymupdf
except ImportError:
    sys.exit("pymupdf is required: pip install -r requirements.txt")

ROOT = Path(__file__).resolve().parent.parent
OUT_JSON = ROOT / "work" / "redline.json"
OUT_DIR = ROOT / "work" / "redline"
SOURCES = {
    "Amdt7": ROOT / "source" / "Change_Information_CS-E_Amdt_7.pdf",
    "Amdt8": ROOT / "source" / "Change_Information_CS-E_Amdt_8.pdf",
}

RED = 16711680          # #ff0000 text fill -> deleted
WHITE = 16777215        # banner heading text, white on the dark blue bar
BANNER_MIN_SIZE = 14.0
CYAN = (0.0, 1.0, 1.0)  # highlight fill behind inserted text
# Classification is per CHARACTER, not per span. An insertion is usually a few
# words inside an otherwise unchanged black sentence - "listed in the Engine type
# certificate data sheet specified in [point] 21.A.41 [of Part 21]" - and pymupdf
# merges all of that into ONE span because the colour and font never change. A
# per-span overlap test dilutes those few words below any sensible threshold and
# reports the paragraph as unchanged.

ID = r"(?:CS-E|AMC E|GM E)\s*\d{1,4}(?:\([^)\s]{1,6}\))*"
DECLARATIONS = [
    re.compile(rf"^\s*({ID})\s+is\s+(?:amended|created|added|deleted|replaced)\b"),
    re.compile(rf"^\s*The following\s+({ID})\s+is\s+(?:added|created)\b"),
    # No trailing \b after ({ID}): an id ending in ")" has no word boundary
    # before the following space, so \b forces the regex to backtrack and
    # capture "AMC E 740" instead of "AMC E 740(i)(2)".
    re.compile(rf"^\s*Point[^\n]{{0,40}}?\s+is\s+added\s+in\s+({ID})"),
    re.compile(rf"^\s*{ID}\s+is\s+renamed\s+as\s+({ID})"),
]
RUNNING = re.compile(
    r"^(?:CS-E\s*Am(?:dt|endment)"
    r"|Page\s+\d+\s+of\s+\d+"
    r"|Annex to ED Decision)",
    re.IGNORECASE,
)


def norm(text: str) -> str:
    return " ".join(text.split())


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def cyan_rects(page: pymupdf.Page) -> list[pymupdf.Rect]:
    out = []
    for d in page.get_drawings():
        fill = d.get("fill")
        if fill and tuple(round(c, 2) for c in fill) == CYAN:
            out.append(d["rect"])
    return out


def classify_char(char: dict, color: int, highlights: list[pymupdf.Rect]) -> str:
    if color == RED:
        return "deleted"
    bbox = pymupdf.Rect(char["bbox"])
    mid = ((bbox.x0 + bbox.x1) / 2, (bbox.y0 + bbox.y1) / 2)
    for rect in highlights:
        if rect.x0 <= mid[0] <= rect.x1 and rect.y0 <= mid[1] <= rect.y1:
            return "inserted"
    return "unchanged"


def line_runs(line: dict, highlights: list[pymupdf.Rect]) -> list[tuple[str, str]]:
    """Split one line into (class, text) runs at every change of class."""
    runs: list[tuple[str, str]] = []
    for span in line["spans"]:
        for char in span.get("chars", []):
            kind = classify_char(char, span["color"], highlights)
            if runs and runs[-1][0] == kind:
                runs[-1] = (kind, runs[-1][1] + char["c"])
            else:
                runs.append((kind, char["c"]))
    return runs


def merge(runs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    """Join adjacent runs of the same class into readable phrases."""
    out: list[tuple[str, str]] = []
    for kind, text in runs:
        if out and out[-1][0] == kind:
            out[-1] = (kind, f"{out[-1][1]} {text}")
        else:
            out.append((kind, text))
    return [(k, norm(t)) for k, t in out if norm(t)]


def scan(path: Path) -> dict[str, dict]:
    doc = pymupdf.open(path)
    found: dict[str, dict] = {}
    current: str | None = None

    for i in range(len(doc)):
        page = doc[i]
        highlights = cyan_rects(page)
        rows: list[tuple[float, dict]] = []
        for block in page.get_text("rawdict")["blocks"]:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                rows.append((round(line["bbox"][1], 1), line))
        rows.sort(key=lambda r: r[0])

        for _y, line in rows:
            # A paragraph banner switches ownership even without a declaration.
            # EASA sometimes shows a changed paragraph under its banner alone -
            # CS-E 210 on Amdt 7 CI p29 has no "is amended as follows" line - and
            # without this its edits are attributed to the paragraph above it.
            head = line["spans"][0] if line["spans"] else None
            if head and round(head["size"], 1) >= BANNER_MIN_SIZE and head["color"] == WHITE:
                btext = norm("".join(c["c"] for sp in line["spans"]
                                     for c in sp.get("chars", [])))
                # No \b: see the DECLARATIONS note. "AMC E 20(f) Power ..."
                # would otherwise capture "AMC E 20" and invent a change to a
                # paragraph that did not change.
                bm = re.match(rf"^({ID})", btext)
                if bm:
                    current = norm(bm.group(1))
                    found.setdefault(current, {
                        "declaration": f"(shown under its banner: {btext})",
                        "pages": [], "runs": [],
                    })
                    if i + 1 not in found[current]["pages"]:
                        found[current]["pages"].append(i + 1)
                    continue

            runs = line_runs(line, highlights)
            text = norm("".join(t for _k, t in runs))
            if not text or RUNNING.match(text):
                continue

            hit = next((m for p in DECLARATIONS if (m := p.match(text))), None)
            if hit:
                current = norm(hit.group(1))
                found.setdefault(current, {
                    "declaration": text, "pages": [], "runs": [],
                })
                if i + 1 not in found[current]["pages"]:
                    found[current]["pages"].append(i + 1)
                continue

            if current is None:
                continue
            if i + 1 not in found[current]["pages"]:
                found[current]["pages"].append(i + 1)
            # Separate lines with a space WITHOUT breaking class continuity:
            # a block inserted over 20 lines is one insertion, not 20.
            if runs:
                runs[-1] = (runs[-1][0], runs[-1][1] + " ")
            found[current]["runs"].extend(runs)

    for entry in found.values():
        entry["runs"] = merge(entry["runs"])
    return found


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for stale in OUT_DIR.glob("*.md"):
        stale.unlink()

    result: dict[str, dict] = {}
    for amdt, path in SOURCES.items():
        if not path.exists():
            sys.exit(f"missing {path}")
        entries = scan(path)
        print(f"{path.name}: {len(entries)} declared paragraphs")
        for pid, entry in entries.items():
            ins = [t for k, t in entry["runs"] if k == "inserted"]
            dele = [t for k, t in entry["runs"] if k == "deleted"]
            before = norm(" ".join(t for k, t in entry["runs"] if k != "inserted"))
            after = norm(" ".join(t for k, t in entry["runs"] if k != "deleted"))
            key = f"{pid} [{amdt}]"
            result[key] = {
                "id": pid, "amendment": amdt,
                "declaration": entry["declaration"], "pages": entry["pages"],
                "inserted": ins, "deleted": dele,
                "before": before, "after": after,
            }

    OUT_JSON.write_text(json.dumps(result, indent=1, ensure_ascii=False),
                        encoding="utf-8")

    for key, r in result.items():
        f = OUT_DIR / f"{slug(r['id'])}_{r['amendment']}.md"
        lines = [
            f"# {r['id']} — {r['amendment']} redline",
            "",
            f"Declared as: *{r['declaration']}*",
            f"Source: `{SOURCES[r['amendment']].name}` pp {min(r['pages'])}–{max(r['pages'])}",
            "",
            f"## Inserted at {r['amendment']} ({len(r['inserted'])} run(s))",
            "",
        ]
        lines += [f"- {t}" for t in r["inserted"]] or ["_none_"]
        lines += ["", f"## Deleted at {r['amendment']} ({len(r['deleted'])} run(s))", ""]
        lines += [f"- {t}" for t in r["deleted"]] or ["_none_"]
        f.write_text("\n".join(lines) + "\n", encoding="utf-8")

    tot_i = sum(len(r["inserted"]) for r in result.values())
    tot_d = sum(len(r["deleted"]) for r in result.values())
    print(f"\nwrote {OUT_JSON.relative_to(ROOT)} and {len(result)} files in "
          f"{OUT_DIR.relative_to(ROOT)}")
    print(f"{tot_i} inserted runs, {tot_d} deleted runs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
