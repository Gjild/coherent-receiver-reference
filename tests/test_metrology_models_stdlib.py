"""Distinct double-sum, limits, loading sensitivities and coherent-floor checks."""
import unittest,sys,math,cmath
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import metrology_models as m
class MetrologyFoundations(unittest.TestCase):
    def test_pair_counts_and_white_limit(self):
        for n in [2,3,11,100]:
            got=sum(.9**abs(i-j) for i in range(n) for j in range(n))/n**2
            self.assertAlmostEqual(got,m.mean_factor(n),places=14)
            self.assertAlmostEqual(m.mean_factor(n,0),1/n)
            self.assertAlmostEqual(m.variance_dof(n,0),n-1,places=10)
        self.assertLess(1/m.mean_factor(100),6)
        self.assertNotAlmostEqual(m.variance_dof(100),1/m.mean_factor(100)-1)
    def test_loading_finite_differences(self):
        z=45+5j;step=1e-4
        g=[(cmath.phase(m.loading(z+step*v))-cmath.phase(m.loading(z-step*v)))/(2*step) for v in [1,1j]]
        self.assertAlmostEqual(.2*math.hypot(*g),m.loading_uncertainty(),places=11)
        self.assertEqual(m.loading(50),.5)
    def test_coherent_floor_tangent_and_range(self):
        A=.02;B=.0002;alpha=math.asin(B/A)
        tangent=complex(A-B*B/A,B*math.sqrt(1-(B/A)**2))
        self.assertAlmostEqual(abs(tangent-A),B,places=16)
        self.assertAlmostEqual(cmath.phase(tangent),alpha)
        self.assertGreater(alpha,.002);self.assertLess(math.asin(B/.12),.002)
        self.assertGreater(B/math.sin(.002),.1)
    def test_uncertain_source_uses_the_target_load(self):
        for z,zs in [(45+5j,50+0j),(60-12j,37+8j)]:
            eps=1e-4
            sensitivity=1/(zs+50)-1/(zs+z)
            for direction in [1,1j]:
                fd=(m.loading_correction(z,zs+eps*direction)-m.loading_correction(z,zs-eps*direction))/(2*eps)
                self.assertAlmostEqual(fd,(sensitivity*direction).imag,places=10)
        self.assertAlmostEqual((1/100-1/(95+5j)).real,-.0004972375690607735)
    def test_origin_inside_versus_touching_uncertainty_disk(self):
        center=1+0j
        self.assertGreater(abs(-.05-center),1)  # negative real direction outside touching disk
        self.assertLess(abs(-.05-center),1.1)  # available when zero is strictly interior
        self.assertEqual(abs(0-center),1)
    def test_touching_disk_has_nonlinear_scalar_phase_variance(self):
        # Independent polar-area quadrature; a zero-probability boundary point is allowed.
        N=8192;h=math.pi/N
        def integrate(fn):
            return h/3*(fn(-math.pi/2)+fn(math.pi/2)+sum((4 if k%2 else 2)*fn(-math.pi/2+k*h) for k in range(1,N)))
        density=lambda p:2*math.cos(p)**2/math.pi
        self.assertAlmostEqual(integrate(density),1,places=12)
        v=integrate(lambda p:p*p*density(p))
        self.assertAlmostEqual(v,math.pi**2/12-.5,places=12)
        self.assertGreater(math.sqrt(v),.5)
