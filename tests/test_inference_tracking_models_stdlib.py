"""Bounded mathematical checks; no physical or reader validation."""
import cmath
import itertools
import math
import unittest


def fit(xs, ys):
    xm, ym = sum(xs)/len(xs), sum(ys)/len(ys)
    centered = [x-xm for x in xs]
    slope = sum(x*(y-ym) for x,y in zip(centered,ys))/sum(x*x for x in centered)
    return ym-slope*xm, slope


class InferenceChecks(unittest.TestCase):
    def test_fit_and_precision_exact_noise_ensemble(self):
        xs = [-2e6,-1e6,0,1e6,2e6]
        a, delay, sigma = .3,5e-9,.02
        ys = [a-2*math.pi*x*delay for x in xs]
        self.assertAlmostEqual(fit(xs,ys)[1]/(-2*math.pi),delay,places=18)
        errors=[]
        for e in itertools.product([-sigma,sigma],repeat=5):
            errors.append(fit(xs,[y+n for y,n in zip(ys,e)])[1]/(-2*math.pi)-delay)
        # Finite non-Gaussian ensemble independently checks linear variance.
        expected=sigma**2/(4*math.pi**2*sum(x*x for x in xs))
        self.assertAlmostEqual(sum(e*e for e in errors)/len(errors)/expected,1)
        self.assertAlmostEqual(math.sqrt(expected)/1e-9,1.0065842421,places=9)

    def test_phasor_alias_and_hidden_path(self):
        xs=[-2e6,-1e6,0,1e6,2e6]
        for x in xs:
            one=cmath.exp(1j*(.3-2*math.pi*x*5e-9))
            two=cmath.exp(1j*(.3-2*math.pi*x*(5e-9+1e-6)))
            self.assertLess(abs(one-two),1e-13)
        ys=[.3-2*math.pi*x*(5e-9+3e-9) for x in xs]
        intercept,slope=fit(xs,ys)
        self.assertAlmostEqual(slope/(-2*math.pi),8e-9,places=18)
        self.assertLess(max(abs(y-intercept-slope*x) for x,y in zip(xs,ys)),1e-15)

    def test_curvature_projection_and_conversion(self):
        for xs in [[-8.,-7.,1.,5.,9.],[0.,1.,3.]]:
            center=[x-sum(xs)/len(xs) for x in xs]
            _,slope=fit(center,[.3+.02*x+.001*x*x for x in center])
            bias=.001*sum(x**3 for x in center)/sum(x*x for x in center)
            self.assertAlmostEqual(slope-.02,bias)
        for orientation in [1,-1]:
            xs=[-2e6,-1e6,0,1e6,2e6]
            physical=[.3-2*math.pi*x*5e-9 for x in xs]
            dl,db=.1,.04
            raw=[orientation*(y-dl)+db for y in physical]
            corrected=[orientation*(r-db)+dl for r in raw]
            self.assertAlmostEqual(fit(xs,corrected)[1]/(-2*math.pi),5e-9,places=18)


class TrackingChecks(unittest.TestCase):
    def test_ramp_response_against_time_integration(self):
        k, omega, e0 = 20., .8, .07
        def integrate(n):
            h=.5/n; e=e0
            for _ in range(n):
                f=lambda v: omega-k*v
                a=f(e);b=f(e+h*a/2);c=f(e+h*b/2);d=f(e+h*c)
                e+=h*(a+2*b+2*c+d)/6
            return e
        expected=e0*math.exp(-k*.5)+omega/k*(1-math.exp(-k*.5))
        self.assertAlmostEqual(integrate(100),expected,places=10)
        self.assertLess(abs(integrate(200)-expected),abs(integrate(100)-expected))

    def test_noise_integral_and_wanted_transfer(self):
        for corner in [10,100]:
            k=2*math.pi*corner;band=1000.;n=40000;df=band/n
            quadrature=2*sum(1e-6*k*k/(k*k+(2*math.pi*(i+.5)*df)**2)*df for i in range(n))
            exact=1e-6*k/math.pi*math.atan(2*math.pi*band/k)
            self.assertAlmostEqual(quadrature/exact,1,places=8)
        T=(2*math.pi*100)/(2j*math.pi*1+2*math.pi*100)
        self.assertAlmostEqual(abs(1-T),1/math.sqrt(10001))
        self.assertAlmostEqual(abs(T)**2+abs(1-T)**2,1)

    def test_nonlinear_equilibrium_latency_and_holdover(self):
        k=20.;omega=1.;eq=math.asin(omega/k)
        self.assertAlmostEqual(omega-k*math.sin(eq),0)
        self.assertLess(-k*math.cos(eq),0)
        L=math.pi/(2*k);pole=1j*k
        self.assertLess(abs(pole+k*cmath.exp(-pole*L)),1e-12)
        t=(.1-.02)/(2*math.pi*.1)
        self.assertAlmostEqual(t,.12732395447351627)


class DynamicStressChecks(unittest.TestCase):
    def test_frequency_ramp_against_independent_integration(self):
        k,omega,alpha,e0=20.,.8,2.,.04
        n=2000;h=.5/n;e=e0
        for j in range(n):
            t=j*h
            f=lambda at,v: omega+alpha*at-k*v
            a=f(t,e);b=f(t+h/2,e+h*a/2);c=f(t+h/2,e+h*b/2);d=f(t+h,e+h*c)
            e+=h*(a+2*b+2*c+d)/6
        ep=lambda t:(omega+alpha*t)/k-alpha/k**2
        expected=ep(.5)+(e0-ep(0))*math.exp(-k*.5)
        self.assertAlmostEqual(e,expected,places=12)


if __name__=='__main__':
    unittest.main()
