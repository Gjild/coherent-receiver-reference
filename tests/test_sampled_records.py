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
