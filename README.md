# Council

Review, build together, and review the working result. Four composable agent
skills with **Pi as the default harness**, task-appropriate model selection,
evidence-based rubrics, and a finite finish line.

Council builds on **[Theo Browne's T Stack](https://github.com/t3dotgg/tstack)**.
The original multi-provider review pattern is his; this project adds explicit
invocation, bounded rounds, model/harness controls, rubric contracts, worksharing
and reviewed team trials. See [upstream credit and changes](UPSTREAM.md).

## Four skills, different jobs

| Skill | Purpose |
| --- | --- |
| [council](skills/council/SKILL.md) | Convene independent reviewers from different model providers and reconcile evidence. |
| [council-rubric](skills/council-rubric/SKILL.md) | Define or assess a versioned contract: anchored scores, required gates, evidence and reopening rules. |
| [workshare](skills/workshare/SKILL.md) | Keep a main agent implementing while bounded, model-selected workers contribute useful execution. |
| [council-workshop](skills/council-workshop/SKILL.md) | Compose rubric, plan review, Workshare teams, integration and final Council review. |

Subagents are a **delegation mechanism**. A team or swarm describes **coordination**.
Workshare usually uses lead-led parallel execution; Council uses independent
parallel review. Neither becomes a leaderless swarm merely by adding agents.
Pi is the harness for either workflow, not the coordination policy.

These are instruction packages, not a scheduler or a peer-messaging extension.
Plain Pi does not include built-in subagents; require a supported host delegation
API or an already selected extension that can launch Pi workers. T3 Code is one
supported host. Missing capabilities must be reported, not silently substituted.

## Choose a workflow

### Workshare: one useful team

> Workshare this feature using Pi. Prefer Grok for substantial bounded
> implementation while the main agent keeps coding. Verify the integrated result.

Choose models for the assignments rather than permanently assigning planning to
one provider and building to another. Start with a main agent plus one worker
when there is a genuinely useful split. Identify independent work and freeze
shared decisions/interfaces first; recommend single-agent execution when the
useful steps are inseparable or sequential. Keep writable workspaces isolated and
one integrator responsible for the result. No automatic Council or duplicated whole-feature implementations.

### Council Workshop: review → build → review

> Run council workshop in single-team mode using Pi. Freeze a project-specific
> rubric, review the approach, build with Workshare, then review the integrated
> feature. Stay within three total review rounds, including scoped rechecks.

Use linked but distinct claims: the plan is suitable to attempt, and the final
feature meets its acceptance contract. Preflight can review an existing artifact
as well as the approach; consolidate findings into the same frozen work list for
every team. Baseline defects become repair inputs, not a demand that the old code
already passes the final feature gates. A plan review cannot pass tests of code
that has not been built. A rubric can guide either execution or review.

### Team trials: same task, different worksharing configurations

> Run council team trials using Pi. Compare two Workshare configurations on the
> same feature and starting snapshot: balanced GPT/Grok ownership versus
> Grok-preferred implementation with GPT still contributing. Use the same frozen
> feature rubric, compare actual evidence, integrate one coherent result, and
> Council-review that exact revision.

```text
Common brief + frozen task/plan/feature/evaluator
                    │
            Council plan review
                    │
          ┌─────────┴─────────┐
          │                   │
     Workshare A         Workshare B
     balanced split      different allocation
     isolated writes     isolated writes
          │                   │
          └─────────┬─────────┘
             freeze + compare
                    │
         select / deliberate synthesis
                    │
          verify integrated revision
                    │
           Council final review
```

Use two teams only when explicitly selecting team-trials. Give both the same
whole task, inputs and feature-acceptance contract, but different assignments,
models, supported effort settings or coordination configurations. Do not let
teams copy each other's candidates before they are frozen. Report unequal
resource budgets and feedback contamination. Keep a valid baseline or return no
winner if alternatives do not qualify. Synthesis creates a new revision that
needs its own integration checks and final review; do not merge every patch.

Model family names above are examples, not selected catalog IDs, availability
claims or a universal ranking. Resolve exact models/options at run time. An
all-Pi request does not add native-harness delegates; Council's existing GPT
`token-max` cross-harness pair remains a separate, explicit opt-in.

### Standalone rubric and Council

> Council rubric: define the acceptance contract. Draft only; no reviewers.

> Run council against frozen rubric v1 for commit <sha>, at most two rounds.

Discussing workflows, drafting rubrics or asking how a team could operate does
not authorize launches. Explicitly selecting a workshop authorizes its declared
review/build stages within the frozen scope and budget, not deployment or merge.

## Research-informed, not research-certified

The [source notes](UPSTREAM.md#research-basis-and-limits) distinguish practitioner
methods, vendor engineering reports, preprints and peer-reviewed findings. Each
skill also carries its own linked evidence/limitations reference. Research
supports independent first passes, explicit criteria, task-appropriate parallelism
and dependable candidate selection; it does not validate this exact composition,
our default headcounts/round caps or any current GPT/Grok ranking.

Operationally: verify findings rather than voting away bugs; record judge identity
and order exposure; scope repeat review to changed behavior and dependencies; and
measure accepted work, waits, integration and repairs. Declare whether a trial is
useful delivery only, equal-budget quality or time to accepted quality. Equal
launch caps/effort names do not prove equal compute, and a candidate's completion
time is not its time to accepted integration. One feature is not a benchmark.

## Install

### Pi package

After reviewing the source and checking for existing same-name skills:

```bash
pi install git:github.com/marctheshark3/council
```

For a pinned revision, append `@<commit-or-tag>` to the git source. The manifest
exposes skills only: no extensions, install hooks or runtime dependencies. Pi's
package installation changes its package settings; it does not add delegation,
log into providers or enable background runs. Avoid simultaneously loading this
package and manually installed copies of the same skills.

In a fresh Pi session, invoke an entrypoint explicitly when needed:

```text
/skill:workshare this feature using Pi
/skill:council-workshop run single-team mode for this feature
/skill:council-workshop run team-trials for this feature with two configurations
```

### Portable skill folders

Clone the repo and choose **one** discovery directory:

```bash
git clone https://github.com/marctheshark3/council.git
cd council
```

| Agent | Typical user-scope directory |
| --- | --- |
| Codex or Pi | `~/.agents/skills` |
| Claude Code | `~/.claude/skills` |
| OpenCode | `~/.config/opencode/skills` |
| Grok | `~/.grok/skills` |

Honor the configured discovery root when it differs. Back up an existing
same-name skill outside discovery before replacing it, including T Stack's
`council`. Do not install duplicate names into roots one agent scans.

The Bash recipe below defaults to `~/.agents/skills`. Set `SKILLS_DIR` when needed.
It refuses any occupied package destination, including broken symlinks, before
copying any of the four packages:

```bash
(
  set -eu
  skills_dir="${SKILLS_DIR:-$HOME/.agents/skills}"
  mkdir -p "$skills_dir"
  for skill in council council-rubric workshare council-workshop; do
    if [ -e "$skills_dir/$skill" ] || [ -L "$skills_dir/$skill" ]; then
      printf 'Existing skill preserved: %s\n' "$skills_dir/$skill" >&2
      exit 1
    fi
  done
  cp -R skills/council skills/council-rubric skills/workshare skills/council-workshop "$skills_dir/"
)
```

Start a fresh session and confirm all four names are discovered. Project-local
installs use the agent's documented project skill directory instead. A portable
installation does not automatically make a non-Pi parent session a Pi agent.

## Contracts and limits

Start from the [rubric template](skills/council-rubric/assets/rubric-template.md),
[scorecard](skills/council-rubric/assets/scorecard-template.md),
[work packet](skills/workshare/assets/work-packet.md) and
[workshop plan](skills/council-workshop/assets/workshop-plan.md). The
[team-trials reference](skills/council-workshop/references/team-trials.md) explains
shared inputs, distinct configurations, comparisons and failure handling.

- Use runtime-owned isolated workspaces and permissions. A skill's instructions
  are not a sandbox; a worktree does not isolate databases, ports or services.
- Prefer Pi for every delegated role. Disclose unavailable models/controls and
  require explicit authorization for another harness or paid/priority fallback.
- Keep reviewers independent and read-only; use fresh review tasks instead of
  builder sessions. Report author/reviewer overlap and evidence limits honestly.
- Use global finite budgets. Workshop defaults to one plan review, one final
  review and at most one shared full/scoped recheck—not three rounds per phase.
- Default to two active builders and three builder launches for a single team,
  or four active builders and six launches for two teams; allow one repair cycle
  per team within those launch caps. Failed/replaced attempts consume budget.
- Do not infer quota or subscription capacity from model catalogs or installation.
  Measure useful accepted work, waiting and rework rather than burning tokens.
- Do not average away failed/pending gates, lower requirements after a result, or
  call candidate-only evidence a final integrated pass.
- Keep private task inputs, credentials and transcripts local. A public skill
  source repository is not a public destination for its users' run artifacts.
- A passing review does not authorize merge, deployment, purchase or publication.

Use the standard-library plan checker before an authorized workshop execution:

```bash
python3 skills/council-workshop/scripts/check_plan.py /path/to/local-plan.json
```

The [bundled JSON example](skills/council-workshop/assets/team-trials.example.json)
uses synthetic model IDs and approval references. It demonstrates structure only.
Schema 2 requires frozen common task, plan, feature and evaluator IDs; explicit
task-fit/trial reasoning, selection/resource/identity/order policy; independent
first-pass, evidence-based resolution and delta/dependency recheck declarations;
and a global review cap containing the phase slices. Teams must reference the
same task/evaluator as well as snapshot/rubric, and review-task slot IDs must be
unique across stages and separate from builder IDs. Typed budgets, explicit
rosters and obvious configuration collisions are checked too.

Schema 1 is rejected, not silently upgraded; follow the
[migration notes](skills/council-workshop/references/team-trials.md#migrate-a-schema-1-plan-deliberately).
The checker does not launch agents or prove task suitability, approval truth,
fair resources, masking, fresh runtime contexts, model availability, physical
isolation, runtime enforcement or feature acceptance. Provider accounts, billing
and delegation capability belong to your environment.

## Local checks

With Python 3.10+ and Bash:

```bash
python3 -m unittest discover -s tests -v
```

Tests exercise the documented copy installation, preservation of occupied paths,
resource links, licenses, portable package metadata and plan-checker behavior on
valid/invalid synthetic cases. They do not launch models or prove end-to-end
multi-provider execution, comparative speed, reviewer consensus or certification.

## License

[MIT](LICENSE). Theo Browne's original copyright and permission notice remain in
the Council package. The rubric, Workshare, Council Workshop and project additions
are also MIT-licensed. This is an independent adaptation, not an official T Stack,
T3 Code, Pi or MEGA.dev release.
