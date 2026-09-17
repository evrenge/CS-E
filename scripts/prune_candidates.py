#!/usr/bin/env python3
"""Phase 3 prep — find dead-end sub-points inside paragraphs that apply.

Excluding whole paragraphs is not enough: a paragraph that applies often carries
sub-points that cannot apply to a turboshaft (piston ratings, aeroplane-only
schedules, propeller clauses, turbofan cases). This flags them as candidates for
the note's `Dropped` section. It proposes; a human decides.

A line is a candidate when it carries an out-of-scope term. Lines that also carry
a rotorcraft or turboshaft term are reported separately: those usually set the
contrast that defines our case and are kept per the CLAUDE.md pruning rule.

Usage:
    python3 scripts/prune_candidates.py [SUBPART]
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from classification import CLASSIFICATION  # noqa: E402

INDEX = ROOT / "work" / "paragraph_index.csv"
PARAS = ROOT / "work" / "paragraphs"

OUT_OF_SCOPE = {
    "piston": r"\b[Pp]iston\b",
    "aeroplane": r"\b[Aa]eroplane",
    "propeller": r"\b[Pp]ropeller|[Tt]urbo-?propeller|[Tt]urboprop",
    "reverser": r"[Tt]hrust [Rr]everser",
    "turbofan": r"\b[Tt]urbofan|\b[Tt]urbojet|[Bb]y-?pass ratio",
    "supersonic": r"\b[Ss]upersonic",
    "etops": r"\bETOPS\b",
    "refrigerant": r"[Rr]efrigerant",
    "tld": r"[Tt]ime[- ][Ll]imited [Dd]ispatch|\bTLD\b",
    # Only the two-and-a-half minute rating. Must not match plain "2-Minute OEI",
    # which IS claimed - see engine_profile.md.
    "2.5-min OEI": r"2\s*(?:½|1\s*/\s*2|\.5)\s*-?\s*Minute OEI",
    "30-min OEI": r"30-Minute OEI",
}
IN_SCOPE = r"[Rr]otorcraft|[Hh]elicopter|[Tt]urboshaft|free power-turbine"
SUBPOINT = re.compile(r"^\s*(\([a-z0-9ivx]{1,4}\)|\([A-Z]\))")


def main() -> int:
    want = sys.argv[1].upper() if len(sys.argv) > 1 else None
    verdict = {i: s for i, s, _ in CLASSIFICATION}
    rows = [r for r in csv.DictReader(INDEX.open())
            if r["subpart"] in ("A", "D", "E", "F")
            and verdict.get(r["id"], verdict.get(r["id"].split()[0], "")) == "APPLIES"
            and (want is None or r["subpart"] == want)]

    total_cut = total_keep = 0
    for r in rows:
        path = PARAS / (re.sub(r"[^A-Za-z0-9]+", "_", r["id"]).strip("_") + ".txt")
        if not path.exists():
            continue
        lines = [ln.rstrip() for ln in path.read_text().splitlines()
                 if ln.strip() and not ln.startswith("#")]
        cut, keep = [], []
        for n, ln in enumerate(lines, 1):
            hits = [name for name, rx in OUT_OF_SCOPE.items() if re.search(rx, ln)]
            if not hits:
                continue
            marker = SUBPOINT.match(ln)
            entry = (n, ",".join(hits), marker.group(1) if marker else "", ln[:120])
            (keep if re.search(IN_SCOPE, ln) else cut).append(entry)
        if not cut and not keep:
            continue
        print(f"\n{'=' * 100}\n{r['id']} — {r['title']}  (subpart {r['subpart']}, pp {r['start_page']}-{r['end_page']})")
        for n, hits, mark, text in cut:
            print(f"  CUT?  L{n:<4} [{hits}] {mark:<8} {text}")
        for n, hits, mark, text in keep:
            print(f"  KEEP  L{n:<4} [{hits}+rotorcraft] {mark:<8} {text}")
        total_cut += len(cut)
        total_keep += len(keep)

    print(f"\n{'=' * 100}")
    print(f"{len(rows)} notes scanned: {total_cut} cut candidates, "
          f"{total_keep} lines kept for contrast")
    return 0


if __name__ == "__main__":
    sys.exit(main())
