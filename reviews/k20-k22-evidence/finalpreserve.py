from pathlib import Path
import json,hashlib,sys,subprocess
sys.path.insert(0,'engineering/examples')
import visual_foundations as v,physical_models as p,system_models as s,subsystem_models as t,sampled_models as m,alignment_models as a,calibration_models as c,metrology_models as z
out=Path('/tmp/k2022/final-svg');out.mkdir(exist_ok=True);v.OUT=out
for f in [v.group1,v.group1_details,v.group2,v.group3,v.group4,p.chapter8,p.chapter9,p.chapter10,s.unit11,s.unit12,s.unit13,t.unit14,t.unit15,t.unit16,m.unit17,m.unit18,m.unit19,a.unit20,c.unit21,z.unit22]:f()
repro={f.name:f.read_bytes()==(Path('book/figures')/f.name).read_bytes() for f in out.glob('*.svg')};assert set(repro)=={f.name for f in Path('book/figures').glob('*.svg')}
base=json.loads(Path('/tmp/k2022/baseline.json').read_text());edits=json.loads(Path('/tmp/k2022/integration-reference-edits.json').read_text());exclude={'book/_quarto.yml','book/index.qmd','project/current-work.md','references/references.bib','book/calibration-observability-metrology.qmd'}|set(edits)
protected={n:Path(n).is_file() and hashlib.sha256(Path(n).read_bytes()).hexdigest()==h for n,h in base.items() if n not in exclude}
references={}
for n,mapping in edits.items():
 old=subprocess.check_output(['git','show','58ee480:'+n]).decode()
 for before,after in mapping:
  assert old.count(before)==1;old=old.replace(before,after)
 references[n]=old==Path(n).read_text()
unit={}
for checkpoint,names in [('a534013',['book/complex-response-alignment.qmd','engineering/examples/alignment_models.py']),('17142f3',['book/calibration-procedures-coherence.qmd','engineering/examples/calibration_models.py'])]:
 for n in names:
  expected=subprocess.check_output(['git','show',checkpoint+':'+n]).decode()
  if n=='book/calibration-procedures-coherence.qmd':
   for before,after in json.loads(Path('/tmp/k2022/integration-number-clarifications.json').read_text())[n]:
    assert expected.count(before)==1;expected=expected.replace(before,after)
  unit[n]=expected.encode()==Path(n).read_bytes()
prefix=subprocess.check_output(['git','show','17142f3:book/calibration-observability-metrology.qmd']);current=Path('book/calibration-observability-metrology.qmd').read_bytes();unit['K21a preserved prefix']=current.startswith(prefix.rstrip())
scratch=Path('/tmp/k2022/final-render');copy={}
for folder in ['book','references']:
 for f in Path(folder).rglob('*'):
  if not f.is_file() or any(part in ['_book','.quarto'] for part in f.parts) or f.suffix not in ['.qmd','.svg','.yml','.csv','.bib']:continue
  copy[str(f)]=(scratch/f).is_file() and f.read_bytes()==(scratch/f).read_bytes()
controls={str(f):[i for i,b in enumerate(f.read_bytes()) if b<32 and b not in [9,10,13]] for f in Path('book').glob('*.qmd')};assert not any(controls.values())
assert all(repro.values()) and all(protected.values()) and all(references.values()) and all(unit.values()) and all(copy.values())
r={'svg_reproduction':repro,'protected_baseline':protected,'only_declared_reference_edits':references,'unit_checkpoints':unit,'render_inputs_match':copy,'manuscript_control_bytes':controls}
Path('/tmp/k2022/final-preservation.json').write_text(json.dumps(r,indent=2)+'\n');print('SVG',len(repro),'protected',len(protected),'reference paths',len(references),'unit comparisons',len(unit),'render source files',len(copy))
