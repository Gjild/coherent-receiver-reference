"""Illustrative alignment, calibration and metrology models; no receiver measurements."""
from math import *
import cmath,sys
from visual_foundations import SVG,lin,log as logspace

FS=16e6

def echo_response(f,a=.6,g=.9*cmath.exp(.08j),delay=5):
    w=2*pi*f/FS
    return g*cmath.exp(-1j*w*delay)*(1-a*cmath.exp(-1j*w))


def align_coeff(a,length,g=.9*cmath.exp(.08j)):
    if a<1:return [a**k/g for k in range(length)],5
    if a>1:return [-a**(-(length-k))/g for k in range(length)],5+length
    raise ValueError('unit-circle zero has no bounded full-band inverse')


def align_response(f,a,length,quantized=False,state_a=None):
    q,d=align_coeff(a,length)
    if quantized:q=[complex(round(c.real*2**20),round(c.imag*2**20))/2**20 for c in q]
    w=2*pi*f/FS;Q=sum(c*cmath.exp(-1j*w*k) for k,c in enumerate(q))
    return Q*echo_response(f,a if state_a is None else state_a)*cmath.exp(1j*w*d)


def align_integer(samples,coeffs):
    # Input/output: signed24 F21; coefficient signed24 F20, exact64 F41 sums.
    from sampled_models import round_shift
    words=[(round(x.real*2**21),round(x.imag*2**21)) for x in samples]
    if any(max(abs(a),abs(b))>=2**23 for a,b in words):raise OverflowError('input')
    co=[(round(c.real*2**20),round(c.imag*2**20)) for c in coeffs]
    if any(max(abs(a),abs(b))>=2**23 for a,b in co):raise OverflowError('coefficient')
    out=[];maxpartial=0
    for n in range(len(words)):
        ar=ai=0
        for k,(cr,ci) in enumerate(co[:n+1]):
            xr,xi=words[n-k]
            ar+=xr*cr-xi*ci;ai+=xr*ci+xi*cr
            maxpartial=max(maxpartial,abs(ar),abs(ai))
            if maxpartial>=2**63:raise OverflowError('accumulator')
        r=round_shift(ar,20);i=round_shift(ai,20)
        if max(abs(r),abs(i))>=2**23:raise OverflowError('output')
        out.append(complex(r,i)/2**21)
    return out,maxpartial


def alignment_case(a=.6,length=16):
    import numpy as np
    # Four noiseless supplied coherent response observations; no device fit claim.
    f=np.array([.25,.75,1.25,1.75])*1e6;w=2*pi*f/FS
    measured=np.array([echo_response(x,a)*cmath.exp(1j*2*pi*x*2/FS) for x in f])
    X=np.column_stack([np.ones(4),np.exp(-1j*w)])
    c=np.linalg.lstsq(X,measured*np.exp(3j*w),rcond=None)[0]
    ah=float((-c[1]/c[0]).real);q,d=align_coeff(ah,length,c[0])
    n=np.arange(4096);s=.006*np.exp(-2j*pi*1.625e6*n/FS+.2j)+.003*np.exp(2j*pi*.375e6*n/FS-.4j)+.001*np.exp(2j*pi*1.625e6*n/FS+.7j)
    h=np.r_[np.zeros(5),.9*cmath.exp(.08j),-a*.9*cmath.exp(.08j)]
    y=np.convolve(s,h)[:len(s)];floating=np.convolve(y,q)[:len(s)]
    fixed,partial=align_integer(y,q);fixed=np.asarray(fixed)
    target=np.r_[np.zeros(d),s[:-d]];valid=np.arange(len(s))>=5+length
    def rel(v,w):return float(np.linalg.norm(v[valid]-w[valid])/np.linalg.norm(w[valid])*100)
    old=np.array([align_response(x,a,length,state_a=a+.03) for x in [-2e6,0,2e6]])
    return dict(a_est=ah,g_est=[float(c[0].real),float(c[0].imag)],delay_samples=d,
        residual_bound=a**length if a<1 else a**(-length),
        noise_energy=sum(abs(c)**2 for c in q),l1=sum(abs(c) for c in q),
        floating_record_pct=rel(floating,target),integer_record_pct=rel(fixed,target),
        arithmetic_vs_float_pct=rel(fixed,floating),maxpartial=int(partial),
        changed_state_max_pct=float(max(abs(old-1))*100))


def regularized_response(h,lam):
    return h.conjugate()/(abs(h)**2+lam**2)


