from pathlib import Path
import math,cmath,json,re,xml.etree.ElementTree as E
src=Path('/tmp/k2022/check20.py').read_text();exec(src[src.index('lin=lambda'):src.index('\n\nimport cmath')])
ns=sorted(set(round(math.exp(math.log(2)+(math.log(1000)-math.log(2))*k/240)) for k in range(241)))
rho=.9
# Independent innovation weights for variance of the mean.
def ff(n):
 sums=[(1-rho**k)/(1-rho) for k in range(1,n+1)]
 return (sums[-1]**2+(1-rho*rho)*sum(x*x for x in sums[:-1]))/n**2
# Closed row sums instead of the author's explicit matrix-entry sums.
def nu(n):
 S=sum((1+rho-rho**(k+1)-rho**(n-k))/(1-rho) for k in range(n))
 row2=sum(((1+rho-rho**(k+1)-rho**(n-k))/(1-rho))**2 for k in range(n))
 trR2=n+2*sum((n-k)*rho**(2*k) for k in range(1,n))
 return max(1.,(n-S/n)**2/(trR2-2*row2/n+(S/n)**2))
uL=.2*50/(math.hypot(45,5)*math.hypot(95,5));floor=.002**2+.001**2+uL*uL
check('metrology-records',70,(2,1000),(0,.012),[(ns,[math.sqrt(2)*.006*math.sqrt(ff(n)) for n in ns]),(ns,[math.sqrt(2)*.006/math.sqrt(n) for n in ns]),(ns,[math.sqrt(2*.006**2*ff(n)+floor) for n in ns])],True,False)
check('metrology-records',520,(2,1000),(1,1000),[(ns,[1/ff(n) for n in ns]),(ns,[nu(n) for n in ns]),(ns,[n-1 for n in ns])],True,True)
a=logs(.005,.15)
check('metrology-level-floor',70,(.005,.15),(.0005,.05),[(a,[math.atan2(.0002,math.sqrt(x*x-.0002**2)) for x in a]),(a,[math.atan2(.01,math.sqrt(1-.01**2))]*len(a)),(a,[.002]*len(a))],True,True)
r={'figures':3,'vertices':sum(x['vertices'] for x in checks),'checks':checks,'u_loading_rad':uL,'mean_factor_innovation_100':ff(100),'dof_closed_rows_100':nu(100)}
Path('/tmp/k2022/k22-graphical.json').write_text(json.dumps(r,indent=2)+'\n');print(r['vertices'],'vertices checked')
pp=lin(-math.pi/2,math.pi/2)
check('metrology-phase-disk',620,(-math.pi/2,math.pi/2),(0,.7),[(pp,[(1+math.cos(2*x))/math.pi for x in pp])])
root=E.parse('book/figures/metrology-phase-disk.svg').getroot();circles=[e for e in root if e.tag.endswith('circle') and 'stroke-dasharray' in e.attrib]
assert [(float(e.attrib['cx']),float(e.attrib['cy']),float(e.attrib['r'])) for e in circles]==[(350,290,209),(350,290,190)]
r.update(figures=4,vertices=sum(x['vertices'] for x in checks),checks=checks)
Path('/tmp/k2022/k22-graphical.json').write_text(json.dumps(r,indent=2)+'\n');print(r['vertices'],'vertices including disk density checked')
ray=[e for e in root if e.tag.endswith('path') and e.attrib.get('d','').startswith('M160.000,290.000')]
assert len(ray)==1
pts=[tuple(map(float,q)) for q in re.findall(r'[ML]([\d.-]+),([\d.-]+)',ray[0].attrib['d'])]
x,y=pts[-1];z=complex((x-160)/190,(290-y)/190)
assert abs(abs(z-1)-1)<4e-6 and abs(cmath.phase(z)-.6)<4e-6
r['ray_circle_residual']=abs(abs(z-1)-1);r['ray_phase_residual_rad']=abs(cmath.phase(z)-.6)
Path('/tmp/k2022/k22-graphical.json').write_text(json.dumps(r,indent=2)+'\n')
