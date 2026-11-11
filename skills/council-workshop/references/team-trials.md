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
allocations; otherwise report the actual difference as a tradeoff. Do not claim a
configuration won because of its provider when assignments or budgets also varied.

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

Use the bundled example as a shape reference. Supply these fields:

- `schema_version: 1`, `mode` (`single-team` or `team-trials`), immutable
  `base_snapshot`, and optional `example: true` for synthetic data.
- `rubric` and `plan_review`: each with a stable `id`, `status: frozen`, and an
  actual `approval` reference. The checker cannot verify that reference's truth.
- `budgets`: integer `max_active_builders`, `max_builder_launches`,
  `max_team_repairs`, `plan_review_rounds`, `final_review_rounds` and
  `repair_review_rounds`. Use positive launch/concurrency and initial review
  limits; allow zero repairs/rechecks. Count every replacement against launches.
- `teams`: unique `id` and `workspace_id`, the shared `base_snapshot` and
  `rubric_id`, `coordination` (`lead-led` or `peer-team`), and `members`.
- Each builder: unique `id`, `role` (`lead` or `worker`), exact `model`, actual
  `provider_instance_id`, `harness`, explicit `options`, and bounded `assignment`.
  Include exactly one lead and at least one worker per team. Keep workspace IDs
  as allocation labels until supported runtime receipts establish real isolation.
- `reviewers.plan` and `reviewers.final`: explicit rosters with the same identity
  and routing fields and `role: reviewer`. Apply Council's independent-provider
  and effort policy separately; the checker does not resolve provider capability.
- A non-Pi `harness` requires a `harness_override_approval` reference. Use Pi's
  provider-qualified model ID and explicit string `options.thinking` for Pi.

The checker rejects differing candidate inputs, invalid typed budgets, absent
rosters, obvious ID collisions and byte-equivalent normalized configurations.
It cannot prove that two written assignments differ meaningfully, that workspaces
are physically separate, or that a model/option is available. It does not inspect
code, measure cost, compute a review score or authorize execution. Perform runtime
preflight, source verification and real acceptance checks separately.

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
