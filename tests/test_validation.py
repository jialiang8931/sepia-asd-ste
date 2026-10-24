from pathlib import Path
import subprocess
import unittest

from tools.validate_repository import check_core, check_path, check_script, scan_text


class ValidationTests(unittest.TestCase):
    def test_common_secret_is_detected_without_echoing_it(self):
        secret = "AK" + "IA" + "Z" * 16
        findings = scan_text("sample.txt", secret)
        self.assertTrue(findings)
        self.assertNotIn(secret, "\n".join(findings))

    def test_sensitive_paths_are_rejected(self):
        for name in (".aws/config", ".env", ".env.production", "state.tfstate", "deploy.tfplan", "server.key"):
            with self.subTest(name=name):
                self.assertTrue(check_path(name))

    def test_safe_documentation_path(self):
        self.assertFalse(check_path("docs/aws.md"))
        self.assertFalse(scan_text("docs/aws.md", "Use ~/.aws without exposing credentials."))

    def test_core_cannot_import_shell_or_io(self):
        for source in ("import os", "from services.sample.shell import main", "import random"):
            with self.subTest(source=source):
                self.assertTrue(check_core("core.py", source, frozenset()))

    def test_pure_core_is_accepted(self):
        self.assertFalse(check_core("core.py", "def add(first, second):\n    return first + second\n", frozenset()))

    def test_each_entrypoint_rejects_arguments_before_docker(self):
        root = Path(__file__).resolve().parents[1]
        for script in (root / "scripts").glob("*.sh"):
            with self.subTest(script=script.name):
                content = script.read_text()
                self.assertFalse(check_script(script.name, content))
                self.assertTrue(check_script(script.name, content.replace('if [ "$#" -ne 0 ]; then', "if false; then")))
                self.assertTrue(check_script(script.name, content + '\nexec "$@"\n'))

    def test_arguments_fail_without_access_to_docker(self):
        root = Path(__file__).resolve().parents[1]
        for script in (root / "scripts").glob("*.sh"):
            for argument in ("--run-tests", "production", "--help"):
                with self.subTest(script=script.name, argument=argument):
                    result = subprocess.run(
                        ["/bin/sh", str(script), argument],
                        cwd="/tmp", text=True, capture_output=True, check=False,
                    )
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(result.stdout, "")
                    self.assertEqual(result.stderr, f"{script.name} accepts no arguments.\n")

    def test_scripts_are_valid_posix_shell(self):
        root = Path(__file__).resolve().parents[1]
        for script in (root / "scripts").glob("*.sh"):
            with self.subTest(script=script.name):
                result = subprocess.run(
                    ["/bin/sh", "-n", str(script)],
                    text=True, capture_output=True, check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
