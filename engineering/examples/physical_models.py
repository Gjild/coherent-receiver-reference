"""Reproducible synthetic illustrations for bounded Chapters 8–10.

Run `python3 engineering/examples/physical_models.py 8` (then 9 or 10).
Uses the established SVG language; no measurements or device specifications.
"""
from pathlib import Path
import sys
from math import pi, sin, cos, tan, atan, radians, degrees, log10, sqrt, exp, isfinite
import cmath
from statistics import NormalDist
from visual_foundations import SVG, lin, COLORS


def chapter8():
    s = SVG('field-port-paths', 'Geometry, transduction and electronics have different planes', 675)
    s.text(45, 90, 'Plane wave: travel direction −ell', 20)
    s.path([(700, 120), (190, 120)], COLORS[0], arrow=True)
    for x, name in [(320, 'r₁'), (650, 'r₂')]:
        s.dot(x, 225, 7)
        s.text(x, 260, name, anchor='middle')
    s.path([(320, 225), (650, 225)], COLORS[1], arrow=True)
    s.text(480, 210, 'b = r₂ − r₁', 19, anchor='middle')
    s.path([(320, 300), (650, 300)], COLORS[2], arrow=True)
    s.text(700, 305, 'ell: sourceward', 19)
    s.text(50, 350, 'If ell · b > 0: position 2 is earlier; Δτg < 0, Δφg > 0.', 20)
    for x, w, lines in [(25, 165, ['Transverse field', 'E⊥ (V/m)']),
                         (245, 165, ['H (m)', 'open-circuit V']),
                         (465, 200, ['L = ZL (ZA+ZL)⁻¹', 'loaded ports Q (V)']),
                         (720, 210, ['G: normalized', 'output z (V)'])]:
        s.box(x, 425, w, 80, lines)
    for a,b in [(190,245),(410,465),(665,720)]:
        s.path([(a,465),(b,465)],arrow=True)
    s.path([(690,590),(690,465)],COLORS[1],arrow=True)
    s.text(400,625,'Injection at Q bypasses H and L',20)
    s.save()
    s = SVG('polarization-error', 'Cross-polar leakage can hide in an excellent amplitude match', 910)
    x=lin(-60,60,241)
    s.plot(70, 'Synthetic rows: h₁ = h(1,0); h₂ = h(1,j0.10)', (-60,60),(-11,11),
           'Linear-polarization angle ψ (degrees)', 'Added relative phase (degrees)',
           [('atan(0.10 tan ψ)',x,[degrees(atan(.1*tan(radians(v)))) for v in x]),
            ('criterion +2°',x,[2]*len(x)),('criterion −2°',x,[-2]*len(x))])
    s.plot(485, 'Equal geometry removed; identical 50-ohm matched loading',(-60,60),(0,.15),
           'Linear-polarization angle ψ (degrees)', '20 log₁₀ |v₂/v₁| after geometry (dB)',
           [('10 log₁₀(1 + 0.01 tan² ψ)',x,[10*log10(1+.01*tan(radians(v))**2) for v in x])])
    s.text(100,865,'Copolar null at |ψ| = 90° is excluded; relative phase there is undefined.',17)
    s.save()
    s = SVG('transduction-blind-path', 'Phase observes path length; separate causes need separate evidence', 550)
    s.box(30,100,170,70,['Range R (m)'])
    s.box(30,250,170,70,['Index n'])
    s.box(300,170,190,85,['Path nR (m)','one-way length'])
    s.box(620,170,290,85,['φ = β − 4πfc nR/c₀','round-trip phase (rad)'])
    s.path([(200,135),(250,135),(250,195),(300,195)],arrow=True)
    s.path([(200,285),(250,285),(250,230),(300,230)],COLORS[1],arrow=True)
    s.path([(490,212),(620,212)],arrow=True)
    s.path([(765,110),(765,170)],COLORS[2],arrow=True)
    s.text(545,85,'Electronic reference β (rad)',19)
    s.text(45,390,'10 GHz, R = 1 m, n = 1: +0.10 mm OR dn = 10⁻⁴ gives −2.40°.',20)
    s.text(45,440,'Injection constrains β; an independent physical reference must constrain R or n.',18)
    s.save()


