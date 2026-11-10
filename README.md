# Council

Multi-model reviews with a clear finish line: an adapted Council skill plus an
evidence-based rubric companion, in one repo.

Council builds on **[Theo Browne's T Stack](https://github.com/t3dotgg/tstack)**.
The original multi-provider review workflow is his; this version adds explicit
invocation, bounded rounds, model/harness controls, and the Council Rubric
workflow. See [upstream credit and changes](UPSTREAM.md).

## Two skills, different jobs

| Skill | Purpose |
| --- | --- |
| [council](skills/council/SKILL.md) | Convene reviewers from different model providers, keep findings separate, and stop within a finite budget. |
| [council-rubric](skills/council-rubric/SKILL.md) | Define or assess a versioned review contract with anchored scores, acceptance gates, evidence, and reopening rules. |

Rubric work can run with one agent. Discussing Council or drafting a rubric does
**not** authorize launching reviewers. An explicit Council run against a rubric
uses both skills.

## Install

These are instruction packages, not an agent runner. Clone the repo, then copy
both skill folders into your agent's discovery directory:

```bash
git clone https://github.com/marctheshark3/council.git
cd council
```

Choose **one** discovery directory for your setup:

| Agent | Typical user-scope directory |
| --- | --- |
| Codex or Pi | `~/.agents/skills` |
| Claude Code | `~/.claude/skills` |
| OpenCode | `~/.config/opencode/skills` |
| Grok | `~/.grok/skills` |

Honor your agent's configured discovery root if it differs. Do not install the
same skill into several directories that one agent scans. If you already use
T Stack's `council`, back up or move that copy outside discovery before replacing
it; do not keep two different skills with the same name.

The following Bash command defaults to `~/.agents/skills`. Set `SKILLS_DIR` to a
different directory if needed. It refuses an occupied destination, including a
broken symlink, before copying either package:

```bash
(
  set -eu
  skills_dir="${SKILLS_DIR:-$HOME/.agents/skills}"
  mkdir -p "$skills_dir"
  for skill in council council-rubric; do
    if [ -e "$skills_dir/$skill" ] || [ -L "$skills_dir/$skill" ]; then
      printf 'Existing skill preserved: %s\n' "$skills_dir/$skill" >&2
      exit 1
    fi
  done
  cp -R skills/council skills/council-rubric "$skills_dir/"
)
```

Start a fresh agent session and confirm that both skills are discovered. For a
project-local install, use that agent's documented project skill directory
instead. Nothing here installs runtimes, signs into providers, or changes services.

## Use

1. **Define a contract:**
   > Council rubric: define a review rubric for this CLI release. Draft only;
   > do not launch reviewers.
2. **Select and freeze it:** settle the claim, criteria, gates, evidence,
   reviewer policy, and budget before scoring. A draft assessment is provisional.
3. **Assess with one agent:**
   > Assess commit <sha> against rubric v1. Single-agent assessment.
4. **Or request the Council explicitly:**
   > Run council against rubric v1 for commit <sha>, with at most two rounds.
5. **After a change:**
   > Recheck gates G2 and G3 for commit <new-sha>. Carry earlier evidence only
   > where the dependencies are unchanged.

Start from the [rubric template](skills/council-rubric/assets/rubric-template.md)
and [scorecard template](skills/council-rubric/assets/scorecard-template.md).
The [worked examples](skills/council-rubric/references/examples.md) are synthetic
CAD and software cases, not real-project results or universal thresholds.

## Requirements and limits

- `council-rubric` needs an agent that can inspect the relevant artifact and
  evidence. It does not need multiple providers or T3 Code.
- `council` needs a harness that can run delegates on the requested model
  providers. T3 Code uses `orchestrator_capabilities` and `delegate_task`;
  other harnesses need their own supported delegation controls.
- By default, Council selects three model providers and prefers Pi where the
  chosen model is runnable, with explicitly supported `xhigh` reasoning. Named
  models, harnesses, and effort settings take precedence. Missing capabilities
  must be disclosed, not silently substituted.
- Opt-in GPT `token-max` pairs the same GPT model through Pi and native Codex.
  It can add a delegate and cost. Effort labels are not guaranteed token counts;
  `token-max fast` requests a supported speed tier separately from reasoning.
- Without another finite budget, Council allows the initial round plus two
  full or scoped follow-ups. Missing evidence can stop a run earlier.
- Scores cannot override failed or pending required gates. A passing review
  does not authorize a merge, deployment, purchase, print, or publication.

Provider access, billing, supported options, and tool availability belong to your
own environment. These instructions do not guarantee review quality, consensus,
safety certification, or identical behavior across models and harnesses.

## Local checks

With Python 3.10+ and Bash:

```bash
python3 -m unittest discover -s tests -v
```

The checks exercise the documented install in temporary directories, including
existing-copy preservation, resource links, and bundled licenses. They do not
launch models or establish provider-side reasoning behavior.

## License

[MIT](LICENSE). Theo Browne's original copyright and permission notice are
retained in the Council package. Council Rubric and this project's additions
are also MIT-licensed. This is an independent adaptation, not an official
T Stack or T3 Code release.
