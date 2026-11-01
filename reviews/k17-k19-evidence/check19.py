from pathlib import Path
code=Path('/tmp/k1719/check17.py').read_text().split('import numpy as np')[0].replace('svg17','svg19').replace('m.unit17()','m.unit19()').replace('len(pts)>2','len(pts)>1')
exec(code)
import numpy as np,cmath
from fractions import Fraction as Q
# Different I0 series and centered cosine sum for coefficients / curves.
def i0(x):
 t=1.;terms=[t]
 for k in range(1,100):
  t*=x*x/(4*k*k);terms.append(t)
  if t<1e-18*sum(terms):break
 return math.fsum(terms)
def coeff(n=257,beta=12):
 d=(n-1)/2;h=[]
 for k in range(n):
  a=(k-d)/16;sinc=math.sin(math.pi*a)/(math.pi*a) if a else 1
  h.append(sinc/16*i0(beta*math.sqrt(max(0,1-((k-d)/d)**2)))/i0(beta))
 return np.array(h)/math.fsum(h)
def metrics(h):
 n=524288;df=128e6/n;grid=np.fft.rfftfreq(n,1/128e6);a=np.abs(np.fft.rfft(h,n));k=np.arange(len(h))-(len(h)-1)/2
 gap=(2*np.pi/128e6)**2*math.fsum(k*k*abs(h))*df*df/8
 at=np.argmax(np.where(grid>=6e6,a,0));direct=abs(math.fsum(float(c)*math.cos(2*math.pi*grid[at]*j/128e6) for j,c in zip(k,h)))
 assert abs(direct-a[at])<2e-14
 return -20*math.log10(max(a[grid>=6e6])+gap)
ff=list(np.linspace(0,12,1537));curves=[]
for n,beta in [(129,12),(257,12),(385,14)]:
 h=coeff(n,beta);assert np.max(abs(h-m.fir_coeff(n,beta)))<2e-16
 k=np.arange(n)-(n-1)/2
 curves.append((ff,[20*math.log10(max(abs(math.fsum(float(c)*math.cos(2*math.pi*f*1e6*j/128e6) for j,c in zip(k,h))),1e-8)) for f in ff]))
