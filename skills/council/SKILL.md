---
name: council
description: 'Convene multiple model providers when the user explicitly asks to "run council", "council review", or "ask the council" for review or feedback. Do not launch reviewers for discussion of Council or requests to define, assess or recheck a "council rubric" alone; use council-rubric for those. An explicit Council run against a rubric uses both skills.'
---

# Council

## Invocation and rubric companion

Convene reviewers only for an explicit Council run, not merely because the word
"council" appears. For rubric drafting, standalone assessment or gate rechecks,
load `council-rubric` by skill name without launching delegates. For "run council
against rubric v1", use both skills: keep Council's routing and reviewer policy,
and give each reviewer the same frozen rubric, artifact snapshot and evidence.
Do not resolve sibling skills through relative filesystem paths.

## Prepare the review

Within existing implementation and test authorization, address outstanding PR
comments, fix known issues and run relevant checks before an audit. Snapshot the
updated implementation for review; do not defer authorized known fixes until
reviews return. For a read-only review, report known issues and assess the
requested snapshot without altering it. If the user wants to discard the
implementation and explore new ideas, skip fixes to code being replaced.

Before launching reviewers, use the approved rubric's finite review budget or
declare a finite run budget. If none is specified, allow at most three rounds:
the initial review plus two follow-ups, full or scoped. Record full rounds and
scoped rechecks separately, but count both against this default budget. Stop
earlier when acceptance is established or required evidence/access is unavailable;
stop blocked at the limit with remaining findings and the smallest next action.
Do not start extra rounds without a new authorized budget.

By default, bring in three delegates to help with the user's request, usually
for review or feedback. Opt-in token-max can add a second harness for a GPT
member as described below. Use one strong model from each of three different model providers,
at extra-high reasoning effort as resolved below. Different model providers
still count when all three delegates use the Pi harness. If the user's
instructions name council members, use those. Otherwise pick the latest
flagship model from each provider, for example Claude Opus, GPT Sol, and
Gemini Pro.

## Select the harness and reasoning

Honor explicit user choices of model, harness, and reasoning level first.
Otherwise prefer Pi when it offers the selected model and can run the delegate,
with the additional Codex GPT delegate in opt-in `token-max` mode below.
If Pi cannot run that model, use an available native harness for the same model
and disclose the fallback. Do not silently replace a model, bypass an explicit
harness choice, or change harnesses after a launch error; report the blocker.
If you cannot reach three model providers, or a named member is unavailable,
report it instead of substituting.

In T3 Code, use `orchestrator_capabilities` to resolve the model, runnable
provider instance, and that exact model's supported options. Use the catalog's
provider-qualified model ID when selecting Pi. Set `target.providerInstanceId`
and `target.model` explicitly in each `delegate_task` call.

Resolve reasoning separately for each selected model and harness:

- Default to `xhigh` when that model advertises it. Do not select `max`,
  `ultra`, or another higher level just because it is available; only an explicit
  reasoning override or the opt-in `token-max` mode below can raise this default.
- If `xhigh` is absent but `high` is supported, explicitly set `high` and
  disclose the reduced-effort fallback. If neither is supported, report the
  limitation rather than silently accepting a lower level or an unknown default.
- Pass the setting explicitly in `target.options`, using the advertised option
  key and value. Pi uses `thinking`; native harnesses may instead expose
  `reasoningEffort` or `effort`. For example, a Pi model advertising `xhigh`
  uses `target.options: {"thinking": "xhigh"}`. Do not pass Pi's key to a
  native harness or assume every model on one harness supports the same levels.
- Honor an explicit user reasoning level only if the selected model and harness
  support it. Otherwise report the unsupported setting; do not silently downgrade.

Thinking levels are model-specific controls, not equal token budgets or a
promise of equivalent reasoning across providers. Use the harness's advertised
mapping; do not invent token budgets or translate special effort names by guess.
Prompt text asking a delegate to "think harder" is not a substitute for setting
the option, and omitted options can inherit an unintended default.

Start one delegate per model in parallel with `delegate_task`, plus the extra
Codex delegate when GPT token-max is requested. Elsewhere, use
the harness's subagent tools and their documented model/effort controls. Apply
the same preferences only where those tools support them; report any inability
to select Pi or set reasoning rather than claiming the preference was enforced.

Record each delegate's exact model, harness, and explicitly requested reasoning
option in the review results, including any fallback. Distinguish requested
settings from runtime settings actually verified; do not claim provider-side
execution details that the tools do not expose.

## Opt-in token-max mode

Treat "token-max for <member>" or "max out reasoning for <member>" as a
run-scoped request to maximize that member's supported reasoning. For a GPT
member, run the same model through BOTH Pi and native Codex, not Codex instead
of Pi. Treat "token-max fast for <member>" as the same reasoning request with
fast service as specified below, not less reasoning. For example:
"Council review, token-max fast for GPT."

### Scope and paired GPT delegates

- Apply the mode only to the named member in this council run, including fresh
  review rounds for that member. Keep all other members at the normal `xhigh`
  policy. Do not save global defaults or carry the override to a later run.
- Resolve the member unambiguously before launch. If the request names no member,
  or matches several, ask which member to maximize. Apply it to everyone only
  when the user explicitly requests "token-max for all council members".
- For a GPT member, retain its Pi delegate and add a native Codex delegate for
  the exact same GPT model, resolving each harness's catalog ID separately.
  Maximize each delegate's reasoning using that harness's supported controls.
  This normally expands a three-member council to four delegates, not four
  model providers. Keep the other two model providers; the GPT pair counts as
  one model provider. Do not create a duplicate Codex delegate if already paired.
