#!/usr/bin/env python3
"""Phase 2b — scope-keyword evidence per in-scope paragraph.

Counts the terms that decide turboshaft applicability in each paragraph of
Subparts A, D, E and F, and captures the first sentence carrying each term so a
classification can cite the text rather than an impression.

Writes work/scope_evidence.json and prints a compact table.

Usage:
    python3 scripts/scope_evidence.py
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "work" / "paragraph_index.csv"
PARAS = ROOT / "work" / "paragraphs"
OUT = ROOT / "work" / "scope_evidence.json"
IN_SCOPE = ("A", "D", "E", "F")

TERMS: dict[str, str] = {
    "aeroplane": r"[Aa]eroplane",
    "propeller": r"[Pp]ropeller",
    "reverser": r"[Tt]hrust [Rr]everser",
    "turbofan": r"[Tt]urbofan|[Bb]y-?pass ratio|[Ff]an [Bb]lade",
    "turbojet": r"[Tt]urbojet",
    "rotorcraft": r"[Rr]otorcraft|[Hh]elicopter",
    "shaft": r"[Tt]urboshaft|[Tt]urbopropeller|[Ss]haft [Pp]ower|Power rating",
    "oei": r"\bOEI\b|One Engine Inoperative|30-Second|2-Minute|2½-Minute|2\.5-[Mm]inute",
    "p30min": r"30-Minute Power",
    "eecs": r"\bEECS\b|Electronic Engine Control|\bFADEC\b",
    "refrigerant": r"[Rr]efrigerant",
    "tld": r"Time-Limited Dispatch|time-limited dispatch|\bTLD\b",
    "etops": r"\bETOPS\b",
    "piston": r"[Pp]iston",
    "thrust": r"\b[Tt]hrust\b",
}
COMPILED = {k: re.compile(v) for k, v in TERMS.items()}
SENTENCE = re.compile(r"[^.!?]*(?:[.!?]|$)")


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def body_of(path: Path) -> str:
    lines = [ln for ln in path.read_text(encoding="utf-8").splitlines()
             if not ln.startswith("#")]
    return " ".join(" ".join(lines).split())


def main() -> int:
    if not INDEX.exists():
        sys.exit("run scripts/build_index.py first")
    rows = [r for r in csv.DictReader(INDEX.open()) if r["subpart"] in IN_SCOPE]

    out = []
    for r in rows:
        path = PARAS / f"{slug(r['id'])}.txt"
        text = body_of(path) if path.exists() else ""
        hits, quotes = {}, {}
        for name, rx in COMPILED.items():
            found = rx.findall(text)
            if found:
                hits[name] = len(found)
                m = rx.search(text)
                sent = next((s.strip() for s in SENTENCE.findall(text[max(0, m.start() - 200):])
                             if rx.search(s)), "")
                quotes[name] = " ".join(sent.split())[:230]
        out.append({
            "id": r["id"], "title": r["title"], "subpart": r["subpart"],
            "pages": f"{r['start_page']}-{r['end_page']}",
            "changed_in": r["changed_in"],
            "figure": r["has_figure_or_table"],
            "words": len(text.split()),
            "hits": hits, "quotes": quotes,
        })

    OUT.write_text(json.dumps(out, indent=1), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(out)} in-scope paragraphs\n")
    cols = list(TERMS)
    print(f"{'id':<22}{'sp':<4}{'words':>6}  " + "".join(c[:5].rjust(6) for c in cols))
    for e in out:
        line = f"{e['id']:<22}{e['subpart']:<4}{e['words']:>6}  "
        line += "".join((str(e["hits"].get(c, "")) or "·").rjust(6) for c in cols)
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
