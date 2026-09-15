import importlib.util
from pathlib import Path
import tempfile
import unittest
spec=importlib.util.spec_from_file_location('installer',Path(__file__).resolve().parents[1]/'scripts/install.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name);self.home=self.root/'home';self.src=self.root/'source'
        (self.src/'example').mkdir(parents=True)
        (self.src/'example/SKILL.md').write_text('original')
    def test_both_and_idempotency(self):
        self.assertEqual(m.install(self.home,'both',source=self.src),2)
        self.assertEqual(m.install(self.home,'both',source=self.src),0)
    def test_conflict_preflight_preserves_all(self):
        conflict=self.home/'.claude/skills/example';conflict.mkdir(parents=True)
        (conflict/'SKILL.md').write_text('mine')
        with self.assertRaises(ValueError):m.install(self.home,'both',source=self.src)
        self.assertFalse((self.home/'.agents/skills/example').exists())
        self.assertEqual((conflict/'SKILL.md').read_text(),'mine')
    def test_update_requires_flag_and_backs_up(self):
        m.install(self.home,'codex',source=self.src)
        (self.src/'example/SKILL.md').write_text('new')
        with self.assertRaises(ValueError):m.install(self.home,'codex',source=self.src)
        m.install(self.home,'codex',True,source=self.src)
        backups=list((self.home/'.agents/design-delivery-backups').rglob('SKILL.md'))
        self.assertEqual(backups[0].read_text(),'original')
    def test_local_edit_preserved(self):
        m.install(self.home,'codex',source=self.src)
        p=self.home/'.agents/skills/example/SKILL.md';p.write_text('local edit')
        with self.assertRaises(ValueError):m.install(self.home,'codex',True,source=self.src)
        self.assertEqual(p.read_text(),'local edit')
    def test_symlink_refused(self):
        p=self.home/'.agents/skills/example';p.parent.mkdir(parents=True)
        p.symlink_to(self.src/'example',target_is_directory=True)
        with self.assertRaises(ValueError):m.install(self.home,'codex',source=self.src)

if __name__=='__main__':unittest.main()
