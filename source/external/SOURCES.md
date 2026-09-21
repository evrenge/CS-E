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
| `AMC-GM_Part-21_Issue-2_Amendment_18.pdf` | 18 | AMC & GM to Annex I (Part 21) to Regulation (EU) 748/2012, Issue 2, Amendment 18 | 2026/005/R |

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

## AMC & GM to Part 21 — what this file is not

`AMC-GM_Part-21_Issue-2_Amendment_18.pdf` is an **amendment delta**, not a
consolidated document. Its 18 pages show struck-through and highlighted changes
for `21.A.174` and `21.B.320` to `21.B.326` only. It contains none of the Part 21
material the vault needs, and **Part 21 remains a dead end**:

- `AMC1 21.A.3B(b)` — the definition of "unsafe condition", which the whole
  AMC E 510(3)(d)(iii) uncontained-debris assessment turns on.
- `point 21.A.3` — occurrence reporting, feeding the AMC E 515 Service
  Management Plan.
- `21.A.20(d)2` — the reason CS-E 160 exists.
- `21.A.801(a)`, `21.A.801(b)`, `21.A.805` — what the CS-E 120 marking must
  contain and where it goes.
- `21.A.61(a)` — deleted from CS-E 25(a) at Amendment 7; the amendment history
  says so and cannot say what it required.

Closing those needs the **consolidated** Easy Access Rules for Part 21, or
Annex I to Regulation (EU) 748/2012 itself for the `21.A.8xx` points, which are
Regulation text rather than AMC or GM.

## Still missing

| Document | What it blocks |
|---|---|
| **CS-34** | Essentially the whole content of CS-E 1010 and CS-E 1020 — every fuel venting specification, every emissions limit, operating cycle and measurement method — and whether CS-E 1000 makes either mandatory |
| **Part 21, consolidated** | The five points listed above |
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
