"""Bounded synthetic calibration and operational metrology; no device measurements."""
from math import *
import cmath
from visual_foundations import SVG,lin,log as logspace
import alignment_models as align

FS=16e6

def fixture(f):
    return .98*cmath.exp(.03j-2j*(2*pi*f/FS))


def calibrate(seed=2101,omit_fixture=False,details=False):
    import numpy as np
    rng=np.random.default_rng(seed);freq=np.array([.25,.75,1.25,1.75])*1e6
    probes=np.array([1,1j,-1,-1j]);rows=[]
    for f in freq:
        w=2*pi*f/FS;s=.05*cmath.exp(1j*(.7+.2*f/1e6))
        z=[]
        for h,p,b in [(cmath.exp(-2j*w),1,.001+.002j),(align.echo_response(f),fixture(f),.003-.001j)]:
            noise=20e-6/sqrt(2)*(rng.normal(size=(64,4))+1j*rng.normal(size=(64,4)))
            y=h*p*s*probes+b+noise
            z.append(np.mean(y*probes.conj()))
        rows.append(z[1]/z[0]/(1 if omit_fixture else fixture(f))*cmath.exp(3j*w))
    w=2*pi*freq/FS;X=np.column_stack([np.ones(4),np.exp(-1j*w)])
    c=np.linalg.lstsq(X,rows,rcond=None)[0];a=float((-c[1]/c[0]).real);g=complex(c[0])
    fit=float(np.linalg.norm(X@c-rows)/np.linalg.norm(rows))
    if details:
        constrained=float(np.linalg.norm(X@np.array([g,-g*a])-rows)/np.linalg.norm(rows))
        return g,a,fit,float((-c[1]/c[0]).imag),constrained
    return g,a,fit


def correction(f,g,a,quantized=True):
    q=[a**k/g for k in range(16)]
    if quantized:q=[complex(round(v.real*2**20),round(v.imag*2**20))/2**20 for v in q]
    return sum(v*cmath.exp(-2j*pi*f/FS*k) for k,v in enumerate(q))


def calibrated_response(f,g,a,state='nominal'):
    actual_a=.63 if state=='echo changed' else .6
    level=.97*cmath.exp(.02j) if state=='gain changed' else 1
    return correction(f,g,a)*align.echo_response(f,actual_a)*level*cmath.exp(2j*pi*f/FS*5)


def calibration_case():
    import numpy as np
    g,a,fit,discarded,constrained=calibrate(details=True);q=[a**k/g for k in range(16)]
    n=np.arange(4096);s=.006*np.exp(-2j*pi*1.625e6*n/FS+.2j)+.003*np.exp(2j*pi*.375e6*n/FS-.4j)+.001*np.exp(2j*pi*1.625e6*n/FS+.7j)
    h=np.r_[np.zeros(5),.9*cmath.exp(.08j),-.6*.9*cmath.exp(.08j)]
    y=np.convolve(s,h)[:len(s)]
    # Known-zero raw input, same loading/state; separately estimate operational offset.
    rng=np.random.default_rng(2102);offset=.003-.001j
    blank=offset+20e-6/sqrt(2)*(rng.normal(size=1024)+1j*rng.normal(size=1024))
    offset_est=complex(np.mean(blank));raw=y+offset
    fixed,partial=align.align_integer(raw-offset_est,q)
    unremoved,_=align.align_integer(raw,q)
    target=np.r_[np.zeros(5),s[:-5]];valid=n>=21
    err=float(np.linalg.norm((np.array(fixed)-target)[valid])/np.linalg.norm(target[valid]))
    sweep=[-2e6+4e6*k/400 for k in range(401)]
    failures={state:max(abs(calibrated_response(f,g,a,state)-1) for f in sweep) for state in ['nominal','gain changed','echo changed']}
    # A real desired DC input, not a tone evaluated at a frequency approaching zero.
    dc=np.ones(128)*.01;dy=np.convolve(dc,h)[:128];dout,_=align.align_integer(dy+offset-offset_est,q)
    dc_gain=complex(np.mean(np.array(dout)[21:])/.01)
    return dict(offset_est=[offset_est.real,offset_est.imag],offset_error=[(offset_est-offset).real,(offset_est-offset).imag],unremoved_record_error=float(np.linalg.norm((np.array(unremoved)-target)[valid])/np.linalg.norm(target[valid])),g=[g.real,g.imag],a=a,training_relative_fit=fit,discarded_echo_imag=discarded,constrained_training_relative_fit=constrained,heldout_integer_relative_error=err,
        swept_error=failures,noise_energy=sum(abs(v)**2 for v in q),maxpartial=partial,
        dc_gain=[dc_gain.real,dc_gain.imag],fixture_omitted_fit=calibrate(omit_fixture=True)[2],fixture_omitted_selected_fit=calibrate(omit_fixture=True,details=True)[4],fixture_omitted_a=calibrate(omit_fixture=True)[1])


