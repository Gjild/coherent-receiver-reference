"""Reproducible synthetic illustrations for bounded Chapters 8–10.

Run `python3 engineering/examples/physical_models.py 8` (then 9 or 10).
Uses the established SVG language; no measurements or device specifications.
"""
from pathlib import Path
import sys
from math import pi, sin, cos, tan, atan, radians, degrees, log10, sqrt
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


if __name__ == '__main__':
    {'8': chapter8, '9': chapter9}[sys.argv[1]]()
