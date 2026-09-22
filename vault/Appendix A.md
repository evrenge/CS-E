---
id: "Appendix A"
type: AMC
subpart: E
pages: 210-212
changed_in: []
tags: [rain, hail, concentrations, rwc, hwc, droplet-size, hailstone-size, altitude]
---
# Appendix A — Certification Standard Atmospheric Concentrations of Rain and Hail

> [!summary]
> This appendix supplies the numbers that CS-E 790(a)(2) tests against: one
> figure and four tables giving the atmospheric concentrations and size
> distributions of rain and hail. The values are ambient conditions, not
> conditions at the engine inlet. Substituting different droplet or hailstone
> shapes and sizes is accepted, provided the substitution does not reduce the
> severity of the test.

## Requirement

| Ref | Obligation | Strength |
|---|---|---|
| — | Figure A1, Table A1, Table A2, Table A3 and Table A4 specify the atmospheric concentrations and size distributions of rain and hail for establishing certification, in accordance with the specifications of CS-E 790(a)(2). | Statement |
| — | In conducting tests, normally by spraying liquid water to simulate rain conditions and by delivering hailstones fabricated from ice to simulate hail conditions, the use of water droplets and hailstones having shapes, sizes and distributions of sizes other than those defined in this Appendix A, or the use of a single size or shape for each water droplet or hailstone, can be accepted, provided the substitution does not reduce the severity of the test. | Permitted |

Appendix A is unnumbered prose followed by a figure and four tables, so the `Ref`
cells carry no sub-point identifier.

The substitution permission is broad, but its single condition is strict. Any
shape, size or distribution may be used, including a single size, provided the
severity of the test is not reduced. The burden is on showing that, not on
matching the tables.

The values are ambient. [[AMC E 790|AMC E 790(a)(2)(2)(b)]] states the point
directly: "the water concentrations defined for rain and hail in Appendix A
represent ambient conditions, not test conditions at the Engine inlet". The
amplification between ambient and inlet is what the scoop factor and relative
velocity analysis of AMC E 790(a)(2) exists to quantify.

The appendix notes its own data source and its unit choice. The values come
from the Aerospace Industries Association Propulsion Committee Study, Project
PC 338-1, June 1990. "The unit for altitude has been kept as "feet" to be
consistent with the source of data. This is compatible with Annex 5 of ICAO."
[Appendix A]

### The figure and tables

The figure and all four tables are embedded as their source crops. They are
tabulated numerical data and a plotted chart, so accuracy rule 6 applies. A
transcription could not be checked against the source, and the extracted text
layer flattens the table structure into a single column of unlabelled numbers.

### Figure A1 — Illustration of Rain and Hail Threats

![[Appendix_A_p210.png]]

### Table A1 — Certification Standard Atmospheric Rain Concentrations

![[Appendix_A_p210_2.png]]

### Table A2 — Certification Standard Atmospheric Hail Concentrations

![[Appendix_A_p210_3.png]]
![[Appendix_A_p211.png]]

### Table A3 — Certification Standard Atmospheric Rain Droplet Size Distribution

![[Appendix_A_p211_2.png]]

### Table A4 — Certification Standard Atmospheric Hailstone Size Distribution

![[Appendix_A_p211_3.png]]
![[Appendix_A_p212.png]]

Table A1 and Table A2 both state that values at other altitudes may be determined
by linear interpolation. Table A2 adds that "The hail threat below 7 300 feet and
above 29 000 feet is based on linearly extrapolated data." [Appendix A]

Table A3 gives a median rain droplet diameter of 2.66 mm, and Table A4 a median
hailstone diameter of 16 mm.

## Compliance

- Rain and hail test concentrations derived from Tables A1 and A2 at the altitudes analysed, with linear interpolation where needed [Appendix A].
- Droplet and hailstone size distributions from Tables A3 and A4, or a substitution shown not to reduce the severity of the test [Appendix A].
- Conversion from the ambient concentrations of this appendix to engine inlet conditions, through the amplification and attenuation analysis of [[AMC E 790|AMC E 790(a)(2)(4)(b)(ii)]].
- Critical point analysis using the threats of Figure A1 and Tables A1 to A4 [Appendix A], required by [[AMC E 790|AMC E 790(a)(2)(4)(b)(i)]] for the [[CS-E 790|CS-E 790(a)(2)]] route.

## Application to this engine

The appendix applies where [[CS-E 790|CS-E 790(a)(2)]] applies. For this engine
that route is elective, because [[AMC E 790|AMC E 790(a)(2)(2)(d)]] permits the
static rain ingestion test of [[CS-E 790|CS-E 790(b)]] to replace it for
rotorcraft applications.

If the CS-E 790(b) alternative is taken, the concentration used is the
specification's own 4 percent water droplet flow to airflow by weight. These
tables are then not the test input. They remain relevant in two ways. The
4 percent figure is stated in
[[AMC E 790|AMC E 790(a)(2)(2)(d)]] as an increase "from Appendix A values" that
"will usually compensate for any flight effects", so the tables are the baseline
the alternative is calibrated against. Figure A1, embedded above, is where the
4 percent condition can be read against the ambient threat. The source
describes it only as an "Illustration of Rain and Hail Threats" [Appendix A].
What it plots is therefore not stated in the text layer, and is not restated
here.

The altitude range of the tables runs to 46 000 feet, far above a rotorcraft
envelope. The CS-E 790(a)(1) hailstone ingestion is separately bounded at
"altitudes up to 4 500 metres" [CS-E 790(a)(1)], which is the range that matters
for this installation.

[VERIFY: whether the applicant elects the CS-E 790(b) static rain ingestion test
or the CS-E 790(a)(2) route against these concentrations. `engine_profile.md`
does not record the choice, and it determines whether this appendix supplies the
test input or only the baseline for the 4 percent alternative.]

## References

Specification: [[CS-E 790]]
Related: [[AMC E 790]] · [[CS-E 780]] · [[CS-E 800]] · [[CS-E 540]] · [[CS-E 650]]
