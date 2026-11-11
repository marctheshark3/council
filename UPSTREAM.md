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

The repo now distributes these four skills only. It is not a fork of T3 Code or
Pi, does not bundle other T Stack workflows, and does not imply endorsement by
Theo Browne, T3 Tools, Pi or MEGA.dev.
