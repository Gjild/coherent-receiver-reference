"""Synthetic converter/quadrature/multirate teaching models; no hardware data."""
from math import pi, sqrt, sin, cos, exp, log, log10, floor, asin, degrees, tan, atan2
import cmath
import sys
from visual_foundations import SVG, COLORS, lin, log as logspace


def converter_case(gain=24.):
    factor=10**(gain/20)
    wanted=sqrt(.1)*10**(-56/20)*factor
    blocker=sqrt(.1)*10**(-23/20)*factor
    slope=sqrt(sum((2*pi*f*a)**2 for f,a in
                   [(20e6,wanted),(30e6,blocker),(40e6,blocker)])/2)
    return dict(wanted=wanted,blocker=blocker,peak=wanted+2*blocker,
                broadband_peak=(.2+2*converter_blocker24())*10**((gain-24)/20),
                slope=slope,raw_jitter=slope*1e-13)


def converter_blocker24():
    return sqrt(.1)*10**((-23+24)/20)


def aperture_phase(shared=.8,opposite=False,blocker_scale=1.,count=256000):
    """Shared/private independent sample timing sources, stated phase weights."""
    c=converter_case();a=c['wanted'];b=c['blocker']*blocker_scale
    sc=1e-13*shared;sa=1e-13*sqrt(1-shared*shared)
    jb=sum((2*pi*f*b)**2 for f in [30e6,40e6])
    va=3*sa**2*(2*pi*20e6)**2/count+2*sa**2*jb/(count*a*a)
    vc=4*sc**2*jb/(count*a*a) if opposite else 0.
    return degrees(sqrt(va+vc))


def quantize(value,bits=14):
    step=2/2**bits
    return step*max(-2**(bits-1),min(2**(bits-1)-1,floor(value/step+.5)))


def converter_period(phases=(0.,.2,-.4),count=64):
    c=converter_case();amps=[c['wanted'],c['blocker'],c['blocker']]
    return [sum(a*cos(2*pi*k*n/64+p) for a,k,p in zip(amps,[10,15,20],phases))
            for n in range(count)]


def coherent_quantization(bits):
    zz=[]
    for phases in [(0.,.2,-.4),(.3,1.1,-.7)]:
        u=converter_period(phases)
        zz.append(sum(quantize(v,bits)*cmath.exp(-2j*pi*10*n/64) for n,v in enumerate(u))/32)
    return degrees(cmath.phase(zz[1]*zz[0].conjugate())-.3)


def dither_phase_bound(bits=16,noise=50e-6,count=256000):
    return degrees(sqrt(4*noise*noise+(2/2**bits)**2)/
                   (converter_case()['wanted']*sqrt(count)))


def interleave_bias(skew):
    c=converter_case()
    return degrees(asin(c['blocker']/c['wanted']*pi*44e6*skew))


