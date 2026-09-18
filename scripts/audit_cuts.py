"""Does every recorded cut correspond to something the source actually says?

`## Not applicable` is the section whose whole job is to let a reader tell
"deliberately excluded" from "forgotten". An entry that records a cut which was
never in the source is worse than a missing entry: it asserts the source
contains material it does not, and a reader checking against the PDF finds
nothing there.

Two checks:

1. **Trigger words.** A cut is justified by a reason -- "the fan", "propeller",
   "piston", "turbofan". If that word appears nowhere in the note's own source
   paragraphs, the entry is describing something else's text. This is how
   AMC E 510 came to record a cut of "the fan" from a paragraph in which the
   word "fan" does not occur.
2. **Sub-point citations.** Every `CS-E nnn(x)(y)` citation anywhere in a note
   is checked against the sub-point labels its target paragraph actually
   carries, so a reference to CS-E 510(a)(5) -- a sub-point that does not exist,
   CS-E 510(a) running (1) to (4) -- is caught rather than followed.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "vault"
PARAS = ROOT / "work" / "paragraphs"

sys.path.insert(0, str(ROOT / "scripts"))

# Words a cut is justified by. Each must occur in the source it is cut from.
TRIGGERS = ["fan", "propeller", "piston", "turbofan", "turbopropeller",
            "thrust reverser", "reverse thrust", "ETOPS", "aeroplane",
            "refrigerant", "supersonic", "turbocharger"]

CITE = re.compile(r"\[((?:CS-E|AMC E) \d{1,4})((?:\([^)\s]{1,6}\))+)[^\]]*\]")


def slug(pid: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", pid).strip("_")


def source_text(ids: list[str]) -> str:
    out = []
    for pid in ids:
        f = PARAS / f"{slug(pid)}.txt"
        if f.exists():
            out.append(f.read_text(encoding="utf-8"))
    return "\n".join(out).lower()


def sub_labels(text: str) -> set[str]:
    """Every sub-point label the paragraph text carries, as it is written."""
    return {m.group(1) for m in re.finditer(r"(?m)^\((\w{1,6})\)\s*$", text)} | {
        m.group(1) for m in re.finditer(r"(?m)^\((\w{1,6})\)\s", text)}


def main() -> int:
    from classification import CLASSIFICATION
    from vault_map import expected_notes
    meta = expected_notes({i: s for i, s, _ in CLASSIFICATION})

    problems = 0
    for note in sorted(VAULT.glob("*.md")):
        text = note.read_text(encoding="utf-8")
        ids = meta.get(note.stem, {}).get("ids", [note.stem])
        src = source_text(ids)
        said: list[str] = []

        if "## Not applicable" in text:
            block = text.split("## Not applicable", 1)[1].split("\n## ", 1)[0]
            for line in block.splitlines():
                if not line.strip().startswith("- "):
                    continue
                low = line.lower()
                for word in TRIGGERS:
                    if word in low and word not in src:
                        said.append(f"records a cut of {word!r}, "
                                    f"which does not occur in its source: "
                                    f"{line.strip()[:90]}")

        # Citations into OTHER paragraphs: check the sub-point exists there.
        for m in CITE.finditer(text):
            target, subs = m.group(1), m.group(2)
            f = PARAS / f"{slug(target)}.txt"
            if not f.exists():
                continue
            labels = sub_labels(f.read_text(encoding="utf-8"))
            first = re.match(r"\((\w{1,6})\)", subs).group(1)
            rest = re.findall(r"\((\w{1,6})\)", subs)
            missing = [p for p in ([first] + rest[1:]) if p not in labels]
            if missing:
                said.append(f"cites {target}{subs} but {', '.join(missing)} "
                            f"is not a sub-point label of {target}")

        for s in sorted(set(said)):
            print(f"  {note.name}: {s}")
            problems += 1

    print(f"\n{problems} problem(s) in {len(list(VAULT.glob('*.md')))} notes")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
