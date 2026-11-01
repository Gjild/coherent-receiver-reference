"""NumPy periodic-record checks against independently constructed physical errors."""
import unittest,sys,math,cmath
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import sampled_models as m

class QuadratureRecords(unittest.TestCase):
    def test_modulated_and_near_dc_error_from_cubic_physics(self):
        dc=.005+.003j;den=1.05*math.cos(math.pi/60)+.75*.5*.02**2
        # Exactly DC: no separate positive/negative tone lines or sine-cube fundamental.
        for constant in [.01+0j,.01j]:
            got=m.iq_apply_periodic(m.iq_wave(np.arange(64)/1000,[],constant),1000)
            expected=constant+1j*.5*(constant.imag**3-.75*.02**2*constant.imag)/den
            self.assertLess(np.max(np.abs(got-expected)),1e-16)
        cases=[(16e6,4096,[(.375e6,.009*cmath.exp(.1j)),(-.625e6,.007*cmath.exp(-.4j)),(1.375e6,.004*cmath.exp(.8j))]),
               (1000,1000,[(10,.01)])]
        for fs,n,tones in cases:
            t=np.arange(n)/fs
            want=dc+sum(a*np.exp(2j*np.pi*f*(t-20e-9)) for f,a in tones)
            actual=m.iq_apply_periodic(m.iq_wave(t,tones,dc),fs)
            # Independent physical residual: fitting the calibration fundamental
            # absorbs 3 gamma Acal^2/4 into Q gain, but not an arbitrary cubic wave.
            expected=1j*.5*(want.imag**3-.75*.02**2*want.imag)/den
            self.assertLess(np.max(np.abs(actual-want-expected)),1e-13)
            self.assertLess(np.linalg.norm(actual-want)/np.linalg.norm(want-dc),.001)
            self.assertLess(abs(np.mean(actual).real-dc.real),1e-14)

    def test_high_level_harmonic_error_and_changed_state(self):
        den=1.05*math.cos(math.pi/60)+.75*.5*.02**2;a=.2;fs=16e6;t=np.arange(4096)/fs;f=.375e6
        y=m.iq_apply_periodic(m.iq_wave(t,[(f,a)]),fs);w=a*np.exp(2j*np.pi*f*(t-20e-9))
        expected=math.hypot(.75*.5*(a*a-.02**2)*a,.25*.5*a**3)/math.sqrt(2)/den/a
        self.assertAlmostEqual(np.linalg.norm(y-w)/np.linalg.norm(w),expected,places=12)
        self.assertGreater(expected,.01)
        b=.02;y=m.iq_apply_periodic(m.iq_wave(t,[(f,b)],g=1.07,epsilon=np.pi/45,delay=24e-9,offset=.004-.001j),fs)
        # Changed blank alone propagates through the old real correction matrix.
        g,e,_=m.iq_fit_cached();mean=.001+1j*(.001/(g*math.cos(e))+math.tan(e)*.001)
        self.assertLess(abs(np.mean(y)-mean),1e-14)
        phase=np.angle(np.mean(y*np.exp(-2j*np.pi*f*(t-20e-9)))/b)
        self.assertGreater(abs(math.degrees(phase)),.05)

    def test_figure_record_values_follow_executed_pipeline(self):
        r=m.iq_record_results()
        self.assertLess(r['mod_pct'],.1);self.assertLess(r['near_pct'],.1)
        self.assertGreater(r['flat_pct'],5);self.assertGreater(r['high_pct'],1)
        self.assertLess(r['state_phase'],-.8)


