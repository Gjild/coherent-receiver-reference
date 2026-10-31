"""Synthetic analog/reference subsystem models; no selected hardware or measurements.

Run from root: python3 engineering/examples/subsystem_models.py 14.
"""
from math import pi, log10, log, sqrt, exp, asin, degrees, isfinite
from dataclasses import dataclass
from visual_foundations import SVG, COLORS, lin
import sys


def analog_case(attenuation=49.):
    """Equal 50-ohm delivered powers; one selected in-band IM3 product."""
    gains=[20.,6.,20.]; intercepts=[0.,20.,25.]
    wanted=-102.; blocker=-20.-attenuation
    wanted_inputs=[];blocker_inputs=[];products=[]
    for i,(gain,ip) in enumerate(zip(gains,intercepts)):
        wanted_inputs.append(wanted);blocker_inputs.append(blocker)
        products.append(3*blocker-2*ip+sum(gains[i:]))
        wanted+=gain;blocker+=gain
    r=sum(10**((p-wanted)/20) for p in products)
    loss=10**.2;g1=100.;gm=10**.6;f1=10**.2;fm=10**.8;fb=10**.6
    early=loss*f1+loss*(fm-1)/g1+loss*(fb-1)/(g1*gm)
    late=f1+(loss-1)/g1+loss*(fm-1)/g1+loss*(fb-1)/(g1*gm)
    return dict(wanted=wanted,blocker=blocker,peak=20*log10(2*10**(blocker/20)+10**(wanted/20)),
                wanted_inputs=wanted_inputs,blocker_inputs=blocker_inputs,
                output_products=products,phasor_radius=r,bias_degrees=degrees(asin(r)),
                early_nf=10*log10(early),late_nf=10*log10(late))


@dataclass
class GainPolicy:
    """Bounded simulation policy, microsecond time; monitor/pulse knowledge supplied.

    pulse is exposure at this instant; integrate the preceding held interval.
    Unknown/out-of-envelope history latches fault. This never promises protection.
    """
    state: str='H'
    q: float=0.
    previous_t: float | None=None
    previous_pulse: bool=False
    quiet_since: float | None=None
    changed_t: float=float('-inf')
    fault: bool=False

    def step(self,t,pulse=False,peak_h=-16.8827,wanted_h=-56.,qualified=True,calibrated=True):
        if not all(isfinite(v) for v in [t,peak_h,wanted_h]):raise ValueError('finite inputs required')
        if self.previous_t is not None:
            dt=t-self.previous_t
            if dt<=0:raise ValueError('time must increase')
            self.q=1. if self.previous_pulse else self.q*exp(-dt/40.)
        if not qualified:self.fault=True
        if pulse:self.q=1.
        if pulse or peak_h>-16:self.quiet_since=None
        elif self.previous_pulse or self.quiet_since is None:self.quiet_since=t
        new=self.state
        if pulse or peak_h>-13:new='L'
        elif self.state=='L' and peak_h<=-16 and t-self.quiet_since>=20:new='H'
        if new!=self.state:self.state=new;self.changed_t=t
        age=t-self.changed_t
        phase=8*self.q+3*exp(-age/15.)
        amplitude=.1*self.q+.02*exp(-age/5.)
        peak=peak_h-(20 if self.state=='L' else 0)
        wanted=wanted_h-(20 if self.state=='L' else 0)
        valid=(not self.fault and not pulse and calibrated and peak<=-10 and wanted>=-60
               and phase<=.1 and amplitude<=.01 and age>=10)
        self.previous_t=t;self.previous_pulse=pulse
        return dict(t=t,state=self.state,q=self.q,phase=phase,amplitude=amplitude,
                    peak=peak,wanted=wanted,valid=valid,fault=self.fault)


def policy_trace(attenuation=49,stop=240):
    policy=GainPolicy();peak=analog_case(attenuation)['peak']
    return [policy.step(t,pulse=t<10,peak_h=peak) for t in range(stop+1)]


