"""Mathematical demonstration: differential transfer of a common process.

This is an idealized linear pure-delay example. It is NOT a complete physical
receiver, phase-noise prediction, or validated engineering method.
"""
from __future__ import annotations
import numpy as np


def differential_delay_magnitude_squared(offset_hz, delay_difference_s):
    """Return |exp(-j2πfτ1)-exp(-j2πfτ2)|² for pure delays.

    Parameters
    ----------
    offset_hz: scalar or array; offset frequency in Hz.
    delay_difference_s: scalar; τ1-τ2 in seconds.

    No assumptions about oscillator noise PSD, phase variance or observation
    operators are implied by this algebraic transfer magnitude.
    """
    f = np.asarray(offset_hz, dtype=float)
    dt = float(delay_difference_s)
    if not np.all(np.isfinite(f)) or not np.isfinite(dt):
        raise ValueError("Inputs must be finite")
    return 4.0 * np.sin(np.pi * f * dt) ** 2


def small_offset_approximation(offset_hz, delay_difference_s):
    """Leading-order approximation for |f Δτ| << 1 (not globally valid)."""
    f = np.asarray(offset_hz, dtype=float)
    dt = float(delay_difference_s)
    if not np.all(np.isfinite(f)) or not np.isfinite(dt):
        raise ValueError("Inputs must be finite")
    return (2.0 * np.pi * f * dt) ** 2
