# Upstream credit and changes

## Original Council

The Council skill is derived from **Theo Browne's
[T Stack](https://github.com/t3dotgg/tstack)**, the agent skills he uses with
Claude Code, Codex, and T3 Code.

- Baseline revision: [`1085050f3baed1ac724caa4a8166145fb2ac88af`](https://github.com/t3dotgg/tstack/commit/1085050f3baed1ac724caa4a8166145fb2ac88af).
- Original file: [`skills/council/SKILL.md`](https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/council/SKILL.md).
- Original [MIT license](https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/LICENSE): copyright (c) 2026 Theo Browne.

Theo supplied the core pattern: three strong models from different providers,
independent reviews, separate scores, useful disagreement, and follow-up reviews
without scope creep. The copyright and full MIT terms remain in
[`skills/council/LICENSE`](skills/council/LICENSE) and the root license.

## What this adaptation changes

| Area | Changes relative to that baseline |
| --- | --- |
| Invocation | Launch only for an explicit Council run or declared review stage of an explicitly invoked Council Workshop; discussion and rubric-only work do not launch delegates. |
| Authority | Pre-review fixes require existing implementation/test authorization; a review-only request preserves the snapshot. |
| Finish line | Declare a finite budget. Without another budget, stop after at most three full/scoped rounds; report accepted or blocked rather than looping indefinitely. |
| Harness and effort | Default to Pi, require authorization for another harness, resolve exact model/harness controls, explicitly request supported `xhigh` or disclose a `high` effort fallback, and record requested versus verified settings. |
| Opt-in reasoning | GPT `token-max` pairs Pi and native Codex for the same model; reasoning ceilings and speed/service tiers are resolved separately. No literal token-budget guarantee. |
| Rubric integration | Share one frozen contract, artifact snapshot, and evidence pack; retain per-reviewer scores, gate results, dissent, and scoped recheck accounting. |
| Evidence and convergence | Preserve independent first passes, verify rather than vote away defects, track/deduplicate finding IDs, and focus subsequent review on deltas and affected dependencies. |

## Council Rubric

`skills/council-rubric` is a new companion from this project's contributors,
not a skill copied from T Stack. It adds:

- Project-specific criteria with observable anchors, weights, and optional floors.
- Independent acceptance gates: pass, fail, pending, or authorized not-applicable.
- Missing-evidence coverage without invented scores or silent reweighting.
- Versioned contracts, traceable scorecards, finite stopping rules, and reopening
  conditions tied to changed dependencies.
- Copyable templates and explicitly synthetic CAD/software examples.

The initial standalone release preserved the Council and rubric resources and
added public packaging, attribution and installation checks. The subsequent
Workshare release adds the composition described below; it does not replace
Council's independent-review contract with builder self-assessment.

## Workshare and Council Workshop

`skills/workshare` and `skills/council-workshop` are new companion packages, not
additional skills copied from T Stack. They add Pi-first capability-aware work
allocation, bounded handoff/result contracts, an implementing team lead, isolated
writers, single-team review/build/review and explicitly selected whole-task team
trials. A standard-library checker validates structural run-plan invariants; it
does not implement a scheduler, permission boundary or multi-agent protocol.

Conceptual references include MEGA.dev's **S02E04: Multi-Agent Collaboration**
and its [public multi-agent examples](https://github.com/MEGA-DOT-DEV/examples),
including the distinction between subagents as a delegation mechanism and
hierarchy, team and swarm as coordination patterns. Handoff context, ownership,
shared-resource conflicts, task states and deterministic boundaries inform these
packages. The lesson and its illustrations are not redistributed, and its
illustrative efficiency/activity figures are not claimed as measured results
for this project. No A2A service, peer bus or durable engine is bundled.

## Research basis and limits

A targeted primary-source review on **2026-11-11** informed the follow-up. The
sources support ingredients, not the exact composition or a measured gain from
these instruction packages. They are linked with their relevant instructions so
each independently installed skill retains the evidence and its limitations:

| Package reference | Sources and what they inform |
| --- | --- |
| [Council evidence](skills/council/references/evidence-and-limits.md) | Theo's pinned instructions; ReConcile; Debate or Vote?; Voting or Consensus?; Anthropic's code-review account. Independent first passes, evidence-backed reconciliation and bounded convergence. |
| [Rubric evidence](skills/council-rubric/references/evidence-and-limits.md) | G-Eval; Prometheus; Judging LLM-as-a-Judge. Structured criteria, reference cases, judge bias and the distinction between preference scores and correctness. |
| [Workshare evidence](skills/workshare/references/evidence-and-limits.md) | Anthropic, Cursor and Cognition engineering reports; Scaling Agent Systems v3; MAST. Task fit, context/resource boundaries, verification and accepted-contribution measurement. |
| [Workshop evidence](skills/council-workshop/references/evidence-and-limits.md) | CodeMonkeys; Large Language Monkeys; AFlow; Scaling Agent Systems v3; Anthropic's code-review account. Candidate generation versus selection, controlled comparison limits and integrated review. |

Distinguish peer-reviewed benchmark results, preprints, practitioner instructions
and observational vendor reports. Different study populations, metrics, baselines
and compute budgets do not form one leaderboard. No transcript-backed claims are
made about videos whose full captions were unavailable. Facts are summarized
with links; research papers, course text and raw run transcripts are not bundled.

The default three-review-round cap, builder counts, schema-2 admission fields,
Pi-first policy and role allocations are **this project's operating choices**,
not empirically optimal constants. A score of 9/10 is not a calibrated 90%
correctness probability; a reproducible minority defect can outweigh a majority
miss. The JSON checker verifies declarations/references, not real approval,
provider availability, isolation, fresh contexts, fairness or acceptance.

No end-to-end workshop, active-user installation, latency/quality improvement or
universal GPT/Grok role ranking has been established by the package's local
checks. Those require separately authorized trials and delivery verification.

The repo now distributes these four skills only. It is not a fork of T3 Code or
Pi, does not bundle other T Stack workflows, and does not imply endorsement by
Theo Browne, T3 Tools, Pi or MEGA.dev.
