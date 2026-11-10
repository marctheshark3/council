"""Exercise the published install recipe without touching an agent's real skills."""

import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("council", "council-rubric")


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

    def test_existing_second_package_blocks_both_copies_without_changing_it(self):
        for kind in ("file", "directory", "broken-symlink"):
            with self.subTest(kind=kind), tempfile.TemporaryDirectory() as temporary:
                destination = Path(temporary)
                occupied = destination / "council-rubric"
                if kind == "directory":
                    occupied.mkdir()
                    (occupied / "keep.txt").write_text("local customization")
                elif kind == "file":
                    occupied.write_text("local customization")
                else:
                    occupied.symlink_to("missing-original")
                result = install(destination)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse((destination / "council").exists())
                if kind == "broken-symlink":
                    self.assertEqual(os.readlink(occupied), "missing-original")
                elif kind == "file":
                    self.assertEqual(occupied.read_text(), "local customization")
                else:
                    self.assertEqual(files(occupied), {Path("keep.txt"): b"local customization"})

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
