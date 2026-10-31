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


def pll_transfer(f,fn=20000.,zeta=2**-.5):
    w=2*pi*fn;s=2j*pi*f;d=s*s+2*zeta*w*s+w*w
    return (2*zeta*w*s+w*w)/d,s*s/d


def pll_density(f,fn=20000.):
    if abs(f)>20e6:return 0.
    h,e=pll_transfer(f,fn)
    return 102**2*1e-16*abs(h)**2+1e-3/(f*f+1)*abs(e)**2


def pll_case(fn=20000.,n=4096):
    from visual_foundations import quad
    variance=2*quad(lambda u:pll_density(exp(u),fn)*exp(u),log(10),log(1e6),n)
    wait=log(2**.5/.01)/((2**-.5)*2*pi*fn)
    return dict(variance=variance,sigma_degrees=degrees(sqrt(variance)),wait_us=1e6*wait)


def lo_contract(branch_density=3e-11,beta=2e-4):
    from math import sin,radians
    pb=1e-9;ps=10**(-13.2);allowed=10**(-19.2)
    endpoint=pll_density(10e6)+2e-12+branch_density
    radius=sqrt(pb/ps)*beta/2
    return dict(mask=allowed/pb,endpoint=endpoint,rm_dbm_hz=10*log10(pb*endpoint/.001),
                beta_limit=2*sin(radians(.02))*sqrt(ps/pb),
                phase_spur_degrees=degrees(asin(radius)) if radius<1 else None,
                average_sigma_degrees=degrees(sqrt(2*branch_density/.002+2*5e-12*5e-9/.002**2)))


