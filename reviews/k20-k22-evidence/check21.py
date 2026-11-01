from pathlib import Path
import math,cmath,json,sys,re,xml.etree.ElementTree as E
exec(Path('/tmp/k2022/check20.py').read_text().split('\n\nimport cmath')[0].split('import alignment_models')[0] if False else Path('/tmp/k2022/check20.py').read_text()[Path('/tmp/k2022/check20.py').read_text().index('lin=lambda'):Path('/tmp/k2022/check20.py').read_text().index('\n\nimport cmath')].replace("import cmath", ""))
# check() parses actual SVG coordinates; independent formulas below.
f=lin(-2,2);r=json.loads(Path('/tmp/k2022/k21-values.json').read_text());g=complex(*r['g']);a=r['a']
q=[complex(round((a**k/g).real*2**20),round((a**k/g).imag*2**20))/2**20 for k in range(16)]
def residual(f,state):
 w=2*math.pi*f/16;aa=.63 if state==2 else .6
 qr=sum(c*(math.cos(w*k)-1j*math.sin(w*k)) for k,c in enumerate(q))
 hh=.9*(math.cos(.08)+1j*math.sin(.08))*(1-aa*(math.cos(w)-1j*math.sin(w)))
 if state==1:hh*=.97*(math.cos(.02)+1j*math.sin(.02))
 return abs(qr*hh-1)
check('calibration-heldout',70,(-2,2),(0,.13),[(f,[residual(x,s) for x in f]) for s in range(3)]+[(f,[.005]*len(f))])
check('calibration-heldout',520,(-2,2),(0,.0006),[(f,[residual(x,0) for x in f]),(f,[math.exp(16*math.log(.6))]*len(f))])
c=lin(1,30)
check('calibration-cadence',70,(1,30),(0,.018),[(c,[.003+.001*math.sqrt(.2/d)+.0004*(x+d/2+.05) for x in c]) for d in [.2,1]]+[(c,[.01]*len(c))])
check('calibration-cadence',520,(1,30),(.005,1),[(c,[d/x for x in c]) for d in [.2,1]]+[(c,[.02]*len(c))],False,True)
ff=logs(.001,10)
check('calibration-wanted',70,(.001,10),(0,1.05),[(ff,[x/math.hypot(x,.1) for x in ff]),(ff,[1]*len(ff)),(ff,[math.hypot(.9,x/.1)/math.hypot(1,x/.1) for x in ff])],True,False)
check('calibration-wanted',520,(.001,10),(0,1.05),[(ff,[x/math.hypot(x,.1) for x in ff])],True,False)
r={'figures':4,'vertices':sum(x['vertices'] for x in checks),'checks':checks}
Path('/tmp/k2022/k21-graphical.json').write_text(json.dumps(r,indent=2)+'\n');print(r['vertices'],'vertices verified')
