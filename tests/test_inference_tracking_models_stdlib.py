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


class ModelAdequacyChecks(unittest.TestCase):
    def test_covariance_source_path_decision(self):
        u=math.sqrt(.00036);local=math.sqrt(.00004)
        for gain,target in [(1,.00008),(.5,.00017)]:
            diffs=[gain*a+c-(a+b) for a,b,c in itertools.product([-u,u],[-local,local],[-local,local])]
            variance=sum(x*x for x in diffs)/8
            self.assertAlmostEqual(variance,target)
            delay_sd=math.sqrt(variance)/(2*math.pi*1e7)
            self.assertEqual(delay_sd<.15e-9,gain==1)

    def test_nonlinear_variance_against_density_quadrature(self):
        sigma=.2;n=24000;dz=18/n
        density=lambda z: math.exp(-z*z/2)/math.sqrt(2*math.pi)
        mean=sum(math.cos(sigma*(-9+(i+.5)*dz))*density(-9+(i+.5)*dz)*dz for i in range(n))
        second=sum(math.cos(sigma*(-9+(i+.5)*dz))**2*density(-9+(i+.5)*dz)*dz for i in range(n))
        self.assertAlmostEqual(mean,math.exp(-sigma*sigma/2),places=12)
        exact=.5*(1-math.exp(-sigma*sigma))**2
        self.assertAlmostEqual(second-mean*mean,exact,places=12)
        self.assertGreater(math.sqrt(exact),.01)

    def test_cancellation_against_high_precision_and_integral(self):
        from decimal import Decimal,localcontext
        with localcontext() as context:
            context.prec=70
            d=Decimal('1e-8')
            reference=float(2*(d-1+(-d).exp())/(d*d))
        x=1e-8
        stable=1-x/3+x*x/12-x**3/60
        self.assertAlmostEqual(stable,reference,places=15)
        n=10000;dv=1/n
        integral=2*sum((1-(i+.5)*dv)*math.exp(-x*(i+.5)*dv)*dv for i in range(n))
        self.assertAlmostEqual(integral,reference,places=12)
        # Do not require a particular platform's naive rounded value.
        self.assertGreater(abs(2*(x-1+math.exp(-x))/x**2-reference),.1)


class PropagationConditionChecks(unittest.TestCase):
    def test_timing_correlation_and_reciprocal_tails(self):
        V=.00036
        for rho in [.98,.99]:
            diffs=[b-a+math.sqrt(V)*(rho*u+math.sqrt(1-rho*rho)*v-u)
                   for a,b,u,v in itertools.product([-math.sqrt(.00004),math.sqrt(.00004)],
                       [-math.sqrt(.00004),math.sqrt(.00004)],[-1,1],[-1,1])]
            var=sum(x*x for x in diffs)/len(diffs)
            self.assertAlmostEqual(var,.00008+2*V*(1-rho))
            self.assertEqual(math.sqrt(var)/(2*math.pi*1e7)<.15e-9,rho==.99)
        mean,sd,low=1e7,1000.,1.
        probability=sd**2/(sd**2+(mean-low)**2)
        high=mean+sd**2/(mean-low)
        exact_sd=math.sqrt(probability*(1-probability))*(.05/low-.05/high)
        self.assertGreater(exact_sd/1e-9,4900)
        width=math.sqrt(3)*sd;n=20000
        errors=[5e-9*(mean/(mean-width+(i+.5)*2*width/n)-1) for i in range(n)]
        em=sum(errors)/n
        bounded_sd=math.sqrt(sum((e-em)**2 for e in errors)/n)
        self.assertAlmostEqual(bounded_sd/(5e-9*sd/mean),1,places=6)


if __name__=='__main__':
    unittest.main()