curves.append(([6,12],[-116,-116]))
check('processing-filter-precision',70,(0,12),(-145,1),curves)
h=coeff();bits=list(range(17,30));check('processing-filter-precision',520,(17,29),(70,125),[(bits,[metrics(np.rint(h*2**b)/2**b) for b in bits]),(bits,[116]*len(bits))])
# Solve Vandermonde moments independently instead of using author product basis.
mu=lin(0,1)
def response(f,x,n):
 j=np.arange(-(n//2-1),n//2+1,dtype=float);w=np.linalg.solve(np.vander(j,N=n,increasing=True).T,np.array([x**k for k in range(n)]))
 return np.sum(w*np.exp(2j*np.pi*f/16e6*(j-x)))
cs=[(2,2e6),(8,2e6),(8,4e6)]
check('processing-fractional-delay',70,(0,1),(-.75,.01),[(mu,[20*math.log10(abs(response(f,x,n))) for x in mu]) for n,f in cs])
check('processing-fractional-delay',520,(0,1),(-.5,.5),[(mu,[math.degrees(np.angle(response(f,x,n))) for x in mu]) for n,f in cs])
# Independent periodic waveform and convolution, retaining explicit real mirrors.
N=8192;n=np.arange(N);p=n%64;A=math.sqrt(.1)*10**((-56+24)/20);B=math.sqrt(.1)*10**((-23+24)/20)
words=np.rint(2**15*(A*np.cos(2*np.pi*10*p/64+.3)+B*(np.cos(2*np.pi*15*p/64+1.1)+np.cos(2*np.pi*20*p/64-.7)))).astype(np.int64)
assert np.array_equal(words,m.digital_input())
def chain(x,step=False):
 q=np.arange(len(x));ph=2*np.pi*5*q/32+(np.pi/2*(q>=2048) if step else 0)
 return np.convolve(2*x*np.exp(-1j*ph),h)[:len(x)][::8]
bas=chain(words/2**15);nco=chain(words/2**15,True);dr=chain(np.delete(words,2048)/2**15)
ix=np.arange(0,N,8);di=np.arange(0,N-1,8);sel=(ix>=1800)&(ix<=2600);ds=(di>=1800)&(di<=2600)
check('processing-state-faults',70,(14,21),(-180,180),[(list(ix[sel]/128),list(np.angle(nco[sel]/bas[sel])*180/np.pi)),(list(di[ds]/128),list(np.angle(dr[ds]/bas[:len(dr)][ds])*180/np.pi))])
# Exact object convolution and rational rounding provide a different arithmetic route.
angle=2*np.pi*5*(n%32)/32;mix=[2*words*np.rint(np.cos(angle)*2**23).astype(np.int64),2*words*np.rint(-np.sin(angle)*2**23).astype(np.int64)]
bs=list(range(17,30,2));vals=[]
for b in bs:
 c=np.rint(h*2**b).astype(np.int64);zz=[]
 for v in mix:
  cv=np.convolve(np.asarray(v,dtype=object),np.asarray(c,dtype=object))
  zz.append(np.array([round(Q(int(cv[k]),2**(38+b-21)))/2**21 for k in ix]))
 out=zz[0]+1j*zz[1];vals.append(float(np.sqrt(np.mean(abs(out[ix>=256]-bas[ix>=256])**2))*1e6))
check('processing-word-residuals',70,(17,29),(.1,40),[(bs,vals)],False,True)
# Exact polynomial coefficients establish L1 maximum over mu, rather than a sampled guess.
def poly_mul(a,b):
 c=[Q(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]+=x*y
 return c
l1=[Q(0)]*8
for j in range(-3,5):
 p=[Q(1)]
 for k in range(-3,5):
  if j!=k:p=poly_mul(p,[Q(-k,j-k),Q(1,j-k)])
 sign=1 if sum(p[i]*Q(1,2)**i for i in range(len(p)))>0 else -1
 l1=[a+sign*b for a,b in zip(l1,p)]
c1=l1[1];c3=-l1[6];c2=l1[4]+3*c3
assert c1>0 and c2>0 and c3>0
maxl1=1+c1/4+c2/16+c3/64;assert maxl1==Q(381,256)
# Exact packet recurrence including pre/post-arrival points.
def queue(bad):
 q=Q(131072);lost=Q(0);old=0;out=[(0,q,lost)]
 for t in sorted(set(range(0,6000001,64000))|{500000,6000000}):
  service=Q(6,25)*max(0,t-max(old,500000));q=max(Q(0),q-service);out.append((t,q,lost))
  if t%64000==0:
   q+=16432 if bad else 12336;lost+=max(Q(0),q-262144);q=min(q,Q(262144));out.append((t,q,lost))
  old=t
 return out
hp=queue(False);hu=queue(True)
check('processing-queues-resources',330,(0,6),(0,280),[([t/1e6 for t,q,l in hp],[float(q)/1024 for t,q,l in hp]),([t/1e6 for t,q,l in hu],[float(q)/1024 for t,q,l in hu]),([0,6],[256,256])])
r={'reproduced':6,'vertices':sum(c['vertices'] for c in checks),'checks':checks,'exact_lagrange_l1_polynomial':[str(a) for a in l1],'l1_max':float(maxl1),'packet_peak':float(max(q for t,q,l in hp)),'padded_loss_bytes':float(hu[-1][2])}
Path('/tmp/k1719/k19-graphical.json').write_text(json.dumps(r,indent=2)+'\n');print('verified',r['vertices'],'vertices; L1max',maxl1,'packetpeak',r['packet_peak'])
