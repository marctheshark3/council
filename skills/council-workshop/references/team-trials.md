# Reviewed teams and team trials

## Keep purpose, mechanism and coordination separate

Use Council for independent review and Council Rubric for its evidence-based
contract. Use Workshare for execution. Use this workshop to compose those jobs
into declared stages. Prefer Pi as the common harness, selecting model families
and reasoning options separately for the work. Do not require different harnesses
merely to obtain model diversity.

Treat subagents as a handoff mechanism. Arrange them as a lead-led team when one
controller assigns and integrates work. Arrange a peer team only when the
existing runtime actually supports the selected shared context and communication.
Reserve "swarm" for an explicitly selected self-organizing pattern; do not equate
every team or parallel fan-out with a leaderless swarm. This release does not
implement a peer bus, A2A service, autonomous task board or durable agent engine.

## Example: two teams, the same CSV export task

Use these as configuration ideas, not a selected roster or performance claim.
Resolve current catalog IDs and supported controls before an actual run.

- **Team A / balanced:** a GPT-family Pi lead implements the UI and integration;
  a Grok-family Pi worker implements a CSV writer and its contract tests.
- **Team B / provider-preferred:** a GPT-family Pi lead implements independent
  compatibility coverage and integration; a Grok-family Pi worker owns the main
  export implementation against the same interface and acceptance requirements.
- **Optional different-model trial:** substitute an explicitly selected
  Claude-family Pi lead or a different supported worker/effort allocation as a
  separately budgeted configuration. Do not automatically add a third team.

Give A and B the same whole feature request, base revision, environment contract,
reference fixtures and feature rubric. Change the ownership/configuration, not
the acceptance bar. Keep writable resources independent. State launch, repair,
concurrency and time budgets. If equal-resource comparison matters, control those
allocations; otherwise report the actual difference as a tradeoff. Freeze the
selection rule, identity handling and candidate order before results. Mask labels
and counterbalance order when practical, recording any remaining identity exposure.
Do not claim a configuration won because of its provider when assignments or
budgets also varied. Consult [evidence-and-limits.md](evidence-and-limits.md) for
primary sources and the distinction between candidate coverage and selection.

Use two teams only when the expected value of a real alternative justifies
repeated work. A high-quality single-team result may be preferable to a comparison.
Increasing the number of agents can move the bottleneck into setup, test resources
or integration. Retain a valid baseline if replacements provide no useful gain.

## Review two different claims

Review the proposed interfaces, risks and evaluator in preflight. Do not score
runtime correctness of unbuilt code. Let the plan contract accept only that it is
reasonable to attempt the declared configurations under the stated constraints.

Review the resulting integrated feature in the final Council round. Reproduce
required checks on the final revision and its delivered artifacts. Keep reviewers
read-only and use fresh tasks instead of asking the builders to certify themselves.
Reusing a model family in a fresh context does not establish statistical
independence; label any author/reviewer overlap and access limits honestly.

Keep shared requirements traceable across stage-specific contracts. Version
scope/threshold changes before scoring affected candidates and preserve old
results. Never let a preflight pass become a proxy for an implementation pass.

## Structural JSON plan

Use the bundled example as a shape reference. Supply these schema-2 fields:

- `schema_version: 2`, `mode` (`single-team` or `team-trials`), immutable
  `base_snapshot`, and optional `example: true` for synthetic data.
- `task`, `rubric`, `plan_review` and `evaluation`: each with a stable `id`,
  `status: frozen` and an actual `approval` reference. `task` identifies the same
  post-preflight work-list for every team. Approval truth is not machine-verified.
- `parallelism.independent_work` and `parallelism.shared_decisions`: nonempty
  reasoning about the split and interface/context/resource constraints.
  `parallelism.trial_reason` is also required for `team-trials`. These declarations
  do not prove that parallel work or duplicate teams are worthwhile.
- `evaluation.selection_rule`: the frozen gate-first rule, references,
  tie-breakers and no-winner behavior; `evaluation.resource_policy`: resources to
  control or record; `evaluation.presentation_order`: order and bias precautions.
  Each is a nonempty string. The checker does not parse or judge their adequacy.
- `evaluation.comparison_basis`: `delivery-only`, `equal-budget-quality` or
  `time-to-accepted-quality`. `evaluation.identity_policy`: `masked` or
  `disclosed`. State exposure limits, not a fictitious blind/equal-compute claim.
- `review_policy`: `independent_first_pass: true`,
  `finding_resolution: evidence-not-vote`, `recheck_scope: delta-and-dependencies`.
  The last policy applies after the initial pass; broaden when impact is unclear.
