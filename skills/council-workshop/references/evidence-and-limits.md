# Workshop and team-trial evidence

Research checked on 2026-11-11. The reviewed-build-reviewed lifecycle is an
engineering synthesis. No cited study validates these four skills together,
the default headcounts/round caps, Pi routing or a current model roster.

## Parallel candidates need dependable selection

[CodeMonkeys, 2025, v2](https://arxiv.org/abs/2501.14723v2) combines independent
patch attempts, bounded serial refinement, generated tests and a separate
execution-informed selector. On 500 SWE-bench Verified issues, the same pool of
ten candidate patches gives:

| Outcome | Resolved issues |
| --- | ---: |
| Expected random selection | 45.8% |
| Implemented selection procedure | 57.4% |
| Oracle coverage: any candidate correct | 69.8% |

The last row is an upper bound assuming perfect selection, not an implemented
result. This comparison isolates selection over the same pool; it is not an
equal-compute test of one versus ten agents. A separate heterogeneous ensemble
reaches 66.2% selected resolution versus 62.8% for its best member. Do not mix the
two candidate pools or present these historical results as today's leaderboard.

[Large Language Monkeys, 2024](https://arxiv.org/abs/2407.21787) shows growing
candidate coverage with repeated attempts. Domains with reliable verifiers can
benefit most; without dependable selection, a correct candidate may be lost.
Pass-at-k coverage is not delivered pass-at-one performance.

[AFlow, 2024, revised 2025, v4](https://arxiv.org/abs/2410.10762v4) searches
workflow configurations using execution feedback. It provides a precedent for
measuring alternatives, not proof that duplicating every one-off feature is
cost-effective. Workflow tuning and final evaluation should use distinct cases
when making general configuration claims; do not tune to the held-out answers.

## Task fit and convergence remain separate questions

[Towards a Science of Scaling Agent Systems, v3, 2026-04-08](https://arxiv.org/abs/2512.08296v3)
is a preprint reporting both large gains and degradation under different task
structures across 260 configurations and six benchmarks. Coding subsets have
20 issues per configuration and wide uncertainty. It supports investigating
architecture/task fit, not a universal multi-agent or single-agent winner.

Anthropic's [code-review report, 2026-10-15](https://claude.dev/blog/solving-code-review-at-anthropic/)
reports fewer review rounds after bundled convergence changes, including a
three-round reconsideration cap, narrower re-reviews and duplicate suppression.
This observational account does not isolate an optimal cap or validate our
preflight/final budget allocation. Required human review and repository gates
remain in force.

## Operational inference for this package

- Use a single team by default. Require explicit trial authority and a concrete
  reason for duplicating the whole task. Sequential or inseparable work may be
  better kept with one agent outside this workflow.
- Freeze the shared task/work-list, evaluator, acceptance contract, identity
  handling, presentation order and selection rule before candidates. Give teams
  identical inputs and shared preflight findings, not privately tailored help.
- Declare the comparison basis: `delivery-only`, `equal-budget-quality` or
  `time-to-accepted-quality`. The first selects a useful result without a
  controlled-performance claim. The second needs genuinely comparable resources;
  the third needs a common acceptance bar and observed timing. Effort names,
  identical launch caps and subscription tiers do not establish equal compute.
- Include a capable single-agent baseline when studying the value of coordination,
  or label its absence as a limit. Repeat matched tasks and preserve holdouts
  before drawing general configuration conclusions. A one-task delivery trial
  can still be useful without claiming benchmark evidence.
- Check the selector against known cases when available. Prefer reproducible
  behavioral evidence over candidate self-reports; mask team labels and balance
  order where feasible, and disclose remaining identity/feedback exposure.
- Reject failed candidate gates; leave missing proof pending. Keep candidate
  selection provisional until the integrated artifact passes its own checks and
  final review. Synthesis creates a new revision, not an average score.

The JSON checker verifies declarations and structural references only. It cannot
prove approvals, decomposition quality, fair resources, masking, independent
contexts, isolation, provider availability, runtime counters or actual acceptance.