def reading_uncertainty():
    import numpy as np
    g,a,_=calibrate();freq=np.array([.25,.75,1.25,1.75])*1e6;w=2*pi*freq/FS
    X=np.column_stack([np.ones(4),np.exp(-1j*w)]);B=np.linalg.inv(X.conj().T@X)@X.conj().T
    # Independent projected phasor means: sigma_z=20uV/sqrt(256).
    rr=np.array([align.echo_response(f)*fixture(f)*cmath.exp(2j*ww) for f,ww in zip(freq,w)])
    vari=(20e-6/16/.05)**2*(1+abs(rr)**2)/np.array([abs(fixture(f))**2 for f in freq])
    C=B@np.diag(vari)@B.conj().T
    Cr=.5*np.block([[C.real,-C.imag],[C.imag,C.real]])
    c0=g;c1=-g*a;values=[];combined=[]
    for f in [-2e6+4e6*k/400 for k in range(401)]:
        ww=2*pi*f/FS;qq=sum(a**k*cmath.exp(-1j*ww*k) for k in range(16))/g
        dq=sum(k*a**(k-1)*cmath.exp(-1j*ww*k) for k in range(1,16))/g
        j=[]
        for dc0,dc1 in [(1,0),(0,1),(1j,0),(0,1j)]:
            da=(-dc1/c0+c1*dc0/c0**2).real
            j.append((-qq*dc0/c0+dq*da)*align.echo_response(f)*cmath.exp(5j*ww))
        j=np.array(j);v=float((j@Cr@j.conj()).real);values.append(v)
        RR=qq*align.echo_response(f)*cmath.exp(5j*ww)
        combined.append(v+abs(RR)**2*(.002**2+.001**2))
    return dict(max_reading_relative_rms=sqrt(max(values)),
        combined_with_fixture_relative_rms=sqrt(max(combined)),
        coefficient_covariance_real=Cr.tolist())


def cadence_error(cycle,duration=.2,latency=.05,rate=.0004):
    e0=.003+.001*sqrt(.2/duration)
    return e0+rate*(cycle+duration/2+latency)


def tracking_transfer(f,eta=1,corner=.1):
    L=1/(1+1j*f/corner)
    return 1-eta*L,1-L