- `budgets`: integer `max_active_builders`, `max_builder_launches`,
  `max_team_repairs`, `max_review_rounds`, `plan_review_rounds`,
  `final_review_rounds` and `repair_review_rounds`. Launch/concurrency, global
  review and initial review limits are positive; repairs/rechecks may be zero.
  The three review slices must sum to no more than `max_review_rounds`.
  Count replacements against launches; declarations are not runtime counters.
- `teams`: unique `id` and `workspace_id`, the shared `base_snapshot`, `task_id`,
  `rubric_id` and `evaluation_id`, `coordination` (`lead-led` or `peer-team`),
  and `members`. IDs reference the frozen objects above, not separately rewritten
  team briefs. Supply identical actual inputs and distribute approved changes.
- Each builder: unique `id`, `role` (`lead` or `worker`), exact `model`, actual
  `provider_instance_id`, `harness`, explicit `options`, and bounded `assignment`.
  Include exactly one lead and at least one worker per team. Keep workspace IDs
  as allocation labels until supported runtime receipts establish real isolation.
- `reviewers.plan` and `reviewers.final`: explicit rosters with the same routing
  fields and `role: reviewer`. Give every planned invocation slot a distinct `id`,
  disjoint from builder IDs, even when model families recur in both stages. Record
  actual fresh runtime IDs for every launch/recheck in the ledger. The checker
  cannot establish session freshness, provider independence or effort capability.
- A non-Pi `harness` requires a `harness_override_approval` reference. Use Pi's
  provider-qualified model ID and explicit string `options.thinking` for Pi.

The checker rejects differing candidate references, invalid typed budgets,
overallocated review slices, absent policy/roster fields, obvious ID collisions
and byte-equivalent normalized configurations. It cannot prove that assignments
differ meaningfully, that physical workspaces and contexts are independent, that
resources/ordering/masking are fair, or that a model/option is available. It does
not inspect code, measure cost, score a review or authorize execution. Perform
runtime preflight, source verification and real acceptance checks separately.

### Migrate a schema-1 plan deliberately

The checker rejects version 1 rather than silently approving new policies. Keep
its historical record. Name and approve the frozen common `task` and `evaluation`,
add the parallelism and review policy declarations, and reference the new IDs in
every team. Give plan/final review slots unique IDs and allocate an explicit global
review cap that contains all three phase slices. Set `schema_version` to 2 only
after those choices are made. Do not copy the synthetic example's approvals or
models into a runnable plan. Recheck any changed contract before building.

### Bound comparison claims

`delivery-only` chooses a useful result without a controlled-performance claim.
Equal-budget quality requires comparable actual resources, not matching effort
labels or launch caps. Time-to-accepted-quality needs a common acceptance bar and
observed end-to-end times, including waits, integration, repairs and review. An
unselected candidate with no final acceptance has no accepted-result time; record
that outcome, not its build-completion time as a substitute. Extra baseline runs
or candidate reviews require their own preallocated authority and budget.

For a configuration study, include a capable single-agent baseline or disclose
its absence, use repeated matched tasks and keep tuning cases separate from final
evaluation. The normal one-feature workshop does not establish a general provider
ranking or an isolated benefit from agent count.

## Failure and recovery examples

- **Named Pi model unavailable:** stop that required stage and report it. Do not
  switch to a native harness or another model without authorization.
- **Worker waiting on a missing interface:** mark input-required or blocked;
  clarify the shared contract and distribute any approved change to both teams.
- **One candidate fails a required gate:** retain the failure. Use only its
  allocated repair, or exclude it. Do not average it against another team's pass.
- **No candidate meets the rules:** return no winner and the smallest useful next
  test or owner decision. Do not start an unlimited tournament.
- **Two candidates contribute useful pieces:** create a new synthesis revision,
  re-run integration checks, then review that exact result. Earlier passes remain
  evidence only where dependencies are demonstrably unchanged.
- **Reviewer disagreement:** reproduce disputed evidence. Preserve a demonstrated
  failure and mark unresolved/missing proof pending, rather than taking a vote.
- **Interruption:** reconcile existing runtime IDs, artifacts and counters before
  resuming. Cancel superseded work and do not create duplicate workers by guessing
  that silence means failure. Use runtime events, not extra polling infrastructure.
- **Budget exhausted before final acceptance:** stop blocked, report consumed and
  remaining phase budgets, and identify what a continuation would need. Do not
  relabel a partial candidate assessment as final Council acceptance.
