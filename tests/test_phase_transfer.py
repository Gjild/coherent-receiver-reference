import numpy as np
import pytest
from coherent_receiver.phase_transfer import (
    differential_delay_magnitude_squared as exact,
    small_offset_approximation as approx,
)


def test_identical_paths_have_no_differential_transfer():
    np.testing.assert_allclose(exact(np.array([0.0, 1.0, 100.0]), 0.0), 0.0)


def test_periodic_and_bounded():
    result = exact(np.linspace(-2, 2, 1001), 1.0)
    assert np.all(result >= 0)
    assert np.all(result <= 4.0 + 1e-14)
    assert exact(0.5, 1.0) == pytest.approx(4.0)
    assert exact(1.0, 1.0) == pytest.approx(0.0, abs=1e-29)


def test_small_offset_limit():
    x = np.array([1e-6, 1e-5, 1e-4])
    np.testing.assert_allclose(exact(x, 1.0), approx(x, 1.0), rtol=1e-7)


def test_nonfinite_rejected():
    with pytest.raises(ValueError): exact(float('nan'), 1.0)
    with pytest.raises(ValueError): approx(1.0, float('inf'))
