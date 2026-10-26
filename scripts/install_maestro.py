"""Install the main-agent instructions; preserve unrelated bytes. Python 3.9+."""
import argparse
import hashlib
import os
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
START = b'<!-- agentes:maestro:start -->\n'
END = b'<!-- agentes:maestro:end -->\n'


def update(target, dry_run=False, uninstall=False):
    if target.is_symlink() or target.parent.is_symlink():
        raise ValueError('Symbolic-link destination refused; nothing changed.')
    if target.exists() and not target.is_file():
        raise ValueError('Destination is not a regular file.')
    override = target.with_name('AGENTS.override.md')
    if not uninstall and override.exists() and override.stat().st_size:
        raise ValueError('AGENTS.override.md takes precedence. Reconcile it before installing Maestro.')
    old = target.read_bytes() if target.exists() else b''
    payload = (ROOT / 'coordinator/maestro.md').read_bytes()
    block = START + payload + END
    known = {hashlib.sha256(block).hexdigest()}
    history = ROOT / 'releases/known-maestro-hashes.txt'
    if history.exists():
        known.update(line.strip() for line in history.read_text().splitlines() if line and not line.startswith('#'))
    if (old.count(START.rstrip(b'\n')) != old.count(START)
            or old.count(END.rstrip(b'\n')) != old.count(END)):
        raise ValueError('Noncanonical Maestro markers; preserve and reconcile manually.')
    if old.count(START) != old.count(END) or old.count(START) > 1:
        raise ValueError('Ambiguous Maestro markers; preserve and reconcile manually.')
    if START in old:
        a, b = old.index(START), old.index(END) + len(END)
        if b <= a or hashlib.sha256(old[a:b]).hexdigest() not in known:
            raise ValueError('Maestro block was edited or is unknown; preserving it.')
        new = old[:a] + (b'' if uninstall else block) + old[b:]
    else:
        new = old if uninstall else block + old
    if new == old:
        print('Already current:', target)
        return
    if dry_run:
        print('Preview:', target)
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    lock = target.parent / '.maestro-install.lock'
    lock.mkdir()  # A concurrent installer must not race this one.
    staged = None
    try:
        if target.is_symlink() or (target.read_bytes() if target.exists() else b'') != old:
            raise ValueError('Concurrent edit; stopped.')
        if target.exists():
            backups = target.parent / '.maestro-backups'
            if backups.is_symlink():
                raise ValueError('Unsafe backup directory.')
            backups.mkdir(exist_ok=True)
            backup = Path(tempfile.mkdtemp(prefix='before-', dir=backups)) / target.name
            shutil.copy2(target, backup)
            print('Backup:', backup)
        fd, path = tempfile.mkstemp(prefix='.maestro-', dir=target.parent)
        staged = Path(path)
        with os.fdopen(fd, 'wb') as stream:
            stream.write(new)
        os.chmod(staged, target.stat().st_mode & 0o777 if target.exists() else 0o644)
        if target.is_symlink() or (target.read_bytes() if target.exists() else b'') != old:
            raise ValueError('Concurrent edit; stopped.')
        os.replace(staged, target)
        print('Removed Maestro block:' if uninstall else 'Installed Maestro main instructions:', target)
    finally:
        if staged and staged.exists():
            staged.unlink()
        lock.rmdir()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--dest', type=Path, default=Path(os.environ.get('CODEX_HOME', str(Path.home()/'.codex')))/'AGENTS.md')
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--uninstall', action='store_true')
    args = parser.parse_args()
    try:
        update(args.dest.absolute(), args.dry_run, args.uninstall)
    except (ValueError, OSError) as exc:
        parser.exit(1, str(exc)+'\n')