def unit20():
    f=lin(-2,2)
    s=SVG('alignment-access','Preserve channel access and distinguish noise injection planes',950)
    for y,ch,h in [(120,'A','H_A = z^-2'),(320,'B','H_B = g z^-5 (1 − a z^-1)')]:
        s.box(40,y,120,65,['s[n] + u[n]']);s.box(230,y,275,65,[h]);s.box(585,y,100,65,['+ v_'+ch]);s.box(755,y,170,65,['Q_'+ch+'; target z^-D'])
        s.path([(160,y+32),(230,y+32)],arrow=True);s.path([(505,y+32),(585,y+32)],arrow=True);s.path([(685,y+32),(755,y+32)],arrow=True)
    s.box(245,530,590,95,['Retain separate complex data until alignment is justified','Before-path noise u passes through H and Q','After-path noise v is multiplied by the inverse'])
    s.text(45,720,'Same input is a supplied calibration/illumination model, not a universal array manifold.',18)
    s.text(45,775,'An analog sum can erase a mode before digital correction has access to it.',19)
    s.text(45,830,'Reference planes, loading, state and admissible input range are part of H.',18);s.save()
    s=SVG('alignment-phase-access','Equal magnitudes can conceal different inverse requirements',1080)
    s.plot(70,'Fs = 16 MS/s; echo responses 1 − 0.8 exp(−jω) and 0.8 − exp(−jω)',(-2,2),(-15,6),
        'Signed baseband frequency (MHz)','Magnitude (dB)',[(label,f,[20*log10(abs(fun(2*pi*x*1e6/FS))) for x in f]) for label,fun in [('inside zero',lambda w:1-.8*cmath.exp(-1j*w)),('outside zero',lambda w:.8-cmath.exp(-1j*w))]])
    s.plot(520,'Identical magnitude; phase is referred to the same input and output planes',(-2,2),(-90,300),
        'Signed baseband frequency (MHz)','Continuous phase (degrees; outside branch 180° at DC)',[(label,f,[(degrees(cmath.phase(fun(2*pi*x*1e6/FS)))+(360 if label=='outside zero' and x<0 else 0)) for x in f]) for label,fun in [('inside zero',lambda w:1-.8*cmath.exp(-1j*w)),('outside zero',lambda w:.8-cmath.exp(-1j*w))]])
    s.text(45,940,'A magnitude sweep cannot establish all-pass phase, delay, or the correct inverse support.',18)
    s.text(45,995,'An outside zero needs future data for an exact stable inverse; finite delay permits approximation.',17);s.save()
    s=SVG('alignment-latency-residual','Finite inverse length trades residual against permissible delay',1090)
    lengths=list(range(4,49))
    s.plot(70,'Exact residual magnitude: a^L inside; a^(−P) outside',(4,48),(1e-11,1),
        'Number of inverse taps','Complex response error magnitude (log scale)',[
        ('a=0.6, causal truncated inverse',lengths,[.6**k for k in lengths]),
        ('a=1.25, delayed future-data approximation',lengths,[1.25**(-k) for k in lengths]),
        ('illustrative 0.1% response limit',lengths,[.001]*len(lengths))],False,True)
    s.plot(520,'Target epoch delay includes the five-sample channel delay',(4,48),(0,3.5),
        'Number of inverse taps','Common target delay (μs)',[
        ('a=0.6: no extra preview',lengths,[5/16]*len(lengths)),
        ('a=1.25: P sample preview',lengths,[(5+k)/16 for k in lengths]),
        ('illustrative 3 μs delay limit',lengths,[3]*len(lengths))])
    s.text(45,940,'Selected: L=16 inside (0.0282%); P=32 outside (0.0792%, 2.3125 μs).',18)
    s.text(45,995,'Finite-support and word checks still apply; these are not hardware latency measurements.',18);s.save()
    s=SVG('alignment-null-noise','Finite attenuation is invertible; a true steady-state null needs different information',1090)
    aa=lin(.6,.999,241)
    s.plot(70,'|H_B(0)|=0.9(1−a); desired input 10 mV; DC phasor noise 20 μV RMS',(.6,.999),(-10,50),
        'Echo cancellation coefficient a','DC reconstructed SNR (dB)',[
        ('exact inverse: output SNR',aa,[20*log10(.01*.9*(1-a)/20e-6) for a in aa]),
        ('20 dB illustrative minimum',aa,[20]*len(aa))])
    lams=logspace(.0001,.1)
    h=.018
    s.plot(520,'DC phasor regularization at a=0.98: λ is a response-scale penalty',(.0001,.1),(0,1.1),
        'Regularization λ (log scale)','Desired transfer and normalized error',[
        ('desired transfer |Q H|',lams,[h*h/(h*h+l*l) for l in lams]),
        ('relative RMS error, 10mV desired',lams,[sqrt((l*l/(h*h+l*l))**2+(20e-6/.01*h/(h*h+l*l))**2) for l in lams])],True,False)
    s.text(45,940,'Regularization limits noise gain by retaining bias; it is not full desired-response recovery.',18)
    s.text(45,995,'At a=1, constant steady-state inputs are indistinguishable without another observation.',18);s.save()

if __name__=='__main__':unit20()
