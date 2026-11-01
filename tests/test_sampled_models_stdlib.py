"""Distinct waveform, probability, timing and implementation checks."""
import unittest,sys,math,cmath
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import sampled_models as m


class ConverterModels(unittest.TestCase):
    def test_range_and_real_alias_orientation(self):
        c=m.converter_case()
        # Actual real waveforms attain the aligned bound at the origin.
        n=4096
        vals=[c['wanted']*math.cos(2*math.pi*20*k/n)+c['blocker']*(
            math.cos(2*math.pi*30*k/n)+math.cos(2*math.pi*40*k/n)) for k in range(n)]
        self.assertAlmostEqual(max(map(abs,vals)),c['peak'],places=14)
        self.assertLess(c['peak'],.8);self.assertGreater(c['broadband_peak'],.8)
        self.assertLess(m.converter_case(22)['broadband_peak'],.8)
        for k in range(128):
            u=cmath.exp(2j*math.pi*108*k/128)
            v=cmath.exp(-2j*math.pi*20*k/128)
            self.assertLess(abs(u-v),2e-13)
        bandpass=sum(math.cos(2*math.pi*20*k/32+.3)*cmath.exp(-2j*math.pi*12*k/32) for k in range(512))/256
        self.assertLess(abs(bandpass-cmath.exp(-.3j)),1e-13)
        self.assertTrue(all(abs(math.cos(math.pi*k+.3)-math.cos(math.pi*k-.3))<1e-13 for k in range(128)))
        attenuation=20*math.log10(c['blocker']/(c['wanted']*math.sin(math.radians(.02))))
        ratio=c['blocker']*10**(-attenuation/20)/c['wanted']
        self.assertAlmostEqual(math.degrees(math.asin(ratio)),.02,places=14)

    def test_timing_from_physical_weights_and_exact_time_shift(self):
        c=m.converter_case();a=c['wanted'];b=c['blocker'];N=256000
        phase=[2*math.pi*10*n/64 for n in range(64)]
        ds=[]
        for sign in [1,-1]:
            ds.append([-2*math.pi*(20e6*a*math.sin(phase[n])+sign*b*(
                30e6*math.sin(2*math.pi*15*n/64)+40e6*math.sin(2*math.pi*20*n/64))) for n in range(64)])
        for opp in [False,True]:
            weights=[[-2*ds[j if opp else 0][n]*math.sin(phase[n])/a for n in range(64)] for j in range(2)]
            energy=sum((80e-15*(weights[1][n]-weights[0][n]))**2+
                       (60e-15)**2*(weights[0][n]**2+weights[1][n]**2) for n in range(64))/64/N
            self.assertAlmostEqual(math.degrees(math.sqrt(energy)),m.aperture_phase(.8,opp),places=14)
        # A tiny exact analog shift converges to slope-weighted voltage.
        eps=1e-13;dif=[]
        for n in range(64):
            t=n/128e6
            exact=sum(amp*(math.cos(2*math.pi*f*(t+eps))-math.cos(2*math.pi*f*t))
                      for f,amp in [(20e6,a),(30e6,b),(40e6,b)])
            dif.append(exact/eps)
        rms=math.sqrt(sum(v*v for v in dif)/64)
        self.assertLess(abs(rms/c['slope']-1),2e-7)

    def test_quantized_period_repetition_and_subcode_erasure(self):
        for bits in [14,16]:
            zz=[]
            for phases in [(0.,.2,-.4),(.3,1.1,-.7)]:
                v=m.converter_period(phases)
                q=[m.quantize(u,bits) for u in v]
                z=sum(u*cmath.exp(-2j*math.pi*10*n/64) for n,u in enumerate(q))/32
                zrep=sum(q[n%64]*cmath.exp(-2j*math.pi*10*(n%64)/64) for n in range(640))/320
                self.assertLess(abs(z-zrep),1e-16);zz.append(z)
                self.assertTrue(all(m.quantize(10e-6*math.cos(2*math.pi*n/64),bits)==0 for n in range(64)))
            result=math.degrees(cmath.phase(zz[1]*zz[0].conjugate())-.3)
            self.assertAlmostEqual(result,m.coherent_quantization(bits),places=12)
            self.assertGreater(abs(result),.01)

    def test_dither_by_explicit_threshold_interval_integration(self):
        # Integrate each output-code interval under uniform dither; no RNG assumption.
        step=2/2**14
        for x in [-1.35*step,-.1*step,0.,.23*step,1.78*step]:
            edges=sorted({x-step/2,x+step/2}|{(k+.5)*step for k in range(-4,5) if x-step/2<(k+.5)*step<x+step/2})
            mean=second=0.
            for lo,hi in zip(edges,edges[1:]):
                q=m.quantize((lo+hi)/2);p=(hi-lo)/step
                mean+=p*q;second+=p*(q-x)**2
            frac=x/step-math.floor(x/step)
            self.assertLess(abs((mean-x)/step),1e-14)
            self.assertAlmostEqual(second/step**2,frac*(1-frac),places=14)
        # Shared uniform dither: same marginals, different cross-channel covariance.
        terms=[]
        for lo,hi in zip([-.5,-.2,.3],[ -.2,.3,.5]):
            d=(lo+hi)/2
            terms.append((hi-lo,math.floor(.2+d+.5)-.2,math.floor(.7+d+.5)-.7))
        self.assertAlmostEqual(sum(p*a*b for p,a,b in terms),.06,places=14)
        self.assertAlmostEqual(sum(p*(a-b)**2 for p,a,b in terms),.25,places=14)
        self.assertAlmostEqual(.2*.8+.7*.3,.37,places=14)
        self.assertGreater(m.dither_phase_bound(14),.002)
        self.assertLess(m.dither_phase_bound(16),.002)
        self.assertGreater(m.dither_phase_bound(16,120e-6),.002)

    def test_real_alternating_aperture_image_and_skew_sign(self):
        # Sample two genuinely offset apertures, then project the image.
        fs=128e6;f=44e6;delta=5e-12;n=4096
        theta=.37
        for skew in [delta,-delta]:
            z=sum(math.cos(2*math.pi*f*(k/fs+(-1)**k*skew/2)+theta)*cmath.exp(-2j*math.pi*20*k/128)
                  for k in range(n))*2/n
            exact=-1j*math.sin(math.pi*f*skew)*cmath.exp(-1j*theta)
            self.assertLess(abs(z-exact)/abs(exact),1e-9)
        adv=50e-12
        wanted=sum(math.cos(2*math.pi*20e6*(k/fs+adv))*cmath.exp(-2j*math.pi*20*k/128) for k in range(n))*2/n
        self.assertAlmostEqual(math.degrees(cmath.phase(wanted)),.36,places=10)

    def test_driver_by_numerical_rc_step_and_power_noise_bound(self):
        # Euler realization of the declared step response; test actual residual scale.
        tau=.2545932425098171e-9;dt=tau/20000;time=3e-9
        residue=2.;steps=round(time/dt)
        for _ in range(steps):residue-=residue*dt/tau
        self.assertLess(abs(residue/(1/2**16)-1),.001)
        c=m.converter_case()
        self.assertLess(.9+c['peak']/2,1.45)
        self.assertGreater(.9-c['peak']/2,.35)