def unit17():
    s=SVG('converter-alias-interfaces','Preserve analog information before the sample identity enters a pipeline',1350)
    for x,lines in [(35,['Analog mask','all admitted bands']),(270,['Driver / load','differential pins']),(505,['Aperture n','epoch + state']),(740,['Pipeline / link','word identity n'])]:
        s.box(x,105,185,90,lines)
        if x<740:s.path([(x+185,150),(x+235,150)],arrow=True)
    s.text(45,245,'Alternate lower-side plan: RF 1000 / 1010 / 1020 MHz − LO 980 MHz → IF 20 / 30 / 40 MHz.',17)
    s.text(45,290,'Wanted band 18–22 MHz; 108 MHz disturbance is specified at the analog mask input.',18)
    for y,rate,alias,images in [(355,128,'−20 MHz: overlaps wanted mirror','106–110 and 146–150 MHz'),
                               (570,160,'−52 MHz: outside wanted','138–142 and 178–182 MHz')]:
        s.box(40,y,245,85,[f'Fs = {rate} MS/s','real sample spectrum'])
        s.box(370,y,225,85,['Analog 108 MHz',f'108 − {rate} MHz'])
        s.box(670,y,245,85,[alias.split(':')[0],alias.split(': ')[1]])
        s.path([(285,y+42),(370,y+42)],arrow=True);s.path([(595,y+42),(670,y+42)],arrow=True)
        s.text(45,y+130,'Positive analog image bands mapping onto wanted: '+images+'.',17)
    s.box(40,790,420,85,['32 MS/s: 18–22 → −14 to −10 MHz','Band and conjugate mirror stay separate'])
    s.box(505,790,420,85,['40 MS/s: 18 and 22 MHz collide','20 MHz at Nyquist loses quadrature'])
    s.text(45,950,'At 128 MS/s a B-sized coherent alias needs ≥102.142 dB complete analog rejection.',19)
    s.text(45,1010,'A different rate moves this blocker, while changing every image/noise/clock/data interface.',18)
    s.text(45,1070,'The 30/40 MHz blockers can be filtered later, but already create slope and nonlinear errors.',17)
    s.text(45,1130,'An ADC input is not the old 50 Ω power plane: matching, gain and loading must be reconciled.',17)
    s.text(45,1195,'Pipeline latency and packet delivery describe data age, not a new aperture event.',19)
    s.text(45,1260,'All rejection / driver / converter envelopes here are supplied assumptions.',18);s.save()
    s=SVG('converter-timing-observable','Timing requirements depend on complete waveforms and phase weights',1100)
    bb=lin(0,1.2);c=converter_case()
    raw=lambda b:1e6*1e-13*sqrt(((2*pi*20e6*c['wanted'])**2+
                              sum((2*pi*f*c['blocker']*b)**2 for f in [30e6,40e6]))/2)
    s.plot(70,'Raw slope error at 100 fs RMS: not an in-band phase result',(0,1.2),(0,10),
           'Blocker amplitude / nominal B','RMS voltage error (μV)',
           [('complete three-tone waveform',bb,[raw(b) for b in bb]),
            ('wanted tone only',bb,[raw(0)]*len(bb))])
    cc=lin(0,1)
    s.plot(520,'2 ms differential phase; total per-channel jitter remains 100 fs',
           (0,1),(0,.0004),'Shared timing RMS / total RMS','Phase SD (degrees)',
           [('identical waveforms',cc,[aperture_phase(v) for v in cc]),
            ('opposite blocker phases',cc,[aperture_phase(v,True) for v in cc]),
            ('0.0002° timing share',cc,[.0002]*len(cc))])
    s.text(45,940,'80 fs shared + 60 fs private: identical 0.000134848°; opposite 0.000287803°.',18)
    s.text(45,995,'Static aperture advance: +50 ps → +0.36° at 20 MHz; 0.02° needs ≤2.77778 ps.',18)
    s.text(45,1050,'Independent sample timing errors are an assumed model; colored / periodic jitter needs new weights.',17);s.save()
    s=SVG('converter-quantization','Repeated quantization bias and dither uncertainty are different objects',1120)
    xx=lin(-1.4,1.4)
    sx=[-1.4,-.5,-.5,.5,.5,1.4];stair=[-1,-1,0,0,1,1]
    s.plot(70,'Ideal codes near zero, away from overload',(-1.4,1.4),(-1.5,1.5),
           'Input / code step Δ','Output / code step Δ',
           [('nearest-code output',sx,stair),('uniform-dither ensemble mean',xx,xx)])
    nn=sorted(set(64*round(v/64) for v in logspace(64,1e6)))
    s.plot(520,'Same 64-sample waveform repeated: actual deterministic bias does not average away',
           (64,1e6),(.0001,.3),'Record length N (samples)','Phase error / SD bound (degrees)',
           [('14-bit periodic |bias|',nn,[abs(coherent_quantization(14))]*len(nn)),
            ('16-bit periodic |bias|',nn,[abs(coherent_quantization(16))]*len(nn)),
            ('14-bit dither bound; σv=50 μV',nn,[dither_phase_bound(14,count=n) for n in nn]),
            ('16-bit dither bound; σv=50 μV',nn,[dither_phase_bound(16,count=n) for n in nn])],True,True)
    s.text(45,940,'No dither / no noise: a 10 μV peak tone returns all zeros in either 2 V-span quantizer.',18)
    s.text(45,995,'Dither preserves conditional mean only under the specified injection / independence / range model.',17)
    s.text(45,1050,'Bias curves and stochastic bounds are separate criteria, not measured converter performance.',18);s.save()
    s=SVG('converter-interleaving','Alternating-aperture error makes an image that ordinary sampling does not',1090)
    s.box(40,115,250,85,['Changed input: 44 MHz','blocker peak B, wanted A'])
    s.box(355,115,250,85,['Alternating gain / skew','(−1)ⁿ [g u + δ u′] / 2'])
    s.box(675,115,240,85,['Image at 64 − 44 MHz','20 MHz wanted band'])
    s.path([(290,158),(355,158)],arrow=True);s.path([(605,158),(675,158)],arrow=True)
    dd=logspace(1,10000)
    s.plot(290,'128 MS/s; pure differential skew, small-time expansion',
           (1,10000),(.0001,10),'Even-minus-odd aperture advance |δ| (fs)',
           'Worst retained phase displacement (degrees)',
           [('skew image phasor bound',dd,[interleave_bias(v*1e-15) for v in dd]),
            ('0.01° allocation',dd,[.01]*len(dd))],True,True)
    s.text(45,720,'5 ps → 1.76915°; 0.01° from skew alone needs ≤28.2667 fs.',20)
    s.text(45,780,'Gain mismatch alone needs ≤7.81461 ppm; offset mismatch appears at Fs / 2.',19)
    s.text(45,840,'The original 40 MHz blocker is replaced by 44 MHz here; earlier jitter numbers do not transfer.',17)
    s.text(45,900,'Prevention, a different architecture or characterized correction require a new comparison.',18)
    s.text(45,960,'Bus interleaving / channel multiplexing does not imply this analog-aperture model.',18)
    s.text(45,1035,'Real frequency/level/state-dependent mismatch needs examined data.',18);s.save()
    s=SVG('converter-driver-range','Driver range, waveform crest and acquisition settling constrain different choices',1110)
    gg=lin(18,28)
    s.plot(70,'Complete waveform at converter pins; nominal 2 V differential span',
           (18,28),(0,1.6),'Added driver gain (dB)','Conservative composite peak (V)',
           [('weak tone + two blockers',gg,[converter_case(g)['peak'] for g in gg]),
            ('specified broadband crest + blockers',gg,[converter_case(g)['broadband_peak'] for g in gg]),
            ('qualified peak 0.8 V',gg,[.8]*len(gg)),('nominal positive limit 1 V',gg,[1]*len(gg))])
    tt=lin(.15,1)
    s.plot(520,'Supplied single-pole full-span step model, 3 ns effective tracking window',
           (.15,1),(1e-9,1),'Time constant τ (ns)','Residual differential step error (V)',
           [('2 exp(−3 ns / τ)',tt,[2*exp(-3/t) for t in tt]),
            ('14-bit half code step',tt,[1/2**14]*len(tt)),
            ('16-bit half code step',tt,[1/2**16]*len(tt))],False,True)
    s.text(45,940,'24 dB passes tone peaks but fails the supplied broadband crest bound; 22 dB passes both.',18)
    s.text(45,995,'At 16 bits the model needs τ ≤0.254593 ns; actual kickback / slew / recovery need evidence.',17)
    s.text(45,1055,'Common mode, pin limits, loading and reference isolation remain separate interfaces.',18);s.save()




