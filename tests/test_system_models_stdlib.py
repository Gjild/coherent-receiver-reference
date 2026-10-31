"""Distinct physical/numerical formulations for bounded system examples."""
import unittest,math,cmath,sys,random
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import system_models as model


class RequirementModels(unittest.TestCase):
    def test_peak_voltage_against_phase_swept_real_waveforms(self):
        for attenuation,loss in [(0,0),(30,2),(40,2),(60,2)]:
            lo,hi=model.gain_bounds(attenuation,loss)
            ps=1e-3*10**((-100-loss)/10);pb=1e-3*10**((-20-attenuation)/10)
            a=math.sqrt(100*ps);b=math.sqrt(100*pb)
            # Commensurate tones reach their worst joint peak at t=0.
            peak=max(abs(a*math.cos(2*math.pi*.7*t/10000)+b*math.cos(2*math.pi*1.3*t/10000)) for t in range(10001))
            self.assertAlmostEqual(peak*10**(hi/20),.1,places=13)
            self.assertAlmostEqual(a*10**(lo/20),math.sqrt(100e-9),places=13)
        self.assertGreater(*model.gain_bounds(0,0))
        self.assertLess(*model.gain_bounds(40,2))

    def test_spatial_aliases_and_local_finite_difference(self):
        k=2*math.pi/.3
        self.assertAlmostEqual(abs(cmath.exp(1j*k*1.2*.25)-cmath.exp(1j*k*1.2*.5)),0,places=13)
        self.assertGreater(abs(cmath.exp(1j*k*.15*.25)-cmath.exp(1j*k*.15*.5)),.7)
        th=math.pi/3;eps=1e-6
        derivative=(k*1.2*math.sin(th+eps)-k*1.2*math.sin(th-eps))/(2*eps)
        sigma=math.degrees(1/derivative/math.sqrt(100))
        self.assertAlmostEqual(sigma,.45594532639052,places=8)
        low,high=model.aperture_limits();self.assertGreater(low,high)
        self.assertAlmostEqual(cmath.exp(1j*k*high*math.sin(th)),cmath.exp(-1j*k*high*math.sin(th)),places=12)

    def test_finite_tone_observation_against_midpoint_integration(self):
        n=20000;T=.001;df=100
        average=sum(cmath.exp(2j*math.pi*df*(i+.5)*T/n) for i in range(n))/n
        self.assertAlmostEqual(abs(average)**2*100,model.requirement_case()['rho'],places=7)
        needed=model.requirement_case()['short_rho'];self.assertGreater(needed/1e5,.0025)
        self.assertAlmostEqual(needed,5321.885200828357,places=8)

    def test_branch_error_covariance_from_three_physical_noise_sources(self):
        rng=random.Random(1113);k=2*math.pi/.3;rho=model.requirement_case()['rho']
        a,b=1/(k*.15),1/(k*1.2);sd=1/math.sqrt(2*rho);n=100000
        moments=0.
        for _ in range(n):
            e0,es,el=[rng.gauss(0,sd) for _ in range(3)]
            error=a*(es-e0)-b*(el-e0);moments+=error**2
        theoretical=(a*a+b*b-a*b)/rho
        self.assertLess(abs(moments/n/theoretical-1),.018)
        self.assertLess(model.requirement_case()['branch_sum'],1e-3)
        self.assertAlmostEqual(3*14*100e6*1.1,4.62e9,places=4)
        self.assertGreater(3*14*100e6*1.25,5e9)

    def test_retained_blocker_disk_and_composite_contract(self):
        q=model.retained_blocker();r=q['r'];phases=[2*math.pi*i/20000 for i in range(20001)]
        maximum=max(abs(cmath.phase(1+r*cmath.exp(1j*p))) for p in phases)
        minimum=min(abs(1+r*cmath.exp(1j*p)) for p in phases)
        self.assertLess(abs(maximum-q['beta']),1e-10)
        self.assertAlmostEqual(minimum,1-r,places=14)
        self.assertLess(q['branch_bound'],1e-3)
        # Exact inverse manifold, rather than a linear angular conversion.
        perturbed=math.asin(math.sin(math.pi/3)+2*q['beta']/(8*math.pi))
        self.assertLess(math.degrees(perturbed-math.pi/3),.02)
        amplitude_leak=10**(42/20)*abs(math.sin(math.pi*100.5)/(math.pi*100.5))
        self.assertGreater(amplitude_leak,.39)
        self.assertLess(q['minimum_rho'],model.requirement_case()['rho'])

    def test_reference_endpoint_allowances_by_complex_tones(self):
        tau=.05/(360*1.02e9)
        self.assertAlmostEqual(math.degrees(abs(cmath.phase(cmath.exp(-2j*math.pi*1.02e9*tau)))),.05,places=13)
        df=.05/(360*.001)
        self.assertAlmostEqual(math.degrees(cmath.phase(cmath.exp(2j*math.pi*df*.001))),.05,places=13)
        eps=.05/(360*20e6*.001)
        self.assertAlmostEqual(math.degrees(cmath.phase(cmath.exp(2j*math.pi*20e6*eps*.001))),.05,places=13)
        self.assertAlmostEqual(math.degrees(cmath.phase(cmath.exp(2j*math.pi*20e6/100e6))),72.,places=12)
        required=sum([1e-3/10**(-6/10)]*3)
        self.assertAlmostEqual(required,.011943215116604916,places=14)

    def test_phase_uncertainty_against_complex_voltage_noise(self):
        rng=random.Random(321);rho=model.requirement_case()['rho'];sd=1/math.sqrt(2*rho)
        n=60000;variance=0.
        for _ in range(n):
            x=1+complex(rng.gauss(0,sd),rng.gauss(0,sd))
            y=1+complex(rng.gauss(0,sd),rng.gauss(0,sd))
            variance+=cmath.phase(y*x.conjugate())**2
        # Checks the local approximation at the supplied SNR, not rare-event tails.
        self.assertLess(abs(variance/n*rho-1),.025)


if __name__=='__main__':unittest.main()
