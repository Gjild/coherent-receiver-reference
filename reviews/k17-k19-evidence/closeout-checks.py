from pathlib import Path
import json,hashlib,subprocess,importlib.util
base=json.loads(Path('/tmp/k1719/baseline.json').read_text())
exclude={'book/_quarto.yml','book/index.qmd','project/current-work.md','references/references.bib'}
protected={n:Path(n).is_file() and hashlib.sha256(Path(n).read_bytes()).hexdigest()==h for n,h in base.items() if n not in exclude}
assert all(protected.values())
checks={}
for rev,names in [('fdbe152',['book/sampling-converter-feasibility.qmd']),('ae285c1',['book/quadrature-conjugate-fidelity.qmd'])]:
 for n in names:
  old=subprocess.check_output(['git','show',rev+':'+n]);checks[n]=old==Path(n).read_bytes()
assert all(checks.values())
untouched={n:hashlib.sha256(Path(n).read_bytes()).hexdigest() for n in ['book/.gitignore','book/index.toc']}
assert not subprocess.check_output(['git','ls-files','--','book/.gitignore','book/index.toc'])
control={}
for p in Path('book').glob('*.qmd'):
 bad=[b for b in p.read_bytes() if b<32 and b not in (9,10)]
 if bad:control[str(p)]=bad
assert not control
out={'protected':protected,'unit_checkpoint_bytes':checks,'preserved_untracked':untouched,'modules':{n:importlib.util.find_spec(n) is not None for n in ['numpy','scipy','pytest']},'control_bytes':control}
Path('/tmp/k1719/final-preservation.json').write_text(json.dumps(out,indent=2)+'\n')
print('protected',len(protected),'earlier units',checks,'modules',out['modules'])