# K18: real quadrature paths, periodic synthetic records; no device measurements.
def iq_pair(f,g=1.05,epsilon=pi/60,delay=20e-9,amplitude=0.,gamma=.5):
    """Nonzero-tone fundamental; f=0 is its limit, not a constant stimulus."""
    cy=g*cos(epsilon)+.75*gamma*amplitude**2;cx=g*sin(epsilon)
    h=cmath.exp(-2j*pi*f*delay)
    return ((1+(cy-1j*cx)*h)/2,(1-(cy+1j*cx)*h)/2,
            (1-(cy-1j*cx)*h)/2,(1+(cy+1j*cx)*h)/2)


def iq_wave(times,tones,dc=0j,g=1.05,epsilon=pi/60,delay=20e-9,
            offset=.003-.002j,gamma=.5):
    """Actual real I and delayed Q mixers, with a weak cubic Q path."""
    out=[]
    for t in times:
        a=dc+sum(v*cmath.exp(2j*pi*f*t) for f,v in tones)
        b=dc+sum(v*cmath.exp(2j*pi*f*(t-delay)) for f,v in tones)
        q=g*(b.imag*cos(epsilon)-b.real*sin(epsilon))+gamma*b.imag**3
        out.append(a.real+1j*q+offset)
    return out


def iq_fit():
    """Fit four rotating 20 mV training tones via actual real-path records."""
    fs=16e6;n=4096;times=[k/fs for k in range(n)];xx=[];ph=[];gg=[]
    for f in [.25e6,.75e6,1.25e6,1.75e6]:
        vv=iq_wave(times,[(f,.02)])
        pos=sum(z*cmath.exp(-2j*pi*f*t) for t,z in zip(times,vv))/n/.02
        neg=sum(z*cmath.exp(2j*pi*f*t) for t,z in zip(times,vv))/n/.02
        c=pos-neg.conjugate();xx.append(f);ph.append(cmath.phase(c));gg.append(abs(c))
    xm=sum(xx)/4;pm=sum(ph)/4
    slope=sum((x-xm)*(y-pm) for x,y in zip(xx,ph))/sum((x-xm)**2 for x in xx)
    return sum(gg)/4,-(pm-slope*xm),-slope/(2*pi)


