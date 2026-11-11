# Workshop plan: [run ID]

## Authority and inputs

- Explicit invocation / selected mode: [single-team or explicitly selected team-trials]
- Implementation/test authority / excluded effects: [reference; merge/deploy separate]
- Common task / intended user outcome / constraints: [same feature for every team]
- Preflight artifact findings / frozen shared work list: [same prioritized repairs
  and clarifications for all teams; baseline defects are inputs, not final passes]
- Base snapshot / input manifest: [commit or bounded immutable snapshot; dirty inputs explicit]
- Baseline checks / environment / mutable resource ownership: [observations and limits]
- Companion discovery / Pi delegation adapter: [actual available skills and controls]

## Frozen contracts

- Plan-review contract / approval: [version and authority; assesses suitability to attempt]
- Feature-acceptance rubric / approval: [version and authority; same for all teams]
- Mandatory gates / anchors / targets / floors / evidence: [references, not universal defaults]
- Candidate evaluator / selection rule / tie-breakers / no-winner rule: [freeze before results]
- Stage boundaries and reopening dependencies: [plan pass is not a feature pass]

## Topology and configuration

| Team / workspace allocation | Lead / model / harness / options | Workers / models / harnesses / options | Ownership and interfaces | Reason this configuration differs |
| --- | --- | --- | --- | --- |
| [ID; real isolation receipt once allocated] | [implementing lead + integrator] | [bounded work] | [independent resource owners] | [hypothesis and useful evaluator] |

- Preflight Council roster / reviewer policy: [fresh read-only tasks; model/provider/harness/options]
- Final Council roster / reviewer policy: [fresh read-only tasks; not builder sessions]
- Pi exceptions / actual user authorization: [none or approved exception reference]
- Nested delegation / flat fallback: [explicit allocated slots; no implicit spawning]
- Cross-team information barrier / shared clarifications: [freeze before exchanging candidates]
- Runtime-enforced permissions / limits not enforced: [separate from instruction-only rules]

## Global finite budget

- Active builder cap including team leads: [2 single-team / 4 two-team default, or selected cap]
- Builder launch cap including replacements: [3 single-team / 6 two-team default, or selected cap]
- Repair cycles per team: [at most 1 default, also within launch cap]
- Review budget: [1 plan + 1 final + 1 shared full/scoped repair default; no per-stage reset]
- Reviewer launches per roster and phase: [counts; include failed/replaced attempts]
- Enforceable deadlines / token or cost observations: [supported controls or unknown]
- Stop/cancel/escalate conditions: [capability, evidence, failed gate, scope or budget limit]

## Phase and task ledger

| Phase / task ID / parent | Snapshot / contract | State / actual runtime ID | Evidence / approved changes | Consumed and remaining global budget |
| --- | --- | --- | --- | --- |
| [plan review / build A / build B / compare / integrate / final review / recheck] | [immutable references] | [ready/running/input-required/blocked/completed/failed/cancelled] | [artifact and result references] | [no reset after a repair] |

Record actual times and artifacts at handoff boundaries. Keep secrets, raw
conversations and runtime credentials outside this record. Retain the plan,
packets, evidence and results locally; publishing a skill does not publish a run.
