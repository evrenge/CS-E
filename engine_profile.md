# Engine profile

This file is project input, not derived data. It records the applicant's
declared configuration, and it decides applicability for the paragraphs that
CS-E scopes by rating or by system. When a value here changes, update
`scripts/classification.py` and re-run `scripts/build_applicability.py`.

Anything a script can recompute does **not** belong in this file or in
`CLAUDE.md` — it belongs in `work/`.

## Application

Rotorcraft turboshaft, multi-engine installation.

## Ratings declared

The table maps each declared rating onto a CS-E Amendment 8 term. The left
column gives the applicant's own name.

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

- **`Maximum Take-off 30 min`** is CS-E 40(b)(4) Rated 30-Minute Power, as
  confirmed by the applicant. AMC E 40(b)(3)(7) defines it as "the approved
  brake horsepower, developed under static conditions at specified altitudes and
  temperatures within the operating limitations established for the Engine, and
  limited in use for periods of no more than 30 minutes".
- **`OEI override`** is a control-system feature, not a declared rating, as
  confirmed by the applicant. It is therefore assessed under CS-E 50 / AMC E 50
  and the CS-E 510 safety analysis, not under the CS-E 40 ratings, and it has no
  CS-E 40 entry.

## Terms the source leaves undefined

CS-E Amendment 8 uses two terms and defines neither, in CS-E 15 or anywhere else
in scope. `review/dead_ends.md` records them as Kind 2 gaps. The applicant has
supplied a working reading of each.

These are **applicant input, not CS-E text**. They sit here for the same reason
the ratings do: the vault may reason from a declared input, and it may not put
words into the regulation. A note cites this file, never the source, for them,
and each keeps its `[VERIFY]` because only the Agency can settle the reading.

| Term | Where | Applicant's working reading |
|---|---|---|
| **rotor-lock** | AMC E 910(3)(b) | Friction holds the output shaft, so engine torque cannot turn the helicopter rotor: a locked rotor |
| **Maximum Engine Over-speed (20 Second)** | CS-E 870(b)(1) | The steady overshoot limit: for a short period the engine runs above its rated speed limit |

What each reading settles, and what it leaves open:

- **rotor-lock.** The reading brings the **output shaft** into the assessment,
  not only the engine spools. That matches what the `AMC E 910` note already
  says about a free power turbine coupled to the rotor drive system. What stays
  open is the boundary: whether the assessment stops at the engine's own rotors
  or reaches the coupling into the transmission.
- **Maximum Engine Over-speed (20 Second).** The reading treats the term as an
  over-speed held for a short period, which is consistent with the Maximum
  Engine Over-speed of CS-E 830 plus a duration qualifier. What stays open is
  whether the two are the same limit. CS-E 870(b)(1) excludes the 20-second
  value from its test speed, so the answer changes what the over-temperature
  test is run at.

## Systems

| Variable | Value | Consequence |
|---|---|---|
| Control system | **EECS / FADEC, full authority** | CS-E 50, AMC E 50, AMC E 170 and AMC to CS-E 50(l) all apply in full |
| Refrigerant injection | **No** | CS-E 880 EXCLUDED. That paragraph is power augmentation — "Refrigerant Injection Used to Increase ISA Take-off and/or 2½-Minute OEI Performance" — not water ingestion, which is CS-E 790 and does apply |
| Time-limited dispatch | **Not claimed** | CS-E 1030 and AMC E 1030 EXCLUDED. The paragraph is optional by its own wording: "If approval is sought for dispatch with Faults present in an Electronic Engine Control System (EECS)". Re-openable later without affecting any other paragraph |
| Thrust reverser | **No** | CS-E 890, AMC E 890, AMC E 10(b) EXCLUDED |
| Propeller | **No** — rotor drive | CS-E 180, AMC E 180, CS-E 900 EXCLUDED |
| Power turbine architecture | **Not declared** | Several paragraphs bind only on "an Engine incorporating a free power turbine" or open "In the case of a free power-turbine Engine": CS-E 740(f)(3), (g)(3) and (g)(4), CS-E 750(d) and CS-E 820(a). Until it is declared, those notes carry a `[VERIFY]` and the vault reasons about a free power turbine conditionally, never as a declared fact |

## Endurance test selected by these ratings

The combination of 30-Second, 2-Minute and Continuous OEI Power ratings selects
**CS-E 740(c)(3)(i)**:

> "If a Continuous OEI Power rating is associated with the 30-Second and
> 2-Minute OEI Power ratings, the following tests must be conducted and must be
> complemented by the additional test of CS-E 740(c)(3)(iii)"

The test runs 25 six-hour stages. In each stage, Part 3 is one hour at Maximum
Continuous Power followed by one hour at Continuous OEI Power. The additional
2-hour test of CS-E 740(c)(3)(iii) complements the schedule.

Rated 30-Minute Power is claimed, so AMC E 740(c)(2)(i) also applies: the
applicant "may propose either to include the required additional 25 hours within
the" endurance test, run them as a complementary test on the same test article,
or use "a combination of these methods". **[VERIFY]** how those 25 hours
combine with the CS-E 740(c)(3)(i) schedule — the AMC offers a choice and the
selected option should be agreed with EASA.

## What is still to be declared

This file records what the applicant has declared. Many of the vault's open
`[VERIFY]` items ask for something this file does not yet carry — the engine
inlet throat area, the maximum airspeed for normal flight operations, the
Maximum Engine Over-torque, Maximum Engine Over-speed and Maximum Exhaust Gas
Over-Temperature limits, the installation attitude, and the rest.

They are not listed here, because a hand-written copy of a list derived from the
vault goes stale. The inventory is `review/dead_ends.md`, **Kind 3 — engine
information not yet declared**, and it names the note each item blocks. The
single largest of them is the target rotorcraft and its transmission, which
alone blocks at least nine separate items.

## Effect on the applicability matrix

Filling in the variables above resolves every CONDITIONAL verdict: a paragraph
scoped by a rating or a system either applies to this engine or it does not, and
none is left open.

The counts are derived, so this file does not record them. See
`work/applicability.md` for each verdict and the reason behind it, and
`scripts/classification.py` for the data it is rendered from.
