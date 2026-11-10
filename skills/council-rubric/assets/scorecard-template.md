# Scorecard: [claim / snapshot]

- Rubric ID/version and approval reference: [frozen contract, or provisional draft]
- Assessment mode: [single-agent / Council / scoped recheck]
- Artifact snapshot: [commit or snapshot ID, deliverable manifest with hashes]
- Reviewer identity: [agent/role; actual model, harness and requested options when delegated]
- Date/environment: [test conditions, relevant tool versions]
- Prior scorecard/delta: [reference and changed inputs, or initial assessment]
- Scope/limits: [claims assessed; inaccessible artifacts or tests not performed]

## Evidence register

Keep observations distinct from assumptions and estimates. Link stable artifact
revisions, not only mutable paths. Record commands/results where relevant and
retain raw sensitive evidence separately.

| ID | Source / artifact revision | Method, date and conditions | Observation / result | Limits / dependencies |
| --- | --- | --- | --- | --- |
| E1 | [revision/path/hash] | [command + exit status, measurement, or dated inspection] | [what was demonstrated] | [what it does not prove] |

## Quality results

Create a separate scorecard or separate rows for each required reviewer. Do not
invent a joint score. Use `unscored` for missing support, not zero.

| Criterion ID | Score | Anchor-based rationale | Evidence IDs | Validity: new/rechecked/carried with basis |
| --- | --- | --- | --- | --- |
| C1 | [number or unscored] | [observations, not generic praise] | [IDs] | [prior reference and unchanged dependencies if carried] |

- Supported coverage: [scored weight / 100%; unscored IDs]
- Weighted total: [unrounded calculation and display value; unavailable if incomplete]
- Overall target and criterion/category floors: [met / below target / unproven, with IDs]
- Confidence/evidence limits: [separate from score]

## Gate results

| Gate ID | Required? | State | Evidence IDs and reason / authorized N/A basis | Next verification and owner if pending |
| --- | --- | --- | --- | --- |
| G1 | [yes/no] | [pass/fail/pending/not-applicable] | [observation or missing proof] | [bounded action or none] |

## Disagreement and recheck history

- Reviewer differences: [separate scores/judgments, factual crux and resolution; no vote over evidence]
- Reopened results: [IDs, change and invalidated evidence; retain previous failures here]
- Carried results: [IDs, prior evidence reference, unchanged-dependency basis]
- New evidence/resolution: [IDs; what changed and what remains unknown]
- Review accounting: [full rounds and scoped rechecks separately; remaining budget]

## Decision

- Claim accepted / not accepted: [exact scoped claim and reason]
- Stop: [accepted / blocked / continue within remaining authorized budget]
- Governing-rule check: [approval, reviewer completeness, gates, total, every floor, disagreements]
- Blockers and limitations: [demonstrated failures versus pending/unscored evidence]
- Smallest next action / owner: [bounded verification, repair or decision]
- Actions actually authorized/performed: [do not imply deployment/printing/merge from this result]
