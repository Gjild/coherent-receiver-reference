from pathlib import Path
code=Path('/tmp/k1719/check17.py').read_text().split('import numpy as np')[0].replace('svg17','svg18').replace('m.unit17()','m.unit18()')
exec(code)
import numpy as np
P=np.array([[1,1j],[1,-1j]]);Pinv=np.linalg.inv(P)
cy=1.05*math.cos(math.pi/60)+.75*.5*.02**2;cx=1.05*math.sin(math.pi/60)
g=math.hypot(cy,cx);e=math.atan2(cx,cy)
def response(f,mode):
 h=np.exp(-2j*np.pi*f*20e-9)
 phys=np.array([[1,0],[-1.05*np.sin(np.pi/60)*h,(1.05*np.cos(np.pi/60)+.75*.5*.01**2)*h]])
 if mode=='raw':return (P@phys@Pinv)[0]
 c=np.array([[1 if mode=='flat' else h,0],[math.tan(e)*(1 if mode=='flat' else h),1/(g*math.cos(e))]])
 return (P@c@phys@Pinv)[0]
xx=lin(-2,2);modes=['raw','flat','matched']
check('quadrature-band-correction',70,(-2,2),(-100,0),[(xx,[20*math.log10(abs(response(f*1e6,mode)[1]/response(f*1e6,mode)[0])) for f in xx]) for mode in modes])
check('quadrature-band-correction',520,(-2,2),(-9,9),[(xx,[math.degrees(np.angle(response(f*1e6,mode)[0]*np.exp(2j*np.pi*f*1e6*20e-9))) for f in xx]) for mode in modes])
ff=logs(1,10000)
check('quadrature-near-dc',70,(1,10000),(-45,1),[(ff,[20*math.log10(abs(1j*f/(100+1j*f))) for f in ff]),(ff,[0]*241)],True)
check('quadrature-near-dc',520,(1,10000),(0,90),[(ff,[math.degrees(np.angle(1j*f/(100+1j*f))) for f in ff])],True)
r={'reproduced':4,'checks':checks,'vertices':sum(c['vertices'] for c in checks)}
Path('/tmp/k1719/k18-graphical.json').write_text(json.dumps(r,indent=2)+'\n');print('vertices',r['vertices'])
