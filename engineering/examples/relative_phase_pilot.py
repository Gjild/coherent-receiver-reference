"""Run from root with PYTHONPATH=engineering/src; all inputs illustrative."""
import math
from coherent_receiver.relative_phase import endpoint_psd, simpson, fit_phase_delay, absolute_phase_variance

print('ILLUSTRATIVE predictions; two-sided 1–10000 Hz band; no measured data')
for case, delay, shared_branch in [("compact",1e-8,1e-9),("exposed distribution",1e-7,1e-7)]:
    for name, branch, corner in [('shared LO',shared_branch,None),('local locked',1e-8,100)]:
        f = lambda x: endpoint_psd(x,delay,1e-6,branch,corner)
        vs = [2*simpson(f,1,10000,n) for n in [4096,8192,16384]]
        print(f'{case}, {delay:g} s {name}: variance={vs[-1]:.10g} rad², '
              f'sd={math.sqrt(vs[-1])*180/math.pi:.6f} deg; '
              f'last refinement={abs(vs[-1]-vs[-2]):.3g} rad²')
print('RF delay sign: delta theta = -360 * f_RF * delta delay (degrees)')
print('2 ps/K * 2 K at 1 GHz:',-360*1e9*4e-12,'deg')
print('30 ps/K * 2 K at 1 GHz:',-360*1e9*60e-12,'deg')
print('Drift-only age scale:', .5/.216, 's (not update period)')
for name,dt,b,corner,T in [('compact',1e-8,1e-9,None,.01),
                          ('local10',1e-7,1e-8,100,.01),
                          ('local50',1e-7,1e-8,100,.05)]:
    def integrand(f):
        w=math.sin(math.pi*f*T)/(math.pi*f*T)
        return endpoint_psd(f,dt,1e-6,b,corner)*w*w
    v=[2*simpson(integrand,1,10000,n) for n in [65536,131072]]
    sd=math.sqrt(v[-1])*180/math.pi
    print(name,'snapshot SD=',sd,'deg; including independent 0.03 deg=',
          math.hypot(sd,.03),'deg; refinement=',abs(v[-1]-v[0]),'rad²')
    print('center period bound=',.5/.216-(.75*T+.1),
          's; P=2s drift bound=',.216*(2+.75*T+.1),
          'deg; invalid fraction=',(.02+T+.1)/2)
freqs=[.999e9,1e9,1.0015e9]
phases=[.3-2*math.pi*(f-1e9)*2e-9 for f in freqs]
fit=fit_phase_delay(freqs,phases,state_ids=['fixed']*3)
print('Synthetic local fit:',fit)
print('Phase at stated 1 GHz reference:',fit.phase_at(1e9),'rad')
print('Absolute residual SD for independent 0.05 deg calibration:',
      math.sqrt(absolute_phase_variance(.362364**2,.05**2)),'deg')
print('DC-rejecting band SD remains 0.362364 deg for frozen calibration')
u=math.sqrt(.03**2+.03**2-2*.8*.03*.03+.04**2+.02**2)
print('Illustrative absolute phase combined standard uncertainty:',u,'deg; twice u:',2*u)
