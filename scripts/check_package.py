"""Dependency-free checks for this package's simple skill format and local links."""
from pathlib import Path
from html.parser import HTMLParser
import json
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]

def check():
    skills = list((ROOT / 'skills').glob('*/SKILL.md'))
    assert len(skills) == 3, 'Expected three core skills'
    for path in skills:
        text = path.read_text()
        parts = text.split('---', 2)
        assert len(parts) == 3 and not parts[0].strip(), f'Missing frontmatter: {path}'
        fields = dict(line.split(': ', 1) for line in parts[1].strip().splitlines())
        assert fields['name'] == path.parent.name, f'Name mismatch: {path}'
        assert re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields['name']), path
        assert 1 <= len(fields['description']) <= 1024, path
    for path in [*ROOT.glob('*.md'), *ROOT.glob('docs/*.md'), *ROOT.glob('skills/**/*.md')]:
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            target = urlsplit(link)
            if target.scheme or not target.path:
                continue
            assert (path.parent / unquote(target.path)).exists(), f'Broken link: {path}: {link}'
    class Page(HTMLParser):
        def __init__(self):
            super().__init__(); self.ids = set(); self.links = []
        def handle_starttag(self, tag, attrs):
            attrs = dict(attrs)
            if 'id' in attrs:
                assert attrs['id'] not in self.ids, 'Duplicate HTML id'
                self.ids.add(attrs['id'])
            self.links.extend(attrs[k] for k in ('src', 'href') if k in attrs)
    page = Page(); page.feed((ROOT / 'site/index.html').read_text())
    for link in page.links:
        if link.startswith('#'):
            assert link == '#' or link[1:] in page.ids, f'Missing anchor: {link}'
        elif not urlsplit(link).scheme:
            assert (ROOT / 'site' / link).is_file(), f'Missing asset: {link}'
    scenarios = json.loads((ROOT / 'evals/scenarios.json').read_text())
    assert len({s['id'] for s in scenarios}) == len(scenarios), 'Duplicate evaluation id'
    assert all(s['task'] and s['observe'] for s in scenarios), 'Incomplete evaluation'
    print('Package checks passed: skill metadata, local references, showcase assets and scenario definitions.')

if __name__ == '__main__':
    check()
