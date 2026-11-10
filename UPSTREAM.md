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
| Invocation | Launch only for an explicit Council run; discussion and rubric-only work do not launch delegates. |
| Authority | Pre-review fixes require existing implementation/test authorization; a review-only request preserves the snapshot. |
| Finish line | Declare a finite budget. Without another budget, stop after at most three full/scoped rounds; report accepted or blocked rather than looping indefinitely. |
| Harness and effort | Prefer Pi where available, resolve exact model/harness controls, explicitly request supported `xhigh` or disclose a `high` fallback, and record requested versus verified settings. |
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

Both entrypoints and the rubric resources are preserved from the working
adaptation; this standalone release adds packaging, installation documentation,
license coverage, and installation checks, not a new review algorithm.

This repository distributes only these two skills. It is not a fork of the
T3 Code application, does not bundle other T Stack workflows, and does not imply
endorsement by Theo Browne or T3 Tools.