- If either harness cannot run that GPT model, report the incomplete pair
  before launching it rather than silently replacing a model, dropping a
  harness or claiming the paired mode was delivered. An explicit user request
  to use only one harness overrides the paired expansion.
- Keep Pi-first and a single delegate for non-GPT members. Explicit user harness
  and exact supported reasoning choices still win over the mode defaults.

### Reasoning and speed are independent

- For Codex, prefer `reasoningEffort=ultra` when the selected model advertises
  it. Otherwise select its highest supported level in the order `max`, `xhigh`,
  `high`, `medium`, `low`, and report that `ultra` is unavailable for that model.
- On Pi, choose the highest supported level in the order `max`, `xhigh`, `high`,
  `medium`, `low`, `minimal`, excluding non-reasoning `off`. A model advertising
  `max` uses `thinking=max`; a model whose ceiling is `xhigh` stays there.
- On another harness, use its documented model-specific ordering and option
  key. Do not infer the ranking of special names such as `ultrathink` from
  spelling or catalog listing order. If the maximum cannot be established or
  no reasoning control is available, report the limitation rather than claiming
  token-max was set. An explicit supported exact reasoning level overrides the
  mode's effort selection for that member.
- Plain token-max means regular service. For Codex, explicitly set
  `serviceTier=default`; token-max fast sets `serviceTier=priority`, while
  retaining the same resolved reasoning effort. Do not inherit priority service
  from the parent, and do not interpret "fast" as a weaker or faster model.
- For the GPT pair, the fast modifier selects Codex priority service only.
  Keep Pi at its resolved maximum reasoning and disclose that Pi has no
  advertised fast-tier control when that is the case. Do not send Codex's
  `serviceTier` to Pi or claim the entire pair is on priority service. If Pi
  exposes no regular-service override, report its speed as uncontrolled by
  the delegation tool, not verified regular service.
- For non-GPT members, use only their advertised/documented speed control, such
  as `fastMode=true` for fast or `fastMode=false` for regular service. If fast
  service is requested but cannot be selected, report that limitation before
  launching that member; do not silently change its harness. If no regular
  override exists, disclose that speed could not be explicitly enforced.
- Pass reasoning and any supported speed setting explicitly in `target.options`.
  Report each delegate's model, harness, `token-max` or `token-max fast`, exact
  reasoning setting and speed selection, including an already-reached ceiling.

For a GPT model advertising Pi `max`, Codex `ultra` and both Codex service tiers:

| Member request | Pi delegate options | Additional Codex delegate options |
| --- | --- | --- |
| No mode override | `{"thinking":"xhigh"}` | None |
| token-max | `{"thinking":"max"}` | `{"reasoningEffort":"ultra","serviceTier":"default"}` |
| token-max fast | `{"thinking":"max"}` | `{"reasoningEffort":"ultra","serviceTier":"priority"}` |

These are routing examples, not guarantees that every GPT model supports these
levels. Rediscover each model/harness's options for every launch. Effort labels
across harnesses need not represent equivalent budgets. Report the GPT pair in
separate review rows, such as "GPT Sol via Pi" and "GPT Sol via Codex", with
separate scores and findings; never merge their scores or invent a joint score.

This mode requests more available reasoning capacity, not a guaranteed token
count or unlimited spending. Do not invent `maxTokens`, output-length or
thinking-budget parameters that the delegation tool does not expose, edit
provider configuration to bypass limits, or make the delegate pad its answer,
repeat work or run extra rounds merely to consume tokens. The explicitly
requested GPT pair is the only automatic extra delegate. Keep the task,
concise evidence-based reporting and normal review stopping conditions intact.
If a literal token budget is requested, distinguish it from this effort mode
and report when the available tools cannot enforce it.

## Review and report

Give each delegate the request and relevant context. For review or feedback,
keep their work read-only. Collect their responses and summarize the useful
findings, disagreements, and recommended next steps.

For a code review, ask each delegate for a score out of 10 unless the selected
rubric specifies a different scale. When using `council-rubric`, require its
per-criterion scores, gate judgments, evidence and explicit stopping-rule result;
a scalar score alone is insufficient. Include the rubric version, artifact
snapshot and scorecard references in the review report and PR description.
Keep each delegate's results separate, including paired GPT delegates.

Count each full review pass as one round.
A fresh full review after fixes starts a new round. Label a scoped gate recheck
as scoped rather than claiming another complete review of the whole artifact.

If the work ends in a pull request, put the results in the PR description.
Put this section before the model and harness line at the end:

```markdown
## Council review

Rounds: 2

| Delegate | Harness | Requested reasoning | Round 1 | Round 2 |
| --- | --- | --- | --- | --- |
| Claude Opus | Pi | thinking=xhigh | 7/10 | 9/10 |
| GPT Sol | Pi | thinking=xhigh | 8/10 | 10/10 |
| Gemini Pro | Pi | thinking=xhigh | 7/10 | 9/10 |
```

The table is a format example, not a model availability or option guarantee.
Use actual model IDs and settings for each round; note changes between rounds.
If a delegate gives no score, write `no score`. Do not invent one.
If the PR is open, edit the description. Do not post a comment for this.
If there is no PR, put the same results in the final reply only.

If you agree with their recommendations, make authorized changes and request a
fresh review of the affected scope. With an approved rubric, use its reopening,
acceptance, disagreement and review-budget rules; stop accepted or blocked as
those rules require instead of looping for enthusiasm. Do not average away a
demonstrated failure or lower the bar after seeing the scores. Without a rubric,
continue until all delegates are satisfied within the declared finite budget;
report blockers at the limit rather than implying consensus or looping
indefinitely. Respect user limits and access constraints in either mode.

Do not let repeated reviews result in scope creep. It is your job to fight to
keep scope limited.
