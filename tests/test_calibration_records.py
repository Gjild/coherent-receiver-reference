"""Independent fit/projection and held-out correction checks on supplied records."""
import unittest,sys,cmath,math
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import calibration_models as m
class CalibrationRecords(unittest.TestCase):
    def test_supplied_procedure_and_rejection(self):
        r=m.calibration_case()
        self.assertLess(r['heldout_integer_relative_error'],.0005)
        self.assertLess(r['swept_error']['nominal'],.0005)
        self.assertGreater(r['swept_error']['gain changed'],.03)
        self.assertGreater(r['swept_error']['echo changed'],.07)
        self.assertLess(abs(complex(*r['dc_gain'])-1),.0003)
        self.assertGreater(r['fixture_omitted_fit'],.06)
        self.assertGreater(r['fixture_omitted_selected_fit'],.46)
        self.assertGreater(r['fixture_omitted_a'],1)
        self.assertGreater(r['unremoved_record_error'],1)
        self.assertLess(abs(complex(*r['offset_error'])),.2e-6)
    def test_fit_from_separate_phase_differences(self):
        # Same supplied acquisition, independently cancel offsets by opposite-phase differences.
        rng=np.random.default_rng(2101);freq=np.array([.25,.75,1.25,1.75])*1e6;data=[]
        for f in freq:
            w=2*np.pi*f/m.FS;source=.05*np.exp(1j*(.7+.2*f/1e6));vals=[]
            for h,p,b in [(np.exp(-2j*w),1,.001+.002j),(m.align.echo_response(f),m.fixture(f),.003-.001j)]:
                n=20e-6/np.sqrt(2)*(rng.normal(size=(64,4))+1j*rng.normal(size=(64,4)))
                yy=h*p*source*np.array([1,1j,-1,-1j])+b+n
                vals.append(np.mean((yy[:,0]-yy[:,2]-1j*(yy[:,1]-yy[:,3]))/4))
            data.append(vals[1]/vals[0]/m.fixture(f)*np.exp(3j*w))
        A=np.array([[1,np.exp(-2j*np.pi*f/m.FS)] for f in freq]);c=np.linalg.solve(A.conj().T@A,A.conj().T@data)
        g,a,_=m.calibrate();self.assertLess(abs(c[0]-g),1e-13);self.assertAlmostEqual((-c[1]/c[0]).real,a,places=12)
    def test_reading_covariance_positive_and_finite_difference(self):
        r=m.reading_uncertainty();C=np.array(r['coefficient_covariance_real'])
        self.assertGreater(np.linalg.eigvalsh(C).min(),0)
        g,a,_=m.calibrate();c=np.array([g,-g*a]);f=-2e6;H=m.align.echo_response(f)*np.exp(10j*np.pi*f/m.FS)
        def output(x):
            gg=x[0]+1j*x[2];aa=(-(x[1]+1j*x[3])/gg).real
            return m.correction(f,gg,aa,False)*H
        x=np.r_[c.real,c.imag];eps=1e-6
        J=np.array([(output(x+eps*np.eye(4)[j])-output(x-eps*np.eye(4)[j]))/(2*eps) for j in range(4)])
        v=(J@C@J.conj()).real
        self.assertLessEqual(math.sqrt(v),r['max_reading_relative_rms']*1.00001)
        vv=[]
        for freq in np.linspace(-2e6,2e6,401):
            HH=m.align.echo_response(freq)*np.exp(10j*np.pi*freq/m.FS)
            def out(x):
                gg=x[0]+1j*x[2];aa=(-(x[1]+1j*x[3])/gg).real
                return m.correction(freq,gg,aa,False)*HH
            jj=np.array([(out(x+eps*np.eye(4)[j])-out(x-eps*np.eye(4)[j]))/(2*eps) for j in range(4)])
            vv.append((jj@C@jj.conj()).real+abs(out(x))**2*5e-6)
        self.assertAlmostEqual(r['combined_with_fixture_relative_rms']**2,max(vv),places=14)