def unit15():
    from math import sin,cos,radians
    from visual_foundations import log as logspace
    s=SVG('pll-source-paths','Trace each synthesizer disturbance to its injection plane',1100)
    for x,w,lines in [(35,150,['Reference phase','10 MHz']), (245,135,['Detector','error e']),
                      (435,170,['PI controller','Kp + Ki/s']), (660,140,['VCO','Kv/s'])]:
        s.box(x,100,w,90,lines)
    for a,b in [(185,245),(380,435),(605,660),(800,860)]:s.path([(a,145),(b,145)],arrow=True)
    s.dot(860,145,6);s.path([(866,145),(925,145)],arrow=True);s.text(870,110,'θ',22)
    s.box(470,300,170,75,['Feedback ÷ N','N = 102'])
    s.path([(860,151),(860,337),(640,337)],arrow=True)
    s.path([(470,337),(310,337),(310,190)],arrow=True);s.text(325,225,'−',24)
    s.box(40,300,205,80,['Detector noise n_d','input phase (+)'])
    s.path([(245,335),(265,335),(265,190)],COLORS[1],arrow=True)
    s.box(435,220,210,65,['Tuning noise nᵤ (V)','after controller'])
    s.path([(630,220),(630,145)],COLORS[1],arrow=True);s.dot(630,145)
    s.box(305,405,300,75,['Divider output error ndiv','reference-frequency phase'])
    s.path([(400,405),(400,337)],COLORS[1],arrow=True);s.dot(400,337)
    s.box(665,405,230,75,['Intrinsic VCO phase φv','added before feedback tap'])
    s.path([(840,405),(840,145),(854,145)],COLORS[1],arrow=True)
    s.text(45,535,'θ = N H (φr + nd − ndiv) + E φv + E (Kv/s) nu; E = 1 − H.',19)
    s.text(45,585,'Filter/tuning voltage noise nu and feedback-divider noise need their own planes.',18)
    s.box(45,665,200,85,['Loop output θ','pre-buffer plane'])
    s.box(345,665,230,85,['Common buffer','add φb outside loop'])
    s.box(685,665,230,85,['Distribution branches','A₁φs + η₁; A₂φs + η₂'])
    s.path([(245,708),(345,708)],arrow=True);s.path([(575,708),(685,708)],arrow=True)
    s.text(45,825,'Low-pass reference/PFD noise and high-pass VCO noise trade against settling.',19)
    s.text(45,885,'A wider loop cannot suppress noise or feedthrough added after the feedback tap.',18)
    s.text(45,945,'Divider / fractional / output states and coarse tuning are absent from this locked model.',18)
    s.text(45,1025,'Physical loop-filter values, VCO tuning slope, delays and source spectra need evidence.',18);s.save()
    s=SVG('pll-loop-tradeoff','Choose a loop from noise and settling together',1500)
    ff=logspace(10,1e6)
    s.plot(70,'Pre-buffer phase spectra: same sources, different natural frequency',(10,1e6),(1e-16,1e-9),
           'Offset frequency |f| (Hz)','Two-sided phase PSD (rad²/Hz)',
           [(f'fn = {fn/1000:g} kHz',ff,[pll_density(f,fn) for f in ff]) for fn in [2000,10000,20000,40000]],True,True)
    nn=lin(1000,50000);vals=[pll_case(fn,n=512) for fn in nn]
    s.plot(525,'Band-limited phase RMS: 10 Hz ≤ |f| ≤ 1 MHz',(1,50),(0,.09),
           'Natural frequency fn (kHz)','Pre-buffer phase RMS (degrees)',
           [('integrated synthetic sources',[n/1000 for n in nn],[r['sigma_degrees'] for r in vals]),
            ('0.03° interface',[n/1000 for n in nn],[.03]*len(nn))])
    s.plot(980,'Envelope for a locked-state 1° phase command to reach 0.01°',(1,50),(0,1200),
           'Natural frequency fn (kHz)','Sufficient settling time (μs)',
           [('damped linear envelope',[n/1000 for n in nn],[r['wait_us'] for r in vals]),
            ('100 μs interface',[n/1000 for n in nn],[100]*len(nn))])
    s.text(45,1400,'20 kHz: 0.028421° and 55.727 μs; 40 kHz is faster but violates the noise ceiling.',18)
    s.text(45,1450,'This is not a large-hop lock-time or physical-loop stability guarantee.',18);s.save()
    s=SVG('lo-blocker-contract','Noise and coherent spurs need different LO contracts',1450)
    ss=logspace(1e-12,2e-10)
    s.plot(70,'One −60 dBm blocker at the mixer input; noise allocation −162 dBm/Hz',
           (1e-12,2e-10),(-176,-156),'Additive branch phase PSD Sη (rad²/Hz)',
           'Input-referred reciprocal noise (dBm/Hz)',
           [('source + common buffer + branch',ss,[lo_contract(v)['rm_dbm_hz'] for v in ss]),
            ('allocation',ss,[-162]*len(ss))],True)
    bb=logspace(1e-7,1e-3)
    s.plot(520,'A coherent LO sideband translates the blocker onto the wanted signal',
           (1e-7,1e-3),(.0001,10),'Sinusoidal PM peak β (rad)','Bound on retained phase bias (degrees)',
           [('small-PM conversion',bb,[lo_contract(beta=b)['phase_spur_degrees'] for b in bb]),
            ('0.02° allocation',bb,[.02]*len(bb))],True,True)
    s.box(40,995,245,85,['LO carrier 1.020 GHz','PM sideband 1.030 GHz'])
    s.box(365,995,230,85,['RF blocker 1.010 GHz','−60 dBm after selection'])
    s.box(685,995,230,85,['Difference = 20 MHz','same IF as wanted'])
    s.path([(285,1035),(315,1035),(315,970),(800,970),(800,995)],arrow=True)
    s.path([(595,1035),(685,1035)],arrow=True)
    c=lo_contract()
    s.text(45,1150,f"Sη = 3e−11: reciprocal noise {c['rm_dbm_hz']:.4f} dBm/Hz; mask 6.3096e−11 rad²/Hz.",18)
    s.text(45,1210,'β = 0.0002 rad gives −80 dBc per sideband, yet about 0.721° retained bias.',18)
    s.text(45,1270,'The bias allocation instead requires β ≤ 5.5455e−6 rad (about −111.14 dBc).',18)
    s.text(45,1330,'The 10 MHz IF notch removes the original blocker, not this new 20 MHz component.',18)
    s.text(45,1395,'No universal L(f) conversion or measured synthesizer performance is assumed.',18);s.save()
    s=SVG('reference-endpoint-test','Measure the reference delivered at each receiver endpoint',1140)
    s.box(40,115,185,85,['Shared source φs','post-common-buffer'])
    for y,i in [(100,1),(330,2)]:
        s.box(360,y,220,90,[f'Branch {i}: A{i}, η{i}','load / delay / temperature'])
        s.box(700,y,210,90,[f'LO endpoint L{i}','actual mixer load'])
        s.path([(225,155),(275,155),(275,y+45),(360,y+45)],arrow=True)
        s.path([(580,y+45),(700,y+45)],arrow=True)
    s.box(40,510,205,85,['Witness w','independent or shared?'])
    s.box(405,510,290,85,['Observed phase yi = φi − w','Sy = Si + Sw − 2 Re Siw'])
    s.path([(245,552),(405,552)],COLORS[2],arrow=True)
    s.path([(805,190),(805,235)],arrow=True);s.text(820,230,'φ₁',20)
    s.path([(805,420),(805,465)],arrow=True);s.text(820,460,'φ₂',20)
    s.path([(550,470),(550,510)],arrow=True);s.text(505,485,'φᵢ',20)
    s.path([(700,375),(635,375),(635,215),(470,215),(470,190)],COLORS[1],dash='7 4',arrow=True)
    s.text(655,255,'controlled load change',18,COLORS[1]);s.text(655,285,'can perturb branch 1',18,COLORS[1])
    s.text(45,680,'A perfectly shared witness can hide source phase modulation entirely.',20)
    s.text(45,740,'Inject β = 0.0002 rad at 10 MHz in the model: shared reading = 0; blocker bias ≈ 0.721°.',18)
    s.text(45,800,'Thermal example: differential 0.08 ps/K × 2 K → 0.058752° at 1.020 GHz.',18)
    s.text(45,860,'A 0.05° excursion contract requires ≤ 0.06808 ps/K, or another justified correction.',18)
    s.text(45,920,'Load example: |α| = 0.01, |ΔΓ| = 0.1 → phase bound 0.05730°.',18)
    s.text(45,980,'Source sharing, common power and equal cable lengths do not establish endpoint validity.',18)
    s.text(45,1055,'All excursions / source spectra / coupling coefficients here are synthetic.',18);s.save()


if __name__=='__main__':
    {14:unit14,15:unit15}[int(sys.argv[1])]()