def chapter9():
    s=SVG('loaded-noise-paths','A shared resistive return creates a physical noise path',650)
    # Explicit circuit: two series arms to one common return, two loads.
    for y,i in [(135,1),(325,2)]:
        s.dot(140,y);s.text(35,y-20,f'Port {i}',20)
        s.text(160,y-12,f'+ vL{i}',17)
        s.text(175,y+130,'−',19)
        s.path([(140,y),(280,y)])
        s.box(280,y-35,200,70,[f'R{i} = 10 Ω',f'+ e{i} −'])
        s.path([(480,y),(600,y),(600,230)])
        s.path([(140,y),(140,y+50)])
        s.box(45,y+50,190,55,['RL = 50 Ω'])
        s.path([(140,y+105),(140,y+125)])
        s.path([(115,y+125),(165,y+125)],'#263c49')
        s.path([(125,y+133),(155,y+133)],'#263c49')
        s.path([(135,y+141),(145,y+141)],'#263c49')
    s.dot(600,230);s.path([(600,230),(705,230)])
    s.box(705,195,180,75,['R0 = 10 Ω','+ e0 −'])
    s.path([(885,235),(920,235),(920,290)])
    s.path([(900,290),(940,290)],'#263c49')
    s.path([(907,298),(933,298)],'#263c49')
    s.path([(914,306),(926,306)],'#263c49')
    s.text(280,85,'Series arms join the same return node',19)
    s.text(270,450,'T = 290 K; source + terminal on the left',19)
    s.text(45,490,'Open-circuit vector below: both shown loads disconnected.',17)
    s.text(45,525,'Open-circuit source vector: (e₁ + e₀, e₂ + e₀)ᵀ',21)
    s.text(45,565,'S(e₀) = S(e₁) = S(e₂) = 2kBT × 10 Ω; real two-sided V²/Hz.',18)
    s.text(45,605,'Loads are noiseless: isolate these source contributions, then add load noise if needed.',17)
    s.save()
    s=SVG('reciprocal-noise-paths','Reciprocal mixing depends on both spectra and on filter placement',1000)
    for x,w,lines in [(25,190,['Blocker bRF','power spectrum']),
                       (265,175,['RF selector','F(ν)']),
                       (495,190,['Mixer × exp(−jφ)','effective phase']),
                       (740,185,['Observation W','wanted band'])]:s.box(x,95,w,80,lines)
    for a,b in [(215,265),(440,495),(685,740)]:s.path([(a,135),(b,135)],arrow=True)
    s.box(120,275,235,75,['Source LO phase','through H₀'])
    s.box(590,275,300,75,['Internal branch phase','generated after LO access'])
    s.path([(355,310),(540,310),(540,175)],COLORS[1],arrow=True)
    s.path([(740,275),(740,235),(635,235),(635,175)],COLORS[2],arrow=True)
    s.text(448,120,'b',18)
    s.text(45,378,'After selector: Sb(ν) = |F(ν)|² SbRF(ν), in W/Hz.',18)
    s.text(45,405,'Generated in-band noise survives a later blocker-carrier notch.',20)
    x=[-250,-100.001,-100,100,100.001,250]
    px,py=s.plot(455,'Δ = 1 MHz; S₀ = 10⁻¹² rad²/Hz; symmetric partner near +Δ',(-250,250),(0,5),
      'LO offset q + Δ (kHz); shown near q = −Δ','Effective phase PSD / S₀',
      [('phase density',x,[4,4,1,1,4,4])])
    s.path([(px(-200),py(.4)),(px(200),py(.4))],COLORS[1],width=7)
    s.text(175,855,'Orange footprint: uniform 400 kHz blocker at output offset f = 0.',18)
    s.text(100,900,'Half samples S₀, half samples 4S₀ → mean 2.5S₀.',20)
    s.text(100,945,'For |f| ≤ 50 kHz the footprint shifts; overlap widths stay 200 + 200 kHz.',17)
    s.save()
    s=SVG('waveform-timing','Timing error follows the entire analog slope and clock spectrum',950)
    x=sorted(set(lin(0,1)+lin(0,.01,101)))
    sigma=1e-12;fd=1e7;fb=1e8;ad=.01
    ys=[sigma/sqrt(2)*sqrt((2*pi*fd*ad)**2+(2*pi*fb*a)**2)*1e6 for a in x]
    base=sigma/sqrt(2)*2*pi*fd*ad*1e6
    s.plot(70,'σt = 1 ps; desired: 10 mV peak at 10 MHz; blocker: 100 MHz',
      (0,1),(.1,1000),'Blocker peak amplitude Ab (V)','Total raw timing-error RMS (μV; log scale)',
      [('complete two-tone waveform',x,ys),('desired tone only',x,[base]*len(x))],logy=True)
    s.text(85,490,'These total raw errors do not specify in-band error without a clock PSD.',18)
    s.box(30,555,230,75,['Blocker: Ab = 1 V peak','slope at 100 MHz'])
    s.box(30,710,230,75,['Time error ε','90 MHz; 1 ps RMS'])
    s.box(365,620,190,75,['Multiply','e = ε dx/dt'])
    s.box(665,555,250,75,['10 MHz error','passes wanted band'])
    s.box(665,710,250,75,['190 MHz error','rejected by W'])
    s.path([(260,592),(310,592),(310,640),(365,640)],arrow=True)
    s.path([(260,747),(310,747),(310,675),(365,675)],COLORS[1],arrow=True)
    s.path([(555,645),(610,645),(610,592),(665,592)],arrow=True)
    s.path([(555,675),(610,675),(610,747),(665,747)],arrow=True)
    s.text(60,860,'500 MS/s ideal sampler: no alias needed. Each sideband: 0.3142 mV RMS.',19)
    s.text(60,905,'Raw input must accommodate the 1.01 V peak envelope before digital rejection.',18)
    s.save()


