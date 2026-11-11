"""Exercise the published install recipe without touching an agent's real skills."""

import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("council", "council-rubric", "workshare", "council-workshop")


def files(folder):
    return {path.relative_to(folder): path.read_bytes()
            for path in folder.rglob("*") if path.is_file()}


def install(destination):
    blocks = re.findall(r"```bash\n(.*?)\n```", (ROOT / "README.md").read_text(), re.S)
    recipe, = [block for block in blocks if "SKILLS_DIR" in block]
    return subprocess.run(
        ["bash", "-c", recipe], cwd=ROOT,
        env={**os.environ, "SKILLS_DIR": str(destination)},
        capture_output=True, text=True, timeout=10,
    )


class PackageTests(unittest.TestCase):
    def test_documented_install_preserves_complete_packages_and_resource_links(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "skills with spaces"
            result = install(destination)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual({p.name for p in destination.iterdir()}, set(SKILLS))
            for skill in SKILLS:
                installed = destination / skill
                self.assertEqual(files(installed), files(ROOT / "skills" / skill))
                self.assertTrue((installed / "LICENSE").is_file())
                for markdown in installed.rglob("*.md"):
                    for link in re.findall(r"\]\(([^)]+)\)", markdown.read_text()):
                        if ":" in link or link.startswith("#"):
                            continue
                        resource = (markdown.parent / link.split("#")[0]).resolve()
                        self.assertIn(installed.resolve(), resource.parents)
                        self.assertTrue(resource.is_file(), str(resource))

    def test_any_occupied_package_blocks_all_copies_without_changing_it(self):
        for skill in SKILLS:
            for kind in ("file", "directory", "broken-symlink"):
                with self.subTest(skill=skill, kind=kind), tempfile.TemporaryDirectory() as temporary:
                    destination = Path(temporary)
                    occupied = destination / skill
                    if kind == "directory":
                        occupied.mkdir()
                        (occupied / "keep.txt").write_text("local customization")
                    elif kind == "file":
                        occupied.write_text("local customization")
                    else:
                        occupied.symlink_to("missing-original")
                    result = install(destination)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual({path.name for path in destination.iterdir()}, {skill})
                    if kind == "broken-symlink":
                        self.assertEqual(os.readlink(occupied), "missing-original")
                    elif kind == "file":
                        self.assertEqual(occupied.read_text(), "local customization")
                    else:
                        self.assertEqual(files(occupied), {Path("keep.txt"): b"local customization"})

    def test_portable_skill_frontmatter_and_resources(self):
        for name in SKILLS:
            with self.subTest(skill=name):
                folder = ROOT / "skills" / name
                entry = (folder / "SKILL.md").read_text()
                frontmatter, body = entry.removeprefix("---\n").split("\n---\n", 1)
                self.assertIn(f"name: {name}\n", frontmatter + "\n")
                self.assertRegex(frontmatter, r"(?m)^description: .+")
                self.assertNotIn("TODO", entry)
                self.assertLess(len(body.split()), 5000)
                for path in folder.rglob("*"):
                    self.assertFalse(path.is_symlink(), str(path))
                    if path.is_dir():
                        self.assertTrue(any(path.iterdir()), str(path))
                    elif path.suffix in (".md", ".json", ".py", ".yaml") and path.name != "SKILL.md":
                        relative = path.relative_to(folder).as_posix()
                        if not relative.startswith("agents/"):
                            self.assertIn(relative, body, str(path))

    def test_pi_manifest_exposes_only_skills_without_install_hooks(self):
        manifest = json.loads((ROOT / "package.json").read_text())
        self.assertEqual(manifest["pi"], {"skills": ["./skills"], "extensions": [],
                                          "prompts": [], "themes": []})
        self.assertNotIn("scripts", manifest)
        self.assertNotIn("dependencies", manifest)
        self.assertTrue(manifest["private"])
        self.assertEqual({path.name for path in (ROOT / "skills").iterdir()}, set(SKILLS))

    def test_installed_checker_and_example_work_outside_source_checkout(self):
        with tempfile.TemporaryDirectory() as temporary:
            destination = Path(temporary) / "installed skills"
            self.assertEqual(install(destination).returncode, 0)
            workshop = destination / "council-workshop"
            result = subprocess.run(
                ["python3", str(workshop / "scripts/check_plan.py"),
                 str(workshop / "assets/team-trials.example.json")],
                cwd=temporary, capture_output=True, text=True, timeout=10,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("not launch authorization", result.stdout)

    def test_council_keeps_theos_notice_and_full_mit_terms(self):
        root_license = (ROOT / "LICENSE").read_text()
        council_license = (ROOT / "skills/council/LICENSE").read_text()
        rubric_license = (ROOT / "skills/council-rubric/LICENSE").read_text()
        self.assertEqual(root_license, council_license)
        self.assertIn("Copyright (c) 2026 Theo Browne\n", council_license)
        self.assertEqual(council_license.split("Permission is hereby", 1)[1],
                         rubric_license.split("Permission is hereby", 1)[1])


if __name__ == "__main__":
    unittest.main()
