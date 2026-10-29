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


if __name__ == '__main__':
    unittest.main()
