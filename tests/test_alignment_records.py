"""Executed bounded echo fit, held-out records and exact word reference."""
import unittest,sys,cmath,math
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import alignment_models as m

class AlignmentRecords(unittest.TestCase):
    def test_fit_holdout_and_changed_state(self):
        for a,L in [(.6,16),(1.25,32)]:
            r=m.alignment_case(a,L)
            self.assertAlmostEqual(r['a_est'],a,places=13)
            self.assertLess(r['integer_record_pct'],.1)
            self.assertLess(r['arithmetic_vs_float_pct'],.006)
            self.assertGreater(r['changed_state_max_pct'],7)
            self.assertLess(r['maxpartial'],2**63)

    def test_integer_against_object_convolution_and_exact_rounding(self):
        from fractions import Fraction
        t=np.arange(256)/m.FS
        x=.017*np.exp(2j*np.pi*.8125e6*t+.13j)+.009*np.exp(-2j*np.pi*1.0625e6*t-.31j)
        q,_=m.align_coeff(1.25,32);out,_=m.align_integer(x,q)
        xr=np.array([int(round(v.real*2**21)) for v in x],object)
        xi=np.array([int(round(v.imag*2**21)) for v in x],object)
        cr=np.array([int(round(v.real*2**20)) for v in q],object)
        ci=np.array([int(round(v.imag*2**20)) for v in q],object)
        rr=np.convolve(xr,cr)-np.convolve(xi,ci)
        ii=np.convolve(xr,ci)+np.convolve(xi,cr)
        want=[complex(round(Fraction(int(a),2**20)),round(Fraction(int(b),2**20)))/2**21 for a,b in zip(rr[:256],ii[:256])]
        self.assertLess(max(abs(a-b) for a,b in zip(out,want)),1e-17)
