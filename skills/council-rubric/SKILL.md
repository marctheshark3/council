---
name: council-rubric
description: 'Define, apply, and maintain project-specific quality rubrics and acceptance gates. Use for "council rubric", "define a review rubric", "assess against this rubric", or "recheck the affected gates". Keep scores, evidence, stopping rules and reopening conditions explicit. Work standalone; launch reviewers only for an explicit Council run, not rubric drafting or discussion. Not a substitute for domain validators or certification.'
---

# Council Rubric

Turn a project brief into an evidence-based review contract with a clear finish
line. Separate desirable quality from non-negotiable acceptance conditions, then
assess a named artifact revision against that contract. Reuse the structure, not
another project's weights, thresholds or readiness claims.

## Choose the mode and authority

- **Define:** Draft or revise a rubric, gates, evidence requirements and stopping
  rules. Work with one agent; do not launch delegates.
- **Assess:** Inspect the artifact and produce an evidence-backed scorecard.
  Label a single-agent assessment as such, not as Council consensus.
- **Recheck:** Revisit results invalidated by changes; preserve valid earlier
  evidence with explicit references, not unqualified copied passes.
- **Run with Council:** Load `council` by skill name only when the user explicitly
  asks to convene/run it, including "run council against rubric v1". Let Council
  select and coordinate reviewers; use this skill for their shared contract.
- **Compose a workshop:** Load `council-workshop` by name for an explicitly
  requested review/build/review run. Define linked plan-suitability and feature
  contracts, share the same feature contract across trial teams, and keep the
  claims and evidence separate. Mere workshop discussion does not launch agents.

Use this workflow for repeatable project reviews, not every small edit or casual
request for an opinion. Compose with the relevant domain skills and required
validators rather than replacing them. Do not interpret rubric approval, a high
score or a gate pass as permission to deploy, print, purchase, publish, merge or
change services. Keep reviewers read-only unless implementation is separately
authorized. Do not imply safety, regulatory or professional certification.

## 1. Fix the claim and review snapshot

Identify the decision to make, intended user/use, constraints, stage and excluded
claims. Distinguish "ready for a prototype", "ready for private review" and
"ready to ship"; do not let a narrower success support a broader claim.

Record an immutable snapshot: repository commit, artifact paths and hashes or
an equivalent stable revision, including packaged/generated deliverables. For
dirty work, retain a bounded diff and artifact manifest with a snapshot ID; a
branch name or "latest" is not enough. Record test environment, relevant tool
versions and evidence dates. Flag mixed revisions before using their results.

Use existing project contracts and acceptance requirements first. Ask only for
ambiguities that materially change the decision; otherwise state bounded
assumptions and proceed with a draft. Label proposed requirements and approval
status. Freeze the chosen contract before scoring; cite the user's selection,
existing project authority or explicit confirmation. Treat an unapproved draft
assessment as provisional, not accepted delivery. Do not demand repeated approval
for ordinary work already within the selected contract.

## 2. Define anchored quality criteria

Start from [assets/rubric-template.md](assets/rubric-template.md). Choose a small
set of distinct criteria tied to outcomes, not a long checklist of preferences.
Give each criterion a stable ID, definition, weight, observable scoring anchors,
evidence requirement, dependencies and any mandatory floor. Avoid counting the
same outcome twice under different names. Add category floors when a strong
average could conceal an unacceptable weakness.

Use a 0–10 scale unless an existing contract specifies another. Define concrete
anchors for each criterion, including failure, partial adequacy, the target
level and exceptional performance; for example 0, 5, 8 and 10. Explain intermediate
scores through observed differences rather than false numerical precision.
Keep weights positive and totaling 100%. Define any category calculations too.

Compute the weighted total as `sum(weight_percent * score) / 100` only when all
applicable criteria are scored. Show coverage and unscored IDs otherwise; a
supported subtotal is not an overall score. Do not convert missing evidence to
zero, assume it merits a pass, or silently renormalize around it. Establish
applicability before scoring. If a weighted criterion becomes inapplicable,
version the contract and settle its weights before recalculating.

Choose project-specific target scores and floors; do not impose a universal
"9 overall, none below 8" rule. Display at most one decimal unless measurement
justifies more, but compare thresholds using unrounded values. Keep confidence
and evidence limits separate from the quality score; 9/10 is not a calibrated
90% correctness probability. Where available, check the evaluator against known
good/bad examples, reference artifacts or historical defects, recording mistakes
and remaining limits rather than inventing calibration. Consult
[references/evidence-and-limits.md](references/evidence-and-limits.md) when choosing
judge safeguards or explaining the research basis.

## 3. Define acceptance gates independently

Give each gate a stable ID, required/informational designation, applicability,
exact pass condition, verification method, required evidence, dependencies and
reopening triggers. Cover delivery as well as source quality when the claim
includes a package, exported design, deployed app or handoff.

Use exactly these gate states:

- **pass:** Relevant evidence demonstrates the condition for this snapshot.
- **fail:** Relevant evidence demonstrates a violation.
- **pending:** Evidence is missing, stale, contradictory or not yet verified.
- **not-applicable:** An authorized applicability decision and rationale exclude
  the condition for this claim; do not use it to hide an unperformed test.

Keep an observed failure visible when other checks are missing. A high weighted
score cannot override a failed or pending required gate. Distinguish source tests,
packaged-artifact verification, real environment/user journeys and physical
validation. A render is not a fit test; a slicer's estimate is not a measured
print; local HTTP health is not remote client access; passing unit tests is not
proof that the delivered archive contains that tested implementation.

## 4. Freeze stopping and reopening rules

Record what permits acceptance: required gates, total threshold, criterion or
category floors, required reviewers, disagreement handling and approval authority.
For a multi-reviewer assessment, define whether each required reviewer must meet
the targets or another explicit rule applies. Keep their scores separate. Do not
average away a blocker, manufacture a joint score or resolve factual disagreement
by majority vote. Reproduce disputed evidence; leave the affected result pending
if it cannot be resolved. Retain an independently demonstrated failure.

Set a review budget in rounds, time or another observable limit before launching
reviewers. For a workshop, allocate plan/final/recheck slices from its one global
budget, rather than restarting a full allowance per phase or candidate.
Stop **accepted** when the frozen rules are satisfied. Stop **blocked**
when the budget is exhausted, required evidence/access is unavailable, or a
material decision needs the owner. Report the smallest next test or decision;
do not keep convening reviewers until their language becomes enthusiastic.
Continue only within the authorized scope and remaining budget.

Map likely changes to invalidated criteria, gates and evidence. Include geometry,
configuration, dependencies, packaging, environment and intended-use changes,
not just source edits. Version any change to scope, anchors, weights, thresholds,
evidence standards or reviewer policy, with rationale and approval. Preserve the
old contract and result; never lower a bar retrospectively to label the old
assessment a pass. Reassess under the new version explicitly.

## 5. Assess from traceable evidence

Use [assets/scorecard-template.md](assets/scorecard-template.md). Inspect the actual
snapshot and required evidence, using only authorized tests and tools. Record
observations separately from assumptions, estimates and interpretations. Reference
measurements, commands and exit status, test conditions, dated records and
artifact IDs with enough detail to repeat the check. Keep secrets and raw private
session data out of shared scorecards.

Score each supported criterion against its anchors and cite evidence IDs. Mark
unsupported criteria `unscored`. Record each gate's state, evidence and reason.
Explain a material gap as demonstrated failure, missing proof or disputed
interpretation; do not treat all three as the same problem. Identify the next
bounded verification and owner when a gate remains pending.

For candidate comparisons, freeze identity handling and presentation order before
results. Mask provider/team labels where practical and authorized; counterbalance
order when comparing several candidates. Record unavoidable exposure such as
commit authorship, recognizable output and prior feedback. Do not alter artifacts
to hide identity or claim fully blind judging from aliases alone. Treat these as
bias safeguards, not proof of objectivity.

For an explicit Council run, send every reviewer the same frozen rubric version,
artifact manifest, evidence pack, scope, output template and budget. Collect
independent first-pass per-criterion scores, gate judgments and concrete objections
before exposing other reviewers' conclusions. Record actual reviewers,
models/harnesses and requested options as required by Council;
report unavailable members rather than simulating consensus. Reconcile evidence,
not personalities. Put scorecard references and stopping-rule results alongside
Council's review summary; a scalar code-review score is not a replacement.

## 6. Recheck without erasing history

Record the new snapshot, the delta from the reviewed snapshot and affected
dependency chains. Reopen affected results as pending until revalidated, while
retaining prior failures in history. Recheck generated/delivered artifacts after
an export or packaging change even when source geometry/code is unchanged.

Carry forward an unaffected result only with a reference to its earlier evidence
and an explicit unchanged-dependency basis. If impact cannot be bounded, broaden
the recheck or leave the claim pending. Recompute totals and floors from currently
valid rows only; never combine stale passes with new scores to claim acceptance.
Keep each reviewer's changed rows and unresolved dissent visible. Count a scoped
recheck as scoped, not as a new full Council review of the whole artifact.

Finish with the contract and artifact IDs, assessment mode, scores/coverage,
required gate results, acceptance/stopping decision, remaining limitations and
smallest next action. State exactly which claim passed, failed or remains
unproven; do not broaden "review complete" into "project ready".

## Resources

- [assets/rubric-template.md](assets/rubric-template.md): Copy and fill the review
  contract; replace every placeholder before freezing it.
- [assets/scorecard-template.md](assets/scorecard-template.md): Record one assessed
  snapshot, evidence, reviewer results and any scoped recheck.
- [references/examples.md](references/examples.md): Consult synthetic CAD and
  software cases for delivery failures, unknowns and reopening behavior. Adapt
  their criteria to the current project rather than copying their targets.
- [references/evidence-and-limits.md](references/evidence-and-limits.md): Primary
  rubric/judge studies, bias safeguards and the limits of score-based claims.