def iq_correct_pair(f,flat=False):
    g,e,t=iq_fit_cached();h=1 if flat else cmath.exp(-2j*pi*f*t)
    q=1/(g*cos(e));v=h*(1+1j*tan(e))/2
    return v+q/2,v-q/2


_IQ_FIT=None
def iq_fit_cached():
    global _IQ_FIT
    if _IQ_FIT is None:_IQ_FIT=iq_fit()
    return _IQ_FIT


def iq_response(f,mode='matched',amplitude=.01,g=1.05,epsilon=pi/60,delay=20e-9):
    a,b,c,d=iq_pair(f,g,epsilon,delay,amplitude)
    u,v=(1,0) if mode=='raw' else iq_correct_pair(f,mode=='flat')
    return u*a+v*c,u*b+v*d


def iq_noise_gain(g):
    return (1+1/(g*g))/(2*cos(pi/60)**2)


def iq_apply_periodic(samples,fs,offset=.003-.002j,flat=False):
    """NumPy reference: periodic-record ideal I delay; no causal finite-filter claim."""
    import numpy as np
    g,e,t=iq_fit_cached();v=np.asarray(samples)-offset
    ff=np.fft.fftfreq(len(v),1/fs)
    ii=np.fft.ifft(np.fft.fft(v.real)*np.exp(-2j*pi*ff*(0 if flat else t))).real
    qq=v.imag/(g*cos(e))+tan(e)*ii
    return ii+1j*qq


def iq_record_results():
    """Execute the frozen-fit held-out examples used in Chapter18 / Figure18.3."""
    import numpy as np
    fs=16e6;times=np.arange(4096)/fs;dc=.005+.003j
    tones=[(.375e6,.009*cmath.exp(.1j)),(-.625e6,.007*cmath.exp(-.4j)),(1.375e6,.004*cmath.exp(.8j))]
    want=dc+sum(a*np.exp(2j*pi*f*(times-20e-9)) for f,a in tones)
    vv=iq_wave(times,tones,dc);r={}
    for flat in [False,True]:
        y=iq_apply_periodic(vv,fs,flat=flat)
        r['flat_pct' if flat else 'mod_pct']=float(np.linalg.norm(y-want)/np.linalg.norm(want-dc)*100)
    for amp,state,g,e,t,d in [(.2,'high',1.05,pi/60,20e-9,.003-.002j),(.02,'state',1.07,pi/45,24e-9,.004-.001j)]:
        f=.375e6;vv=iq_wave(times,[(f,amp)],g=g,epsilon=e,delay=t,offset=d)
        y=iq_apply_periodic(vv,fs);want=amp*np.exp(2j*pi*f*(times-20e-9))
        z=np.mean(y*np.exp(-2j*pi*f*times))/amp
        r[state+'_pct']=float(np.linalg.norm(y-want)/np.linalg.norm(want)*100)
        r[state+'_phase']=degrees(cmath.phase(z*cmath.exp(2j*pi*f*20e-9)))
    times=np.arange(1000)/1000;want=dc+.01*np.exp(2j*pi*10*(times-20e-9))
    y=iq_apply_periodic(iq_wave(times,[(10,.01)],dc),1000)
    r['near_pct']=float(np.linalg.norm(y-want)/np.linalg.norm(want-dc)*100)
    return r


