#!/usr/bin/env python3
"""Download the five EASA CS-E source PDFs into source/.

Standard library only. EASA rotates the numeric IDs behind
/en/downloads/<id>/en whenever a document is republished, so every target is
resolved by scraping its document-library landing page for a link whose anchor
text matches a pattern. A target may also declare a direct URL, which is tried
first and falls back to scraping.

Usage:
    python3 scripts/fetch_sources.py            # fetch anything missing
    python3 scripts/fetch_sources.py --force    # re-fetch everything
    python3 scripts/fetch_sources.py --check    # verify against CHECKSUMS.sha256
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

BASE = "https://www.easa.europa.eu"
SOURCE_DIR = Path(__file__).resolve().parent.parent / "source"
UA = "Mozilla/5.0 (X11; Linux x86_64) cs-e-deck/fetch_sources.py"
TIMEOUT = 60

CS_E_8 = f"{BASE}/en/document-library/certification-specifications/cs-e-amendment-8"
CS_E_7 = f"{BASE}/en/document-library/certification-specifications/cs-e-amendment-7"


@dataclass
class Target:
    filename: str
    landing: str
    # Matched case-insensitively against the anchor text on the landing page.
    anchor_pattern: str
    direct: str | None = None
    fallbacks: list[str] = field(default_factory=list)


TARGETS: list[Target] = [
    Target(
        filename="CS-E_Amendment_8.pdf",
        landing=CS_E_8,
        anchor_pattern=r"CS-E\s*[—-]?\s*Amendment\s*8",
    ),
    Target(
        filename="Change_Information_CS-E_Amdt_8.pdf",
        landing=CS_E_8,
        anchor_pattern=r"change\s*information",
    ),
    Target(
        filename="CS-E_Amendment_7.pdf",
        landing=CS_E_7,
        anchor_pattern=r"CS-E\s*[\u2014-]?\s*Amendment\s*7",
    ),
    Target(
        filename="Change_Information_CS-E_Amdt_7.pdf",
        landing=CS_E_7,
        anchor_pattern=r"change\s*information",
        fallbacks=[f"{BASE}/sites/default/files/dfu/change_information_-_cs-e_amendment_7.pdf"],
    ),
    Target(
        filename="EN_to_ED_Decision_2025-003-R.pdf",
        landing=CS_E_8,
        anchor_pattern=r"explanatory\s*note",
        direct=f"{BASE}/en/downloads/141876/en",
    ),
]

ANCHOR_RE = re.compile(
    r'<a\b[^>]*\bhref\s*=\s*["\']([^"\']+)["\'][^>]*>(.*?)</a>',
    re.IGNORECASE | re.DOTALL,
)
TAG_RE = re.compile(r"<[^>]+>")


def _open(url: str) -> tuple[bytes, str]:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return resp.read(), resp.headers.get("Content-Type", "")


def _text(fragment: str) -> str:
    return " ".join(TAG_RE.sub(" ", fragment).split())


def resolve(target: Target) -> list[str]:
    """Return candidate download URLs, best first."""
    candidates: list[str] = []
    if target.direct:
        candidates.append(target.direct)

    try:
        html = _open(target.landing)[0].decode("utf-8", "replace")
    except (urllib.error.URLError, OSError) as exc:
        print(f"  ! landing page unreachable ({exc}); using declared URLs only")
        return candidates + target.fallbacks

    pattern = re.compile(target.anchor_pattern, re.IGNORECASE)
    for href, inner in ANCHOR_RE.findall(html):
        label = _text(inner)
        if not pattern.search(label):
            continue
        url = urllib.parse.urljoin(target.landing, href)
        if "/downloads/" in url or url.lower().endswith(".pdf"):
            if url not in candidates:
                candidates.append(url)

    return candidates + [u for u in target.fallbacks if u not in candidates]


def read_checksums() -> dict[str, str]:
    """Parse source/CHECKSUMS.sha256 into {filename: sha256}."""
    path = SOURCE_DIR / "CHECKSUMS.sha256"
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    for line in path.read_text().splitlines():
        parts = line.split()
        if len(parts) == 2:
            out[parts[1].lstrip("*")] = parts[0]
    return out


def fetch(target: Target, force: bool) -> bool:
    dest = SOURCE_DIR / target.filename
    if dest.exists() and not force:
        print(f"= {target.filename} (present, {dest.stat().st_size:,} B)")
        return True

    print(f"> {target.filename}")
    for url in resolve(target):
        try:
            payload, ctype = _open(url)
        except (urllib.error.URLError, OSError) as exc:
            print(f"  ! {url} -> {exc}")
            continue
        if not payload.startswith(b"%PDF"):
            print(f"  ! {url} -> not a PDF (Content-Type: {ctype or 'unknown'})")
            continue
        dest.write_bytes(payload)
        digest = hashlib.sha256(payload).hexdigest()
        print(f"  ok {url}")
        print(f"     {len(payload):,} B  sha256:{digest}")
        return True

    print(f"  FAILED: no usable download for {target.filename}")
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--force", action="store_true", help="re-download existing files")
    ap.add_argument("--check", action="store_true", help="verify against CHECKSUMS.sha256")
    args = ap.parse_args()

    SOURCE_DIR.mkdir(parents=True, exist_ok=True)

    if args.check:
        expected = read_checksums()
        bad = 0
        for t in TARGETS:
            p = SOURCE_DIR / t.filename
            if not p.exists():
                print(f"x {t.filename}  MISSING")
                bad += 1
                continue
            digest = hashlib.sha256(p.read_bytes()).hexdigest()
            want = expected.get(t.filename)
            if want is None:
                status = "no recorded checksum"
            elif want == digest:
                status = "OK"
            else:
                status = f"MISMATCH (expected {want[:16]}...)"
                bad += 1
            print(f"= {t.filename}  {p.stat().st_size:,} B  sha256:{digest[:16]}...  {status}")
        return 1 if bad else 0

    failures = [t.filename for t in TARGETS if not fetch(t, args.force)]
    if failures:
        print("\nUnresolved:", ", ".join(failures))
        print("Resolve manually from the landing pages listed in source/SOURCES.md.")
        return 1
    print("\nAll source documents present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
