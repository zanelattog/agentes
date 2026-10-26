import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('maestro', ROOT/'scripts/install_maestro.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class MaestroInstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.target = Path(self.tmp.name)/'codex home'/'AGENTS.md'

    def test_dry_run_and_idempotence(self):
        m.update(self.target, dry_run=True)
        self.assertFalse(self.target.parent.exists())
        m.update(self.target)
        stamp = self.target.stat().st_mtime_ns
        m.update(self.target)
        self.assertEqual(stamp, self.target.stat().st_mtime_ns)
        self.assertEqual(self.target.read_bytes().count(m.START), 1)

    def test_existing_bytes_preserved_and_restore(self):
        self.target.parent.mkdir()
        original = b'# Personal\r\nDo not publish.\r\nNo final newline'
        self.target.write_bytes(original)
        m.update(self.target)
        self.assertTrue(self.target.read_bytes().endswith(original))
        backup = list((self.target.parent/'.maestro-backups').glob('*/AGENTS.md'))[0]
        self.assertEqual(backup.read_bytes(), original)
        m.update(self.target, uninstall=True)
        self.assertEqual(self.target.read_bytes(), original)

    def test_personal_changes_inside_block_not_overwritten(self):
        m.update(self.target)
        modified = self.target.read_bytes().replace(b'# Maestro', b'# Personal Maestro', 1)
        self.target.write_bytes(modified)
        for removing in [False, True]:
            with self.assertRaises(ValueError):
                m.update(self.target, uninstall=removing)
            self.assertEqual(self.target.read_bytes(), modified)

    def test_malformed_markers_and_override(self):
        self.target.parent.mkdir()
        self.target.write_bytes(m.START + b'broken')
        with self.assertRaises(ValueError): m.update(self.target)
        self.target.write_bytes(b'personal')
        self.target.with_name('AGENTS.override.md').write_text('priority')
        with self.assertRaises(ValueError): m.update(self.target)
        self.assertEqual(self.target.read_bytes(), b'personal')

    def test_symlink_refused(self):
        self.target.parent.mkdir()
        external = Path(self.tmp.name)/'external'
        external.write_bytes(b'private')
        self.target.symlink_to(external)
        with self.assertRaises(ValueError): m.update(self.target)
        self.assertEqual(external.read_bytes(), b'private')

    def test_no_runtime_or_profile_installed(self):
        m.update(self.target)
        self.assertFalse((self.target.parent/'agents/maestro.toml').exists())
        self.assertFalse((self.target.parent/'config.toml').exists())

    def test_changed_line_endings_or_missing_final_newline_preserved(self):
        m.update(self.target)
        original = self.target.read_bytes()
        for changed in [original.replace(b'\n', b'\r\n'), original.rstrip(b'\n')]:
            self.target.write_bytes(changed)
            for removing in [False, True]:
                with self.assertRaises(ValueError):
                    m.update(self.target, uninstall=removing)
                self.assertEqual(self.target.read_bytes(), changed)


if __name__ == '__main__': unittest.main()
