"""Supplied-record evaluation and independent matrix/eigenvalue DOF verification."""
import unittest,sys,csv,io,math
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import metrology_models as m
class MetrologyRecords(unittest.TestCase):
    def test_published_data_and_reversal(self):
        data=Path(__file__).parents[1]/'book/data/metrology-phase.csv'
        self.assertEqual(data.read_text(),m.records_csv())
        rows=list(csv.DictReader(io.StringIO(data.read_text())));means=[]
        for sign in ['1','-1']:
            z=[float(r['phase_B_rad'])-float(r['phase_A_rad']) for r in rows if r['fixture_sign']==sign]
            self.assertEqual(len(z),100);means.append(sum(z)/100)
        r=m.metrology_case()
        self.assertLess(max(abs(a-b) for a,b in zip(means,r['raw_difference_means_rad'])),1e-12)
        self.assertAlmostEqual((means[0]+means[1])/2+.004-math.atan2(50*5,45*95+25),r['swap_phase_rad'],places=11)
        self.assertLess(r['combined_standard_uncertainty_rad'],.005)
        self.assertGreater(r['independent_refs_standard_uncertainty_rad'],.005)
    def test_matrix_propagation_and_quadratic_eigenvalues(self):
        for n,rho in [(7,.3),(100,.9),(100,.99)]:
            R=rho**abs(np.arange(n)[:,None]-np.arange(n)[None,:]);P=np.eye(n)-np.ones((n,n))/n
            self.assertAlmostEqual(np.sum(R)/n**2,m.mean_factor(n,rho),places=13)
            ev,U=np.linalg.eigh(R);root=(U*np.sqrt(ev))@U.T
            lam=np.linalg.eigvalsh(root@P@root)
            nu=lam.sum()**2/(lam@lam)
            self.assertAlmostEqual(nu,m.variance_dof(n,rho),places=9)
    def test_shared_reference_cancellation_is_not_independent(self):
        for sign,a,b in m.supplied_records():
            ref=np.linspace(-.2,.3,len(a))
            self.assertLess(np.max(abs(((b-ref)-(a-ref))-(b-a))),1e-15)
        # Unknown fixed correction terms survive averaging two configurations.
        r=m.metrology_case();uL=m.loading_uncertainty()
        want=r['repeat_standard_uncertainty_rad']**2/2+.001**2+uL**2+.0015**2
        self.assertAlmostEqual(r['swap_standard_uncertainty_rad']**2,want,places=15)
