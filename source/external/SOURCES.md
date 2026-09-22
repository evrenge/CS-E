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
| `EN_to_ED_Decision_2025-005-R_CS-34-repeal.pdf` | 6 | Explanatory Note to ED Decision 2025/005/R — repeal of CS-34, CS-36 and CS-CO2 | 2025/005/R |
| `CS-34_Amendment_4_repealed.pdf` | 5 | Aircraft Engine Emissions and Fuel Venting (CS-34), Amendment 4 — **repealed May 2025** (the day, 27 May, is EASA's publication listing, not the decision's own text) | 2021/011/R |
| `AMC-20_Amendment_23.pdf` | 678 | General Acceptable Means of Compliance for Airworthiness of Products, Parts and Appliances (AMC-20), Amendment 23 | 2022/001/R |

All carry `/Author = EASA` except CS-Definitions Amendment 2 (`EASA - RPS`).
Metadata was checked against the first page of each file.

## How a note reads one of these

`scripts/external_paragraphs.py` slices the points the vault cites into
`work/external/`, one file each, so a quotation from CS-29 or Part 21 is checked
word-for-word the way a CS-E quotation is. The note cites it as `[ext <id>]` and
declares the document in its `imports:` frontmatter; `CLAUDE.md`, **Imported
obligations**, has the five rules. Adding a point means adding a line to that
script's `WANTED` table, not changing code.

Its docstring records the extraction defects that had to be fixed to make the
slices trustworthy. Each one produced plausible text for the wrong paragraph
rather than failing, which is why every slice is checked to open with the
heading it claims.

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
material. Most of the points the table below lists are Regulation text, which no
AMC & GM document contains at any amendment.

| Reference | What it gives | Feeds |
|---|---|---|
| `GM1 21.A.3B(b)` | a "DETERMINATION OF AN UNSAFE CONDITION" section | AMC E 510(3)(d)(iii) — the trigger for the whole uncontained-debris assessment |
| `21.A.3A`, `21.A.3B` | occurrence reporting and the failure/malfunction/defect duties | the AMC E 515 Service Management Plan |
| `21.A.20(d)`, with `GM 21.A.20(d)` | the final statement, and what "no feature or characteristics" means in `21.A.20(d)2` | the reason CS-E 160 exists |
| `21.A.61` | **not held, and not holdable** — the point no longer exists in Part 21. The numbering runs 21.A.62 then 21.A.65, and an exact search returns nothing; a substring search appears to find it only because 21.A.601 to 21.A.615 exist. CS-E 25(a) cited `21.A.61(a)` until Amendment 7 deleted the reference, and Part 21 has since dropped the point itself. The instructions for continued airworthiness duty is now `21.A.7` | CS-E 25(a) amendment history |
| `21.A.7` | who receives the instructions for continued airworthiness, and when | CS-E 25 |
| `21.A.33` | the conformity machinery before a certification test | AMC E 650(15) |
| `21.A.41` | what a type certificate includes | CS-E 40(e) |
| `21.A.21`, `21.A.20`, `21.B.85`, with `GM1 21.B.85(a)` and `GM2 21.B.85` | the environmental protection chain, from CS-34 to the SARPs of ICAO Annex 16 | CS-E 1010 and CS-E 1020, through the `CS 34.1` and `CS 34.2` notes |
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

## CS-34 — repealed, and it never held the content anyway

`CS-34_Amendment_4_repealed.pdf` is five pages, of which two are a table of
contents and a preamble listing past amendments. Its entire normative content is
two sentences:

> **CS 34.1 Fuel venting.** "The aircraft must be designed to comply with the
> applicable fuel venting requirements as specified in point 21.A.21 of Annex I
> (Part 21) to Commission Regulation (EU) No 748/2012."
>
> **CS 34.2 Aircraft engine emissions.** "The aircraft engine must be designed to
> comply with the applicable emissions requirements as specified in point
> 21.A.21 of Annex I (Part 21) to Commission Regulation (EU) No 748/2012."

It contains no limit, no operating cycle, no measurement method and no test. It
is a redirect. `GM1 34.1` and `GM1 34.2` say where the redirect goes: 21.A.21
does not list the requirements either, but refers to 21.A.20, which requires
compliance with the environmental protection requirements "designated by the
Agency in accordance with point 21.B.85".

