"""Synthetic receiver-system examples; standard-library SVG reproduction.

Run from root: python3 engineering/examples/system_models.py 11 (then12 or13).
No selected components, hardware measurements or human validation.
"""
from math import pi,sin,cos,sqrt,log10,radians,degrees,isfinite
from pathlib import Path
from statistics import NormalDist
import sys
from visual_foundations import SVG,lin,log,COLORS,sinc


def gain_bounds(blocker_attenuation=40,wanted_loss=2):
    """dB bounds at equal50ohm planes; two-tone worst composite voltage."""
    ps=10**((-100-wanted_loss)/10)
    pb=10**((-20-blocker_attenuation)/10)
    return 40+wanted_loss,-10-20*log10(sqrt(ps)+sqrt(pb))


def aperture_limits(rho=100):
    k=2*pi/.3
    return 1/(k*.5*radians(.5)*sqrt(rho)),.3/(2*sin(pi/3))


def requirement_case():
    k=2*pi/.3;ds=.15;dl=1.2;rho=100*sinc(.1)**2
    variance=(1/(k*ds)**2+1/(k*dl)**2-1/(k*ds*k*dl))/rho
    nd=NormalDist();m=pi-k*ds*sin(pi/3)
    terms=(2*nd.cdf(-.3/(2*dl)/sqrt(variance)),2*nd.cdf(-m*sqrt(rho)))
    return {'rho':rho,'gain_bounds':gain_bounds(),
            'fine_sigma_degrees':degrees(1/(k*dl*.5*sqrt(rho))),
            'branch_terms':terms,'branch_sum':sum(terms),
            'short_rho':1/(k*ds*.5*radians(.5))**2}


def retained_blocker(eta=1e-5):
    """Composite path-magnitude contract; high-SNR phase approximation."""
    from math import asin
    k=2*pi/.3;rho=requirement_case()['rho'];r=10**(42/20)*eta
    beta=asin(r);minimum_rho=rho*(1-r)**2
    a,b=1/(k*.15),1/(k*1.2)
    sd=sqrt((a*a+b*b-a*b)/minimum_rho)
    bu=2*beta*(a+b);m=pi-k*.15*sin(pi/3)
    nd=NormalDist()
    return {'r':r,'beta':beta,'minimum_rho':minimum_rho,
            'local_sigma_degrees':degrees(1/(k*1.2*.5*sqrt(minimum_rho))),
            'local_bias_degrees':degrees(2*beta/(k*1.2*.5)),
            'branch_bound':2*nd.cdf(-(.125-bu)/sd)+2*nd.cdf(-(m-2*beta)*sqrt(minimum_rho))}


def unit11():
    s=SVG('gain-feasibility','Preselection can create a gain interval; digital cleanup cannot',910)
    s.text(50,85,'P0 → RF selector → P1 → gain/conversion G → P2 digitizer',21)
    s.text(50,128,'Wanted −100 dBm; blocker −20 dBm at P0. Equal 50 Ω planes.',19)
    s.text(50,168,'Selector family: wanted loss 2 dB; total blocker attenuation Aᵦ.',19)
    aa=lin(0,60)
    px,py=s.plot(235,'Both visibility and composite peak must pass at the same gain',(0,60),(0,80),
        'Total RF blocker attenuation Aᵦ (dB)','Power gain G (dB)',
        [('weak-tone lower bound',[*aa],[gain_bounds(a)[0] for a in aa]),
         ('composite-peak upper bound',[*aa],[gain_bounds(a)[1] for a in aa])])
    lo,hi=gain_bounds();x=px(40)
    s.path([(x,py(lo)),(x,py(hi))],COLORS[2],width=7)
    s.text(70,615,'Green interval at Aᵦ = 40 dB: G = 42…49.93 dB',18,COLORS[2])
    s.text(70,655,'At G = 46 dB: wanted −56 dBm; blocker −14 dBm;',20)
    s.text(70,688,'composite peak equivalent −13.931 dBm ≤ −10 dBm.',20)
    s.text(70,755,'No selector: G ≥ 40 dB and G ≤ 9.999 dB → empty interval.',20,COLORS[1])
    s.text(70,805,'A downstream notch cannot repair upstream clipping or missing weak information.',18)
    s.text(70,848,'Stage linearity/noise, actual loading and recovery still require evidence.',18)
    s.save()
    s=SVG('aperture-feasibility','Precision and ambiguity impose different aperture constraints',1120)
    s.text(50,85,'1 GHz; λ = 0.300 m. Sector ±60°; local uncertainty ≤ 0.5°.',20)
    rr=log(100,100000)
    px,py=s.plot(145,'One baseline cannot satisfy both constraints at the supplied energy',(100,100000),(0,1.3),
       'Coherent per-channel SNR ρ (dimensionless; logarithmic)','Baseline length d (m)',
       [('precision minimum',rr,[aperture_limits(r)[0] for r in rr]),
        ('ambiguity ceiling (strict)',rr,[aperture_limits(r)[1] for r in rr]),
        ('short baseline 0.15 m',rr,[.15]*len(rr)),
        ('long baseline 1.20 m',rr,[1.2]*len(rr))],logx=True)
    s.text(75,550,'At ρ = 100: precision needs 1.0943 m; ambiguity needs d < 0.1732 m.',19)
    s.text(75,590,'Short baseline needs ρ = 5321.9: 53.22 ms at zero offset, beyond the brief.',18)
    s.text(75,635,'Use two simultaneous baseline lengths to supply different information.',19)
    for x,label in [(100,'reference'),(197.5,'short'),(880,'long')]:
        s.dot(x,765,6);s.path([(x,735),(x,785)],width=1.5)
        s.text(x,715,label,18,anchor='middle')
    s.path([(100,765),(880,765)],width=2)
    for x,label in [(100,'0'),(197.5,'0.15'),(880,'1.20')]:s.text(x,812,label,18,anchor='middle')
    s.text(490,852,'Physical element position (m; linear scale)',19,anchor='middle')
    s.text(75,915,'Long-baseline aliases: Δu = λ/dₗ = 0.25, where u = sin θ.',20)
    s.text(75,957,'u = 0.25 and u = 0.50 give identical long-baseline wrapped phase.',18)
    s.text(75,999,'The short comparison supplies branch information; it is not a precision substitute.',18)
    s.text(75,1052,'Single plane-wave manifold, correct orientation and calibrated state are supplied.',18)
    s.save()
    s=SVG('architecture-interfaces','Keep physical, analog-survival and data interfaces visible',1010)
    s.text(50,88,'Three simultaneous channels at positions 0, 0.15 and 1.20 m',21)
    s.box(25,160,140,110,['RF ports P0','3 field inputs','−100 / −20 dBm'])
    s.box(215,160,155,110,['RF selectors','2 dB wanted loss','40 dB blocker loss'])
    s.box(425,160,165,110,['Gain/conversion','G = 46 dB','20 MHz real IF'])
    s.box(650,160,245,110,['Digitizers at P2','100 MS/s, 14 stored bits','composite peak ≤ 0.100 V'])
    for a,b in [(165,215),(370,425),(590,650)]:s.path([(a,215),(b,215)],arrow=True)
    s.text(396,142,'P1',19,anchor='middle')
    s.path([(395,410),(395,215)],COLORS[1],arrow=True)
    s.text(395,445,'Injection after selectors',18,COLORS[1],anchor='middle')
    s.text(395,477,'misses field + selector response',17,COLORS[1],anchor='middle')
    s.box(665,355,225,95,['Reference / state / epoch','conversion orientation','sample identity'])
    s.path([(700,355),(700,300),(515,300),(515,270)],COLORS[2],arrow=True)
    s.path([(790,355),(790,270)],COLORS[2],arrow=True)
    s.text(50,555,'P1: wanted −102 dBm; blocker −60 dBm; effective N₀ = −152 dBm/Hz.',19)
    s.text(50,595,'P2: wanted −56 dBm; blocker −14 dBm; all gains at equal 50 Ω.',19)
    s.text(50,635,'Supplied: noise and final P2 limit. Composite observation rejection ≤ 10⁻⁵ required.',18)
    s.text(50,672,'Drive, phase response and intermediate-stage allocations still need evidence.',18)
    s.box(80,715,355,100,['Three channels preserve comparisons','4.2 Gbit/s raw → 4.62 with 10% framing','2.4 W total ≤ 2.5 W'])
    s.box(515,715,355,100,['Observation and processing','1.0 ms record + 0.6 ms processing','retains wanted response + branch identity'])
    s.path([(433,765),(515,765)],arrow=True)
    s.text(65,888,'Combining before observation trades calibration and ambiguity information for traffic.',18)
    s.text(65,934,'A common reference is not evidence of deterministic phase after reset.',19)
    s.save()
    blocker_observation()


