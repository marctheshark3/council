# Review evidence and limits

Research checked on 2026-11-11. Use these sources to explain design choices, not
to promise a performance gain or certify a particular provider roster. This is a
targeted primary-source review, not a systematic literature review. No paper
below validates this exact skill, Pi routing or the combined workshop lifecycle.

## Practitioner origin

Theo Browne's [T Stack Council instructions at the credited baseline](https://github.com/t3dotgg/tstack/blob/1085050f3baed1ac724caa4a8166145fb2ac88af/skills/council/SKILL.md)
provide the core pattern: different model providers, parallel read-only reviews,
separate findings/scores and review after accepted fixes. This is practitioner
guidance, not a controlled comparison. Preserve its MIT attribution; do not
attribute this adaptation's finite budgets or evidence policy to a research trial.

## Independent answers versus discussion

- [ReConcile, ACL 2024, v3](https://arxiv.org/abs/2309.13007v3) reports benefits
  from diverse model families, independent initial answers, bounded discussion
  and weighted voting across seven reasoning benchmarks. Older model generations
  and mostly small benchmark subsets limit transfer to repository review.
- [Debate or Vote?, NeurIPS 2025 Spotlight, v2](https://arxiv.org/abs/2508.17536v2)
  finds that majority voting accounts for most gains attributed to debate on its
  seven NLP benchmarks. Its formal belief-update model is not a universal proof
  that communication never helps.
- [Voting or Consensus?, Findings of ACL 2025](https://aclanthology.org/2025.findings-acl.606/)
  finds task-dependent decision-protocol effects; additional discussion rounds
  before voting reduced performance in its experiments. Do not infer that one
  voting rule is optimal for every task.

**Operational inference:** collect independent first passes before exposing peers'
conclusions. Reconcile factual claims using the artifact and tests. Voting over
answers on a benchmark is not a license to vote away one reproducible bug.
Different providers and fresh sessions do not prove statistically independent
errors. Retain substantive dissent and unknown evidence.

## Review convergence

Anthropic's [How the Claude Code team does code review, 2026-10-15](https://claude.dev/blog/solving-code-review-at-anthropic/)
describes parallel bug hunters, separate finding verification, automated checks,
risk-based human approval and final-state checks. It reports a PR exceeding fifty
review/fix rounds. Following a bundle of convergence changes, mean reviews to
pass fell from 2.08 to 1.32. The bundle included a three-round reconsideration cap,
narrower re-reviews and duplicate-finding suppression.

This is an observational vendor account, not an isolated causal test of a
three-round optimum or a cross-provider Council. Its process supports tracking
rounds and repair costs alongside useful findings, not removing human review
requirements or existing repository gates.

**Operational inference:** identify findings across rounds, distinguish new
regressions from pre-existing issues, recheck the delta and affected dependencies,
and stop low-value churn. Broaden review when the impact cannot be bounded; a
scoped recheck is not a complete re-audit. The default budget is an operating
choice, not a research-derived constant. Repeated enthusiasm and rising scores
are not acceptance evidence.
