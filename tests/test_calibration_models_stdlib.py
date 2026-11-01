"""Calibration freedoms, age constraints and wanted/nuisance transfer."""
import unittest,sys,cmath,math
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import calibration_models as m
class CalibrationFoundations(unittest.TestCase):
    def test_indistinguishable_factors_and_offset_projection(self):
        c=[1,1j,-1,-1j];h=.9*cmath.exp(.08j);p=.98*cmath.exp(.03j);s=.05*cmath.exp(.7j);b=.003-.001j
        y=[h*p*s*x+b for x in c];z=sum(x.conjugate()*v for x,v in zip(c,y))/4
        self.assertAlmostEqual(abs(z-h*p*s),0,places=17)
        self.assertEqual([h*p*s*x+b for x in c],[(h*p)*s*x+b for x in c])
        leak=.001j;zz=sum(x.conjugate()*(v+leak*x) for x,v in zip(c,y))/4
        self.assertAlmostEqual(abs(zz-z-leak),0,places=17)
        self.assertAlmostEqual(abs(h/(h*p)),1/.98)
    def test_cycle_feasibility_and_outage_age(self):
        self.assertAlmostEqual(m.cadence_error(10),.00806)
        self.assertLess(m.cadence_error(14.85),.010000000001)
        self.assertGreater(m.cadence_error(60),.01)
        self.assertGreater(m.cadence_error(50,1),.01)
        self.assertAlmostEqual((.01-.004)/.0004,15)
        # Changed assumptions r doubles and downtime halves: C>=20, C<=7.35.
        self.assertGreater(m.cadence_error(20,rate=.0008),.01)
    def test_retained_signal_and_shared_science_noise(self):
        f=.01;w,d=m.tracking_transfer(f,1)
        self.assertAlmostEqual(abs(w),f/math.hypot(f,.1))
        self.assertEqual(w,d);self.assertEqual(m.tracking_transfer(f,0)[0],1)
        L=1/(1+1j*f/.1)
        self.assertAlmostEqual(abs(m.tracking_transfer(f,.1)[0]),abs((.9+1j*.1)/(1+1j*.1)))
        # Science-derived measurement noise follows 1-L, not two independent variances.
        self.assertLess(abs(1-L)**2,1+abs(L)**2)
