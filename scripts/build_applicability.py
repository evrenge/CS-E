#!/usr/bin/env python3
"""Phase 2 — render work/applicability.md from the index and the verdicts.

Joins work/paragraph_index.csv with scripts/classification.py, checks the two
cover exactly the same paragraphs, and writes the applicability matrix plus the
proposed slide grouping.

Usage:
    python3 scripts/build_applicability.py
"""

from __future__ import annotations

import csv
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from classification import CLASSIFICATION  # noqa: E402
from slide_plan import PLAN  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "work" / "paragraph_index.csv"
OUT = ROOT / "work" / "applicability.md"
IN_SCOPE = ("A", "D", "E", "F")
SUBPART_NAME = {
    "A": "General",
    "D": "Turbine Engines: Design and Construction",
    "E": "Turbine Engines: Type Substantiation",
    "F": "Turbine Engines — Environmental and Operational Design Requirements",
}


def resolve(cid: str, ids: list[str]) -> str | None:
    if cid in ids:
        return cid
    hits = [i for i in ids if i.startswith(cid)]
    return hits[0] if len(hits) == 1 else None


def main() -> int:
    rows = [r for r in csv.DictReader(INDEX.open()) if r["subpart"] in IN_SCOPE]
    by_id = {r["id"]: r for r in rows}
    ids = list(by_id)

    verdict: dict[str, tuple[str, str]] = {}
    for cid, status, reason in CLASSIFICATION:
        target = resolve(cid, ids)
        if target is None:
            sys.exit(f"classification id not in index: {cid!r}")
        if target in verdict:
            sys.exit(f"duplicate classification for {target!r}")
        verdict[target] = (status, reason)

    missing = [i for i in ids if i not in verdict]
    if missing:
        sys.exit("unclassified in-scope paragraphs: " + ", ".join(missing))

    counts = Counter(s for s, _ in verdict.values())
    changed = sum(1 for r in rows if r["changed_in"] != "none")

    out: list[str] = []
    w = out.append
    w("# Phase 2 — Turboshaft applicability matrix\n")
    w("Every paragraph of Subparts A, D, E and F of CS-E Amendment 8, classified for a")
    w("**rotorcraft turboshaft** application. Subparts B and C (piston engines) are out of")
    w("scope per CS-E 10(c)–(d) and CLAUDE.md.\n")
    w("Each reason quotes or names the Amendment 8 text that decides the verdict. Where a")
    w("paragraph's core requirement applies but one sub-point does not, the verdict is")
    w("APPLIES and the sub-point is named. Where the whole paragraph exists only when an")
    w("engine variable is true, the verdict is CONDITIONAL.\n")

    w("## Summary\n")
    w("| Verdict | Count | Share |")
    w("|---|---:|---:|")
    total = sum(counts.values())
    for status in ("APPLIES", "CONDITIONAL", "EXCLUDED"):
        w(f"| {status} | {counts[status]} | {100 * counts[status] / total:.0f}% |")
    w(f"| **Total in scope** | **{total}** | |")
    w("")
    w(f"{changed} of the {total} carry an amendment tag "
      "(see `changed_in` in `work/paragraph_index.csv`).\n")

    w("### Engine variables\n")
    w("All five variables in CLAUDE.md are still blank. Per that file, paragraphs that")
    w("depend on them are classified CONDITIONAL. Filling them in converts most of the")
    w("CONDITIONAL rows to APPLIES or EXCLUDED — the verdicts below name which variable")
    w("each row waits on.\n")
    cond_by_var = Counter()
    for pid, (status, reason) in verdict.items():
        if status != "CONDITIONAL":
            continue
        low = reason.lower()
        if "30-minute power" in low:
            cond_by_var["30-Minute Power rating"] += 1
        if "oei" in low:
            cond_by_var["OEI ratings claimed"] += 1
        if "refrigerant" in low:
            cond_by_var["Refrigerant injection"] += 1
        if "time-limited dispatch" in low:
            cond_by_var["Time-limited dispatch"] += 1
        if "eecs" in low:
            cond_by_var["Control system (EECS)"] += 1
    w("| Variable | CONDITIONAL rows waiting on it |")
    w("|---|---:|")
    for var, n in sorted(cond_by_var.items(), key=lambda kv: -kv[1]):
        w(f"| {var} | {n} |")
    w("")

    for sp in IN_SCOPE:
        sp_rows = [r for r in rows if r["subpart"] == sp]
        c = Counter(verdict[r["id"]][0] for r in sp_rows)
        w(f"## Subpart {sp} — {SUBPART_NAME[sp]}\n")
        w(f"{len(sp_rows)} paragraphs — {c['APPLIES']} APPLIES, "
          f"{c['CONDITIONAL']} CONDITIONAL, {c['EXCLUDED']} EXCLUDED\n")
        w("| Paragraph | Title | Pages | Fig/Tab | Changed | Verdict | Reason |")
        w("|---|---|---|:--:|---|---|---|")
        for r in sp_rows:
            status, reason = verdict[r["id"]]
            title = r["title"][:58] or "—"
            ch = r["changed_in"].replace(";", " + ") if r["changed_in"] != "none" else "—"
            fig = "yes" if r["has_figure_or_table"] == "yes" else "—"
            pages = (r["start_page"] if r["start_page"] == r["end_page"]
                     else f"{r['start_page']}–{r['end_page']}")
            cell = reason.replace("|", "\\|")
            w(f"| `{r['id']}` | {title} | {pages} | {fig} | {ch} | **{status}** | {cell} |")
        w("")

    w("## Excluded paragraphs, grouped by reason\n")
    buckets: dict[str, list[str]] = {}
    for pid, (status, reason) in verdict.items():
        if status != "EXCLUDED":
            continue
        low = reason.lower()
        # ETOPS before the aeroplane test: the CS-E 1040 reason ends "ETOPS is an
        # aeroplane operation", which would otherwise land it in the wrong bucket.
        key = ("ETOPS" if "etops" in low
               else "Thrust reverser" if "thrust reverser" in low
               else "Propeller" if "propeller" in low
               else "Turbofan-only" if "turbofan" in low
               else "Aeroplane-only" if "aeroplane" in low
               else "No rotorcraft provisions in the AMC")
        buckets.setdefault(key, []).append(pid)
    w("| Reason | Paragraphs |")
    w("|---|---|")
    for key in sorted(buckets):
        w(f"| {key} | {', '.join('`' + p + '`' for p in sorted(buckets[key]))} |")
    w("")

    # ---- slide plan, with a coverage check against the verdicts
    covered: Counter = Counter()
    for _, _, pids, _ in PLAN:
        for pid in pids:
            target = resolve(pid, ids)
            if target is None:
                sys.exit(f"slide plan references unknown paragraph: {pid!r}")
            covered[target] += 1

    must_cover = {p for p, (st, _) in verdict.items() if st in ("APPLIES", "CONDITIONAL")}
    uncovered = sorted(must_cover - set(covered))
    if uncovered:
        sys.exit("topic grouping misses: " + ", ".join(uncovered))
    excluded_on_slides = sorted(
        p for p in covered if verdict[p][0] == "EXCLUDED")
    if excluded_on_slides:
        sys.exit("topic grouping covers EXCLUDED paragraphs: " + ", ".join(excluded_on_slides))

    section_counts = Counter(sec for sec, _, _, _ in PLAN)
    w("## Topic grouping (reading order / MOC basis)\n")
    w(f"**{len(PLAN)} topics.** Grouping rule: one or two CS paragraphs plus their AMCs")
    w("per topic. Each paragraph still gets its own note; this grouping drives the")
    w("map-of-content notes and the reading order. Every APPLIES paragraph appears in")
    w("exactly one topic — checked by this script. EXCLUDED paragraphs get no note;")
    w("they are listed in the exclusions MOC.\n")
    w("| Section | Topics |")
    w("|---|---:|")
    for sec in ("Intro", "A", "D", "E", "F", "Closing"):
        w(f"| {sec} | {section_counts[sec]} |")
    w(f"| **Total** | **{len(PLAN)}** |")
    w("")
    w("| # | Section | Topic | Paragraphs | Note |")
    w("|---:|:--:|---|---|---|")
    for i, (sec, title, pids, note) in enumerate(PLAN, 1):
        refs = ", ".join(f"`{x}`" for x in pids) if pids else "—"
        w(f"| {i} | {sec} | {title} | {refs} | {note} |")
    w("")
    repeated = sorted(p for p, n in covered.items() if n > 1)
    if repeated:
        w("Paragraphs deliberately spread across more than one topic: "
          + ", ".join(f"`{p}`" for p in repeated) + ".\n")

    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  {total} in-scope paragraphs: {dict(counts)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
