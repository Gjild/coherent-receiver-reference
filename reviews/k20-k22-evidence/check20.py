from pathlib import Path
import sys,math,json,re,xml.etree.ElementTree as E
sys.path.insert(0,'engineering/examples');import alignment_models as m,visual_foundations as v
v.OUT=Path('/tmp/k2022/svg20');v.OUT.mkdir(exist_ok=True);m.unit20()
assert all(f.read_bytes()==(Path('book/figures')/f.name).read_bytes() for f in v.OUT.glob('*.svg'))
lin=lambda a,b:[a+(b-a)*i/240 for i in range(241)]
logs=lambda a,b:[10**x for x in lin(math.log10(a),math.log10(b))]
checks=[]
def check(name,y,xlim,ylim,curves,lx=False,ly=False):
 top=y+92;fx=math.log10 if lx else lambda x:x;fy=math.log10 if ly else lambda x:x
 paths=[]
 for p in E.parse('book/figures/'+name+'.svg').getroot():
  pts=[tuple(map(float,q)) for q in re.findall(r'[ML]([\d.-]+),([\d.-]+)',p.attrib.get('d',''))]
  if p.attrib.get('stroke-width')=='2.8' and len(pts)>2 and top-.001<=pts[0][1]<=top+195.001:paths.append(pts)
 expected=[]
 for xs,ys in curves:
  chunk=[]
  for x,z in zip(xs,ys):
   if xlim[0]<=x<=xlim[1] and ylim[0]<=z<=ylim[1]:chunk.append((100+780*(fx(x)-fx(xlim[0]))/(fx(xlim[1])-fx(xlim[0])),top+195-195*(fy(z)-fy(ylim[0]))/(fy(ylim[1])-fy(ylim[0]))))
   else:
    if len(chunk)>1:expected.append(chunk)
    chunk=[]
  if len(chunk)>1:expected.append(chunk)
 assert len(paths)==len(expected),(name,y,len(paths),len(expected))
 for got,w in zip(paths,expected):
  assert len(got)==len(w)
  error=max(max(abs(a-c),abs(b-d)) for (a,b),(c,d) in zip(got,w));assert error<.000501,(name,error)
  checks.append({'figure':name,'vertices':len(got),'error_px':error})


import cmath
f=lin(-2,2)
# Independent real/imaginary formulas, rather than complex author transfer calls.
inside=lambda w: complex(1-.8*math.cos(w),.8*math.sin(w))
outside=lambda w: complex(.8-math.cos(w),math.sin(w))
check('alignment-phase-access',70,(-2,2),(-15,6),[(f,[10*math.log10(1.64-1.6*math.cos(2*math.pi*x/16)) for x in f])]*2)
check('alignment-phase-access',520,(-2,2),(-90,300),[(f,[math.degrees(math.atan2(inside(2*math.pi*x/16).imag,inside(2*math.pi*x/16).real)) for x in f]),(f,[math.degrees(math.atan2(outside(2*math.pi*x/16).imag,outside(2*math.pi*x/16).real))+(360 if x<0 else 0) for x in f])])
ll=list(range(4,49))
check('alignment-latency-residual',70,(4,48),(1e-11,1),[(ll,[math.exp(k*math.log(.6)) for k in ll]),(ll,[math.exp(-k*math.log(1.25)) for k in ll]),(ll,[.001]*len(ll))],False,True)
check('alignment-latency-residual',520,(4,48),(0,3.5),[(ll,[5/16]*len(ll)),(ll,[(5+k)/16 for k in ll]),(ll,[3]*len(ll))])
aa=lin(.6,.999)
check('alignment-null-noise',70,(.6,.999),(-10,50),[(aa,[10*math.log10((.01*.9*(1-a))**2/4e-10) for a in aa]),(aa,[20]*len(aa))])
ls=logs(.0001,.1);h=.018
check('alignment-null-noise',520,(.0001,.1),(0,1.1),[(ls,[1/(1+(l/h)**2) for l in ls]),(ls,[math.hypot((l/h)**2,(20e-6/.01)/h)/(1+(l/h)**2) for l in ls])],True,False)
# Exact finite convolution with rational a proves support and the residual endpoints.
from fractions import Fraction as Q
for a,L in [(Q(3,5),16),(Q(5,4),32)]:
 q=[a**k for k in range(L)] if a<1 else [-a**(-(L-k)) for k in range(L)]
 c=[Q(0)]*(L+1)
 for k,v in enumerate(q):c[k]+=v;c[k+1]-=a*v
 target=[Q(0)]*(L+1)
 if a<1:target[0]=1;target[-1]=-a**L
 else:target[0]=-a**(-L);target[-1]=1
 assert c==target
r={'figures':4,'vertices':sum(x['vertices'] for x in checks),'checks':checks}
Path('/tmp/k2022/k20-graphical.json').write_text(json.dumps(r,indent=2)+'\n');print(r['vertices'],'vertices verified')
