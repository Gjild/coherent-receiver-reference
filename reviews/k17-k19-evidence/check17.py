from pathlib import Path
import sys,math,json,re,xml.etree.ElementTree as E
sys.path.insert(0,'engineering/examples');import sampled_models as m,visual_foundations as v
v.OUT=Path('/tmp/k1719/svg17');v.OUT.mkdir(exist_ok=True);m.unit17()
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

import numpy as np
A=(2*50*10**((-56-30)/10))**.5*10**(24/20)
B=(2*50*10**((-23-30)/10))**.5*10**(24/20)
bb=lin(0,1.2)
raw=lambda r:math.sqrt(((2*math.pi*20e6*A)**2+(2*math.pi*30e6*B*r)**2+(2*math.pi*40e6*B*r)**2)/2)*1e-7
check('converter-timing-observable',70,(0,1.2),(0,10),[(bb,[raw(r) for r in bb]),(bb,[raw(0)]*241)])
cc=lin(0,1)
def phase(r,opposite):
 n=np.arange(64);sw=np.sin(2*np.pi*10*n/64)
 w=2*sw*(2*np.pi*20e6*A*sw+2*np.pi*B*(30e6*np.sin(2*np.pi*15*n/64)+40e6*np.sin(2*np.pi*20*n/64)))/A
 z=2*sw*(2*np.pi*20e6*A*sw-2*np.pi*B*(30e6*np.sin(2*np.pi*15*n/64)+40e6*np.sin(2*np.pi*20*n/64)))/A if opposite else w
 variance=np.mean((r*1e-13*(z-w))**2+(1-r*r)*1e-26*(w*w+z*z))/256000
 return math.degrees(math.sqrt(variance))
check('converter-timing-observable',520,(0,1),(0,.0004),[(cc,[phase(r,False) for r in cc]),(cc,[phase(r,True) for r in cc]),(cc,[.0002]*241)])
xx=lin(-1.4,1.4);sx=[-1.4,-.5,-.5,.5,.5,1.4]
check('converter-quantization',70,(-1.4,1.4),(-1.5,1.5),[(sx,[-1,-1,0,0,1,1]),(xx,xx)])
nn=sorted(set(64*round(v/64) for v in logs(64,1e6)))
def bias(bits):
 ph=[];n=np.arange(64)
 for pp in [(0,.2,-.4),(.3,1.1,-.7)]:
  wave=sum(amp*np.cos(2*np.pi*k*n/64+p) for amp,k,p in zip([A,B,B],[10,15,20],pp))
  q=np.rint(wave/(2/2**bits))*(2/2**bits)
  ph.append(np.fft.fft(q)[10])
 return abs(math.degrees(np.angle(ph[1]/ph[0])-.3))
bound=lambda b,n:math.degrees(math.sqrt((2/2**b)**2+4*(50e-6)**2)/(A*math.sqrt(n)))
check('converter-quantization',520,(64,1e6),(.0001,.3),[(nn,[bias(14)]*len(nn)),(nn,[bias(16)]*len(nn)),(nn,[bound(14,n) for n in nn]),(nn,[bound(16,n) for n in nn])],True,True)
dd=logs(1,10000)
check('converter-interleaving',290,(1,10000),(.0001,10),[(dd,[math.degrees(math.asin(B/A*math.pi*44e6*d*1e-15)) for d in dd]),(dd,[.01]*241)],True,True)
g=lin(18,28)
check('converter-driver-range',70,(18,28),(0,1.6),[(g,[(A+2*B)*10**((v-24)/20) for v in g]),(g,[(.2+2*B)*10**((v-24)/20) for v in g]),(g,[.8]*241),(g,[1]*241)])
t=lin(.15,1)
check('converter-driver-range',520,(.15,1),(1e-9,1),[(t,[2*math.exp(-3/v) for v in t]),(t,[1/2**14]*241),(t,[1/2**16]*241)],False,True)
r={'reproduced':5,'checks':checks,'vertices':sum(x['vertices'] for x in checks)}
Path('/tmp/k1719/k17-graphical.json').write_text(json.dumps(r,indent=2)+'\n');print('vertices',r['vertices'])
