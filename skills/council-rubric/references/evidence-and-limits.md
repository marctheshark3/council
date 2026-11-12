# Rubric evidence and limits

Research checked on 2026-11-11. These sources support useful structured judgment,
not software certification or a calibrated probability of correctness. They do
not validate this exact skill or establish universal weights, floors or targets.

## Primary research

- [G-Eval, 2023, v3](https://arxiv.org/abs/2303.16634v3) combines explicit
  evaluation criteria and form-filling for generated text. It reports a 0.514
  Spearman correlation with human summarization judgments and flags possible
  preference for LLM-generated text. Text-evaluation alignment is not a code
  correctness measurement.
- [Prometheus, ICLR 2024, v2](https://arxiv.org/abs/2310.08491v2) evaluates
  long-form responses against customized rubrics with suitable reference
  materials. Its trained evaluator reports 0.897 Pearson correlation with human
  scores over 45 customized rubrics. This result is conditional on that setup;
  prompting an arbitrary model with a checklist does not inherit the result.
- [Judging LLM-as-a-Judge, NeurIPS 2023, v4](https://arxiv.org/abs/2306.05685v4)
  reports over 80% agreement with human preferences in studied settings, while
  identifying position, verbosity, self-enhancement and reasoning biases.
  Preference agreement, Pearson correlation and Spearman correlation are
  different quantities; do not compare them as one accuracy leaderboard.

## Translate evidence into a contract

Treat the following as engineering safeguards, not a trial of this package:

1. Freeze observable criteria, anchors, applicability and evidence requirements
   before seeing candidate scores. A score such as 9/10 is not a 90% correctness
   probability, and another project's threshold is not automatically applicable.
2. Prefer executable checks for behavior that can be tested. Keep mandatory
   conditions independent of averages; a failed or pending required gate cannot
   be offset by polished prose, documentation or another reviewer's high score.
3. Where available, check the evaluator against known-good and known-bad
   examples, reference artifacts or historical defects. Record mistakes and
   limits; never invent calibration or block ordinary work on nonexistent data.
4. Mask provider/team labels when practical and authorized, and counterbalance
   presentation order for meaningful comparisons. Record unavoidable exposure
   such as commit authorship or recognizable output; do not call this fully blind
   merely because an alias was used. Do not alter artifacts just to hide identity.
5. Preserve first-pass judgments before reconciliation. Resolve disputed facts
   with evidence and retain reproducible minority findings. Keep subjective
   preference disagreements visible rather than converting them into facts.

Keep quality scores, confidence, evidence coverage, measured behavior and final
acceptance separate. A structured rubric helps explain a decision; it cannot
supply a missing test, prove a safety claim or authorize a merge/deployment.
