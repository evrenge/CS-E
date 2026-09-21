---
id: "AMC E 640"
type: AMC
subpart: E
pages: 118-119
changed_in: []
tags: [pressure-loads, definitions, working-pressure, oei, zoning, analytical-model]
---
# AMC E 640 — Pressure Loads

> [!summary]
> The definitions are the substance of this AMC. Normal, maximum working and
> maximum possible pressure are each defined against a different set of
> conditions, and the third includes Failures more likely than Extremely Remote.
> The AMC also identifies which parts count as static parts under pressure load,
> permits a part with varying pressure along its length to be tested in zones,
> sets the test conditions for additional loads and temperature, and allows a
> validated analytical model.

## Requirement

### AMC E 640(1) — definitions

| Ref | Obligation | Strength |
|---|---|---|
| **(1)** | Relate the following definitions to the engine when installed in a typical installation. | Accepted method |
| **(1)** | Normal Working Pressure: the maximum pressure differential likely to occur on most flights, including any pressure fluctuations as a result of the normal operation of valves, cocks and similar, where these could produce significant surge pressures. | Statement |
| **(1)** | Maximum Working Pressure: the maximum pressure differential which could occur under the most adverse operational conditions likely to be encountered in service — for example forward speed, altitude, ambient temperature, engine speed, use of OEI ratings — including any pressure fluctuations from the normal operation of valves, cocks and similar, where these could produce significant surge pressures. | Statement |
| **(1)** | Maximum Possible Pressure: the maximum pressure differential which could occur under the most adverse combination of operational conditions — for example forward speed, altitude, ambient temperature, engine speed, use of OEI ratings — likely to be experienced in service, together with Failure of any relevant parts of the engine or control system, or combinations of Failures which are more likely than Extremely Remote. Give consideration to any pressure fluctuations as a result of normal or emergency use of valves, cocks and similar, where these could produce significant surge pressures. | Statement |
| **(1)** | Static Parts subject to significant gas or liquid pressure loads: the components subject to high-pressure loads, or whose design is influenced by the gas or liquid pressure loads to be contained. | Statement |
| **(1)** | Give special attention to any filler cap. | Accepted method |

The three pressures differ on two axes, and both matter. **Normal** is what most
flights see; **maximum working** is the most adverse operational conditions in
service; **maximum possible** adds Failures of the engine or control system that
are more likely than Extremely Remote. Only the third crosses from operation into
Failure, which is why it feeds the fracture and burst level of
[[CS-E 640|CS-E 640(a)(2)]] and not the distortion level.

The definitions are explicitly installation-relative: they "should be related to
the Engine when installed in a typical installation" [AMC E 640(1)]. The
conditions that set them — forward speed, altitude, ambient temperature — are
installation assumptions under [[CS-E 30]].

The AMC lists example parts: "the compressor, combustor and turbine casings,
heat exchangers, bleed valve solenoids, starter motors or fuel, oil and hydraulic
system components" [AMC E 640(1)]. The list is introduced by "Examples might
include", so it does not bound the population.

### AMC E 640(2) to (4) — tests and modelling

| Ref | Obligation | Strength |
|---|---|---|
| **(2)** | The anticipated engine manual serviceable limits may be used as the criteria to judge the acceptability of any permanent distortion. | Permitted |
| **(2)** | Where a test is performed on a part subjected in service to a varying pressure throughout its length, it is permissible to simulate the pressure conditions by suitably dividing the part into zones and applying the maximum pressure for each zone, including the appropriate factors of CS-E 640(a). | Permitted |
| **(3)** | Where the part is subject to loads in addition to those resulting from differential pressure, such as flight manoeuvre loads or engine mounting loads, analyse those additional loads and examine their effect. | Accepted method |
| **(3)** | Where the effect of those loads is small, it may be possible to simulate them by an addition to the test pressure differential; where they are of significant magnitude or cannot adequately be represented by a pressure increment, carry out the test with such loads acting in addition to the pressure loads. | Accepted method |
| **(3)** | Test the part at the temperature associated with the most critical stress case; alternatively, increase the test pressure differential to simulate the loss of relevant properties as a result of temperature. | Accepted method |
| **(3)** | During pressure testing, make the methods of mounting and restraint by the test facility or test equipment of any critical section such as to simulate the actual conditions occurring on the engine. | Accepted method |
| **(4)** | An analytical modelling method may be used to determine adequate strength and fatigue life, provided that the model is validated by testing or successful field experience with parts of similar design. | Permitted |

The zoning permission in (2) is a practical relief for long parts. It carries
its own condition: the maximum pressure for each zone must still include the
CS-E 640(a) factors. Zoning reduces the test rig, not the margin.

Paragraph (4) extends the analytical route to **fatigue life**, not only to
strength. This is why the same text appears in
[[AMC E 515|AMC E 515(3)(e)(iii)]] for static pressure loaded parts.

## Compliance

- Determination of normal working, maximum working and maximum possible pressure for each part, related to a typical installation [AMC E 640(1)], consistent with the assumptions of [[CS-E 30]].
- Identification of the static parts subject to significant gas or liquid pressure loads, including filler caps [AMC E 640(1)].
- Serviceable limits from the anticipated engine manual, used as the distortion acceptance criteria [AMC E 640(2)], consistent with the manuals of [[CS-E 25]].
- Zoning scheme and the maximum pressure applied to each zone, with the CS-E 640(a) factors included, where a part is tested in zones [AMC E 640(2)].
- Analysis of additional loads with their effect examined, and the test conducted under those loads where they are significant [AMC E 640(3)].
- Test temperature justification, or the increased pressure differential used to substitute for it [AMC E 640(3)].
- Mounting and restraint arrangement simulating the actual engine conditions for any critical section [AMC E 640(3)].
- Analytical model validation by testing or by field experience with parts of similar design, where the model is used [AMC E 640(4)].

## Application to this engine

The AMC applies in full. Nothing in it is restricted by engine type or control
system.

**The OEI ratings raise the test levels.** The source names "use of OEI ratings"
among the most adverse operational conditions that define both the maximum
working pressure and the maximum possible pressure [AMC E 640(1)]. Since this
engine declares 30-Second OEI, 2-Minute OEI and Continuous OEI, the pressures
those ratings produce enter both definitions. They therefore also enter both the
(a)(1) and the (a)(2) levels of [[CS-E 640]]. Omitting the OEI ratings from the
pressure survey would understate both test levels.

**Maximum possible pressure depends on the control system.** The definition
includes "Failure of any relevant parts of the Engine or control system, or
combinations of Failures which are more likely than Extremely Remote"
[AMC E 640(1)]. For a full-authority EECS the relevant Failure set is large, and
the Extremely Remote classification comes from the safety analysis of
[[CS-E 510]] and [[CS-E 50|CS-E 50(d)]]. The pressure survey therefore depends on
a completed safety analysis, not only on a performance model.

The named example parts include fuel and oil system components. This ties the
AMC to [[CS-E 560]] and [[CS-E 570]]. The un-pressurised oil tank case of
[[CS-E 570|CS-E 570(f)(1)]] is tested at 35 kPa — the same increment that appears
in both CS-E 640 levels.

## References

Specification: [[CS-E 640]]
Related: [[CS-E 30]] · [[CS-E 50]] · [[CS-E 510]] · [[CS-E 515]] · [[CS-E 520]] · [[CS-E 560]] · [[CS-E 570]] · [[CS-E 25]] · [[CS-E 70]] · [[AMC E 80]] · [[AMC E 515]]
