"""Does every recorded cut, and every sub-point citation, match the source?

Two invariants that `lint_vault.py` cannot see, both of which broke repeatedly
while the vault was being drafted.

1. **A recorded cut must be of text the source contains.** `## Not applicable`
   exists so a reader can tell "deliberately excluded" from "forgotten". An
   entry recording the removal of something the source never said is worse than
   a missing entry: it asserts content into the regulation. AMC E 510 recorded a
   cut of "the fan" from a paragraph in which the word does not occur.

   Only the part of the entry BEFORE the em-dash is tested -- that is the cut.
   The reason after it names other things freely ("thrust reversers are
   aeroplane equipment") and testing it produces nothing but false alarms.

2. **A cited sub-point must exist.** CS-E 860 cited CS-E 510(a)(5) twice for the
   definition of Extremely Remote. CS-E 510(a) runs (1) to (4). A reader
   following that reference lands on nothing.

   Resolving a citation is not a filename lookup: EASA splits its AMC material
   into separate banners, so AMC E 60(d)(5) lives in AMC_E_60_d.txt as "(5)",
   not in AMC_E_60.txt as "(d)(5)". The longest matching banner wins, and the
   remaining labels are looked for inside it.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "vault"
PARAS = ROOT / "work" / "paragraphs"

sys.path.insert(0, str(ROOT / "scripts"))

# A cut names what was cut, and each such word must occur in the source it is
# cut from. The list holds only words that name the OBJECT of a cut. Words that
# usually name the REASON -- "aeroplane", "piston", "turbofan" -- are excluded,
# because a reason may legitimately name something the source never mentions
# ("thrust reversers are aeroplane equipment" is a valid reason to cut a
# paragraph that says neither word).
TRIGGERS = ["fan", "propeller", "refrigerant", "supersonic", "turbocharger",
            "water methanol"]
# "thrust reverser" is deliberately absent. CS-E 510(f)(9) says "thrust
# reversal systems" and AMC E 40(d)(t) says "reverse thrust", so the phrase
# appears in the REASON of almost every entry that cuts them and in the source
# of none: it produces nothing but false alarms.

CITE = re.compile(r"\[((?:CS-E|AMC E)\s\d{1,4})((?:\([^)\s]{1,8}\))+)")
LABEL = re.compile(r"(?m)^\(([^)\s]{1,8})\)")


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def resolve(target: str, subs: list[str]) -> tuple[Path, list[str]] | None:
    """The paragraph file that owns a citation, and the labels still to find.

    Tries the longest banner first: AMC E 790(a)(2)(5)(c) is looked for as
    AMC E 790(a)(2), leaving (5)(c) to find inside it.
    """
    for take in range(len(subs), -1, -1):
        name = target + "".join(f"({s})" for s in subs[:take])
        f = PARAS / f"{slug(name)}.txt"
        if f.exists():
            return f, subs[take:]
    return None


def labels_in(text: str) -> set[str]:
    """Every sub-point label the paragraph text carries, at any depth.

    Depth is not recoverable from the flat text and must not be guessed. The
    slicer leaves a label alone on its line, or runs it into the sentence it
    opens ("(a)(1) It must be established..."), and a body line may also cite a
    sub-point mid-sentence. Only the first two forms are labels, so the text
    after a label must either end the line or start a sentence.

    This deliberately ignores nesting. An earlier version reconstructed the
    hierarchy by bounding each parent at its next sibling, which is unsound:
    "(i)" is both the letter after "(h)" and the first roman numeral, and
    CS-E 50(h) was bounded at its own (h)(1)(i). A check that reports real
    references as broken is worse than one that catches less.
    """
    out = set()
    for line in text.splitlines():
        m = re.match(r"\(([^)\s]{1,8})\)((?:\([^)\s]{1,8}\))*)(?:$|\s+[A-Z])",
                     line.strip())
        if m:
            out.add(m.group(1))
            out.update(re.findall(r"\(([^)\s]{1,8})\)", m.group(2)))
    return out


def main() -> int:
    problems = 0
    notes = sorted(VAULT.glob("*.md"))
    for note in notes:
        text = note.read_text(encoding="utf-8")
        said: list[str] = []

        if "## Not applicable" in text:
            block = text.split("## Not applicable", 1)[1].split("\n## ", 1)[0]
            own = resolve(note.stem, [])
            src = own[0].read_text(encoding="utf-8").lower() if own else ""
            # A merged AMC note owns several files; read them all.
            for f in PARAS.glob(f"{slug(note.stem)}_*.txt"):
                src += f.read_text(encoding="utf-8").lower()
            for line in block.splitlines():
                if not line.strip().startswith("- "):
                    continue
                # An entry reads "- **(ref)** — <what was cut>. <why>." Only
                # the first clause names the cut; the reason names other things
                # freely ("a turboshaft has no fan") and testing it fires on
                # every correctly written entry.
                tail = re.split(r"\s+—\s+", line.strip(), maxsplit=1)
                low = re.split(r"[.;]", tail[-1], maxsplit=1)[0].lower()
                for word in TRIGGERS:
                    # Word boundaries: "fan" must not match inside "turbofan".
                    here = re.search(rf"\b{re.escape(word)}\b", low)
                    there = re.search(rf"\b{re.escape(word)}\b", src)
                    if here and not there:
                        said.append(f"records a cut of {word!r}, which its "
                                    f"source does not contain: {line.strip()[:80]}")

        for m in CITE.finditer(text):
            target = " ".join(m.group(1).split())
            subs = re.findall(r"\(([^)\s]{1,8})\)", m.group(2))
            # AMC E 780 numbers its sections "1.7", not "(1)(7)". A dotted
            # label is that AMC's own style, not a sub-point path.
            if any("." in s for s in subs):
                continue
            got = resolve(target, subs)
            if got is None:
                continue
            f, rest = got
            if not rest:
                continue
            labels = labels_in(f.read_text(encoding="utf-8"))
            missing = [s for s in rest if s not in labels]
            if missing:
                said.append(f"cites {target}{m.group(2)}, but "
                            f"({'), ('.join(missing)}) is not a sub-point "
                            f"label anywhere in {f.stem.replace('_', ' ')}")

        for s in sorted(set(said)):
            print(f"  {note.name}: {s}")
            problems += 1

    print(f"\n{problems} problem(s) across {len(notes)} notes")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
