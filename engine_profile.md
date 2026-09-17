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
| Maximum Take-off 30 min | Rated 30-Minute Power | CS-E 40(b)(4) | **[VERIFY]** — see below |
| OEI 30 sec | 30-Second OEI Power | CS-E 40(b)(3)(i) | Claimed |
| OEI 2 min | 2-Minute OEI Power | CS-E 40(b)(3)(ii) | Claimed |
| OEI Continuous | Continuous OEI Power | CS-E 40(b)(3)(v) | Claimed |
| OEI override | no CS-E 40 equivalent | — | **[VERIFY]** — see below |
| Flight Idle, Ground Idle | not a CS-E 40 rating | CS-E 745, CS-E 750 | Operating conditions, not ratings |

**Not claimed:** 2½-Minute OEI Power (CS-E 40(b)(3)(iii)), 30-Minute OEI Power
(CS-E 40(b)(3)(iv)).

### Open items

- **`Maximum Take-off 30 min`** — read as CS-E 40(b)(4) Rated 30-Minute Power.
  AMC E 40(b)(3)(7) defines it as "the approved brake horsepower, developed under
  static conditions at specified altitudes and temperatures within the operating
  limitations established for the Engine, and limited in use for periods of no
  more than 30 minutes", settable "at any level between the Maximum Continuous up
  to and including the take-off rating". Confirm the declared rating matches that
  definition.
- **`OEI override`** — not a rating named in CS-E 40. Likely an internal name for
  a topping or override function rather than a certified rating. Confirm whether
  it is a declared rating or a control-system feature; if the latter it belongs
  under CS-E 50, not CS-E 40.

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

**[VERIFY]** how the additional 25 hours that AMC E 740(c)(2)(i) attaches to a
30-Minute Power rating combines with the CS-E 740(c)(3)(i) schedule.

## Effect on the applicability matrix

| | Variables blank | Variables filled |
|---|---:|---:|
| APPLIES | 120 | **129** |
| CONDITIONAL | 12 | **0** |
| EXCLUDED | 13 | **16** |