def unit18():
    s=SVG('quadrature-path-pair','An I/Q label does not determine desired and conjugate response',1120)
    s.box(40,100,240,85,['RF: x cos(LO) − y sin(LO)','s = x + jy (peak V)'])
    s.box(380,95,235,85,['2 cos(LO) → LP','I = x'])
    s.box(380,295,235,105,['−2 sin(LO+ε) → LP','Q = g (y cos ε − x sin ε)','then Q-path delay τ'])
    s.path([(280,140),(330,140),(380,138)],arrow=True)
    s.path([(330,140),(330,345),(380,345)],arrow=True)
    s.box(720,185,200,85,['Form z = I + jQ','add offset d'])
    s.path([(615,138),(670,138),(670,225),(720,225)],arrow=True)
    s.path([(615,345),(670,345),(670,245),(720,245)],arrow=True)
    s.box(40,535,240,95,['S(f)','desired complex input'])
    s.box(390,535,220,95,['a(f) S(f)','desired response'])
    s.box(40,750,240,95,['S*(−f)','conjugated mirror input'])
    s.box(390,750,220,95,['b(f) S*(−f)','conjugate response'])
    s.box(730,635,185,95,['Z(f)','both terms overlap'])
    s.path([(280,580),(390,580)],arrow=True);s.path([(280,795),(390,795)],arrow=True)
    s.path([(610,580),(675,580),(675,665),(730,665)],arrow=True)
    s.path([(610,795),(675,795),(675,700),(730,700)],arrow=True)
    s.text(45,940,'Both sides of the LO can carry desired information. An image response is not an unwanted input.',19)
    s.text(45,1000,'Fit at defined RF/baseband planes and identified level, LO and gain state.',19)
    s.text(45,1060,'The diagram is an idealized mixer/path model; actual source/load and noise paths need evidence.',17);s.save()
    ff=lin(-2,2)
    leak=lambda z:20*log10(max(abs(z[1]/z[0]),1e-7))
    s=SVG('quadrature-band-correction','A constant quadrature trim cannot remove a differential path delay',1130)
    curves=[]
    for mode,label in [('raw','uncorrected'),('flat','constant trim only'),('matched','delay match + trim')]:
        curves.append((label,ff,[leak(iq_response(f*1e6,mode)) for f in ff]))
    s.plot(70,'Independent 10 mV single-tone fundamentals; 20 mV training at other frequencies',(-2,2),(-100,0),
           'Observed baseband frequency f (MHz)','Conjugate / desired response (dB)',curves)
    s.plot(520,'Desired phase relative to target plane delayed by 20 ns',(-2,2),(-9,9),
           'Baseband frequency f (MHz)','Desired phase error (degrees)',
           [(label,ff,[degrees(cmath.phase(iq_response(f*1e6,mode)[0]*cmath.exp(2j*pi*f*1e6*20e-9))) for f in ff])
            for mode,label in [('raw','uncorrected'),('flat','constant trim only'),('matched','delay match + trim')]])
    s.text(45,940,'Curves are single-tone fundamentals of the supplied cubic-path model, not full distortion tests.',17)
    s.text(45,995,'f = 0 is the rotating-tone limit: coincident DC lines do not define a separate image ratio.',17)
    s.text(45,1050,'An overall timestamp shift cannot eliminate conjugate leakage from unequal I/Q delays.',19);s.save()
    s=SVG('quadrature-training-validity','Known rotation supplies information that a real-only stimulus cannot',1060)
    for x,lines in [(40,['Four known phases','+A, +jA, −A, −jA']),(360,['Fit [s, s*, 1]','three independent columns']),(680,['Separate blank + tones','offset and path response'])]:
        s.box(x,110,245,90,lines)
        if x<680:s.path([(x+245,155),(x+320,155)],arrow=True)
    s.box(40,300,415,100,['Real-only stimulus: s = s*','μ and ν cannot be separated','Subtracting mean also removes desired DC'])
    s.box(505,300,415,100,['Independent checks after fitting','new frequencies, both signs, modulation','changed level and reset state'])
    s.text(45,490,'Same physical synthetic model; fit on four 20 mV rotating tones, then freeze coefficients.',18)
    r=iq_record_results()
    rows=[('Held-out low-level modulation',f"{r['mod_pct']:.6f}% waveform error: passes 0.1%"),
          ('200 mV tone, same state',f"{r['high_pct']:.5f}% error: cubic path fails"),
          ('20 mV tone, changed state',f"{r['state_phase']:.5f}° and DC residue: fails")]
    for i,(a,b) in enumerate(rows):
        b=b.replace('-', '−')
        s.box(40,540+120*i,875,85,[a,b])
    s.text(45,965,'These are executed illustrative records. No measured component or reader effectiveness is claimed.',17);s.save()
    s=SVG('quadrature-near-dc','Offset removal must preserve the desired near-DC observable',1110)
    ff=logspace(1,10000)
    s.plot(70,'Supplied first-order AC coupling: corner 100 Hz',(1,10000),(-45,1),
           'Desired baseband frequency (Hz)','Desired amplitude transfer (dB)',
           [('high-pass |H|',ff,[20*log10(f/sqrt(f*f+10000)) for f in ff]),('retain desired signal',ff,[0]*len(ff))],True)
    s.plot(520,'Same filter: phase is part of coherent fidelity',(1,10000),(0,90),
           'Desired baseband frequency (Hz)','Desired phase advance (degrees)',
           [('arg H',ff,[degrees(atan2(100,f)) for f in ff])],True)
    s.text(45,940,'A true 10 Hz component loses 20.0432 dB and advances 84.2894°; DC is erased.',20)
    s.text(45,995,'A separate valid blank can estimate d; an operational mean cannot distinguish d from desired DC.',17)
    s.text(45,1050,'Changing impedance / LO leakage between blank and operation invalidates that estimate.',18);s.save()


if __name__=='__main__':
    {'17':unit17,'18':unit18}[sys.argv[1] if len(sys.argv)>1 else '17']()
