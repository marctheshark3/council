---
name: council-workshop
description: 'This skill should be used when the user asks to "run council workshop", "run council team trials", or "combine Council and Workshare" for execution. Compose council-rubric, independent plan review, Pi-first worksharing, integration and final Council review. Duplicate the same feature across different team configurations only in explicitly selected team-trials mode. Do not launch teams for discussion, rubric drafting or review-only requests.'
license: MIT
---

# Council Workshop

Compose rubric definition, independent Council review and Workshare execution
without making reviewers builders or letting builders certify their own result.
Use one team for normal reviewed delivery; use isolated team trials when the user
explicitly wants different configurations to attack the same task. Keep Pi as the
common default harness and model selection as a separate task-dependent choice.

## 1. Select the mode and preserve authority

Invoke only for an explicit combined execution request. Discussing a workshop or
asking how Council and Workshare could fit together does not start delegates.
Load `council-rubric`, `council` and `workshare` by skill name; report a missing
companion rather than guessing instructions or traversing sibling package paths.

Select **single-team** unless the user explicitly chooses **team-trials**:

- **Single-team:** freeze contracts, review the approach, execute one Workshare
  team, integrate and verify, then convene final Council review.
- **Team-trials:** review the common brief and proposed configurations, give two
  isolated teams the same whole task by default, compare their frozen candidates,
  select or deliberately synthesize a result, verify the integrated revision,
  then convene final Council review. Use more teams only when explicitly budgeted.

Treat a selected mode as run-scoped authority for its declared review/build stages,
not as permission to deploy, merge, publish artifacts or spend without bounds.
Check implementation authority separately when the user's request is review-only.
Do not turn a plain Workshare request into a workshop, or a workshop into trials,
without the corresponding invocation. Do not treat an installed skill as an
active background automation or quota-aware scheduler.

## 2. Freeze a common brief and stage-appropriate contracts

Fill [assets/workshop-plan.md](assets/workshop-plan.md). Identify the user's goal,
current baseline, excluded claims, artifact delivery requirements, constraints,
required tests and decision authority. Preserve existing work. Supply all teams
the same immutable base snapshot, task, approved clarifications and input evidence.
Record dirty inputs explicitly; prepared delegate worktrees do not include them.

Use `council-rubric` to prepare two linked contracts before candidate results:

1. **Plan-review contract:** assess whether the brief, interfaces, risks,
   verification strategy and configurations are suitable to attempt.
2. **Feature-acceptance contract:** assess the eventual integrated feature using
   required gates, anchored quality criteria, project-selected targets/floors,
   evidence, reviewer policy and reopening rules.

Share the same frozen feature contract across all trial teams. Reuse stable
requirements while distinguishing claims and evidence by stage. Do not give a
plan a pass on tests of code that does not yet exist, or call approval to attempt
an approach proof of working software. Record the user's selection or existing
project authority for each frozen contract; keep unapproved drafts provisional.
Do not silently invent approval or lower requirements after seeing a candidate.

Set the comparison rule before launch: required gates first, then the selected
quality thresholds and the user's tradeoffs such as maintainability, waiting,
repair burden and resource cost. Choose applicability and tie-breakers in advance.
Include the baseline when it is a valid alternative. Define candidate selection
eligibility separately from final feature acceptance: use the applicable candidate
checks to choose a provisional result, leaving final-review requirements pending
until Council sees the integrated revision. Keep unknown measurements unknown;
do not convert missing evidence to a pass or fabricate one joint score.

## 3. Allocate models, isolation and one global budget

Read [references/team-trials.md](references/team-trials.md) for configurations,
controlled comparisons and failure examples. Use Pi by default for builders and
reviewers, resolving exact models, runnable instances and supported options for
each role. Keep the active coordinator's actual harness visible; delegate build
leadership to Pi when an all-Pi run requires it. Choose workers with Workshare's
routing policy and reviewers with Council's independent-provider policy. Honor
explicit preferences without making one model permanently planner or builder.

Start small. For single-team, use a lead who implements plus one worker. For
trials, use two such teams with meaningfully different assignments, models,
reasoning settings or supported coordination patterns. Keep one integrator per
team. Do not count renamed identical rosters as different experiments. Keep
reviewer instances separate from builders; fresh contexts matter even when the
same model families appear in both rosters. Do not claim statistical independence
or blind evaluation merely because sessions differ.

Declare finite limits across the whole run, not separately resetting limits for
every child or phase. Without another user budget, allow:

- One plan-review round and one final-review round, plus at most one additional
  full or scoped recheck shared across those stages: at most three rounds total.
- Two active builders in single-team mode or four in two-team trials, including
  each team lead but excluding an idle overall coordinator.
- One initial launch per builder and at most one replacement/repair launch per
  team: three builder launches for one team or six for two teams.
- At most one candidate repair cycle per team, within those launch counts. Do not
  use that allowance to start a new third implementation or expand the task.

Record phase slices, reviewer multiplicity, nested delegation permissions and
optional enforceable deadlines. Keep reviewer launches within their declared
round/roster budgets too. Count actual activity if the coordinator also builds.
Queue work when concurrency is constrained; do not secretly remove a required
reviewer or team. Report incompatible budgets before launch. Do not assume unused
subscription tokens, automatic quota visibility or permission for paid fallback.

Create a local JSON plan using the shape of
[assets/team-trials.example.json](assets/team-trials.example.json), then run:

```bash
python3 scripts/check_plan.py /path/to/local-plan.json
```