EASA repealed CS-34, CS-36 and CS-CO2 in May 2025, weeks after
CS-E Amendment 8 was issued, "to prevent the future use of and reference to
CS-34, CS-36 and CS-CO2 and any potential confusion with the applicable
environmental protection requirements referred to in the first subparagraph of
Article 9(2) of Regulation (EU) 2018/1139". Removing a pure indirection is
consistent with what the document turns out to be. CS-E Amendment 8 still cites
`CS 34.1` and `CS 34.2` by name, which is why the file is kept.

### The chain resolves inside the Part 21 file

Every step after CS-34 is in `Part-21_EAR_Reg-748-2012_Nov-2025.pdf`:

| Step | Says |
|---|---|
| `21.B.85(a)`, per Regulation (EU) 2025/1065 | "the Agency shall designate and notify to the applicant the applicable environmental protection requirements from the essential requirements referred to in the first subparagraph of Article 9(2) of Regulation (EU) 2018/1139" — the same phrase the repeal decision uses |
| `GM2 21.B.85` | those requirements are the SARPs in Volumes I, II and III of ICAO Annex 16 |
| `GM1 21.B.85(a)` | Volume II Part II, **fuel venting**, "applies to turbine engine powered aircraft manufactured after 18 February 1982" |
| `GM1 21.B.85(a)` | Volume II Part III, **engine emissions**, "applies to the aircraft engine emissions certification for turbojet and turbofan engines intended for the propulsion at subsonic and supersonic speeds" |

The 21.B.85 material carries Regulation (EU) 2025/1065 and ED Decision
2025/016/R, so it post-dates the CS-34 repeal. It is the live successor.

### EASA's own account of the repeal

`EN_to_ED_Decision_2025-005-R_CS-34-repeal.pdf` is the explanatory note, and it
states the position directly. Of CS-34, CS-36 and CS-CO2:

> "These CSs contained **neither certification specifications nor the applicable
> environmental protection requirements**."

They were issued only to carry AMC pointing at the appendices to ICAO Annex 16,
which at the time sat outside the essential requirements. Under the first
subparagraph of Article 9(2) of Regulation (EU) 2018/1139 those appendices are
now "an integral part of the essential requirements", so the pointer had nothing
left to do. The note confirms that CS-34 Amendment 4 "only refer[s] to the
requirements in Annex I (Part 21)", and that Regulation (EU) No 748/2012 "does
not refer to environmental protection certification specifications that should
be used as a basis for the environmental protection certification of a product".

It also says where compliance is recorded:

> "The relevant records of compliance with the applicable environmental
> protection requirements are the applicable chapters of ICAO Annex 16
> Volumes I, II and III, and the applicable amendment level of those volumes."

### A conflict this creates inside CS-E Amendment 8

`AMC E 1020(1)` prescribes a type certificate data sheet note in a fixed format:

> "Engine (type/model) complies with CS-34 amendment (number)."

The explanatory note says the opposite of what that note would achieve:

> "Current references to CS-34, CS-36 and CS-CO2 in type-certificate data sheets
> (TCDSs) and type-certificate data sheets for noise (TCDSNs) **do not constitute
> records of compliance** with the applicable environmental protection
> requirements."

So the accepted means in CS-E Amendment 8, issued April 2025, prescribes a TCDS
entry that EASA declared in May 2025 is not a compliance record. Existing data
sheets are untouched — the note says their revision "is not considered
necessary" — but an applicant certifying now cannot follow AMC E 1020(1)
literally and produce a valid record. The substitute is the ICAO Annex 16
volume, chapter and amendment level.

This is recorded, not acted on. Changing what `AMC E 1020` tells a reader to do
means writing note content from a document that is not CS-E, which needs the
Source of truth rule amended first.

### An open scope question this raises

Volume II Part III is stated to apply to **turbojet and turbofan** engines. A
turboshaft is neither. If that holds, CS-E 1020 may not reach this engine at
all, and CS-E 1000's conditional — compliance with CS-E 1010 and CS-E 1020 "may
be mandatory … depending on the specifications referenced under CS-34" —
resolves differently from what the vault currently assumes. Fuel venting is not
affected: Part II reaches any turbine engine powered aircraft, which includes a
rotorcraft.

This is not yet a finding. It rests on a GM sentence describing Annex 16 rather
than on Annex 16 itself, and **ICAO Annex 16 Volume II is not held**. Settling
it needs that document. Nothing in the vault has been changed on the strength of
it.

## Still missing

| Document | What it blocks |
|---|---|
| **ICAO Annex 16, Volume II** | The actual fuel venting and engine emissions SARPs, at the end of the CS-34 chain. Also settles whether Part III reaches a turboshaft at all. Not an EASA document — published by ICAO |
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