def extraction_weights(theta=pi/6, jammer_variance=100):
    """Unit desired response for a=(1,0), background I, jammer path (c,s).

    Observations are x/sigma. This realizes the bounded illustrative receiver;
    it does not estimate a physical covariance or supply a hardware guarantee.
    """
    try:
        theta=float(theta);jammer_variance=float(jammer_variance)
    except (TypeError,ValueError,OverflowError) as exc:
        raise ValueError('Finite real model parameters required') from exc
    if not isfinite(theta) or not isfinite(jammer_variance) or jammer_variance<0:
        raise ValueError('Finite angle and nonnegative finite jammer variance required')
    c,s=cos(theta),sin(theta)
    beta=jammer_variance/(1+jammer_variance)
    q0=s*s+c*c/(1+jammer_variance)
    try:
        w=(1.,-beta*c*s/q0)
        variance=w[0]**2+w[1]**2+jammer_variance*(w[0]*c+w[1]*s)**2
    except (OverflowError,ZeroDivisionError) as exc:
        raise ValueError('Numerically unusable covariance') from exc
    if not isfinite(variance) or variance<=0:
        raise ValueError('Numerically unusable covariance')
    return w,q0,variance


def bounded_extract(x,theta=pi/6,jammer_variance=100,p_fa=.001):
    """Known-phase Gaussian decision; ValueError means invalid, not H0.

    Requires exactly two finite complex observations in normalized voltage units.
    Reads at most three iterator elements to reject extra coordinates promptly.
    Source-draw evaluation lives in tests/test_physical_models_stdlib.py.
    """
    values=[]
    try:
        observations=iter(x)
        for _ in range(3):
            try:
                value=next(observations)
            except StopIteration:
                break
            values.append(complex(value))
        p_fa=float(p_fa)
    except Exception as exc:
        raise ValueError('Two finite complex observations and a valid probability required') from exc
    x=tuple(values)
    if len(x)!=2 or any(not isfinite(v.real) or not isfinite(v.imag) for v in x):
        raise ValueError('Exactly two finite complex observations required')
    if not isfinite(p_fa) or not 0<p_fa<1:
        raise ValueError('False-alarm probability must lie strictly between zero and one')
    w,q0,variance=extraction_weights(theta,jammer_variance)
    amplitude=sum(wi*xi for wi,xi in zip(w,x))
    if not isfinite(amplitude.real) or not isfinite(amplitude.imag):
        raise ValueError('Nonfinite extraction result')
    z=amplitude.real/(sqrt(variance)/sqrt(2))
    if not isfinite(z):
        raise ValueError('Nonfinite extraction result')
    # Tail form avoids cancellation in 1-p_fa for a small probability.
    threshold=-NormalDist().inv_cdf(p_fa)
    return {'amplitude':amplitude,'z':z,'decision':z>threshold,
            'threshold':threshold,'q0':q0,'variance':variance}


