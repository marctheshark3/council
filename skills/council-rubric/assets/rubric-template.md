# Review contract: [project / claim]

- Rubric ID/version: [stable ID, version]
- Lifecycle: [draft / frozen / superseded]
- Authority and approval evidence/date: [selection or confirmation; pending if draft]
- Decision/stage: [the exact claim this review can accept]
- Intended user/use and constraints: [requirements]
- Excluded claims and assumptions: [limits]
- Artifact snapshot: [commit or stable snapshot ID; paths and hashes of deliverables]
- Evidence pack/environment: [manifest ID, conditions, relevant tool versions]
- Supersedes: [prior contract/result; reason for change, or none]

## Quality rubric

Use 0–10 unless the existing project contract specifies another scale. Add
concrete per-criterion anchors and avoid duplicate outcomes. Use positive weights
summing to 100%. Resolve applicability before freezing the weights.

| ID / category | Outcome and definition | Weight % | Observable anchors: failure / partial / target / exceptional | Evidence required | Floor, if any | Dependencies / reopen when |
| --- | --- | --- | --- | --- | --- | --- |
| C1 / [category] | [outcome] | [weight] | [score: observation at each anchor] | [method, measurement and artifact scope] | [value or none] | [inputs and changes] |

- Total formula: `sum(weight_percent * score) / 100` when all applicable rows are scored.
- Category calculations, if used: [IDs, formula and floors, or none]
- Overall target: [project-selected threshold, not a universal default]
- Missing evidence: unscored rows; show coverage, no overall score or silent reweighting.
- Precision: [display precision]; evaluate thresholds before rounding.

## Gates

Keep gates independent of the weighted score. Use `pass`, `fail`, `pending` or
`not-applicable`. Require a recorded authorized basis for not-applicable; missing
proof is pending. Define informational gates explicitly; required gates control
acceptance even when the score is high.

| ID | Required? | Applicability / authorized exclusion basis | Exact pass condition | Method / required evidence | Dependencies / reopen when |
| --- | --- | --- | --- | --- | --- |
| G1 | [yes/no] | [condition] | [observable threshold] | [test and snapshot/environment scope] | [changes] |

## Evaluator safeguards

- Known-good/bad cases / reference material / calibration limits: [available or absent]
- Candidate identity policy / unavoidable exposure: [masked or disclosed; no false blind claim]
- Presentation order / counterbalancing / prior-feedback limits: [freeze before results]
- Independent first-pass judgments / factual-dispute resolution: [verify evidence; retain minority defects]
- Score interpretation: [anchored judgment, not a correctness probability or certification]

## Stopping and disagreement policy

- Acceptance: [required applicable gates pass; target and every floor met; remaining conditions]
- Assessment mode/required reviewers: [single agent or named Council roles; do not launch from this template]
- Reviewer rule: [each required reviewer meets targets/floors, or another explicit rule; retain separate scores]
- Disagreement: [reproduce disputed evidence; pending if unresolved; retain demonstrated failures]
- Review budget: [maximum full rounds/scoped rechecks or time limit]
- Stop blocked when: [budget, access, evidence or owner-decision limit]
- Approval/deployment boundary: [who accepts the claim; separate action authorization]

## Reopening and version policy

| Change | Invalidated criteria / gates / evidence | Minimum recheck | Carry-forward basis for other results |
| --- | --- | --- | --- |
| [source, configuration, dependency, package, environment or intended use] | [IDs and dependency chain] | [method and artifact revision] | [evidence reference plus unchanged inputs] |

Version changes to scope, anchors, weights, thresholds, evidence standards or
reviewer policy. Retain the prior contract/result and change rationale/approval;
never rewrite the old result to meet the new bar.
