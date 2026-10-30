"""Independent formulations for figure mathematics, not physical validation."""
import unittest
import importlib.util
from pathlib import Path
import math
import cmath

spec=importlib.util.spec_from_file_location('visual_models',Path(__file__).parents[1]/'engineering/examples/visual_foundations.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)

class FigureModels(unittest.TestCase):
    def test_coherent_power_from_pair_sum(self):
        # Midpoint double sum of the Gaussian phasor covariance, distinct from
        # the generating one-dimensional lag quadrature.
        for T in (.1,1.,10.):
            n=600
            value=sum(math.exp(-(1-math.exp(-abs(i-j)*T/n))) for i in range(n) for j in range(n))/n**2
            self.assertAlmostEqual(value,v.coherent(T),delta=1e-5)
        self.assertAlmostEqual(v.coherent(10),.456410127844,places=9)
    def test_average_covariance_and_spectral_forms(self):
        time=v.quad(lambda u:2*(1-u)*math.exp(-10*u),0,1)
        spectral=v.quad(lambda f:2*2/(1+(2*math.pi*f)**2)*v.sinc(10*f)**2,0,20,80000)
        self.assertAlmostEqual(v.avg(10),time,places=9)
        self.assertAlmostEqual(time,spectral,delta=3e-9)
    def test_shared_delay_complex_response(self):
        for x in (0,.01,.1,.5,1.):
            self.assertAlmostEqual(abs(cmath.exp(-2j*math.pi*x)-1)**2,4*math.sin(math.pi*x)**2,places=13)
    def test_ar1_estimator_covariance_sums(self):
        for r in (-.7,0,.7):
            for n in (1,2,15,100):
                direct=sum(r**abs(i-j) for i in range(n) for j in range(n))/n**2
                lag=(n+2*sum((n-m)*r**m for m in range(1,n)))/n**2
                self.assertAlmostEqual(direct,lag,places=13)
                var_direct=2*sum(r**(2*abs(i-j)) for i in range(n) for j in range(n))/n**2
                var_lag=2*(n+2*sum((n-m)*r**(2*m) for m in range(1,n)))/n**2
                self.assertAlmostEqual(var_direct,var_lag,places=13)
    def test_complex_filter_and_rotation(self):
        z=(1+1j)*1.1-1j
        self.assertAlmostEqual(cmath.phase(z),.09065988720074511)
        z1=.1*cmath.exp(1j*math.radians(12));z2=.1*cmath.exp(1j*math.radians(52))
        for chi in (0,.8,-1.3):
            rotation=cmath.exp(-1j*chi)
            self.assertAlmostEqual(cmath.phase(z2*rotation*(z1*rotation).conjugate()),math.radians(40))

class CoupledFigureModels(unittest.TestCase):
    def test_covariance_projection_support(self):
        a=math.sqrt(.0005); b=.0008/a; c=math.sqrt(.0025-b*b)
        points=[(a*math.cos(t),b*math.cos(t)+c*math.sin(t)) for t in v.lin(0,2*math.pi,20001)]
        for w1,w2 in [(-1,1),(-2,1)]:
            peak=max(w1*x+w2*y for x,y in points)
            variance=w1*w1*.0005+2*w1*w2*.0008+w2*w2*.0025
            self.assertAlmostEqual(peak,math.sqrt(variance),delta=1e-8)
        self.assertAlmostEqual(-2*.02+.04,0.)
    def test_delay_branches_and_frequency_spread(self):
        freqs=[i*1e6 for i in [-2,-1,0,1,2]]
        for f in freqs:
            self.assertAlmostEqual(abs(cmath.exp(1j*(.3-2*math.pi*f*5e-9))-cmath.exp(1j*(.3-2*math.pi*f*1005e-9))),0.,delta=1e-13)
        sx=sum(f*f for f in freqs)
        self.assertAlmostEqual(.02/(2*math.pi*math.sqrt(sx))*1e9,1.00658424209,places=9)
        self.assertEqual(sum((f/2)**2 for f in freqs),sx/4)
    def test_uncertainty_from_finite_source_ensemble(self):
        import itertools
        for rho in (.9,.9877410560974942,1.):
            diffs=[]
            for u,z,e1,e2 in itertools.product([-1,1],repeat=4):
                x1=math.sqrt(.00036)*u+.006324555320336759*e1
                x2=math.sqrt(.00036)*(rho*u+math.sqrt(1-rho*rho)*z)+.006324555320336759*e2
                diffs.append(x2-x1)
            var=sum(d*d for d in diffs)/len(diffs)
            self.assertAlmostEqual(var,.00008+.00072*(1-rho),places=14)
    def test_nonlinear_gaussian_moments(self):
        for sigma in (.1,.2,.5):
            density=lambda z:math.exp(-z*z/2)/math.sqrt(2*math.pi)
            mean=v.quad(lambda z:math.cos(sigma*z)*density(z),-10,10,4096)
            variance=v.quad(lambda z:(math.cos(sigma*z)-mean)**2*density(z),-10,10,4096)
            self.assertAlmostEqual(mean,math.exp(-sigma*sigma/2),places=12)
            self.assertAlmostEqual(variance,.5*(1-math.exp(-sigma*sigma))**2,places=12)


class TrackingFigureModels(unittest.TestCase):
    def test_residual_budget_against_frequency_integral(self):
        for fc in (10.,28.27,100.,134.33):
            k=2*math.pi*fc
            # Integrate both sides of the declared detector-noise spectrum.
            variance=v.quad(lambda f:1e-6*abs(k/(k+2j*math.pi*f))**2,-1000,1000,32768)
            self.assertAlmostEqual(v.tracking_rms(fc)**2,variance+(.5/fc)**2,places=13)
        self.assertGreater(v.tracking_rms(28),.02)
        self.assertLess(v.tracking_rms(29),.02)
        self.assertLess(v.tracking_rms(134),.02)
        self.assertGreater(v.tracking_rms(135),.02)
    def test_phase_line_and_holdover_bound(self):
        stable=math.asin(.5);unstable=math.pi-stable
        for e in (stable,unstable):self.assertAlmostEqual(.5-math.sin(e),0.)
        self.assertLess(-math.cos(stable),0.);self.assertGreater(-math.cos(unstable),0.)
        for d in (-.01,.01):self.assertGreater(1-math.sin(math.pi/2+d),0.)
        expiry=(.1-.02)/(2*math.pi*.1)
        self.assertAlmostEqual(expiry,.1273239544735163)
        # Independently integrate the bounded constant frequency error.
        self.assertAlmostEqual(.02+v.quad(lambda t:2*math.pi*.1,0,expiry),.1)
    def test_complex_transfers_and_delay_crossing(self):
        for x in (-100.,-1.,0.,.1,1.,100.):
            t=1/(1+1j*x);e=1-t
            self.assertAlmostEqual(abs(t)**2+abs(e)**2,1.)
        for fc in (10.,100.):
            k=2*math.pi*fc;latency=1/(4*fc)
            self.assertLess(abs(1j*k+k*cmath.exp(-1j*k*latency)),1e-11)


class PilotFigureModels(unittest.TestCase):
    def test_shared_endpoint_integral_against_cosine_series(self):
        # Integrate 2(1-cos(2*pi*f*delay)) term by term; this avoids both
        # author sin-squared evaluation and numerical integration.
        for delay in (1e-8,1e-7):
            value=4e-6*sum((-1)**(n+1)*(2*math.pi*delay)**(2*n)*(10000**(2*n+1)-1)/(math.factorial(2*n)*(2*n+1)) for n in range(1,6))
            self.assertAlmostEqual(v.endpoint_common_variance(delay),value,delta=1e-20)
        local=2*v.quad(lambda f:1e-6*abs((cmath.exp(-2j*math.pi*f*1e-7)-1)/(1+1j*f/100))**2,1,10000,32768)
        self.assertAlmostEqual(v.endpoint_common_variance(1e-7,100),local,delta=1e-18)
    def test_held_update_covariance_transform_and_area(self):
        for f in (0.,.25,.37,1.,1.5,3.):
            transformed=v.quad(lambda t:(1-abs(t))*math.cos(2*math.pi*f*t),-1,1,8192)
            self.assertAlmostEqual(transformed,v.sinc(f)**2,delta=1e-12)
        cutoff=40.
        area=v.quad(lambda f:v.sinc(f)**2,-cutoff,cutoff,160000)
        # Independent tail bound from sinc²(f) <= 1/(pi*f)².
        self.assertGreater(area,1-2/(math.pi**2*cutoff))
        self.assertLess(area,1.)

if __name__=='__main__':unittest.main()