def blocker_observation():
    from math import asin
    s=SVG('blocker-observation','An unclipped blocker can still rotate the observation',1110)
    s.text(50,85,'After RF selection: blocker amplitude / wanted amplitude = 125.8925.',19)
    s.text(50,128,'ηᵦ bounds the SUM of blocker image/alias-path magnitudes after observation.',18)
    aa=lin(50,120);rr=[10**((42-a)/20) for a in aa]
    allowed=sin((2*pi/.3)*1.2*(sin(radians(60.02))-sin(radians(60)))/2)
    px,py=s.plot(185,'RF headroom and complete-observation rejection are both needed',(50,120),(1e-4,1),
        'Composite observation rejection −20 log₁₀ ηᵦ (dB)','Retained blocker / wanted amplitude r (dimensionless)',
        [('retained amplitude',aa,rr),('0.02° blocker-bias allocation',aa,[allowed]*len(aa))],logy=True)
    s.dot(px(100),py(10**(-58/20)),5,COLORS[2])
    s.text(65,575,'100 dB contract: r = 0.001259; local bias ≤ about 0.01149° near 60°.',18)
    s.text(65,621,'Without the contract, a nearby blocker can invalidate a noise-only calculation.',18)
    x0,y0,scale,r=110,820,270,.3
    cx=x0+scale;radius=scale*r;tx=x0+scale*(1-r*r);ty=y0-scale*r*sqrt(1-r*r)
    s.path([(x0,y0),(495,y0)],width=1,arrow=True)
    s.path([(x0,y0),(cx,y0)],arrow=True)
    s.s.append(f'<circle cx="{cx}" cy="{y0}" r="{radius}" fill="none" stroke="{COLORS[1]}" stroke-width="2.5"/>')
    s.path([(x0,y0),(tx,ty)],COLORS[1],arrow=True)
    s.path([(cx,y0),(tx,ty)],COLORS[1],dash='4 3',width=1.5)
    s.dot(cx,y0,4);s.text(cx,945,'wanted phasor = 1',18,anchor='middle')
    s.text(165,785,'β',22,COLORS[1])
    s.text(550,745,'Blocker disk: |b| ≤ r < 1',20)
    s.text(550,790,'Tangent ray: β = asin r',20)
    s.text(550,835,'Mean amplitude ≥ 1 − r',20)
    s.text(65,1000,'Disk enlarged to r = 0.30 for geometry; the numerical contract uses 0.001259.',18)
    s.text(65,1048,'Unknown phase is bounded; no independence of blocker paths is assumed.',18)
    s.save()


if __name__=='__main__':
    choice=int(sys.argv[1]) if len(sys.argv)>1 else 11
    {11:unit11}[choice]()
