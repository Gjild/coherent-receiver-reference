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


if __name__ == '__main__':
    {'8': chapter8}[sys.argv[1]]()