Resolve this command relative to this skill's directory. Replace synthetic IDs
and approval references; never launch the example. Use the checker for structural
admission only: it checks shared inputs, declared budgets, roster fields and
obvious configuration collisions. It does not authenticate models, verify approval
truth, allocate isolated workspaces, enforce runtime permissions or launch agents.
Require those checks independently. Do not claim successful admission is delivery.

## 4. Convene preflight Council, then release build work

Hand the selected contract, frozen brief/design snapshot, configuration plan,
evidence and allocated review budget to `council`. Keep reviewers read-only and
independent. Include review of the existing artifact when the task starts from
one; consolidate its findings and the approach review into one prioritized work
list, frozen identically for all teams before they fork. Treat baseline defects
as repair inputs, not a requirement that the unmodified baseline already passes
the final feature gates. Require concrete objections, missing proof and acceptance
conditions, not a vote about a favorite provider. Reconcile evidence and address authorized
plan gaps within the remaining budget. Freeze any approved contract change before
building, distribute the same clarification to every team, and retain history.

Stop blocked if the plan-review stopping rule is not met, a named capability is
unavailable, required evidence is missing or the budget is exhausted. Do not
launch expensive trials just because reviewers returned positive prose. Record
which exact plan snapshot was accepted to attempt; retain the separate unproven
feature claim. Avoid repeated owner approval for ordinary work already within
these frozen permissions and requirements.

## 5. Run Workshare teams against identical task inputs

Hand each team its configuration, common task/snapshot/feature contract, resource
allocation and remaining budget. Use Workshare's work packets, ownership,
verification and result contracts. Keep the team lead implementing independent
work while its workers produce useful feature contributions. Do not force a
planning-only lead or a test-only worker role onto every configuration.

Use runtime-owned isolated writable checkouts and independent mutable resources.
Prevent candidate-to-candidate patch or reviewer feedback exchange until their
initial candidates are frozen; otherwise record the loss of independence. Share
only approved common clarifications, applying them to all teams. Use a single
controller for shared resources and global counters. Enforce permissions through
the runtime, not role descriptions. Keep credentials and private transcripts out
of artifacts shared with another provider or published in the skill source repo.

Authorize team-lead child spawning explicitly and only within allocated slots
when the runtime supports it. Otherwise let the root dispatch flatly for each
logical team and report that topology. Never bypass nesting/isolation limits with
shell agents or new top-level threads. Follow runtime completion/cancellation
rules instead of adding polling loops or services. On interruption, reconcile
existing task IDs, states and artifacts before resuming; do not duplicate work.

## 6. Compare evidence and integrate one coherent feature

Freeze each team's candidate commit or artifact manifest and actual configuration.
Run the same authorized evaluator against each candidate and record environment,
command, exit status, missing checks, failures and resource observations in
[assets/comparison.md](assets/comparison.md). Distinguish single-agent candidate
assessment from Council consensus. Do not convene extra Councils for every team
unless that work and its budget were explicitly selected.

Reject candidates that fail mandatory requirements; leave missing evidence pending.
Choose a provisionally eligible candidate under the frozen selection rule, or
stop with no winner when none qualifies. Keep final-review gates pending; do not
label candidate selection or the least-bad failure accepted delivery. Report
unequal time, repair or compute allocations as tradeoffs, not equal-budget proof
that one configuration is universally better. Treat one run as a useful local
routing observation, not a model benchmark.

Prefer a coherent candidate over blindly merging every team's patch. Synthesize
only complementary changes justified by evidence, preserving provenance and
checking interface conflicts. Treat any synthesis, cherry-pick or repair as a
new integrated revision. Re-run affected source, integration, package and user
journey checks; invalidate dependent candidate evidence. Do not average candidate
scores into a score for code no reviewer has seen.

## 7. Convene final Council on the actual integrated revision

Prepare the final artifact manifest, feature-contract version, integrated test
results, provenance, known limitations and remaining review budget. Start fresh
reviewer tasks through `council`, separate from builder sessions. Send everyone
the same final snapshot and evidence. Use `council-rubric` to preserve per-reviewer
criteria, gate judgments, disagreements, coverage and exact claim/stopping result.
Do not pass plan-review or candidate-only evidence off as final integrated review.

Repair only within authorized scope and remaining global budgets. Reopen affected
criteria/gates and use a fresh scoped review task when permitted; do not reset a
three-round budget for every revised commit. Stop accepted only when the frozen
feature rules are satisfied, or blocked with the smallest next action otherwise.
Keep acceptance separate from any later merge, deployment or publication decision.

Finish with contracts and snapshot IDs, configurations actually run, each team's
retained/rejected contributions, comparison limits, integrated checks, separate
preflight/final review records, all budget use and pending work. Record useful
routing lessons without secrets or transcript dumps. Do not claim provider-side
reasoning, quota utilization, comparative speed or production readiness that was
not observed. Keep local run artifacts out of the public skills repository unless
the user separately authorizes publishing a sanitized example.

## Resources

- [references/team-trials.md](references/team-trials.md): configuration examples,
  fair comparisons, stage boundaries and bounded failure handling.
- [assets/workshop-plan.md](assets/workshop-plan.md): authority, contracts,
  topology, isolation, budgets and phase ledger.
- [assets/team-trials.example.json](assets/team-trials.example.json): synthetic
  structural example, not runnable models or real approval evidence.
- [scripts/check_plan.py](scripts/check_plan.py): standard-library plan checks;
  no runtime scheduling or permission enforcement.
- [assets/comparison.md](assets/comparison.md): per-candidate evidence, selection,
  integration provenance and final-review handoff.
