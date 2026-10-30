"""Reproduce textbook visual models with Python's standard library.

Run from repository root: python3 engineering/examples/visual_foundations.py 1
SVG coordinates are editable; all curves are synthetic mathematical illustrations.
No hardware observations or physical validation. Parameters are declared below.
"""
from pathlib import Path
from math import *
from html import escape
import random
import sys

OUT = Path(__file__).resolve().parents[2] / 'book/figures'
COLORS = ['#125b86','#b34719','#237550','#763c87']

def lin(a,b,n=241): return [a+(b-a)*i/(n-1) for i in range(n)]
def log(a,b,n=241): return [10**v for v in lin(log10(a),log10(b),n)]
def sinc(x): return sin(pi*x)/(pi*x) if x else 1.
def quad(fn,a,b,n=1024):
    h=(b-a)/n
    return h/3*(fn(a)+fn(b)+sum((4 if i%2 else 2)*fn(a+i*h) for i in range(1,n)))

def avg(x):
    return 1-x/3+x*x/12-x**3/60 if x<.001 else 2*(x-1+exp(-x))/x**2

def coherent(x):
    return quad(lambda v:2*(1-v)*exp(-(1-exp(-x*v))),0,1)

class SVG:
    def __init__(self,name,title,height=510):
        self.name=name; self.height=height
        self.s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">Synthetic mathematical illustration. See the caption and adjoining model for assumptions and interpretation.</desc>', '<rect width="960" height="100%" fill="white"/>', '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8" fill="#263c49"/></marker></defs>']
        self.text(32,32,title,23)
    def text(self,x,y,t,size=19,color='#182f3e',anchor='start'):
        self.s.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="{size}" fill="{color}" text-anchor="{anchor}">{escape(str(t))}</text>')
    def path(self,pts,color=COLORS[0],dash='',width=2.8,arrow=False):
        d=' '.join(('M' if i==0 else 'L')+f'{x:.3f},{y:.3f}' for i,(x,y) in enumerate(pts))
        self.s.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"'+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
    def dot(self,x,y,r=4,color=COLORS[0]): self.s.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>')
    def box(self,x,y,w,h,lines):
        self.s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#edf4f8" stroke="#263c49"/>')
        for i,t in enumerate(lines): self.text(x+w/2,y+25+25*i,t,18,anchor='middle')
    def plot(self,y,title,xlim,ylim,xlabel,ylabel,curves,logx=False,logy=False,points=()):
        self.text(100,y,title,20)
        left,top,w,h=100,y+92,780,195
        fx=lambda v:log10(v) if logx else v
        fy=lambda v:log10(v) if logy else v
        px=lambda v:left+w*(fx(v)-fx(xlim[0]))/(fx(xlim[1])-fx(xlim[0]))
        py=lambda v:top+h-h*(fy(v)-fy(ylim[0]))/(fy(ylim[1])-fy(ylim[0]))
        for i in range(5):
            a=i/4
            xv=10**(fx(xlim[0])+a*(fx(xlim[1])-fx(xlim[0]))) if logx else xlim[0]+a*(xlim[1]-xlim[0])
            yv=10**(fy(ylim[0])+a*(fy(ylim[1])-fy(ylim[0]))) if logy else ylim[0]+a*(ylim[1]-ylim[0])
            self.path([(px(xv),top),(px(xv),top+h)],'#dae2e7',width=1)
            self.path([(left,py(yv)),(left+w,py(yv))],'#dae2e7',width=1)
            self.text(px(xv),top+h+25,f'{xv:.3g}',17,anchor='middle')
            self.text(left-12,py(yv)+6,f'{yv:.3g}',17,anchor='end')
        self.path([(left,top),(left,top+h),(left+w,top+h)],'#263c49',width=1.5)
        self.text(left,top-12,ylabel,18)
        self.text(left+w/2,top+h+55,xlabel,18,anchor='middle')
        for j,(label,xs,ys) in enumerate(curves):
            color=COLORS[j%4];dash=['','8 4','3 4','12 4 3 4'][j%4]
            # Legends occupy separate rows, above axes; at most four labels.
            lx=100+(j%2)*400;ly=y+25+(j//2)*22
            self.path([(lx,ly-5),(lx+25,ly-5)],color,dash)
            self.text(lx+33,ly,label,16,color)
            chunk=[]
            for x,v in zip(xs,ys):
                if xlim[0]<=x<=xlim[1] and ylim[0]<=v<=ylim[1] and (not logy or v>0): chunk.append((px(x),py(v)))
                else:
                    if len(chunk)>1:self.path(chunk,color,dash)
                    chunk=[]
            if len(chunk)>1:self.path(chunk,color,dash)
        for x,v in points:self.dot(px(x),py(v),5)
        return px,py
    def save(self):
        self.text(32,self.height-14,'Illustrative model • no measured receiver data',16)
        (OUT/f'{self.name}.svg').write_text('\n'.join(self.s+['</svg>'])+'\n')

def group1():
    s=SVG('comparison-planes','Trace physical planes before referring a phase measurement',410)
    for y,i in [(100,1),(230,2)]:
        s.text(30,y+25,f'P{i}: RF')
        s.box(190,y,145,65,['RF path', '+25 ps only in 2' if i==2 else 'reference path'])
        s.box(400,y,125,65,['Mixer',f'L{i}: LO'])
        s.box(655,y,180,65,['Extraction', 'common IF / epoch'])
        s.path([(110,y+32),(190,y+32)],arrow=True);s.path([(335,y+32),(400,y+32)],arrow=True)
        s.path([(525,y+32),(655,y+32)],arrow=True);s.text(560,y+15,f'Q{i}: IF')
        s.path([(835,y+32),(920,y+32)],arrow=True);s.text(855,y+15,f'O{i}: z{i}')
        s.path([(460,y+95),(460,y+67)],arrow=True);s.text(490,y+90,'LO endpoint')
    s.text(32,365,'Added RF delay: −9° at 1 GHz before conversion; upper-side extraction reverses it.');s.save()
    s=SVG('relative-phasors','A relative angle survives a common reference rotation',710)
    for cx,cy,shift,label in [(260,235,0,'Original reference'),(710,235,-65,'Reference advanced by 65°')]:
        s.text(cx,85,label,19,anchor='middle')
        s.path([(cx-145,cy),(cx+145,cy)],'#9aaab3');s.path([(cx,cy+140),(cx,cy-140)],'#9aaab3')
        for i,a in enumerate([12,52]):
            a=radians(a+shift);s.path([(cx,cy),(cx+125*cos(a),cy-125*sin(a))],COLORS[i],arrow=True)
        s.path([(cx+65*cos(radians(a+shift)),cy-65*sin(radians(a+shift))) for a in lin(12,52)],COLORS[2])
        s.text(cx+70,cy+60,'Δ = +40°',20);s.text(cx-140,cy+170,'I (V); Q (V), equal axis scales',17)
    s.text(55,445,'Blue: z₁; orange: z₂. Positive arc runs from z₁ to z₂.',18);s.text(55,480,'Both magnitudes: 0.10 V peak; carrier 10 MHz; common epoch.');s.text(55,525,'z₂ z₁* = 0.010 exp(j40°) V² in either reference.');s.text(55,570,'Conjugating BOTH channels reverses Q and gives −40°.');s.text(55,615,'Absolute phasor angles depend on the chosen reference; their difference does not.');s.save()
    s=SVG('conversion-orientation','Positive-IF extraction changes input orientation, not added IF phase',495)
    for y,lo,sign,result in [(95,990,1,40),(265,1010,-1,-26)]:
        s.box(35,y,240,90,[f'RF 1000 − LO {lo} MHz',f'signed difference: {sign*10:+d} MHz'])
        s.path([(280,y+45),(370,y+45)],arrow=True)
        s.box(375,y,525,90,['Extract at positive 10 MHz',('Δφ − Δλ + Δβ' if sign==1 else '−Δφ + Δλ + Δβ')+f' = {result:+d}°'])
        s.text(45,y+125,'Δφ = 45° at P; Δλ = 12° at L; Δβ = +7° added at positive IF.',18)
    s.save()
    s=SVG('phase-wrapping','Wrapped observations do not determine a unique continuation',820)
    xs=lin(0,1);s.plot(70,'Two continuations through identical wrapped endpoints',(0,1),(-200,200),'Time (s), synthetic interval','Unwrapped phase (degrees)',[('+2° change',xs,[179+2*t for t in xs]),('−358° change',xs,[179-358*t for t in xs])],points=[(0,179),(1,-179)])
    s.text(100,440,'Endpoint at +181° wraps to −179°. A fade leaves phase undefined.',18)
    xs=lin(0,2);s.plot(475,'Positive delay moves the waveform right',(0,2),(-1.1,1.1),'Time / period (dimensionless)','Voltage / peak amplitude',[('undelayed',xs,[cos(2*pi*t) for t in xs]),('delay = 0.1 period',xs,[cos(2*pi*(t-.1)) for t in xs])]);s.save()
    s=SVG('ensemble-records','Separate restart ensembles from records within a state',1270)
    xs=lin(-.08,.08);g=lambda x,m:exp(-.5*((x-m)/.01)**2)/(.01*sqrt(2*pi))
    s.plot(70,'Equal-probability restart states: a = 0.03 rad, within-state SD = 0.01 rad',(-.08,.08),(0,42),'Phase (rad)','Density (rad⁻¹)',[('state +a',xs,[g(x,.03) for x in xs]),('state −a',xs,[g(x,-.03) for x in xs]),('mixture',xs,[(g(x,.03)+g(x,-.03))/2 for x in xs])])
    rng=random.Random(104);xs=list(range(20)); records=[[rng.gauss(0,.02) for _ in xs] for _ in range(3)]; bs=[-.025,.006,.025]
    s.plot(470,'Independent errors: three illustrative repetitions',(0,19),(-.065,.065),'Sample index within record','Phase error (rad)',[(f'record {i+1}, mean {sum(v)/20:+.3f}',xs,v) for i,v in enumerate(records)])
    s.plot(870,'Random-constant errors: each record retains its own mean',(0,19),(-.065,.065),'Sample index within record','Phase error (rad)',[(f'record {i+1}, mean {b:+.3f}',xs,[b]*20) for i,b in enumerate(bs)])
    s.text(95,1230,'Both models: ensemble mean 0, marginal SD 0.02 rad; traces do not prove ergodicity.',17);s.save()
    s=SVG('averaging-floor','More samples remove independent errors, not a persistent offset',510)
    xs=log(1,1000);s.plot(70,'The observable is the arithmetic phase average',(1,1000),(.0004,.03),'Number of readings N','Ensemble RMS error (rad)',[('independent: 0.02 / √N',xs,[.02/sqrt(n) for n in xs]),('constant: 0.02',xs,[.02]*len(xs)),('mixed: √(0.012²/N + 0.016²)',xs,[sqrt(.012**2/n+.016**2) for n in xs]),('illustrative target 0.003',xs,[.003]*len(xs))],True,True);s.save()
    s=SVG('complex-distributions','Equal second moments do not determine a complex distribution',650)
    for cx,typ,title in [(170,0,'Four equiprobable points'),(480,1,'Joint Gaussian, circular'),(790,2,'Gaussian marginals only')]:
        cy=255;s.text(cx,90,title,17,anchor='middle');s.path([(cx-115,cy),(cx+115,cy)],'#9aaab3');s.path([(cx,cy-115),(cx,cy+115)],'#9aaab3')
        if typ==0:
            for a in [0,pi/2,pi,3*pi/2]:s.dot(cx+85*cos(a),cy-85*sin(a),7)
        elif typ==1:
            for r in [40,75,100]:s.path([(cx+r*cos(a),cy-r*sin(a)) for a in lin(0,2*pi)],COLORS[0])
        else:
            for sg in [-1,1]:s.path([(cx-90,cy+sg*90),(cx+90,cy-sg*90)],COLORS[1],width=4)
        s.text(cx,405,'Re / Im: normalized, equal scale',15,anchor='middle')
    s.text(40,455,'All three: E[z] = 0 and P = E[z²] = 0. Only the middle law is circular.');s.text(40,495,'Right: z = X + jSX, X Gaussian and S an independent equiprobable sign.');s.text(40,545,'All panels: C = E|z|² = 1; Gaussian quadrature variances are 1/2.');s.text(40,585,'Contours are Gaussian density levels, not specified coverage regions.',18);s.save()
    s=SVG('noise-phase','Rotate additive voltage noise into the signal frame',830)
    s.path([(100,235),(860,235)],'#9aaab3');s.text(740,265,'parallel voltage');s.path([(300,340),(300,105)],'#9aaab3');s.text(310,115,'perpendicular voltage')
    s.path([(300,235),(650,235)],COLORS[0],arrow=True);s.text(460,220,'A > 0 V');s.path([(650,235),(720,165)],COLORS[1],arrow=True);s.text(680,145,'n′ (V)');s.text(340,175,'resultant A + n′ (V)',18,color=COLORS[2]);s.path([(300,235),(720,165)],COLORS[2],arrow=True)
    s.text(80,380,'Phase error = atan2(n⊥, A + n∥); undefined if the resulting voltage is zero.');
    xs=lin(-2,2);s.plot(455,'Example slice n∥ = 0: approximation fails as noise approaches signal',(-2,2),(-2.1,2.1),'n⊥ / A (dimensionless)','Phase error (rad)',[('exact atan2',xs,[atan2(t,1) for t in xs]),('linear n⊥/A',xs,xs)]);s.save()
    s=SVG('observation-gains','The observation operator determines spectral weighting',510)
    xs=lin(0,3,601);s.plot(70,'T = L = 1 s; gains are even in offset frequency',(0,3),(0,4.2),'Offset fT (dimensionless); positive half shown','Squared gain (dimensionless)',[('box average: sinc²(fT)',xs,[sinc(t)**2 for t in xs]),('increment: 4 sin²(πfL)',xs,[4*sin(pi*t)**2 for t in xs]),('separated averages: product',xs,[sinc(t)**2*4*sin(pi*t)**2 for t in xs])]);s.text(95,455,'Time weights: average +1/T on [0,T]; increment −δ(t) + δ(t−L).',18);s.save()
    s=SVG('complex-filter-order','Angle extraction and complex filtering do not commute',640)
    s.box(30,85,220,85,['Complex envelope z','small α and φ, A > 0']);s.box(350,85,230,85,['Complex filter h','H₀ = ∫h ≠ 0']);s.box(700,85,220,85,['Extract angle','about AH₀'])
    s.path([(250,125),(350,125)],arrow=True);s.path([(580,125),(700,125)],arrow=True)
    s.text(50,235,'Linearized output phase = Im(h/H₀)*α + Re(h/H₀)*φ + additive-noise term.');s.text(50,270,'Require |h*δz| ≪ |AH₀| at the output, not only small input α and φ.',18);s.text(50,305,'The imaginary part of the normalized impulse response converts AM to PM.');
    s.box(30,335,220,80,['Complex envelope z']);s.box(350,335,230,80,['Extract phase']);s.box(700,335,220,80,['Real phase filter B']);s.path([(250,375),(350,375)],arrow=True);s.path([(580,375),(700,375)],arrow=True)
    s.text(50,480,'Counterexample: h = (1+j, −j), H₀=1; AM-only samples (1.1, 1).');s.text(50,520,'Complex-filter output = 1.1+j0.1; angle = 0.090660 rad (linearized: 0.1 rad).');s.text(50,560,'Extracting the two input angles first gives zero; subsequent phase filtering stays zero.');s.text(50,600,'Finite accuracy also requires filtered input and angle remainder bounds.',17);s.save()
    s=SVG('coherence-observables','Phase averages and coherent accumulation answer different questions',1240)
    xs=log(.01,100,121);s.plot(70,'Stationary jointly Gaussian phase: σ = 1 rad, exponential covariance',(.01,100),(.01,1.05),'Observation T / correlation time tc','Phase-average RMS (rad)',[('√var(phase average)',xs,[sqrt(avg(x)) for x in xs])],True)
    s.plot(470,'The same model; normalized coherent average C',(.01,100),(0,1.05),'Observation T / tc','Dimensionless power',[('E|C|²',xs,[coherent(x) for x in xs]),('|E C|² = exp(−1)',xs,[exp(-1)]*len(xs)),('exp(−var average): wrong substitute',xs,[exp(-avg(x)) for x in xs])],True)
    aa=lin(0,4);s.plot(870,'Same increment variance a²; different characteristic functions',(0,4),(-1.1,1.1),'Increment scale a (rad)','Signed coherence Γ (dimensionless)',[('Gaussian increment',aa,[exp(-a*a/2) for a in aa]),('equiprobable increments ±a',aa,[cos(a) for a in aa])]);s.save()
    s=SVG('covariance-increments','A stationary covariance and a random walk have different limits',830)
    xs=lin(0,4);s.plot(70,'σ = 1 rad, tc = 1 s; random-walk increment rate q = 2 rad²/s',(0,4),(0,8.2),'Lag L (s)','Increment variance (rad²)',[('exponential covariance: saturates',xs,[2*(1-exp(-t)) for t in xs]),('random walk: qL',xs,[2*t for t in xs])]);
    xx=lin(0,2);s.plot(455,'Stationary example only: R(τ)=exp(−|τ|) rad²',(0,2),(0,2.1),'Offset frequency f (Hz); two-sided PSD, positive half','Phase PSD (rad²/Hz)',[('S(f) = 2 / [1 + (2πf)²]',xx,[2/(1+(2*pi*t)**2) for t in xx])]);s.save()
    s=SVG('shared-delay','A shared source cancels only through matched endpoint responses',650)
    s.box(30,75,160,70,['One source p']);s.box(330,65,200,65,['H₁: delay τ₁']);s.box(330,175,200,65,['H₂: delay τ₂']);s.box(710,110,210,80,['difference 2 − 1','(H₂ − H₁)p']);s.path([(190,110),(260,110),(260,95),(330,95)],arrow=True);s.path([(260,110),(260,205),(330,205)],arrow=True);s.path([(530,95),(620,95),(620,135),(710,135)],arrow=True);s.path([(530,205),(650,205),(650,165),(710,165)],arrow=True)
    xs=lin(0,1);s.plot(285,'Pure-delay identity; approximation requires |πfΔτ| ≪ 1',(0,1),(0,4.2),'f |Δτ| (dimensionless)','Differential squared gain',[('exact: 4 sin²(πfΔτ)',xs,[4*sin(pi*x)**2 for x in xs]),('small-offset: (2πfΔτ)²',xs,[(2*pi*x)**2 for x in xs])]);s.save()
    s=SVG('finite-record-uncertainty','Effective sample count belongs to a particular estimator',830)
    ns=list(range(1,101));rhos=[-.7,0,.7]
    means=lambda n,r:sqrt((n+2*sum((n-m)*r**m for m in range(1,n)))/n**2)
    variances=lambda n,r:sqrt(2*(n+2*sum((n-m)*r**(2*m) for m in range(1,n)))/n**2)
    for y,title,fn,unit in [(70,'Stationary Gaussian AR(1), unit marginal phase variance',means,'SD of mean / marginal SD'),(455,'Same records; variance estimator uses the known zero mean',variances,'SD of variance estimate / marginal variance')]:
        s.plot(y,title,(1,100),(0,1.5),'Number of samples N',unit,[(f'lag correlation ρ = {r}',ns,[fn(n,r) for n in ns]) for r in rhos]);
    s.text(500,650,'ρ = −0.7 and +0.7 coincide',16);s.save()

def group1_details():
    s=SVG('circular-mean','Angle averaging must respect the circle',490)
    cx,cy,r=280,240,150
    s.path([(cx+r*cos(a),cy-r*sin(a)) for a in lin(0,2*pi)],'#9aaab3')
    s.path([(cx-r-30,cy),(cx+r+30,cy)],'#9aaab3')
    for a in [179,-179]:s.path([(cx,cy),(cx+r*cos(radians(a)),cy-r*sin(radians(a)))],COLORS[0],arrow=True)
    s.path([(cx,cy),(cx-r,cy)],COLORS[1],arrow=True)
    s.text(70,160,'+179° / −179°',18);s.text(495,190,'Vector mean direction: 180°');s.text(495,240,'Arithmetic angle mean: 0°');s.text(495,290,'No cycle count is recovered.');s.text(85,440,'Unit circle: dimensionless Re / Im axes. Mean direction requires a nonzero vector mean.',18);s.save()
    s=SVG('phase-validity','An invalid interval does not acquire a phase by interpolation',430)
    s.text(75,100,'Unwrapped phase (rad); schematic, not observed data')
    s.path([(90,290),(870,290)],'#9aaab3');s.text(820,325,'Time (s)')
    s.path([(100,250),(220,225),(350,185)],COLORS[0]);s.path([(610,150),(740,125),(860,100)],COLORS[0])
    s.box(390,120,180,165,['Amplitude invalid','phase undefined','no connecting line'])
    s.text(100,365,'Restart/gap branch must be established independently before joining records.',18);s.save()
    s=SVG('observation-weights','Time weights expose what each phase statistic rejects',510)
    xs=[-.3,-.001,0,1,1.001,1.999,2,3,3.001,3.3]
    s.plot(70,'T = 1 s, centers separated by L = 2 s',(-.3,3.3),(-1.2,1.2),'Time u (s)','Weight w(u) (s⁻¹)',[('single average on [0,1]',xs,[0,0,1,1,0,0,0,0,0,0]),('later average minus earlier',xs,[0,0,-1,-1,0,0,1,1,0,0])]);s.text(95,455,'The differenced weight integrates to zero: a constant phase cancels.',18);s.save()

def group2():
    s=SVG('source-covariance','Construct channel covariance from shared and local sources',580)
    s.s.append('<g transform="translate(0 60)">')
    s.box(30,170,180,80,['Shared source u','RMS 0.02 rad'])
    s.box(360,20,180,65,['Local e₁','RMS 0.01 rad'])
    s.box(360,385,180,65,['Local e₂','RMS 0.03 rad'])
    s.box(610,80,300,75,['x₁ = u + e₁','channel 1 phase'])
    s.box(610,270,300,75,['x₂ = 2u + e₂','channel 2 phase'])
    s.path([(210,210),(260,210)]);s.dot(260,210)
    s.path([(260,210),(260,117),(610,117)],arrow=True);s.text(380,104,'sensitivity 1',17)
    s.path([(260,210),(260,307),(610,307)],arrow=True);s.text(380,294,'sensitivity 2',17)
    s.path([(540,52),(760,52),(760,80)],COLORS[1],arrow=True)
    s.path([(540,417),(760,417),(760,345)],COLORS[2],arrow=True)
    s.text(35,480,'u, e₁, e₂ mutually independent and centered; all gains are phase sensitivities.',18);s.s.append('</g>');s.save()
    s=SVG('covariance-projections','Covariance geometry predicts a projection, not a radial intersection',1010)
    cx,cy,scale=480,300,3500
    for z in [-.06,-.03,0,.03,.06]:
        s.path([(cx-210,cy-scale*z),(cx+210,cy-scale*z)],'#dae2e7',width=1)
        s.path([(cx+scale*z,cy-210),(cx+scale*z,cy+210)],'#dae2e7',width=1)
        s.text(cx-225,cy-scale*z+5,f'{z:.2f}',16,anchor='end');s.text(cx+scale*z,cy+238,f'{z:.2f}',16,anchor='middle')
    s.text(cx+250,cy,'x₁ (rad)',18);s.text(cx-205,70,'x₂ (rad); equal scales',18)
    a=sqrt(.0005);b=.0008/a;c=sqrt(.0025-b*b)
    pts=[(a*cos(t),b*cos(t)+c*sin(t)) for t in lin(0,2*pi,721)]
    s.path([(cx+scale*x,cy-scale*y) for x,y in pts])
    s.path([(cx-scale*.02,cy+scale*.04),(cx+scale*.02,cy-scale*.04)],COLORS[1],'8 4',4)
    h=sqrt(.0014);point=(cx+scale*.0003/h,cy-scale*.0017/h)
    s.dot(*point,6,COLORS[2]);s.text(720,390,'x* = Cw / √(wᵀCw)',17)
    s.text(720,425,'w = (−1,1)',17)
    s.path([point,(920,point[1]),(920,715),(480+5000*h,715)],COLORS[2],'4 4',1.6,True)
    s.text(710,675,'map to wᵀx*',17)
    s.text(40,580,'Blue: xᵀC⁻¹x = 1 for full C. Orange: shared-source-only unit geometry.',18)
    s.text(40,615,'Neither is a probability region without distribution and coverage assumptions.',18)
    for y,w,v,norm in [(715,'x₂ − x₁',.0014,'√2'),(815,'x₂ − 2x₁',.0013,'√5')]:
        h=sqrt(v);left=480-5000*h;right=480+5000*h
        s.path([(left,y),(right,y)],COLORS[0],width=5);s.dot(left,y);s.dot(right,y)
        s.text(40,y-25,f'{w}: coefficient norm {norm}; projected half-width √(wᵀCw) = {h:.6f} rad',18)
        s.text(left,y+30,f'−{h:.4f}',17,anchor='middle');s.text(right,y+30,f'+{h:.4f}',17,anchor='middle')
    s.text(40,905,'Shared-only covariance is rank one: (−2,1) is a noise null; no inverse exists.',18)
    s.text(40,945,'The two projections define different observables and different wanted-signal responses.',18);s.save()
    s=SVG('inverse-conditioning','A nonzero sensitivity difference can still give unusable inference',860)
    s.text(45,85,'Response vectors per 1 V of unknown input (V/V); geometry uses ε = 0.1.',18)
    s.path([(110,365),(410,365)],'#9aaab3');s.path([(110,365),(110,105)],'#9aaab3')
    s.path([(110,365),(310,165)],COLORS[0],arrow=True);s.path([(110,365),(310,145)],COLORS[1],arrow=True)
    s.text(350,165,'a: (1,1); b: (1,1+ε)',18);s.text(350,215,'As ε → 0, these directions merge.',18)
    s.text(350,265,'At ε = 0, only a+b is observable.',18);s.text(110,405,'y₁ scale →');s.text(35,125,'y₂')
    xs=log(.001,1);s.plot(455,'Independent centered channel noises: σn = 1 mV',(.001,1),(.001,2),'Sensitivity separation |ε| (dimensionless)','RMS b-estimate error (V)',[('√2 σn / |ε|',xs,[sqrt(2)*.001/x for x in xs])],True,True);s.save()
    s=SVG('delay-fit-precision','Frequency spread sets local delay precision',890)
    xs=lin(-2,2);obs=[-2,-1,0,1,2]
    px,py=s.plot(70,'Input-oriented phases; a = 0.3 rad, total delay = 5 ns',(-2,2),(.17,.43),'RF frequency offset from f₀ (MHz)','Phase (rad)',[('noiseless model, not measured points',xs,[.3-2*pi*5e-3*x for x in xs])],points=[(x,.3-2*pi*5e-3*x) for x in obs])
    for x in obs:
        yy=.3-2*pi*5e-3*x;s.path([(px(x),py(yy-.02)),(px(x),py(yy+.02))],COLORS[1]);s.path([(px(x)-5,py(yy-.02)),(px(x)+5,py(yy-.02))],COLORS[1]);s.path([(px(x)-5,py(yy+.02)),(px(x)+5,py(yy+.02))],COLORS[1])
    s.text(110,440,'Error bars: assumed individual 1 SD = 0.02 rad; not fit coverage intervals.',17)
    xx=lin(.25,2);s.plot(495,'Five frequencies, independent equal-variance Gaussian phase errors',(.25,2),(0,4.2),'Scale multiplying the five offsets (dimensionless)','Local delay SD (ns)',[('1.006584 / span scale',xx,[1.00658424209/x for x in xx]),('illustrative 2 ns target',xx,[2]*len(xx))]);s.save()
    s=SVG('delay-ambiguity','A precise local slope does not select a global delay branch',850)
    xs=lin(-2,2,1201);f=lambda x,t:.3-2*pi*t*x*.001
    s.plot(70,'Same phase intercept at f₀; observation spacing 1 MHz',(-2,2),(-13,13),'RF offset from f₀ (MHz)','Unwrapped phase (rad)',[('delay 5 ns',xs,[f(x,5) for x in xs]),('delay 1005 ns',xs,[f(x,1005) for x in xs])])
    def wrapped(t):
        yy=[atan2(sin(f(x,t)),cos(f(x,t))) for x in xs]
        for i in range(len(yy)-1,0,-1):
            if abs(yy[i]-yy[i-1])>pi:yy[i]=float('nan')
        return yy
    s.plot(455,'Only integer-MHz dots are observations; off-grid curves are model predictions',(-2,2),(-3.3,3.3),'RF offset from f₀ (MHz)','Principal phase (rad)',[('5 ns branch',xs,wrapped(5)),('1005 ns branch',xs,wrapped(1005))],points=[(x,f(x,5)) for x in [-2,-1,0,1,2]]);s.save()
    s=SVG('uncertainty-sensitivity','Cancellation depends on timing and source-path sensitivity',890)
    xs=lin(.9,1);s.plot(70,'Shared-draw correlation ρ; Δf = 10 MHz, equal coupling',(.9,1),(.13,.23),'ρ of the shared-source draws (dimensionless)','Phase-derived delay SD (ns)',[('√[0.00008 + 0.00072(1−ρ)] / (2π Δf)',xs,[sqrt(.00008+.00072*(1-x))/(2*pi*1e7)*1e9 for x in xs]),('illustrative target 0.15 ns',xs,[.15]*len(xs))])
    s.text(100,440,'Target requires ρ ≥ 0.987741; this is not the total phase-error correlation.',17)
    xx=lin(0,2);s.plot(495,'Same shared draw; x₁=u+e₁, x₂=c u+e₂',(0,2),(.1,.4),'Channel-2 shared-source sensitivity c','Phase-derived delay SD (ns)',[('√[(c−1)² 0.00036 + 0.00008] / (2π Δf)',xx,[sqrt((x-1)**2*.00036+.00008)/(2*pi*1e7)*1e9 for x in xx]),('illustrative target 0.15 ns',xx,[.15]*len(xx))]);s.save()
    s=SVG('nonlinear-uncertainty','Zero local slope does not imply zero uncertainty',850)
    xs=lin(-.8,.8);s.plot(70,'Near the quadrature maximum: y = cos δ',(-.8,.8),(.65,1.05),'Phase deviation δ (rad)','Normalized output y',[('exact cosine',xs,[cos(x) for x in xs]),('first order: y = 1',xs,[1]*len(xs)),('second order: 1 − δ²/2',xs,[1-x*x/2 for x in xs])])
    xx=lin(0,.5);s.plot(455,'Centered Gaussian δ with phase SD σ; output is dimensionless',(0,.5),(0,.19),'Input phase SD σ (rad)','Output standard deviation',[('exact (1−exp(−σ²))/√2',xx,[(1-exp(-x*x))/sqrt(2) for x in xx]),('second-order σ²/√2',xx,[x*x/sqrt(2) for x in xx]),('first order: zero',xx,[0]*len(xx)),('illustrative limit 0.01',xx,[.01]*len(xx))]);s.save()
    from decimal import Decimal,localcontext
    xs=log(1e-10,.01,301);direct=[];stable=[]
    with localcontext() as ctx:
        ctx.prec=65
        for x in xs:
            d=Decimal.from_float(x);ref=2*(d-1+(-d).exp())/(d*d)
            direct.append(float(abs(Decimal.from_float(2*(x-1+exp(-x))/x**2)-ref)/ref))
            stable.append(float(abs(Decimal.from_float(avg(x))-ref)/ref))
    s=SVG('numerical-cancellation','Arithmetic cancellation is not a change in the physical model',510)
    s.plot(70,'g(x)=2(x−1+exp(−x))/x², x=T/tc; Python binary64', (1e-10,.01),(1e-18,100),'Observation ratio x (dimensionless)','Relative evaluation error',[('direct subtraction',xs,direct),('series below 0.001; direct otherwise',xs,stable)],True,True)
    s.text(90,455,'Reference: 65-digit Decimal; independent time integral tends to 1 as x → 0.',17);s.save()


def tracking_rms(fc):
    """Locked-state true residual: finite two-sided noise band plus squared bias."""
    k=2*pi*fc
    return sqrt(1e-6*k/pi*atan(2*pi*1000/k)+(pi/k)**2)

def group3():
    s=SVG('tracking-loop','Separate the true phase residual from the noisy detector output',650)
    s.text(40,85,'All phases at the same comparison plane, orientation and epoch; units rad.',18)
    s.box(30,150,215,85,['Incoming phase θ','wanted θs + nuisance θd'])
    s.box(335,150,220,85,['Phase detector','θ + n − θ̂ = e + n'])
    s.box(665,150,245,85,['k then oscillator 1/s','θ̂ = (k/s)(e+n)'])
    s.path([(245,192),(335,192)],arrow=True);s.path([(555,192),(665,192)],arrow=True)
    s.path([(445,105),(445,150)],COLORS[1],arrow=True);s.text(475,125,'+ n',18)
    s.path([(790,235),(790,330),(300,330),(300,215),(335,215)],COLORS[1],arrow=True)
    s.text(465,310,'Subtract correction phase θ̂',18)
    s.text(590,120,'Internal command: k(e+n), rad/s',17)
    s.box(40,390,400,105,['Correction / estimate output','θ̂ = Tθ + Tn','T(s) = k/(s+k)'])
    s.box(510,390,400,105,['True residual output','e = Eθ − Tn','E(s) = s/(s+k)'])
    s.text(45,550,'Detector output e+n = Eθ + En; it is not the true residual e.',20)
    s.text(45,590,'Locked, amplitude-valid linearization; k > 0 in s⁻¹; zero initial conditions.',18)
    s.save()
    s=SVG('tracking-transfer-budget','A residual-noise choice must also retain the wanted signal',940)
    xx=log(.001,1000)
    s.plot(70,'Wanted and nuisance phase at the same input have the same transfer',(.001,1000),(0,1.05),'|f| / fc (dimensionless, logarithmic)','Phase amplitude transfer',[('estimate |T|',xx,[1/sqrt(1+x*x) for x in xx]),('true residual |E|',xx,[x/sqrt(1+x*x) for x in xx])],True)
    s.text(90,440,'At fc = 100 Hz, a wanted 1 Hz phase has residual amplitude gain 0.0099995.',17)
    xx=log(3,500)
    px,py=s.plot(490,'S₀ = 10⁻⁶ rad²/Hz on |f| ≤ 1000 Hz; Ω = π rad/s',(3,500),(.001,.2),'Loop corner fc (Hz, logarithmic)','True residual (rad RMS, logarithmic)',[
      ('centered detector-noise RMS',xx,[sqrt(1e-6*2*x*atan(1000/x)) for x in xx]),
      ('constant-rate phase bias |Ω/k|',xx,[.5/x for x in xx]),
      ('combined RMS',xx,[tracking_rms(x) for x in xx]),
      ('illustrative RMS criterion 0.02 rad',xx,[.02]*len(xx))],True,True)
    for x in [10,100]:s.dot(px(x),py(tracking_rms(x)),5,COLORS[2])
    s.text(70,865,'RMS criterion met for fc ≈ 28.27–134.33 Hz; no joint wanted-signal limit was set.',17)
    s.text(70,900,'Centered noise and deterministic bias are combined as √(variance + bias²).',17)
    s.save()
    s=SVG('tracking-nonlinear-holdover','Capture, holdover and latency need separate limits',1330)
    xx=lin(-pi,pi,801)
    px,py=s.plot(70,'Noiseless sinusoidal detector: ė/k = Ω/k − sin e',(-pi,pi),(-.6,2.6),'Unwrapped phase error e (rad)','Normalized phase rate ė/k',[
      ('Ω/k = 0.5',xx,[.5-sin(x) for x in xx]),('Ω/k = 1 (marginal)',xx,[1-sin(x) for x in xx]),
      ('Ω/k = 1.5 (slips)',xx,[1.5-sin(x) for x in xx]),('zero phase rate',xx,[0]*len(xx))])
    s.dot(px(asin(.5)),py(0),6)
    s.s.append(f'<circle cx="{px(pi-asin(.5))}" cy="{py(0)}" r="6" fill="white" stroke="{COLORS[0]}" stroke-width="2"/>')
    s.text(75,440,'For Ω/k = 0.5: filled = stable, hollow = unstable; slope is −cos e.',17)
    s.text(75,470,'At Ω/k = 1 the tangent equilibrium attracts from only one side.',17)
    tt=lin(0,.2)
    s.plot(525,'Holdover: fixed bounded frequency error, continuous phase; no restart', (0,.2),(0,.16),'Time since reference loss (s)','Guaranteed phase-error bound (rad)',[
      ('0.02 + 2π · 0.1t',tt,[.02+2*pi*.1*t for t in tt]),('illustrative limit 0.1 rad',tt,[.1]*len(tt))])
    s.text(75,895,'Equality at 0.127324 s; beyond it, this bound cannot support the 0.1 rad limit.',17)
    xx=lin(10,200)
    s.plot(950,'Delayed feedback: kL = π/2 is a marginal crossing, not a practical margin',(10,200),(0,27),'Loop corner fc (Hz)','Marginal latency Lcrit (ms)',[
      ('Lcrit = 1/(4fc)',xx,[250/x for x in xx])],points=[(10,25),(100,2.5)])
    s.save()
    s=SVG('relative-phase-state-sequence','Keep wanted data gated until state and phase validity are established',880)
    labels=[['Reset / retune / changed state','Record identity, epoch and configuration'],
      ['Settle and perform coarse acquisition','Time elapsed alone does not prove validity'],
      ['Resolve branch; apply applicable calibration','Known stimulus and declared uncertainty'],
      ['Held-out frequency / time model check','Checks the fit, not independent acquisition'],
      ['Independent validity evidence','Amplitude, continuity, innovation, headroom'],
      ['Valid wanted-data use','Monitor state, reference and calibration age']]
    for i,lines in enumerate(labels):
        y=80+95*i;s.box(45,y,510,65,lines)
        if i<5:s.path([(300,y+65),(300,y+95)],arrow=True)
        if i>0:s.path([(555,y+32),(610,y+32)],COLORS[1],arrow=True)
    s.box(665,645,260,105,['INVALID: gate data','Any failed check, stale','calibration or lost reference'])
    s.path([(610,207),(610,697),(665,697)],COLORS[1],arrow=True)
    s.text(650,180,'Failure / invalidation bus',17)
    s.text(650,245,'Changed state',18);s.text(650,285,'Amplitude/reference loss',18)
    s.text(650,325,'Unresolved phase branch',18);s.text(650,365,'Failed settling or checks',18)
    s.text(45,695,'Held-out fit data cannot independently test',18)
    s.text(45,725,'the acquisition / instrument chain.',18)
    s.path([(795,750),(795,800),(20,800),(20,110),(45,110)],COLORS[1],arrow=True)
    s.text(50,835,'Return through acquisition, branch, calibration and evidence gates before renewed use.',17)
    s.save()


if __name__=='__main__':
    if len(sys.argv)!=2 or sys.argv[1] not in ('1','2','3'):raise SystemExit('Choose implemented group: 1, 2 or 3')
    if sys.argv[1]=='1':
        group1();group1_details()
    elif sys.argv[1]=='2':group2()
    else:group3()
