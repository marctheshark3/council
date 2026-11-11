"""Exercise plan admission checks, not models or a scheduler."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/council-workshop/scripts/check_plan.py"
EXAMPLE = ROOT / "skills/council-workshop/assets/team-trials.example.json"


def member(name, role, model, assignment):
    return {"id": name, "role": role, "model": model, "harness": "pi",
            "provider_instance_id": "pi", "options": {"thinking": "high"},
            "assignment": assignment}


def plan():
    """Return synthetic data: these are not runnable catalog model IDs."""
    teams = []
    for name, assignment in (("balanced", "Own CSV writer and tests"),
                             ("provider-preferred", "Own export feature implementation")):
        teams.append({
            "id": name, "base_snapshot": "synthetic-base-v1", "rubric_id": "feature-v1",
            "task_id": "export-work-v1", "evaluation_id": "export-evaluation-v1",
            "workspace_id": "isolated-" + name, "coordination": "lead-led",
            "members": [member(name + "-lead", "lead", "openai/fixture-lead", "Implement and integrate"),
                        member(name + "-worker", "worker", "xai/fixture-worker", assignment)],
        })
    reviewers = {
        stage: [member(stage + "-review-" + name, "reviewer", provider + "/fixture-reviewer",
                       "Independent review")
                for name, provider in (("a", "openai"), ("b", "anthropic"), ("c", "xai"))]
        for stage in ("plan", "final")
    }
    return {
        "schema_version": 2, "example": True, "mode": "team-trials",
        "base_snapshot": "synthetic-base-v1",
        "task": {"id": "export-work-v1", "status": "frozen", "approval": "Synthetic fixture only"},
        "rubric": {"id": "feature-v1", "status": "frozen", "approval": "Synthetic fixture only"},
        "plan_review": {"id": "design-v1", "status": "frozen", "approval": "Synthetic fixture only"},
        "parallelism": {
            "independent_work": "UI and CSV serialization can be implemented against frozen fixtures.",
            "shared_decisions": "Freeze the CSV interface and resource ownership before parallel writes.",
            "trial_reason": "Compare ownership alternatives using the same executable export checks.",
        },
        "evaluation": {
            "id": "export-evaluation-v1", "status": "frozen", "approval": "Synthetic fixture only",
            "selection_rule": "Feature-v1 candidate gates first; anchored quality then repair burden; no winner if none qualifies.",
            "comparison_basis": "delivery-only",
            "resource_policy": "Equal declared launch caps; actual time and compute remain observations, not matched-budget proof.",
            "identity_policy": "disclosed",
            "presentation_order": "Record candidate order and identity exposure; no blind-judging claim.",
        },
        "review_policy": {
            "independent_first_pass": True,
            "finding_resolution": "evidence-not-vote",
            "recheck_scope": "delta-and-dependencies",
        },
        "budgets": {"max_active_builders": 4, "max_builder_launches": 6,
                    "max_team_repairs": 1, "max_review_rounds": 3, "plan_review_rounds": 1,
                    "final_review_rounds": 1, "repair_review_rounds": 1},
        "reviewers": reviewers,
        "teams": teams,
    }


def check(data):
    with tempfile.TemporaryDirectory() as temporary:
        path = Path(temporary) / "plan with spaces.json"
        path.write_text(json.dumps(data))
        return subprocess.run([sys.executable, str(SCRIPT), str(path)],
                              capture_output=True, text=True, timeout=10)


class WorkshopPlanTests(unittest.TestCase):
    def assert_rejected(self, data, reason):
        result = check(data)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn(reason, result.stderr)

    def test_valid_trial_plan_is_structural_only(self):
        result = check(plan())
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("not launch authorization", result.stdout)
        self.assertIn("synthetic example", result.stdout)

    def test_packaged_example_matches_the_documented_shape(self):
        data = json.loads(EXAMPLE.read_text())
        self.assertEqual(data, plan())
        self.assertEqual(check(data).returncode, 0)

    def test_one_team_mode_is_valid_without_duplicate_work(self):
        data = plan()
        data["mode"] = "single-team"
        data["teams"] = data["teams"][:1]
        del data["parallelism"]["trial_reason"]
        self.assertEqual(check(data).returncode, 0)

    def test_schema_one_requires_explicit_upgrade(self):
        data = plan()
        data["schema_version"] = 1
        self.assert_rejected(data, "schema_version must be 2")

    def test_mode_controls_candidate_count(self):
        data = plan()
        data["mode"] = "single-team"
        self.assert_rejected(data, "single-team requires exactly one team")
        data["mode"] = "team-trials"
        data["teams"] = data["teams"][:1]
        self.assert_rejected(data, "team-trials requires at least two teams")

    def test_candidates_must_share_frozen_input_references(self):
        for key, reason in (("base_snapshot", "same base_snapshot"),
                            ("rubric_id", "same rubric"),
                            ("task_id", "same task"),
                            ("evaluation_id", "same evaluation")):
            with self.subTest(field=key):
                data = plan()
                data["teams"][1][key] = "different"
                self.assert_rejected(data, reason)

    def test_draft_or_unapproved_contracts_cannot_enter_execution(self):
        for name in ("task", "rubric", "plan_review", "evaluation"):
            for key, value in (("status", "draft"), ("approval", ""), ("approval", True)):
                with self.subTest(contract=name, field=key, value=value):
                    data = plan()
                    data[name][key] = value
                    self.assert_rejected(data, name)

    def test_every_budget_is_finite_typed_and_bounded(self):
        for name in plan()["budgets"]:
            for value in (True, "2", -1, None):
                with self.subTest(budget=name, value=value):
                    data = plan()
                    data["budgets"][name] = value
                    self.assert_rejected(data, name)
        for name in ("max_active_builders", "max_builder_launches", "max_review_rounds", "plan_review_rounds", "final_review_rounds"):
            data = plan()
            data["budgets"][name] = 0
            self.assert_rejected(data, name)

    def test_planned_builders_and_concurrency_fit_launch_budget(self):
        data = plan()
        data["budgets"]["max_builder_launches"] = 3
        self.assert_rejected(data, "max_builder_launches")
        data = plan()
        data["budgets"]["max_active_builders"] = 7
        self.assert_rejected(data, "max_active_builders")

    def test_review_slices_fit_one_global_cap(self):
        data = plan()
        data["budgets"]["max_review_rounds"] = 2
        self.assert_rejected(data, "review slices exceed max_review_rounds")
        data["budgets"]["repair_review_rounds"] = 0
        self.assertEqual(check(data).returncode, 0)

    def test_parallel_work_and_trial_reason_are_explicit(self):
        for field in ("independent_work", "shared_decisions", "trial_reason"):
            for value in ("", None, True):
                with self.subTest(field=field, value=value):
                    data = plan()
                    data["parallelism"][field] = value
                    self.assert_rejected(data, "parallelism." + field)

    def test_evaluation_rules_and_comparison_basis_are_declared(self):
        for field in ("selection_rule", "resource_policy", "presentation_order"):
            for value in ("", None, True):
                with self.subTest(field=field, value=value):
                    data = plan()
                    data["evaluation"][field] = value
                    self.assert_rejected(data, "evaluation." + field)
        for field, values in (("comparison_basis", ("", "universal-model-ranking", None, [])),
                              ("identity_policy", ("", "assume-blind", None, []))):
            for value in values:
                with self.subTest(field=field, value=value):
                    data = plan()
                    data["evaluation"][field] = value
                    self.assert_rejected(data, "evaluation." + field)

    def test_supported_comparison_and_identity_policies(self):
        for basis in ("delivery-only", "equal-budget-quality", "time-to-accepted-quality"):
            for identity in ("masked", "disclosed"):
                with self.subTest(basis=basis, identity=identity):
                    data = plan()
                    data["evaluation"].update(comparison_basis=basis, identity_policy=identity)
                    self.assertEqual(check(data).returncode, 0)

    def test_review_requires_independent_evidence_based_delta_checks(self):
        for field, values in (("independent_first_pass", (False, "true", None, 1)),
                              ("finding_resolution", ("majority-vote", "", None)),
                              ("recheck_scope", ("full-review-every-time", "", None))):
            for value in values:
                with self.subTest(field=field, value=value):
                    data = plan()
                    data["review_policy"][field] = value
                    self.assert_rejected(data, "review_policy." + field)

    def test_review_task_ids_cannot_be_reused_or_be_builders(self):
        data = plan()
        data["reviewers"]["final"][0]["id"] = data["reviewers"]["plan"][0]["id"]
        self.assert_rejected(data, "review task id reused")
        data = plan()
        data["teams"][0]["members"][0]["id"] = data["reviewers"]["plan"][0]["id"]
        self.assert_rejected(data, "review task id used by builder")

    def test_workspace_and_identity_collisions_are_rejected(self):
        for name in ("id", "workspace_id"):
            data = plan()
            data["teams"][1][name] = data["teams"][0][name]
            self.assert_rejected(data, "duplicate " + name)
        data = plan()
        data["teams"][1]["members"][1]["id"] = data["teams"][0]["members"][1]["id"]
        self.assert_rejected(data, "duplicate builder id")

    def test_renaming_identical_teams_does_not_create_an_experiment(self):
        data = plan()
        data["teams"][1]["members"][1]["assignment"] = data["teams"][0]["members"][1]["assignment"]
        self.assert_rejected(data, "identical team configurations")

    def test_model_settings_and_roles_must_be_explicit(self):
        cases = (("model", "", "model"), ("harness", "", "harness"),
                 ("provider_instance_id", "", "provider_instance_id"),
                 ("assignment", "", "assignment"), ("options", {}, "thinking"),
                 ("options", {"thinking": True}, "thinking"),
                 ("role", "reviewer", "lead or worker"))
        for key, value, reason in cases:
            with self.subTest(field=key, value=value):
                data = plan()
                data["teams"][0]["members"][1][key] = value
                self.assert_rejected(data, reason)

    def test_non_pi_harness_needs_an_explicit_override(self):
        data = plan()
        worker = data["teams"][0]["members"][1]
        worker.update(harness="other", provider_instance_id="other", options={"effort": "high"})
        self.assert_rejected(data, "harness_override_approval")
        worker["harness_override_approval"] = "Synthetic explicit user choice"
        self.assertEqual(check(data).returncode, 0)

    def test_each_team_needs_one_lead_and_at_least_one_worker(self):
        data = plan()
        data["teams"][0]["members"] = data["teams"][0]["members"][:1]
        self.assert_rejected(data, "at least two builders")
        data = plan()
        data["teams"][0]["members"][1]["role"] = "lead"
        self.assert_rejected(data, "exactly one lead")

    def test_both_review_stages_need_explicit_read_only_rosters(self):
        for stage in ("plan", "final"):
            data = plan()
            data["reviewers"][stage] = []
            self.assert_rejected(data, "reviewers." + stage)
        data = plan()
        data["reviewers"]["final"][0]["role"] = "worker"
        self.assert_rejected(data, "reviewer role")

    def test_pi_model_ids_must_be_provider_qualified(self):
        data = plan()
        data["teams"][0]["members"][0]["model"] = "fixture-lead"
        self.assert_rejected(data, "provider-qualified")

    def test_duplicate_json_keys_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "duplicate.json"
            path.write_text('{"mode":"single-team","mode":"team-trials"}')
            result = subprocess.run([sys.executable, str(SCRIPT), str(path)],
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 1)
            self.assertIn("duplicate JSON key", result.stderr)

    def test_malformed_inputs_fail_without_tracebacks(self):
        for data in (None, [], {"schema_version": 99}, {**plan(), "teams": [None]},
                     {**plan(), "reviewers": None}, {**plan(), "budgets": []},
                     {**plan(), "parallelism": None}, {**plan(), "evaluation": []},
                     {**plan(), "review_policy": True}):
            with self.subTest(data=data):
                result = check(data)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertNotIn("Traceback", result.stderr)
        with tempfile.TemporaryDirectory() as temporary:
            bad = Path(temporary) / "bad.json"
            bad.write_text("not json")
            result = subprocess.run([sys.executable, str(SCRIPT), str(bad)],
                                    capture_output=True, text=True, timeout=10)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn("Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
