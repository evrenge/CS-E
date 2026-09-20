# Engine profile

Project input, not derived data. This is the applicant's declared configuration;
it decides applicability for the paragraphs that CS-E scopes by rating or by
system. Change a value here, update `scripts/classification.py`, re-run
`scripts/build_applicability.py`.

Anything a script can recompute does **not** belong in this file or in
`CLAUDE.md` — it belongs in `work/`.

## Application

Rotorcraft turboshaft, multi-engine installation.

## Ratings declared

Mapped onto CS-E Amendment 8 terms. The left column is the applicant's naming.

| Declared | CS-E term | Reference | Notes |
|---|---|---|---|
| Maximum Continuous Power | Maximum Continuous Power | CS-E 40(a) | Mandatory for all Engines |
| Maximum Take-off 5 min | Take-off Power | CS-E 40(a) | Mandatory for all Engines |
| Maximum Take-off 30 min | Rated 30-Minute Power | CS-E 40(b)(4) | Confirmed by applicant |
| OEI 30 sec | 30-Second OEI Power | CS-E 40(b)(3)(i) | Claimed |
| OEI 2 min | 2-Minute OEI Power | CS-E 40(b)(3)(ii) | Claimed |
| OEI Continuous | Continuous OEI Power | CS-E 40(b)(3)(v) | Claimed |
| OEI override | not a rating | CS-E 50 | Control-system feature, confirmed by applicant. Not a CS-E 40 rating |
| Flight Idle, Ground Idle | not a CS-E 40 rating | CS-E 745, CS-E 750 | Operating conditions, not ratings |

**Not claimed:** 2½-Minute OEI Power (CS-E 40(b)(3)(iii)), 30-Minute OEI Power
(CS-E 40(b)(3)(iv)).

### Resolved

- **`Maximum Take-off 30 min`** is CS-E 40(b)(4) Rated 30-Minute Power, confirmed
  by the applicant. AMC E 40(b)(3)(7) defines it as "the approved brake
  horsepower, developed under static conditions at specified altitudes and
  temperatures within the operating limitations established for the Engine, and
  limited in use for periods of no more than 30 minutes".
- **`OEI override`** is a control-system feature, not a declared rating, confirmed
  by the applicant. It is therefore assessed under CS-E 50 / AMC E 50 and the
  CS-E 510 safety analysis, not under CS-E 40 ratings. No CS-E 40 entry.

## Systems

| Variable | Value | Consequence |
|---|---|---|
| Control system | **EECS / FADEC, full authority** | CS-E 50, AMC E 50, AMC E 170 and AMC to CS-E 50(l) fully in play |
| Refrigerant injection | **No** | CS-E 880 EXCLUDED. That paragraph is power augmentation — "Refrigerant Injection Used to Increase ISA Take-off and/or 2½-Minute OEI Performance" — not water ingestion, which is CS-E 790 and does apply |
| Time-limited dispatch | **Not claimed** | CS-E 1030 and AMC E 1030 EXCLUDED. Optional by its own wording: "If approval is sought for dispatch with Faults present in an Electronic Engine Control System (EECS)". Re-openable later without affecting any other paragraph |
| Thrust reverser | **No** | CS-E 890, AMC E 890, AMC E 10(b) EXCLUDED |
| Propeller | **No** — rotor drive | CS-E 180, AMC E 180, CS-E 900 EXCLUDED |

## Endurance test selected by these ratings

30-Second + 2-Minute + Continuous OEI selects **CS-E 740(c)(3)(i)**:

> "If a Continuous OEI Power rating is associated with the 30-Second and 2-Minute
> OEI Power ratings, the following tests must be conducted and must be
> complemented by the additional test of CS-E 740(c)(3)(iii)"

25 six-hour stages, Part 3 being one hour at Maximum Continuous Power followed by
one hour at Continuous OEI Power, plus the additional 2-hour test of
CS-E 740(c)(3)(iii).

Rated 30-Minute Power is claimed, so AMC E 740(c)(2)(i) also applies: the
applicant "may propose either to include the required additional 25 hours within
the" endurance test or run them separately. **[VERIFY]** how those 25 hours
combine with the CS-E 740(c)(3)(i) schedule — the AMC offers a choice and the
selected option should be agreed with EASA.

## What is still to be declared

This file records what the applicant has declared. Many of the vault's open
`[VERIFY]` items ask it for something it does not yet carry — the engine inlet
throat area, the maximum airspeed for normal flight operations, the declared
over-limit ratings, the installation attitude, and the rest.

They are not listed here, because a hand-written copy of a list derived from the
vault goes stale. `review/dead_ends.md`, **Kind 3 — engine information not yet
declared**, is the inventory, and it names the note each item blocks. The single
largest of them is the target rotorcraft and its transmission, which alone
blocks at least nine separate items.

## Effect on the applicability matrix

Filling in the variables above resolves every CONDITIONAL verdict: a paragraph
scoped by a rating or a system either applies to this engine or it does not, and
none is left open.

The counts are derived, so they are not written here — see `work/applicability.md`
for the verdict and the reason behind each one, and `scripts/classification.py`
for the data it is rendered from.