def gamma_tail_integer(shape,threshold):
    """Finite gamma survival sum for the small integer-shape examples."""
    term=total=1.
    for k in range(1,shape):
        term*=threshold/k;total+=term
    return exp(-threshold)*total


def energy_detection_probability(records,total_rho,threshold):
    """Poisson/gamma mixture, truncated at 200 terms for this unit's cases.

    Intended for N=1 or4 and total_rho<=17; not a general numerical CDF library.
    """
    weight=exp(-total_rho);probability=0.
    for k in range(200):
        probability+=weight*gamma_tail_integer(records+k,threshold)
        weight*=total_rho/(k+1)
    return probability


def chapter10():
    s=SVG('detection-statistic','A detection claim needs hypotheses, a statistic and a threshold',930)
    s.box(30,100,200,85,['Finite record x','known C and a'])
    s.box(295,100,250,85,['Whiten x AND a','t = aᴴ C⁻¹ x'])
    s.box(620,100,300,85,['r = t / √q','Z = √2 Re r > γ'])
    s.path([(230,142),(295,142)],arrow=True);s.path([(545,142),(620,142)],arrow=True)
    s.text(50,255,'Proper complex Gaussian noise; q = aᴴC⁻¹a, ρ = A²q.',20)
    s.text(50,305,'Known phase; one specified test, α = 0.001. Geometry and state fixed.',18)
    xx=lin(-4,8,361);q0=26/101;mu=sqrt(32*q0);g=NormalDist().inv_cdf(.999)
    px,py=s.plot(365,'Worked detector: A/σ = 4, template separation 30°',(-4,8),(0,.44),
       'Normalized real statistic Z (dimensionless)','Probability density per unit Z',
       [('H₀: mean 0, variance 1',xx,[exp(-v*v/2)/sqrt(2*pi) for v in xx]),
        (f'H₁: mean {mu:.4f}, variance 1',xx,[exp(-(v-mu)**2/2)/sqrt(2*pi) for v in xx])])
    s.path([(px(g),py(0)),(px(g),py(.44))],COLORS[2],'5 4')
    s.text(px(g)+10,py(.44)-13,'γ = 3.0902',17,COLORS[2])
    s.text(100,795,'PFA = 0.001; PD = 0.4129. Improving a detector does not ensure adequacy.',19)
    s.text(100,850,'Unknown phase uses |r|² and a different null law/threshold.',19)
    s.save()
    s=SVG('integration-retention','A coherent sum can lose a wanted signal that still has energy',980)
    s.text(55,90,'Four aligned desired terms',20)
    for i in range(4):s.path([(60+85*i,180),(145+85*i,180)],COLORS[0],arrow=True)
    s.text(50,250,'Complex sum = 4u; energy sum = 4|u|²',18)
    s.text(505,90,'Quarter-turn progression',20)
    pts=[(610,245),(750,245),(750,105),(610,105),(610,245)]
    for i in range(4):s.path(pts[i:i+2],COLORS[i],arrow=True)
    s.text(505,300,'Complex sum = 0; energy sum = 4|u|²',18)
    s.text(60,340,'u = A√q: wanted scalar term in each normalized record',18)
    xx=lin(0,180,361)
    loss=lambda d:abs(sum(cmath.exp(1j*m*radians(d)) for m in range(4))/4)**2
    s.plot(380,'Equal independent noise per record; residual phase advance δ',
      (0,180),(0,1.05),'Phase advance δ per record (degrees)','Coherent signal-to-noise ratio / (4ρ)',
      [('L₄ = |Σ exp(jmδ) / 4|²',xx,[loss(d) for d in xx])])
    s.text(80,815,'At δ = 90° the desired complex sum cancels; correct relative phasing restores it.',18)
    s.text(80,865,'Noncoherent Q₄ retains energy but has a gamma null, not the coherent null.',18)
    s.text(80,915,'A nonzero mean/energy is not by itself a detection probability.',18)
    s.save()
    s=SVG('rejection-information','Exact rejection spends desired information when templates align',1000)
    cx,cy=210,245;scale=190
    s.path([(70,cy),(460,cy)],'#9aaab3');s.path([(cx,355),(cx,90)],'#9aaab3')
    s.path([(cx,cy),(cx+scale,cy)],COLORS[0],arrow=True);s.text(410,240,'a',22)
    s.path([(cx,cy),(cx+scale*cos(pi/6),cy-scale*sin(pi/6))],COLORS[1],arrow=True)
    s.text(390,140,'b',22,COLORS[1])
    s.path([(cx,cy),(cx+scale*.25,cy+scale*sqrt(3)/4)],COLORS[2],arrow=True)
    s.text(270,350,'P⊥a',20,COLORS[2])
    s.text(500,115,'θ = 30°; dimensionless template vectors',18)
    s.text(500,170,'Projection keeps ||P⊥a||² = 1/4.',20)
    s.text(500,225,'Unit response needs 4σ² output noise.',20)
    s.text(500,280,'At 30°: optimum 0.25743; null 0.25000.',18)
    s.text(500,335,'The template-space angle is not bearing.',18)
    xx=lin(0,90,241)
    s.plot(405,'Independent background σ²I; finite jammer variance 100σ²',
      (0,90),(0,1.05),'Template separation θ (degrees; vector space)','Output SNR / (A²/σ²), dimensionless',
      [('colored optimum',xx,[sin(radians(t))**2+cos(radians(t))**2/101 for t in xx]),
       ('exact nuisance null',xx,[sin(radians(t))**2 for t in xx]),
       ('first mode only',xx,[1/(1+100*cos(radians(t))**2) for t in xx])])
    s.text(80,840,'At θ = 0: hard null erases a; finite random noise still leaves q > 0.',19)
    s.text(80,895,'At θ = 90°: nuisance and wanted templates are orthogonal.',19)
    s.text(80,950,'Normalization restores amplitude, not the discarded information.',18)
    s.save()
    s=SVG('reference-leakage','Frozen cancellation weights also subtract wanted leakage',1030)
    s.box(30,75,180,70,['Wanted s'])
    s.box(30,295,180,70,['Interferer j'])
    s.box(350,80,200,100,['Primary x','s + j + n'])
    s.box(350,280,200,100,['Reference r','j + ℓs + v'])
    s.path([(210,110),(270,110)]);s.dot(270,110)
    s.path([(270,110),(350,110)],arrow=True)
    s.path([(270,110),(270,305),(350,305)],COLORS[1],arrow=True)
    s.text(285,260,'leakage ℓ',18,COLORS[1])
    s.path([(210,330),(240,330)]);s.dot(240,330)
    s.path([(240,330),(240,160),(350,160)],arrow=True)
    s.path([(240,330),(350,330)],arrow=True)
    s.box(585,295,90,70,['h'])
    s.box(720,170,210,100,['y = x − hr','(1−hℓ)s wanted'])
    s.path([(550,130),(690,130),(690,200),(720,200)],arrow=True)
    s.text(695,187,'+',22)
    s.path([(550,330),(585,330)],arrow=True)
    s.path([(675,330),(690,330),(690,245),(720,245)],arrow=True)
    s.text(695,268,'−',22)
    h=100/101;xx=lin(0,1)
    s.plot(445,'Weight trained with s = 0, then frozen: h = 100/101',
      (0,1),(-48,0),'Operational real leakage ℓ (dimensionless)','Desired power transfer (dB)',
      [('20 log₁₀ |1 − hℓ|',xx,[20*log10(abs(1-h*v)) for v in xx])])
    s.text(80,875,'At ℓ = 1: noise falls 17.05 dB, wanted power falls 40.09 dB.',20)
    s.text(80,930,'Wanted-to-noise ratio worsens by 23.03 dB despite the quieter output.',19)
    s.text(80,985,'Complex leakage is dangerous when hℓ ≈ 1, including its phase.',18)
    s.save()


if __name__ == '__main__':
    {'8': chapter8, '9': chapter9, '10': chapter10}[sys.argv[1]]()
