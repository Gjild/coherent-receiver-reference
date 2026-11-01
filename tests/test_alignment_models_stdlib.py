"""Distinct finite-polynomial, support, noise and information checks."""
import unittest,sys,math,cmath
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import alignment_models as m

class AlignmentBasics(unittest.TestCase):
    def test_finite_inverse_polynomial_and_support(self):
        for a,N in [(.6,16),(1.25,32)]:
            q,D=m.align_coeff(a,N);g=.9*cmath.exp(.08j)
            c=[0j]*(N+1)
            for k,v in enumerate(q):c[k]+=g*v;c[k+1]-=g*a*v
            want=[0j]*(N+1)
            if a<1:want[0]=1;want[N]=-a**N
            else:want[0]=-a**(-N);want[N]=1
            self.assertLess(max(abs(x-y) for x,y in zip(c,want)),1e-15)
            for f in [-1.9375e6,-.375e6,0,.9375e6,1.875e6]:
                w=2*math.pi*f/m.FS
                expected=1-a**N*cmath.exp(-1j*w*N) if a<1 else 1-a**(-N)*cmath.exp(1j*w*N)
                self.assertLess(abs(m.align_response(f,a,N)-expected),2e-14)
            self.assertGreaterEqual(D-5,0)

    def test_magnitude_cannot_choose_inverse_support(self):
        for k in range(501):
            w=-math.pi+2*math.pi*k/500
            self.assertAlmostEqual(abs(1-.8*cmath.exp(-1j*w)),abs(.8-cmath.exp(-1j*w)),places=14)
        # Causal recursion for an outside zero diverges; stable expansion has negative support.
        self.assertGreater(1.25**32,1000)
        self.assertAlmostEqual(sum(1.25**(-j) for j in range(1,1000)),4,places=13)

    def test_noise_plane_and_regularization_bias(self):
        for a,N in [(.6,16),(1.25,32)]:
            q,_=m.align_coeff(a,N)
            ratio=a*a if a<1 else a**-2
            expected=(1-ratio**N)/(1-ratio)/.81*(1 if a<1 else ratio)
            self.assertAlmostEqual(sum(abs(v)**2 for v in q),expected,places=13)
        h=.018;sig=20e-6;s=.01
        snr_before=h*s/sig;snr_after=s/(sig/h)
        self.assertAlmostEqual(snr_before,snr_after)
        Q=m.regularized_response(h,.01)
        self.assertAlmostEqual(Q*h,.7641509433962264)
        self.assertLess(abs(Q),50)

    def test_steady_state_null_and_combination_rank(self):
        for c in [.01,.02+.03j,-.005j]:self.assertEqual(c-c,0)
        # Two distinct channel pairs have identical single summed observation.
        x=(.2+.1j,.4-.2j);delta=.1-.3j
        self.assertEqual(x[0]+x[1],(x[0]+delta)+(x[1]-delta))
        # Known zero history is additional information, not the steady-state domain.
        x=[.01]*64;y=[x[n]-(x[n-1] if n else 0) for n in range(64)]
        self.assertEqual(y[0],.01);self.assertEqual(sum(abs(t) for t in y[1:]),0)
