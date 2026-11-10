# Worked examples

Treat every value and observation below as synthetic. Use these to exercise the
workflow, not as evidence about a real project or universal acceptance standards.

## CAD: efficiency is not whole-product or delivery readiness

**Contract:** enclosure `prototype-review/v1`, frozen for source snapshot A and
export bundle A. Claim: ready to begin a supervised physical prototype, not
ready to sell or proven to fit hardware. Single-agent review; one initial pass
and at most two scoped rechecks. Require total at least 9 and every criterion
at least 8, with all applicable required gates passing.

| ID | Criterion | Weight | Synthetic score |
| --- | --- | --- | --- |
| C1 | Geometry and clearance reasoning | 30% | 9.4 |
| C2 | Print efficiency | 25% | 9.0 |
| C3 | Assembly/service access | 25% | 8.8 |
| C4 | Prototype handoff clarity | 20% | 9.2 |

Before freezing, anchor each criterion to observations. For C2, an example set
is 0 = cannot slice within the specified bed, 5 = slices with an unaddressed
avoidable support/time burden, 8 = documented orientation and efficiency budget
met with settings inspected, 10 = measured alternatives improve that budget
without violating the geometry/process contract. Define the other criteria to
the same specificity; do not score against criterion titles alone.

Synthetic evidence E1 supports the scores: stable source/mesh manifest, clearance
analysis, slicer reports and assembly walkthrough. Calculate
`0.30*9.4 + 0.25*9.0 + 0.25*8.8 + 0.20*9.2 = 9.11`, displayed as 9.1.
Do not call an efficiency-only 9.0 a whole-product 9.0.

Required gates:

- G1 geometry validator for the pinned meshes: **pass**, from E1.
- G2 delivered combined project retains process settings for every object/plate:
  **fail**, because independent bundle inspection E2 shows a lost per-object
  setting despite correct settings in the individual print files.
- G3 approved physical-test procedure/coupon package is included: **pending**,
  because no package evidence was supplied. Actual physical fit is excluded
  from this prototype-preparation claim and remains unproven, not "pass".

**Decision:** stop blocked, not accepted, despite 9.1 and all numeric floors met.
Repair the combined export and provide the physical-test handoff. If the claim
changes to "fit verified", create a new rubric version with an actual physical
coupon/assembly gate; do not retroactively call G3 physical proof.

**Recheck:** bundle B changes export settings only. Reopen G2 and any quality row
whose evidence depends on those settings, including C2. Inspect/slice the actual
combined B project, not just the source recipes. Carry C1/C3 only after confirming
unchanged geometry/assembly dependencies; retain their A evidence references.
Keep G3 pending until the procedure package is verified. Record this as a scoped
recheck, not a fresh full Council review or completed physical print.

## Software: missing evidence is not a zero or a high average

**Contract:** private-app `review-ready/v1`, source commit S and archive P. Claim:
ready for remote private review, not production readiness. Require total at least
8.5, each criterion at least 8, source checks, archive/source identity, and the
actual authorized private-client journey. Use one initial pass and one recheck.

Quality criteria: C1 behavior 35%, C2 maintainability 25%, C3 client usability 25%,
C4 handoff 15%. Define anchors before assessment; for C3, 0 = core journey
unusable, 5 = journey needs undocumented workarounds, 8 = defined journey works
at the target viewport/input with no blocking issue, 10 = observed representative
use also meets the contract's explicit recovery/accessibility goals.

Synthetic source evidence supports C1=9, C2=9.2 and C4=9. No relevant client
session exists for C3. Mark C3 **unscored**. Report 75% coverage and a supported
weighted subtotal of 6.80, not an overall 6.8 or renormalized 9.1. Leave the total
and floor outcome unproven. Do not make up usability evidence from a screenshot.

G1 source tests at S pass. G2 archive/source identity fails: P contains an older
build. G3 private-client journey is pending: a local health probe is insufficient.
Stop blocked. Do not deploy, open a tunnel or change services merely to fill a
scorecard; use the owning project's review/access workflow and authorization.

For a separately authorized corrected archive P2 and client check, reopen G2/G3,
C3 and any dependent handoff/behavior rows. Carry G1 only with proof S and its
test inputs are unchanged. If a dependency changed during the rebuild, broaden
the checks instead of copying the old pass. If required reviewers disagree about
a reproducible failure, retain it; stop at the budget with the factual crux and
next check rather than averaging scores or lowering the floor.
