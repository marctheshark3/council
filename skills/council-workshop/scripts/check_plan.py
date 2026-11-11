#!/usr/bin/env python3
"""Check a workshop plan's structural invariants; never launch agents.

Usage: python3 check_plan.py /path/to/local-plan.json
Requires Python 3.10+ and the standard library only. Exit 0 for a structurally
valid plan, 1 for invalid input. Approval truth, capability, physical isolation,
runtime budgets and artifact acceptance must be verified separately.
"""

import argparse
import json
from pathlib import Path
import sys


POSITIVE_BUDGETS = ("max_active_builders", "max_builder_launches",
                    "plan_review_rounds", "final_review_rounds")
REPAIR_BUDGETS = ("max_team_repairs", "repair_review_rounds")


class Checks:
    def __init__(self):
        self.errors = []

    def text(self, value, label):
        if not isinstance(value, str) or not value.strip():
            self.errors.append(f"{label} must be a nonempty string")
            return ""
        return value.strip()

    def object(self, value, label):
        if not isinstance(value, dict):
            self.errors.append(f"{label} must be an object")
            return {}
        return value

    def contract(self, value, label):
        contract = self.object(value, label)
        identity = self.text(contract.get("id"), label + ".id")
        if contract.get("status") != "frozen":
            self.errors.append(f"{label}.status must be frozen before execution")
        self.text(contract.get("approval"), label + ".approval")
        return identity

    def budget(self, value, name, minimum):
        if type(value) is not int or value < minimum:
            self.errors.append(f"budgets.{name} must be an integer >= {minimum}")
            return None
        return value

    def roster(self, value, label, builders=False):
        if not isinstance(value, list) or not value:
            self.errors.append(f"{label} must be a nonempty roster")
            return []
        if builders and len(value) < 2:
            self.errors.append(f"{label} requires at least two builders")
        normalized = []
        identities = set()
        for index, item in enumerate(value):
            prefix = f"{label}[{index}]"
            member = self.object(item, prefix)
            identity = self.text(member.get("id"), prefix + ".id")
            if identity in identities:
                self.errors.append(f"{prefix}: duplicate member id {identity}")
            identities.add(identity)
            role = member.get("role")
            if builders and role not in ("lead", "worker"):
                self.errors.append(f"{prefix}.role must be lead or worker")
            if not builders and role != "reviewer":
                self.errors.append(f"{prefix} requires reviewer role")
            model = self.text(member.get("model"), prefix + ".model")
            harness = self.text(member.get("harness"), prefix + ".harness")
            provider = self.text(member.get("provider_instance_id"), prefix + ".provider_instance_id")
            assignment = self.text(member.get("assignment"), prefix + ".assignment")
            options = self.object(member.get("options"), prefix + ".options")
            for key, option in options.items():
                if not isinstance(key, str) or not isinstance(option, (str, bool)):
                    self.errors.append(f"{prefix}.options must contain string keys and string/boolean values")
            if harness == "pi":
                self.text(options.get("thinking"), prefix + ".options.thinking")
                if "/" not in model or not all(model.split("/", 1)):
                    self.errors.append(f"{prefix}.model must be provider-qualified for Pi")
            elif harness:
                self.text(member.get("harness_override_approval"), prefix + ".harness_override_approval")
            normalized.append({"id": identity, "role": role, "model": model,
                               "harness": harness, "provider_instance_id": provider,
                               "assignment": assignment, "options": options})
        if builders and sum(item["role"] == "lead" for item in normalized) != 1:
            self.errors.append(f"{label} requires exactly one lead")
        return normalized


def configuration(team, members):
    """Ignore allocation/identity labels when detecting exact duplicate trials."""
    roles = [{key: value for key, value in member.items() if key != "id"}
             for member in members]
    return json.dumps({"coordination": team.get("coordination"),
                       "members": sorted(roles, key=lambda item: json.dumps(item, sort_keys=True))},
                      sort_keys=True)


def validate_plan(value):
    checks = Checks()
    plan = checks.object(value, "plan")
    if type(plan.get("schema_version")) is not int or plan.get("schema_version") != 1:
        checks.errors.append("schema_version must be 1")
    if "example" in plan and type(plan["example"]) is not bool:
        checks.errors.append("example must be a boolean when present")
    mode = plan.get("mode")
    if mode not in ("single-team", "team-trials"):
        checks.errors.append("mode must be single-team or team-trials")
    base = checks.text(plan.get("base_snapshot"), "base_snapshot")
    rubric_id = checks.contract(plan.get("rubric"), "rubric")
    checks.contract(plan.get("plan_review"), "plan_review")
    raw_budgets = checks.object(plan.get("budgets"), "budgets")
    budgets = {name: checks.budget(raw_budgets.get(name), name, 1)
               for name in POSITIVE_BUDGETS}
    budgets.update({name: checks.budget(raw_budgets.get(name), name, 0)
                    for name in REPAIR_BUDGETS})
    reviewers = checks.object(plan.get("reviewers"), "reviewers")
    for stage in ("plan", "final"):
        checks.roster(reviewers.get(stage), "reviewers." + stage)

    teams = plan.get("teams")
    if not isinstance(teams, list):
        checks.errors.append("teams must be a list")
        teams = []
    if mode == "single-team" and len(teams) != 1:
        checks.errors.append("single-team requires exactly one team")
    if mode == "team-trials" and len(teams) < 2:
        checks.errors.append("team-trials requires at least two teams")
    seen = {"id": set(), "workspace_id": set()}
    builder_ids = set()
    signatures = set()
    builder_count = 0
    for index, value in enumerate(teams):
        label = f"teams[{index}]"
        team = checks.object(value, label)
        for key in seen:
            identity = checks.text(team.get(key), label + "." + key)
            if identity in seen[key]:
                checks.errors.append(f"{label}: duplicate {key} {identity}")
            seen[key].add(identity)
        if team.get("base_snapshot") != base:
            checks.errors.append(f"{label} must use the same base_snapshot")
        if team.get("rubric_id") != rubric_id:
            checks.errors.append(f"{label} must use the same rubric")
        if team.get("coordination") not in ("lead-led", "peer-team"):
            checks.errors.append(f"{label}.coordination must be lead-led or peer-team")
        members = checks.roster(team.get("members"), label + ".members", builders=True)
        builder_count += len(members)
        for member in members:
            if member["id"] in builder_ids:
                checks.errors.append(f"{label}: duplicate builder id {member['id']}")
            builder_ids.add(member["id"])
        signature = configuration(team, members)
        if mode == "team-trials" and signature in signatures:
            checks.errors.append("identical team configurations do not create distinct trials")
        signatures.add(signature)

    launches = budgets["max_builder_launches"]
    active = budgets["max_active_builders"]
    if launches is not None and builder_count > launches:
        checks.errors.append("max_builder_launches cannot cover the planned builders")
    if active is not None and launches is not None and active > launches:
        checks.errors.append("max_active_builders cannot exceed max_builder_launches")
    return checks.errors


def unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(), object_pairs_hook=unique_keys)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Invalid plan input: {error}", file=sys.stderr)
        return 1
    errors = validate_plan(plan)
    if errors:
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    label = "synthetic example" if plan.get("example") else "plan"
    print(f"Valid structural {label}; not launch authorization, capability verification, "
          "runtime isolation, budget enforcement or feature acceptance.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
