# Workshop plan: [run ID]

## Authority and inputs

- Explicit invocation / selected mode: [single-team or explicitly selected team-trials]
- Implementation/test authority / excluded effects: [reference; merge/deploy separate]
- Common task / intended user outcome / constraints: [same feature for every team]
- Independent work / shared decisions and interfaces: [why parallelism helps; what must freeze]
- Trial rationale if selected: [value of duplicate work, uncertainty and dependable selection]
- Preflight artifact findings / frozen shared work list: [same prioritized repairs
  and clarifications for all teams; baseline defects are inputs, not final passes]
- Base snapshot / input manifest: [commit or bounded immutable snapshot; dirty inputs explicit]
- Baseline checks / environment / mutable resource ownership: [observations and limits]
- Companion discovery / Pi delegation adapter: [actual available skills and controls]

## Frozen contracts

- Plan-review contract / approval: [version and authority; assesses suitability to attempt]
- Feature-acceptance rubric / approval: [version and authority; same for all teams]
- Mandatory gates / anchors / targets / floors / evidence: [references, not universal defaults]
- Common task/work-list ID / approval: [same post-preflight inputs; referenced by every team]
- Evaluator ID / approval / selection rule / tie-breakers / no-winner rule: [freeze before results]
- Comparison basis / resource policy: [delivery-only, equal-budget-quality or time-to-accepted-quality;
  actual controls/observations, not equal-effort assumptions]
- Identity policy / exposure limits / presentation order: [masked or disclosed; bias precautions]
- Evaluator checks / known cases / baseline / held-out cases: [available evidence or explicit absence;
  repeated matched tasks needed for general configuration claims]
- Stage boundaries and reopening dependencies: [plan pass is not a feature pass]

## Topology and configuration

| Team / workspace allocation | Lead / model / harness / options | Workers / models / harnesses / options | Ownership and interfaces | Reason this configuration differs |
| --- | --- | --- | --- | --- |
| [ID; real isolation receipt once allocated] | [implementing lead + integrator] | [bounded work] | [independent resource owners] | [hypothesis and useful evaluator] |

- Preflight Council roster / reviewer policy: [fresh read-only tasks; model/provider/harness/options]
- Final Council roster / reviewer policy: [fresh read-only tasks; slot IDs disjoint from plan/build IDs]
- First-pass / finding / recheck policy: [independent judgments before peer conclusions;
  verify rather than vote; stable finding IDs; delta and affected dependencies after initial pass]
- Pi exceptions / actual user authorization: [none or approved exception reference]
- Nested delegation / flat fallback: [explicit allocated slots; no implicit spawning]
- Cross-team information barrier / shared clarifications: [freeze before exchanging candidates]
- Runtime-enforced permissions / limits not enforced: [separate from instruction-only rules]

## Global finite budget

- Active builder cap including team leads: [2 single-team / 4 two-team default, or selected cap]
- Builder launch cap including replacements: [3 single-team / 6 two-team default, or selected cap]
- Repair cycles per team: [at most 1 default, also within launch cap]
- Global review cap and slices: [max_review_rounds 3 default: 1 plan + 1 final +
  1 shared full/scoped recheck; sum slices within cap; no per-stage reset]
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