def unit14():
    s=SVG('analog-prevention-paths','Filter placement trades noise against survival and generated products',1050)
    for y,label,early in [(115,'Early selection',True),(380,'Late selection',False)]:
        s.text(40,y-25,label,21)
        blocks=[['Selector','wanted −2 dB','blockers −49 dB'],['LNA','G = 20 dB','IIP3 = 0 dBm']]
        if not early:blocks.reverse()
        blocks += [['Mixer / IF','G = 6 dB','IIP3 = +20 dBm'],['Backend H','G = 20 dB','IIP3 = +25 dBm']]
        for i,lines in enumerate(blocks):
            x=40+i*230;s.box(x,y,190,110,lines)
            if i<3:s.path([(x+190,y+55),(x+230,y+55)],arrow=True)
        s.text(45,y+155,'P0: wanted 1.000 GHz; blockers 1.010 / 1.020 GHz, each −20 dBm.',18)
        s.text(45,y+190,'Early: LNA input −69 dBm/tone; late: −20 dBm/tone before any rejection.' if early else
               '2f₁ − f₂ = 1.000 GHz: an upstream product follows the wanted passband.',18)
    c=analog_case()
    s.text(45,680,f"Synthetic thermal NF: early {c['early_nf']:.3f} dB; late {c['late_nf']:.3f} dB.",20)
    s.text(45,735,'Late selection has a quieter linear model but violates the LNA peak envelope.',19)
    s.text(45,790,'Post-conversion gain reduction cannot undo earlier compression or in-band IM3.',19)
    s.text(45,845,'LO drive / impedance, matching, reverse coupling, bias and dissipation need evidence.',18)
    s.text(45,905,'A pulse in the wanted band needs isolation / protection; this selector cannot remove it.',18)
    s.text(45,975,'All gains/intercepts/qualification limits are supplied envelopes, not device data.',18);s.save()
    s=SVG('analog-blocker-region','Headroom, coherent distortion and gain-policy restoration are different tests',1130)
    aa=lin(40,52)
    s.plot(75,'Full three-tone peak at the readout, all phases allowed',(40,52),(-21,-7),
           'RF rejection per blocker Aᵦ (dB)','Equivalent peak power (dBm)',
           [('wanted + two blockers',aa,[analog_case(a)['peak'] for a in aa]),
            ('absolute ceiling',aa,[-10]*len(aa)),('H → L threshold',aa,[-13]*len(aa)),
            ('L → H threshold',aa,[-16]*len(aa))])
    xx=lin(42.1,52)
    s.plot(520,'One in-band IM3 product: worst-phase sum of three stage contributions',(42.1,52),(0,.05),
           'RF rejection per blocker Aᵦ (dB)','Bound on coherent phase bias (degrees)',
           [('cubic small-signal model',xx,[analog_case(a)['bias_degrees'] for a in xx]),
            ('illustrative allocation',xx,[.02]*len(xx))])
    c=analog_case()
    s.text(45,970,f"At Aᵦ = 49 dB: peak {c['peak']:.5f} dBm; IM3 bound {c['bias_degrees']:.6f}°.",19)
    s.text(45,1020,'At 46 dB, H may persist but cannot return after L: hysteresis consumes margin.',18)
    s.text(45,1075,'Cubic curves apply only within qualified stage envelopes; no overload extrapolation.',18);s.save()
    s=SVG('analog-memory-recovery','A quiet output can retain history-dependent phase error',1050)
    tt=lin(0,240)
    s.plot(70,'After pulse end: q(t) = q₀ exp(−t / 40 μs)',(0,240),(.01,10),
           'Time since pulse end (μs)','Residual phase bound / model (degrees)',
           [('10 μs exposure: q₀ = 1 − exp(−2)',tt,[8*(1-exp(-2))*exp(-t/40) for t in tt]),
            ('all qualified histories: q₀ ≤ 1',tt,[8*exp(-t/40) for t in tt]),
            ('phase limit',tt,[.1]*len(tt))],logy=True)
    s.text(45,505,'Post-pulse weak response: (1 − 0.1q) exp[j (8°)q] times its calibrated state.',19)
    s.text(45,560,'The memoryless model sets q = 0 as soon as the pulse ends; it fails this example.',18)
    s.text(45,615,'Specific pulse reaches 0.1° after 169.465 μs; q₀ ≤ 1 needs 175.281 μs.',18)
    s.text(45,670,'Gain-state settling adds phase: budget the sum, not two separate full allowances.',18)
    s.text(45,725,'A 176 μs hold passes with the stated concurrent gain transition and 40 μs bound.',18)
    s.text(45,780,'Doubling the recovery constant doubles the memory wait: the 180 μs deadline fails.',18)
    s.text(45,835,'These exponential coefficients are a synthetic envelope, not a measured device model.',18)
    s.text(45,895,'Characterize pulse width / spacing, level, bias, temperature and load before adopting it.',18)
    s.text(45,975,'Unknown exposure or missing state calibration latches/holds invalid data.',18);s.save()
    tr=policy_trace();s=SVG('analog-validity-policy','Execute the gain and validity policy against the same exposure history',1170)
    tt=[x['t'] for x in tr]
    s.plot(70,'Pulse from 0 to 10 μs; H is restored after 20 μs quiet dwell',(0,240),(-.1,1.1),
           'Time from pulse start (μs)','State indicator (dimensionless)',
           [('H gain selected',tt,[int(x['state']=='H') for x in tr]),
            ('valid weak observation',tt,[int(x['valid']) for x in tr])])
    s.plot(515,'Residual allowance is checked after restoring the high-gain calibration',(0,240),(.01,12),
           'Time from pulse start (μs)','Conservative phase bound (degrees)',
           [('memory + gain transition',tt,[x['phase'] for x in tr]),('limit',tt,[.1]*len(tr))],logy=True)
    s.text(45,970,'H returns at 30 μs; first valid 1 μs-grid output is 186 μs (176 μs after pulse).',18)
    s.text(45,1025,'Low gain is safer downstream but wanted −76 dBm fails the −60 dBm visibility floor.',18)
    s.text(45,1080,'Input protection is a separate physical contract; an invalid flag does not protect hardware.',18)
    s.text(45,1130,'State coefficient, pulse history and exposure qualification accompany every valid record.',18);s.save()


if __name__=='__main__':
    {14:unit14}[int(sys.argv[1])]()
