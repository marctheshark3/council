# Worksharing evidence and limits

Research checked on 2026-11-11. Match coordination to the task, not to unused
model capacity. No source below demonstrates this exact package, a current
GPT/Grok hierarchy or a productivity gain from the Pi harness.

## Where parallel work has helped

- Anthropic's [multi-agent research system, 2025-06-13](https://www.anthropic.com/research/multi-agent-research-system)
  reports 90.2% improvement over a single Opus 4 agent on an internal research
  evaluation, especially breadth-first searches. It is not compute-matched.
  Reported multi-agent token use is about 15 times ordinary chats, not 15 times
  a single-agent run. The authors explicitly flag tightly coupled coding and
  synchronous waits as limitations.
- [Cursor's long-running coding experiments, 2026-01-14](https://cursor.com/blog/scaling-agents)
  describe shared-file/lock coordination in which twenty agents delivered the
  effective throughput of two or three. Planner/worker structure worked better;
  a separate integrator role became a bottleneck. Large line counts and long
  runs do not by themselves establish correctness or developer productivity.
- [Cursor/NVIDIA kernel optimization, 2026-04-14](https://cursor.com/blog/multi-agent-kernels)
  reports 38% geometric-mean kernel speedup over a single-agent-optimized PyTorch
  baseline across 235 problems. The system used three weeks and 27 B200 GPUs.
  This measures kernel execution, not development speed, and changed tools,
  implementation freedom and compute do not isolate an agent-count effect.

## Context and task structure constrain the gain

Cognition's [Don't Build Multi-Agents, 2025-06-12](https://cognition.com/blog/dont-build-multi-agents)
is a practitioner argument about context loss and incompatible implicit
choices, not a universal experimental prohibition. Its later [Devin usage
account, 2026-02-27](https://cognition.com/blog/how-cognition-uses-devin-to-build-devin)
recommends isolated sessions, explicit postconditions and verification. Isolated
sessions are not necessarily a shared-state peer swarm.

[Towards a Science of Scaling Agent Systems, v3, 2026-04-08](https://arxiv.org/abs/2512.08296v3)
is a preprint comparing 260 configurations on six benchmarks with standardized
tools/prompts and reported compute matching. Centralized coordination gains
80.8% relative on Finance Agent and loses 50.3% relative on PlanCraft. All tested
multi-agent variants degrade on PlanCraft. Its coding subsets have only 20
issues per configuration and wide uncertainty; do not turn the fitted capability
threshold or architecture ranking into a universal rule.

[Why Do Multi-Agent LLM Systems Fail?, 2025, v3](https://arxiv.org/abs/2503.13657v3)
analyzes 1,600-plus traces across seven frameworks. Its fourteen failure modes
span design, agent alignment and verification. It does not establish that a
particular handoff template removes those failures.

## Operational inference

Before launching, name the independent work, freeze shared decisions/interfaces,
and explain how an accepted contribution will be checked. If the useful actions
are sequential or the common context cannot be bounded, recommend single-agent
execution instead of inventing a parallel assignment. Keep an implementing lead,
not a permanent planning-only provider; make responsibilities task-dependent.

Prefer a few cohesive packets, independent mutable resources and observable
handoffs. Track accepted/repaired/rejected contributions, time to useful evidence,
time to accepted integration, waiting and repair burden. Distinguish observed
values, estimates and unknowns. A full subscription is not a performance result;
spending more tokens is not success. Repeat matched tasks before generalizing a
routing preference, and separate quality at fixed resources from time to an
accepted result. These are evaluation recommendations, not measured package gains.
