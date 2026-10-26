"""Run with Python 3.9+. Every destination is inside a disposable directory."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
INSTALLER = ROOT / "scripts" / "install.sh"
PROFILES = sorted((ROOT / "agents").glob("*.toml"))


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="agentes-test-")
        self.addCleanup(self.scratch.cleanup)
        self.dest = Path(self.scratch.name) / "pasta com espaços" / "agents"

    def run_installer(self, *args, ok=True):
        result = subprocess.run(
            ["/bin/bash", str(INSTALLER), "--dest", str(self.dest), *args],
            text=True, capture_output=True,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def test_dry_run_writes_nothing(self):
        self.run_installer("--dry-run")
        self.assertFalse(self.dest.exists())

    def test_install_is_exact_and_idempotent(self):
        self.run_installer()
        self.assertEqual(len(list(self.dest.glob("*.toml"))), 6)
        stamps = {}
        for source in PROFILES:
            target = self.dest / source.name
            self.assertEqual(source.read_bytes(), target.read_bytes())
            stamps[source.name] = target.stat().st_mtime_ns
        self.run_installer()
        self.assertEqual(stamps, {p.name: p.stat().st_mtime_ns for p in self.dest.glob("*.toml")})

    def test_conflict_stops_before_any_profile_write(self):
        self.dest.mkdir(parents=True)
        conflict = self.dest / PROFILES[-1].name
        conflict.write_text("personal instructions", encoding="utf-8")
        self.run_installer(ok=False)
        self.assertEqual(list(self.dest.iterdir()), [conflict])
        self.assertEqual(conflict.read_text(), "personal instructions")

    def test_symlink_is_preserved(self):
        self.dest.mkdir(parents=True)
        outside = Path(self.scratch.name) / "external.txt"
        outside.write_text("do not change")
        link = self.dest / PROFILES[0].name
        link.symlink_to(outside)
        self.run_installer(ok=False)
        self.assertTrue(link.is_symlink())
        self.assertEqual(outside.read_text(), "do not change")

    def test_uninstall_preserves_unrelated_files(self):
        self.run_installer()
        other = self.dest / "other-agent.toml"
        other.write_text("unrelated")
        self.run_installer("--uninstall")
        self.assertEqual(list(self.dest.iterdir()), [other])

    def test_uninstall_stops_if_any_profile_was_modified(self):
        self.run_installer()
        modified = self.dest / PROFILES[-1].name
        modified.write_text("my changes")
        self.run_installer("--uninstall", ok=False)
        self.assertEqual(len(list(self.dest.glob("*.toml"))), 6)
        self.assertEqual(modified.read_text(), "my changes")

    def test_codex_home_override(self):
        isolated = Path(self.scratch.name) / "isolated-codex"
        env = dict(os.environ, CODEX_HOME=str(isolated))
        result = subprocess.run(["/bin/bash", str(INSTALLER)], env=env,
                                text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(len(list((isolated / "agents").glob("*.toml"))), 6)

    def test_missing_destination_is_rejected(self):
        self.run_installer("--dest", ok=False)
        self.assertFalse(self.dest.exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
