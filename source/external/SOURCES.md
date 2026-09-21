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
| `Part-21_EAR_Reg-748-2012_Nov-2025.pdf` | 1041 | Easy Access Rules for Initial Airworthiness and Environmental Protection (Regulation (EU) No 748/2012), November 2025 revision | consolidated |
| `AMC-20_Amendment_23.pdf` | 678 | General Acceptable Means of Compliance for Airworthiness of Products, Parts and Appliances (AMC-20), Amendment 23 | 2022/001/R |

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

## Part 21

`Part-21_EAR_Reg-748-2012_Nov-2025.pdf` is EASA's **Easy Access Rules** edition:
1,041 pages interleaving the Annex I (Part 21) Regulation text with its AMC and
GM, produced by EASA eRules. It is the one document that closes every Part 21
reference the vault raises, and it does so because it carries both kinds of
material. Four of the five points are Regulation text, which no AMC & GM
document contains at any amendment.

| Reference | What it gives | Feeds |
|---|---|---|
| `GM1 21.A.3B(b)` | a "DETERMINATION OF AN UNSAFE CONDITION" section | AMC E 510(3)(d)(iii) — the trigger for the whole uncontained-debris assessment |
| `21.A.3A`, `21.A.3B` | occurrence reporting and the failure/malfunction/defect duties | the AMC E 515 Service Management Plan |
| `21.A.20(d)`, with `GM 21.A.20(d)` | the final statement, and what "no feature or characteristics" means in `21.A.20(d)2` | the reason CS-E 160 exists |
| `21.A.61` | instructions for continued airworthiness | CS-E 25(a), whose Amendment 7 change deleted the reference |
| `21.A.801`, `21.A.805`, with `GM1 21.A.805` | identification of products, and the marking rules for critical parts | CS-E 120 |

### Why the three AMC & GM deltas were removed

Three amendment deltas of AMC & GM to Part 21 — Issue 2, Amendments 16, 17 and
18 — were held here briefly and are deleted. Each showed only what its own
amendment changed. Searching all three for every Part 21 reference the vault
raises returned one hit, `GM 21.A.20(d)` in Amendment 17, and this document
carries that too. They are superseded entirely.

They were also the wrong shape for this vault. Reconstructing consolidated text
by stacking deltas runs directly into the failure CLAUDE.md documents under
**Redline marking scheme**: a text-layer extraction merges struck-through and
inserted words into sentences that exist in no amendment. Doing that to
manufacture regulation text is the worst defect class available to a vault whose
guarantee is that every statement traces to a source. The deltas remain in
history at `5c2982f` if they are ever wanted.

## Still missing

| Document | What it blocks |
|---|---|
| **CS-34** | Essentially the whole content of CS-E 1010 and CS-E 1020 — every fuel venting specification, every emissions limit, operating cycle and measurement method — and whether CS-E 1000 makes either mandatory |
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
