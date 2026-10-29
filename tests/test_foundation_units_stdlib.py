"""Analytical consistency checks; no physical validation. Run with unittest."""
import cmath
import math
import unittest


class ScalarPhaseChecks(unittest.TestCase):
    def test_record_average_against_exact_ensemble(self):
        values = [-1, 1]
        means = [(a+b)/2 for a in values for b in values]
        self.assertAlmostEqual(sum(x*x for x in means)/4, 0.5)
        self.assertEqual(sum(x*x for x in values)/2, 1)
        self.assertAlmostEqual(math.sqrt(.012**2/100+.016**2), .016044936896105262, places=10)

    def test_proper_is_not_circular(self):
        z = [1, 1j, -1, -1j]
        self.assertAlmostEqual(abs(sum(x*x for x in z)/4), 0)
        self.assertGreater(min(abs(cmath.exp(1j*math.pi/4)-x) for x in z), .7)

    def test_phase_linearization_error_scales_quadratically(self):
        def error(e):
            return abs(cmath.phase(1+e*(.7+1j))-e)
        self.assertGreater(error(.01)/error(.005), 3.9)
        self.assertLess(error(.01)/error(.005), 4.1)
        self.assertGreater(abs(cmath.phase(1+1j)-1), .2)

    def test_uncorrelated_dependent_counterexample(self):
        x = [-1, 0, 1]
        self.assertEqual(sum(t**3 for t in x), 0)
        self.assertEqual([t*t for t in x], [1, 0, 1])

    def test_dependent_rotation_and_alternating_process(self):
        errors = [cmath.phase(1+.01*cmath.exp(1j*t)*cmath.exp(-1j*t))
                  for t in [0, .7, 1.2, 3.5]]
        self.assertLess(max(abs(e) for e in errors), 1e-15)
        for n in [4, 5]:
            mean = sum((-1)**k for k in range(1, n+1))/n
            self.assertAlmostEqual(mean**2, 0 if n % 2 == 0 else 1/n**2)


class ObservationChecks(unittest.TestCase):
    def test_time_spectral_box_average(self):
        # Independent quadratures: triangular covariance integral vs spectrum.
        sigma2, tc, duration = .0004, 1., 10.
        n = 40000
        dt = duration/n
        time = 2/duration**2 * sum((duration-(k+.5)*dt)*sigma2*
                                  math.exp(-(k+.5)*dt/tc)*dt for k in range(n))
        df = 100/n
        spectral = 0.
        for k in range(n):
            f = (k+.5)*df
            window = math.sin(math.pi*f*duration)/(math.pi*f*duration)
            spectral += 2*(2*sigma2*tc/(1+(2*math.pi*f*tc)**2))*window**2*df
        exact = 2*sigma2/duration**2*(duration*tc-tc**2*(1-math.exp(-duration/tc)))
        self.assertAlmostEqual(time/exact, 1, places=7)
        self.assertAlmostEqual(spectral/exact, 1, places=6)

    def test_delay_and_non_gaussian_coherence(self):
        f, delay = 1000., .0001
        direct = abs(cmath.exp(-2j*math.pi*f*delay)-1)**2
        self.assertAlmostEqual(direct, .3819660112501051)
        self.assertAlmostEqual(direct, 4*math.sin(math.pi*f*delay)**2)
        a = 1.
        discrete = (cmath.exp(1j*a)+cmath.exp(-1j*a))/2
        self.assertGreater(abs(discrete-math.exp(-a*a/2)), .06)

    def test_sample_variance_bias_exact_discrete_ensemble(self):
        import itertools
        records = list(itertools.product([-1., 1.], repeat=4))
        estimates = [sum((x-sum(r)/4)**2 for x in r)/4 for r in records]
        self.assertAlmostEqual(sum(estimates)/len(estimates), 1-1/4)


class CoherenceCorrectionChecks(unittest.TestCase):
    def test_gaussian_integration_power_and_phase_filter_counterexample(self):
        n, duration = 20000, 10.
        du = duration/n
        power = 2/duration**2*sum((duration-(k+.5)*du)*
            math.exp(-(1-math.exp(-(k+.5)*du)))*du for k in range(n))
        self.assertAlmostEqual(power, .4564101278443839, places=7)
        self.assertGreater(abs(power-math.exp(-.18000090799859525)), .37)
        self.assertGreater(abs(cmath.phase(.75+.25j)-math.pi/8), .07)


if __name__ == '__main__':
    unittest.main()