def unit21():
    s=SVG('calibration-access','The injection plane determines which response is observable',850)
    s.box(40,110,200,85,['Incident field','external path Aᵢ'])
    s.box(380,110,200,85,['Loaded input Pᵢ','receiver Hᵢ'])
    s.box(710,110,200,85,['Complex output','Yᵢ'])
    s.path([(240,152),(380,152)],arrow=True);s.path([(580,152),(710,152)],arrow=True)
    s.box(240,350,290,90,['Probe source S cₖ','fixture Pᵢᶜᵃˡ'])
    s.path([(385,350),(385,275),(350,275),(350,152)],arrow=True)
    s.text(40,510,'Yᵢₖ = Hᵢ Pᵢᶜᵃˡ S cₖ + bᵢ + nᵢₖ',24)
    s.text(40,575,'Phase cycling separates a constant offset bᵢ, not synchronous leakage.',19)
    s.text(40,630,'Ratios remove common S; differential fixture response remains.',19)
    s.text(40,685,'External field/sensor path Aᵢ is bypassed by this electronic injection.',19)
    s.text(40,740,'Known output products do not uniquely identify their unknown factors.',19);s.save()
    g,a,_=calibrate();f=lin(-2,2)
    s=SVG('calibration-heldout','Keep coefficients fixed while challenging band, level and state',1080)
    s.plot(70,'Independent signed-frequency grid; fitting used four positive frequencies',(-2,2),(0,.13),
        'Signed baseband frequency (MHz)','|corrected response / target − 1|',[
        (state,f,[abs(calibrated_response(x*1e6,g,a,state)-1) for x in f]) for state in ['nominal','gain changed','echo changed']]+[('illustrative 0.5% limit',f,[.005]*len(f))])
    s.plot(520,'Nominal residual enlarged; Fs=16MS/s,16taps,F20 coefficients',(-2,2),(0,.0006),
        'Signed baseband frequency (MHz)','Nominal complex-response error',[
        ('estimated + rounded correction',f,[abs(calibrated_response(x*1e6,g,a)-1) for x in f]),
        ('exact-parameter finite inverse',f,[.6**16]*len(f))])
    s.text(40,940,'Training, held-out waveform and swept tests are supplied synthetic calculations.',18)
    s.text(40,995,'A previous pass does not authorize a changed gain, echo path or reference state.',18);s.save()
    c=lin(1,30)
    s=SVG('calibration-cadence','Cadence must satisfy drift, evidence age and lost observing time',1080)
    s.plot(70,'Error envelope includes acquisition midpoint and processing latency', (1,30),(0,.018),
        'Burst start-to-start cycle C (s)','Bounded residual phase magnitude (rad)',[
        ('0.2s acquisition',c,[cadence_error(x) for x in c]),
        ('1s acquisition',c,[cadence_error(x,1) for x in c]),
        ('illustrative 0.01rad limit',c,[.01]*len(c))])
    s.plot(520,'Science is unavailable throughout each dedicated calibration burst',(1,30),(.005,1),
        'Burst start-to-start cycle C (s)','Acquisition downtime fraction d/C (log scale)',[
        ('0.2s acquisition',c,[.2/x for x in c]),('1s acquisition',c,[1/x for x in c]),
        ('illustrative 2% limit',c,[.02]*len(c))],False,True)
    s.text(40,940,'At C = 10 s, d = 0.2 s: age ≤ 10.15 s; error ≤ 0.00806 rad; downtime 2%.',18)
    s.text(40,995,'Drift bound and calibration-error envelopes are inputs requiring physical evidence.',18);s.save()
    ff=logspace(.001,10)
    s=SVG('calibration-wanted','An adaptive estimate must distinguish wanted motion from receiver drift',1080)
    s.plot(70,'L(f)=1/(1+jf/0.1Hz); small unwrapped phase; no fade',( .001,10),(0,1.05),
        'Modulation frequency (Hz; log scale)','Magnitude of wanted phase transfer',[
        ('estimate from science: η=1',ff,[abs(tracking_transfer(x,1)[0]) for x in ff]),
        ('separate pilot: η=0',ff,[1]*len(ff)),
        ('pilot with η=0.1 contamination',ff,[abs(tracking_transfer(x,.1)[0]) for x in ff])],True,False)
    s.plot(520,'All three models track the same receiver-drift term',( .001,10),(0,1.05),
        'Modulation frequency (Hz; log scale)','Magnitude of nuisance phase transfer',[
        ('residual drift |1−L|',ff,[abs(tracking_transfer(x)[1]) for x in ff])],True,False)
    s.text(40,940,'At 0.01 Hz, science-derived tracking retains only 0.09950 of wanted phase amplitude.',18)
    s.text(40,995,'An electronically isolated pilot preserves only the paths it actually samples.',18);s.save()

if __name__=='__main__':unit21()