class MultirateRecords(unittest.TestCase):
    def test_joined_modulated_chain_and_absolute_epochs(self):
        r,words,q,ideal,actual,epochs=m.joined_processing_case()
        h=m.fir_coeff();taps=np.arange(257)
        # Independent combined raw-input response, using moment equations for weights.
        nodes=np.arange(-3,5);moments=np.array([nodes**k for k in range(8)],float)
        for a in [0,len(q)//2,len(q)-1]:
            p=int(np.floor(q[a]));mu=q[a]-p
            w=np.linalg.solve(moments,np.array([mu**k for k in range(8)]))
            expected=0j
            for j,weight in zip(nodes,w):
                n=8*(32+p+j)-taps
                expected+=weight*np.sum(h*2*words[n]/2**15*np.exp(-2j*np.pi*20/128*n))
            self.assertLess(abs(expected-ideal[a]),1e-14)
        self.assertLess(np.max(abs(epochs-(1e-6+q/16e6))),1e-19)
        self.assertLess(np.linalg.norm(actual-ideal)/np.linalg.norm(ideal),.0002)
        self.assertEqual(r['overflows'],0);self.assertEqual(r['clips'],0)

    def test_impulse_polyphase_and_complete_tone_transfer(self):
        h=m.fir_coeff();x=np.zeros(1024);x[0]=1.;ix,y=m.ddc_reference(x)
        self.assertLess(np.max(abs(y[:33]-2*h[ix[:33]])),1e-15)
        rng=np.random.default_rng(1901);v=rng.uniform(-.2,.2,1024)+1j*rng.uniform(-.2,.2,1024)
        reference=np.convolve(v,h)[:1024][::8]
        # Explicit polyphase groups retain every input, not just every eighth one.
        grouped=[]
        for n in range(0,1024,8):
            grouped.append(sum(sum(h[k]*v[n-k] for k in range(p,257,8) if k<=n) for p in range(8)))
        self.assertLess(np.max(abs(np.array(grouped)-reference)),1e-15)
        n=np.arange(4096);t=n/128e6
        for M in [8,16]:
            components=[(20.5e6,.004,.3),(19e6,.002,-.6),(21.5e6,.001,.7)]
            wave=sum(a*np.cos(2*np.pi*f*t+p) for f,a,p in components)
            ix,y=m.ddc_reference(wave,decimation=M);want=np.zeros(len(ix),complex)
            for f,a,p in components:
                for sign in [1,-1]:
                    w=2*np.pi*(sign*f-20e6)/128e6
                    H=np.sum(h*np.exp(-1j*w*np.arange(257)))
                    want+=a*H*np.exp(1j*(w*ix+sign*p))
            self.assertLess(np.max(abs(y[ix>=256]-want[ix>=256])),2e-14)
        self.assertGreater(abs(sum(h*np.exp(-2j*np.pi*4e6/128e6*np.arange(257)))),.49)
        # Shared prototype/DFT channelizer at nonzero decimation origin: sign matters.
        x=rng.uniform(-.2,.2,1024);nn=np.arange(1024);r=3
        ix=np.arange(r,1024,8);v0=2*x*np.exp(-2j*np.pi*20/128*nn)
        groups=np.asarray([[sum(h[k]*v0[n-k] for k in range(p,257,8) if k<=n) for n in ix] for p in range(8)])
        for ell in [0,1,3,7]:
            shared=np.exp(-2j*np.pi*ell*r/8)*sum(np.exp(2j*np.pi*ell*p/8)*groups[p] for p in range(8))
            direct=np.convolve(2*x*np.exp(-2j*np.pi*(20+16*ell)/128*nn),h)[:1024][ix]
            self.assertLess(max(abs(shared-direct)),1e-13)

    def test_word_case_against_unbounded_exact_convolution(self):
        from fractions import Fraction
        words=m.digital_input(2048);ix,y,flags=m.ddc_integer(words)
        n=np.arange(len(words));ang=2*np.pi*5*n/32
        c=np.rint(np.cos(ang)*2**23).astype(np.int64);s=np.rint(-np.sin(ang)*2**23).astype(np.int64)
        co=[int(round(v*2**29)) for v in m.fir_coeff()]
        expected=[]
        for tr in [2*words*c,2*words*s]:
            conv=np.convolve(np.asarray([int(a) for a in tr],dtype=object),np.asarray(co,dtype=object))
            expected.append(np.asarray([round(Fraction(int(conv[k]),2**46))/2**21 for k in ix]))
        self.assertLess(np.max(abs(y-(expected[0]+1j*expected[1]))),1e-16)
        self.assertEqual(flags['overflows'],0);self.assertEqual(flags['clips'],0)
        _,bad,bf=m.ddc_integer(words,accumulator=56)
        self.assertGreater(bf['overflows'],1000);self.assertGreater(np.sqrt(np.mean(abs(bad-y)**2)),.005)
        self.assertLess(m.fir_metrics(fraction=23)['stop_db'],116)
        self.assertGreater(m.fir_metrics(fraction=29)['stop_db'],116)

    def test_nco_sample_loss_origin_and_rate_state(self):
        x=m.digital_input(4096)/2**15;ix,clean=m.ddc_reference(x)
        _,nco=m.ddc_reference(x,fault_index=2048);i,drop=m.ddc_reference(np.delete(x,2048))
        a=ix>=2304;b=i>=2304
        self.assertAlmostEqual(np.degrees(np.angle(np.mean(nco[a])/np.mean(clean[a]))),-90,places=6)
        self.assertAlmostEqual(np.degrees(np.angle(np.mean(drop[b])/np.mean(clean[:len(drop)][b]))),56.25,places=5)
        self.assertEqual(len(ix[(ix>=2048)&(ix<=2304)]),33)
        self.assertEqual(ix[ix>2304][0],2312)
        # A decimation-origin shift with correct absolute NCO advances the envelope only.
        f=20.5e6;n=np.arange(4096);wave=np.cos(2*np.pi*f*n/128e6)
        i0,y0=m.ddc_reference(wave);i1,y1=m.ddc_reference(wave,origin=1)
        # Project each at its own baseband epoch to compare the same response.
        z0=np.mean(y0[i0>=256]*np.exp(-2j*np.pi*.5e6*i0[i0>=256]/128e6))
        z1=np.mean(y1[i1>=256]*np.exp(-2j*np.pi*.5e6*i1[i1>=256]/128e6))
        self.assertLess(abs(z0-z1),1e-7)

    def test_affine_resampling_orientation_finite_support_and_integer(self):
        fb=16e6;alpha=1+20e-6;beta=10e-9;n=np.arange(4096);times=np.arange(16,4080)/fb
        wave=lambda t:.004*np.exp(2j*np.pi*2e6*t+.2j)+.003*np.exp(-2j*np.pi*.75e6*t-.3j)
        source=wave((n/fb-beta)/alpha);q=fb*(alpha*times+beta);out=m.resample_finite(source,q)
        self.assertLess(np.linalg.norm(out-wave(times))/np.linalg.norm(wave(times)),.0002)
        wrong=m.resample_finite(source,fb*(times-beta)/alpha)
        self.assertGreater(np.linalg.norm(wrong-wave(times))/np.linalg.norm(wave(times)),.02)
        fixed=m.resample_finite(source,q,phase_bits=15,coefficient_fraction=29,integer=True)
        self.assertLess(np.linalg.norm(fixed-wave(times))/np.linalg.norm(wave(times)),.0002)
        with self.assertRaises(ValueError):m.resample_finite(source,[1.2])
        bound=43.06640625*(np.pi/4)**8/math.factorial(8)
        for mu in np.linspace(0,1,31):
            self.assertLessEqual(abs(m.interpolation_response(2e6,mu)-1),bound+1e-15)
        self.assertGreater(abs(m.interpolation_response(4e6,.5)-1),.02)
