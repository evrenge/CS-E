# External reference documents

Documents CS-E cites and does not contain. They are **not** a source of CS-E
requirement content — `source/CS-E_Amendment_8.pdf` remains the only authority
for that, per CLAUDE.md. These answer their own questions: what CS-27 or CS-29
asks of the rotorcraft, what a term in CS-Definitions means, what the AMC 20
series accepts as a means of compliance.

Read-only, checksum-pinned, and **not tracked across amendments**. The version
here is the version the vault was written against; if a newer amendment matters
later, that is when change tracking starts. This is deliberate: the amendment
machinery in `source/` exists because CS-E is the deliverable, and these are not.

| File | Pages | Document | ED Decision |
|---|---:|---|---|
| `CS-27_Amendment_10.pdf` | 322 | Easy Access Rules for Small Rotorcraft (CS-27), Amendment 10 | 2023/001/R |
| `CS-29_Amendment_12.pdf` | 438 | Large Rotorcraft (CS-29), Amendment 12 | 2024/009/R |
| `CS-Definitions_Amendment_2.pdf` | 26 | Definitions and abbreviations used in Certification Specifications, Amendment 2 | 2010/014/R |
| `AMC-20_Amendment_23.pdf` | 678 | General Acceptable Means of Compliance for Airworthiness of Products, Parts and Appliances (AMC-20), Amendment 23 | 2022/001/R |
| `AMC-GM_Part-21_Issue-2_Amendment_16.pdf` | 146 | AMC & GM to Annex I (Part 21) to Regulation (EU) 748/2012, Issue 2, Amendment 16 | 2023/014/R |
| `AMC-GM_Part-21_Issue-2_Amendment_17.pdf` | 34 | …Issue 2, Amendment 17 | 2025/016/R |
| `AMC-GM_Part-21_Issue-2_Amendment_18.pdf` | 18 | …Issue 2, Amendment 18 | 2026/005/R |

All carry `/Author = EASA` except CS-Definitions Amendment 2 (`EASA - RPS`).
Metadata was checked against the first page of each file.

## What each one unblocks

Checked by searching the extracted text of every file for each reference the
vault raises. `review/dead_ends.md` is the inventory those references come from.

| Document | Dead ends it closes |
|---|---|
| **CS-27** | `CS-27.45(f)` power availability, behind AMC E 20(f)(1). `CS 27.1093(b)` ice protection, behind CS-E 780(a)(2). Also the CS-27-or-CS-29 question in CS-E 20(b) and CS-E 30 |
| **CS-29** | `CS-29.45(f)` and `CS 29.1093(b)`, the CS-29 side of the same two |
| **CS-Definitions** | `Fire-resistant` and `Fireproof`, which CS-E 130 turns on and CS-E 15(a) defers twice. `Icing Atmospheric Conditions`, behind CS-E 780(a)(2) |
| **AMC-20** | `AMC 20-1`, `AMC 20-3` (CS-E 50 for an EECS, and AMC E 80 Table 2 item 18, which names no alternative at all), `AMC 20-42` (the whole CS-E 50(l) security method), `AMC 20-115`, and `AMC 25.1309` cited by AMC E 510(5) |

## AMC & GM to Part 21 — three deltas, and why they do not close it

All three Part 21 files are **amendment deltas**, not consolidated documents.
Each shows only what its own amendment changed, struck through and highlighted:

| File | Touches |
|---|---|
| Amendment 16 | production and design organisation material — 21.A.4, 21.A.122 to 21.A.147, 21.A.263, 21.A.433, 21.B.130 to 21.B.220 |
| Amendment 17 | 21.A.14, 21.A.130, 21.A.165, 21.A.239, 21.A.243, 21.A.263, 21.A.432C, 21.A.15, **GM 21.A.20(d)**, 21.A.249, 21.A.265, 21.A.435, 21.A.701, 21.B.100 |
| Amendment 18 | 21.A.174 and 21.B.320 to 21.B.326 only |

Searching all three for every Part 21 reference the vault raises returns one hit:
`GM 21.A.20(d)` in Amendment 17, which explains what "No feature or
characteristics" means in point `21.A.20(d)2`. That is guidance on the point
CS-E 160 defers to, not the Regulation text of the point itself. Useful context;
not the answer.

Everything else is absent. `21.A.3B` does not occur in any of the three, so
`AMC1 21.A.3B(b)` — the definition of "unsafe condition" — is not here. The
"unsafe condition" wording that does appear in Amendment 16 is incidental, in
production-organisation reporting duties under 21.A.3A.

**Part 21 remains a dead end:**

- `AMC1 21.A.3B(b)` — the definition of "unsafe condition", which the whole
  AMC E 510(3)(d)(iii) uncontained-debris assessment turns on.
- `point 21.A.3` — occurrence reporting, feeding the AMC E 515 Service
  Management Plan.
- `21.A.20(d)2` — the reason CS-E 160 exists.
- `21.A.801(a)`, `21.A.801(b)`, `21.A.805` — what the CS-E 120 marking must
  contain and where it goes.
- `21.A.61(a)` — deleted from CS-E 25(a) at Amendment 7; the amendment history
  says so and cannot say what it required.

One download closes all five: the **Easy Access Rules for Part 21**, EASA's
consolidated edition, which interleaves the Annex I Regulation text with the AMC
and GM. No AMC & GM amendment of any number can do it, for two reasons that
compound. `AMC1 21.A.3B(b)` is AMC material but none of amendments 16 to 18
touched it, so no delta carries it. And `21.A.20(d)2`, `21.A.61(a)`, `21.A.801`
and `21.A.805` are **Regulation** text — Annex I to Commission Regulation (EU)
No 748/2012 — which an AMC & GM document does not contain at any amendment,
consolidated or not.

These three are kept as context rather than deleted. They can go once the
consolidated edition arrives, which supersedes all of them for this purpose.

## Still missing

| Document | What it blocks |
|---|---|
| **CS-34** | Essentially the whole content of CS-E 1010 and CS-E 1020 — every fuel venting specification, every emissions limit, operating cycle and measurement method — and whether CS-E 1000 makes either mandatory |
| **Easy Access Rules for Part 21** (consolidated) | The five points listed above. Free EASA download; supersedes the three deltas held here |
| **EUROCAE ED-14 / RTCA DO-160** | The test procedure for 15 of the 19 items in AMC E 80 Table 2 |
| **ISO 2685** | The fire test standard behind AMC E 130 — flame definition, temperature, duration |
| **FAA AC 33.70-2, AC 33.70-3** | Damage tolerance methods named by AMC E 515 |
| **SAE ARP4754A / EUROCAE ED-79A**, "Systematic Safety" (Lloyd & Tye) | Reference documents in AMC E 510(5) |

The last four are industry standards behind a paywall; the first two are free
EASA downloads.

## Provenance rule

Same as `source/`: do not substitute a mirror or a third-party copy, and do not
re-save these PDFs. Verify with `sha256sum -c CHECKSUMS.sha256` from this
directory.
