"""Compliance matrix: one row per obligation, exported to deck/compliance_matrix.xlsx.

The vault is the working document; the matrix is what a certification programme
tracks against. It is derived, never hand-edited -- every obligation in it comes
from a `## Requirement` table in a note, so a note and the matrix cannot drift.

Imported obligations do not appear on the Requirements sheet: that sheet is the
1:1 map to CS-E, and CLAUDE.md rule A keeps another document's obligation out of
it. They reach the applicant on the Imports sheet instead, one row per `[ext ...]`
citation, with the document it comes from and the sentence that carries it.

The four right-hand columns of the Requirements sheet are deliberately empty.
They are the applicant's: how compliance is shown, which document shows it, where
it stands, and any remark. Re-running this script rewrites the file and discards
whatever was typed there, which is why the matrix is an export and not a
register. Keep the filled-in copy elsewhere.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "vault"
APPLICABILITY = ROOT / "work" / "applicability.md"
OUT = ROOT / "deck" / "compliance_matrix.xlsx"

sys.path.insert(0, str(ROOT / "scripts"))

STRENGTHS = ["Required", "Required if claimed", "Recommended",
             "Accepted method", "Permitted", "Relief", "Statement"]

HEAD = PatternFill("solid", fgColor="1F3864")
HEAD_FONT = Font(color="FFFFFF", bold=True)
FILLABLE = PatternFill("solid", fgColor="FFF2CC")
VERIFY = re.compile(r"\[VERIFY:\s*", re.S)
EXT_CITE = re.compile(r"\[ext ([^\]]+)\]")


def verify_items(text: str):
    """Every [VERIFY: ...] item, whole.

    A non-greedy match to the first "]" truncates any item containing a
    wikilink or a citation, and most of them do: 13 of the 86 items reached
    the Open items sheet cut off, one of them mid-question. Matching brackets
    by depth is the only way to find the item's real end.

    A bare "[VERIFY]" with no colon is a cross-reference to an item in another
    note, not an item, and is not collected.
    """
    for m in VERIFY.finditer(text):
        depth, i = 1, m.end()
        while i < len(text) and depth:
            if text[i] == "[":
                depth += 1
            elif text[i] == "]":
                depth -= 1
            i += 1
        yield " ".join(text[m.end():i - 1].split())


def strip_markup(cell: str) -> str:
    """Plain text from a table cell: no bold, no wikilinks, no citations kept raw."""
    cell = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", cell)   # [[A|B]] -> B
    cell = re.sub(r"\[\[([^\]]+)\]\]", r"\1", cell)              # [[A]]   -> A
    cell = cell.replace("**", "").replace("`", "")
    return " ".join(cell.split())


def sections(text: str) -> dict[str, str]:
    """`## ` sections of a note, keyed by heading without the marker."""
    out: dict[str, str] = {}
    parts = re.split(r"(?m)^## (.+)$", text)
    for i in range(1, len(parts), 2):
        out[parts[i].strip()] = parts[i + 1]
    return out


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    block = text.split("---\n", 2)[1]
    fm = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def requirement_rows(block: str):
    """(group, ref, obligation, strength) for every obligation table row.

    A `## Requirement` section may hold several tables under `###` headings, and
    it may also hold tables that are not obligation tables at all -- CS-E 920
    compares its two tests, AMC E 850 lists nine service Failure modes, AMC E 620
    sets out Symbol / Meaning / Unit. The header decides: an obligation table
    starts at Ref and ends at Strength. Everything else is prose to a reader and
    noise to the matrix.
    """
    group = ""
    header: list[str] | None = None
    for line in block.splitlines():
        stripped = line.strip()
        if stripped.startswith("### "):
            group, header = stripped[4:].strip(), None
            continue
        if not stripped.startswith("|"):
            header = None
            continue
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):          # the |---|---| rule
            continue
        plain = [strip_markup(c) for c in cells]
        if header is None:
            if plain and plain[0] == "Ref" and plain[-1] == "Strength":
                header = plain
            continue
        if len(plain) != len(header):
            continue
        ref = plain[0]
        strength = plain[-1]
        obligation = " — ".join(c for c in plain[1:-1] if c)
        yield group, ref, obligation, strength


def accepted_means(text: str) -> str:
    m = re.search(r"(?m)^(?:Accepted means|Specification):\s*(.+)$", text)
    return strip_markup(m.group(1)) if m else ""


def not_applicable_rows(block: str):
    for line in block.splitlines():
        if not line.strip().startswith("- "):
            continue
        item = line.strip()[2:]
        refs = re.findall(r"\*\*(.+?)\*\*", item)
        reason = strip_markup(re.sub(r"^.*?—\s*", "", item, count=1))
        yield ", ".join(refs) or "—", reason


def excluded_paragraphs():
    """The EXCLUDED verdicts, read from work/applicability.md."""
    if not APPLICABILITY.exists():
        return
    for line in APPLICABILITY.read_text(encoding="utf-8").splitlines():
        if "**EXCLUDED**" not in line or not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 7:
            continue
        yield strip_markup(cells[0]), strip_markup(cells[1]), strip_markup(cells[6])


def sheet(wb, title, headers, rows, widths, fill_from=None, wrap=()):
    ws = wb.create_sheet(title) if wb.sheetnames != ["Sheet"] else wb.active
    ws.title = title
    ws.append(headers)
    for c in ws[1]:
        c.fill, c.font = HEAD, HEAD_FONT
        c.alignment = Alignment(vertical="center", wrap_text=True)
    for row in rows:
        ws.append(list(row))
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w
    for i in wrap:
        for row in ws.iter_rows(min_row=2, min_col=i, max_col=i):
            row[0].alignment = Alignment(vertical="top", wrap_text=True)
    for row in ws.iter_rows(min_row=2):
        for c in row:
            if c.alignment.wrap_text is not True:
                c.alignment = Alignment(vertical="top")
    if fill_from:
        for row in ws.iter_rows(min_row=2, min_col=fill_from):
            for c in row:
                c.fill = FILLABLE
    ws.freeze_panes = "A2"
    if len(rows):
        ws.auto_filter.ref = f"A1:{get_column_letter(len(headers))}{len(rows) + 1}"
    ws.row_dimensions[1].height = 30
    return ws


def main() -> int:
    from classification import CLASSIFICATION
    from vault_map import expected_notes
    # One authority for which document an [ext ...] id belongs to: the linter
    # builds it from the slices in work/external/, and a second copy here would
    # drift the first time a document is added.
    from lint_vault import ext_document
    meta = expected_notes({i: s for i, s, _ in CLASSIFICATION})

    def order(note: Path) -> tuple:
        """Source order, not filename order.

        Sorting the sheets by filename puts AMC E 1000 first and CS-E 15 after
        CS-E 140. A certification reader walks the specification in the order
        EASA wrote it, so the matrix does too: subpart, then first page, then the
        CS paragraph ahead of the AMC that serves it.
        """
        fm = frontmatter(note.read_text(encoding="utf-8"))
        # Keyed by NOTE name, not by the frontmatter id: a merged AMC note is
        # named "AMC E 740" while the index knows only its constituents,
        # "AMC E 740(c)(3)" and the rest, so an index lookup misses it and the
        # note sorts to the end of its subpart.
        page = meta[note.stem]["start"] if note.stem in meta else 9999
        # The paragraph number breaks a page tie: four Subpart F paragraphs open
        # on page 252, and without it CS-E 1020 sorts ahead of AMC E 1000.
        m = re.search(r"(\d{1,4})", note.stem)
        num = int(m.group(1)) if m else 0
        return (fm.get("subpart", "Z"), page, num,
                0 if fm.get("type") == "CS" else 1, note.stem)

    reqs, comps, opens, nas, imports = [], [], [], [], []
    for note in sorted(VAULT.glob("*.md"), key=order):
        text = note.read_text(encoding="utf-8")
        fm = frontmatter(text)
        sec = sections(text)
        name = note.stem
        subpart = fm.get("subpart", "")
        ntype = fm.get("type", "")
        changed = fm.get("changed_in", "[]").strip("[]").replace('"', "") or "—"
        means = accepted_means(sec.get("References", ""))
        pages = fm.get("pages", "")

        for group, ref, obligation, strength in requirement_rows(sec.get("Requirement", "")):
            if strength not in STRENGTHS:
                print(f"  ! {name}: strength {strength!r} is not one of the seven")
            reqs.append([subpart, name, ntype, pages, group, ref, obligation,
                         strength, changed, means, "", "", "", ""])

        for line in sec.get("Compliance", "").splitlines():
            if line.strip().startswith("- "):
                item = line.strip()[2:]
                cite = " ".join(re.findall(r"\[((?:CS-E|AMC E)[^\]]*)\]", item))
                imported = " · ".join(f"[ext {c}]" for c in EXT_CITE.findall(item))
                body = re.sub(r"\[(?:CS-E|AMC E)[^\]]*\]", "", item)
                comps.append([subpart, name,
                              strip_markup(body).rstrip(" ."), cite, imported])

        # Rule A keeps an import off the Requirements sheet, so this is the only
        # place it reaches the applicant. Every section is scanned, because an
        # import is as likely to sit in the applicability prose as in a
        # compliance bullet.
        for section, block in sec.items():
            for line in block.splitlines():
                ids = EXT_CITE.findall(line)
                if not ids:
                    continue
                sentence = strip_markup(re.sub(r"^\s*[-*]\s*", "", line))
                for cid in ids:
                    doc, _ = ext_document(cid.strip())
                    imports.append([subpart, name, section, doc or "?",
                                    cid.strip(), sentence])

        for item in verify_items(text):
            opens.append([subpart, name, item])

        for ref, reason in not_applicable_rows(sec.get("Not applicable", "")):
            nas.append([subpart, name, ref, reason])

    # The external notes carry open items too, and they are the applicant's in
    # exactly the same way: an emissions note wording to agree, an airframe code
    # to fix. They are not CS-E paragraphs, so nothing else on this sheet reads
    # them, and without this they reach no deliverable at all.
    for note in sorted((VAULT / "external").glob("*.md")):
        for item in verify_items(note.read_text(encoding="utf-8")):
            opens.append(["EXT", note.stem, item])

    wb = Workbook()

    sheet(wb, "Requirements",
          ["Subpart", "Note", "Type", "Pages", "Group", "Ref", "Obligation",
           "Strength", "Changed at", "Accepted means",
           "Compliance method", "Evidence reference", "Status", "Remarks"],
          reqs,
          [8, 16, 6, 9, 26, 14, 88, 18, 11, 30, 22, 24, 12, 30],
          fill_from=11, wrap=(7, 10, 11, 12, 14))

    sheet(wb, "Compliance items",
          ["Subpart", "Note", "What must be produced", "Citation",
           "Imported from"],
          comps, [8, 16, 100, 26, 26], wrap=(3, 4, 5))

    sheet(wb, "Imports",
          ["Subpart", "Note", "Section", "Document", "Paragraph",
           "What it says"],
          imports, [8, 16, 26, 16, 20, 96], wrap=(6,))

    sheet(wb, "Open items",
          ["Subpart", "Note", "VERIFY"],
          opens, [8, 16, 120], wrap=(3,))

    sheet(wb, "Pruned sub-points",
          ["Subpart", "Note", "Ref", "Reason for the cut"],
          nas, [8, 16, 26, 96], wrap=(4,))

    sheet(wb, "Excluded paragraphs",
          ["Paragraph", "Title", "Reason"],
          list(excluded_paragraphs()), [16, 44, 110], wrap=(3,))

    by_strength = [[s, sum(1 for r in reqs if r[7] == s)] for s in STRENGTHS]
    by_subpart = [[sp, len({r[1] for r in reqs if r[0] == sp}),
                   sum(1 for r in reqs if r[0] == sp)]
                  for sp in sorted({r[0] for r in reqs})]
    summary = ([["Notes", len(list(VAULT.glob('*.md'))), ""],
                ["Obligations", len(reqs), ""],
                ["Compliance items", len(comps), ""],
                ["Open VERIFY items", len(opens), ""],
                ["Pruned sub-points", len(nas), ""],
                ["Imported obligations", len(imports), ""],
                ["Excluded paragraphs", len(list(excluded_paragraphs())), ""],
                ["", "", ""],
                ["By obligation strength", "", ""]]
               + [[s, n, ""] for s, n in by_strength]
               + [["", "", ""], ["By subpart", "notes", "obligations"]]
               + by_subpart)
    ws = sheet(wb, "Summary", ["", "", ""], summary, [30, 14, 14])
    ws.auto_filter.ref = None
    for r in ws.iter_rows(min_row=2, max_col=1):
        if r[0].value in ("By obligation strength", "By subpart"):
            r[0].font = Font(bold=True)

    wb.move_sheet("Summary", offset=-len(wb.sheetnames) + 1)
    OUT.parent.mkdir(exist_ok=True)
    wb.save(OUT)

    print(f"wrote {OUT.relative_to(ROOT)}")
    print(f"  {len(reqs)} obligations from {len({r[1] for r in reqs})} notes")
    print(f"  {len(comps)} compliance items, {len(opens)} open VERIFY items, "
          f"{len(nas)} pruned sub-points")
    if imports:
        docs = sorted({r[3] for r in imports})
        print(f"  {len(imports)} imported obligation(s) from {', '.join(docs)}")
    missing = sorted({n.stem for n in VAULT.glob('*.md')} - {r[1] for r in reqs})
    if missing:
        print(f"  ! no obligation rows parsed from: {', '.join(missing)}")
        return 1
    unknown = sorted({r[7] for r in reqs} - set(STRENGTHS))
    return 1 if unknown else 0


if __name__ == "__main__":
    raise SystemExit(main())
