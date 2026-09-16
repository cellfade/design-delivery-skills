"""Install portable skills without overwriting unrelated or locally edited skills."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MARKER = '.design-delivery-managed.json'

def digest(path):
    result = {}
    for p in sorted(path.rglob('*')):
        if p.is_symlink():
            raise ValueError(f'Symlink not supported: {p}')
        if p.is_file() and p.name != MARKER:
            result[str(p.relative_to(path))] = hashlib.sha256(p.read_bytes()).hexdigest()
    return result

def install(home, target, update=False, source=ROOT / 'skills'):
    folders = {'codex': home / '.agents/skills', 'claude': home / '.claude/skills'}
    targets = list(folders.values()) if target == 'both' else [folders[target]]
    if source.is_symlink():
        raise ValueError(f'Symlink not supported: {source}')
    plans = []
    found = False
    for dest in targets:
        for skill in sorted(source.iterdir()):
            if not skill.is_dir() or not (skill / 'SKILL.md').is_file():
                continue
            if skill.is_symlink():
                raise ValueError(f'Symlink not supported: {skill}')
            found = True
            path = dest / skill.name
            desired = digest(skill)
            if path.is_symlink():
                raise ValueError(f'Refusing existing symlink: {path}')
            if path.exists():
                if not path.is_dir():
                    raise ValueError(f'Not a skill directory: {path}')
                marker = path / MARKER
                if not marker.exists():
                    raise ValueError(f'Unmanaged existing skill: {path}')
                previous = json.loads(marker.read_text())
                if not isinstance(previous, dict):
                    raise ValueError(f'Invalid management record: {marker}')
                actual = digest(path)
                if previous.get('package') != 'design-delivery-skills' or actual != previous.get('files'):
                    raise ValueError(f'Locally changed or unrecognized skill: {path}')
                if actual == desired:
                    continue
                if not update:
                    raise ValueError(f'Review update, then use --update: {path}')
            plans.append((skill, path, desired))
    if not found:
        raise ValueError(f'No skills found in {source}')
    # All conflicts are checked before any installation is changed.
    for skill, path, desired in plans:
        path.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=path.parent) as temp:
            staged = Path(temp) / path.name
            shutil.copytree(skill, staged)
            (staged / MARKER).write_text(json.dumps({'package':'design-delivery-skills','files':desired}, indent=2)+'\n')
            backup = None
            if path.exists():
                backup_root = path.parent.parent / 'design-delivery-backups'
                backup_root.mkdir(exist_ok=True)
                backup = Path(tempfile.mkdtemp(prefix=path.name+'-',dir=backup_root)) / path.name
                path.rename(backup)
            try:
                staged.rename(path)
            except Exception:
                if backup:
                    backup.rename(path)
                raise
            print(f'Installed {path}')
    return len(plans)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', choices=['codex','claude','both'], default='both')
    parser.add_argument('--update',action='store_true')
    args = parser.parse_args()
    try:
        count=install(Path.home(),args.target,args.update)
        print(f'{count} skills installed or updated; unchanged managed skills retained.')
    except (ValueError,OSError,json.JSONDecodeError) as exc:
        parser.exit(1,f'{exc}\n')
