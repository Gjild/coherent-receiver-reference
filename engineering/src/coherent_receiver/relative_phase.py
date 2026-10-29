"""Illustrative phase mathematics; no hardware validation. Two-sided spectra.

Input finiteness/shape checks do not validate physical models. A spectral matrix
must be Hermitian PSD at every frequency, obey real-process spectral symmetry
where applicable, and define convergent observation integrals. Its full physical
validity is a caller precondition; a single quadratic form cannot establish it.
"""
import cmath
import math
from typing import NamedTuple


def _real(value):
    try:
        value = float(value)
    except (ValueError, TypeError, OverflowError) as exc:
        raise ValueError('finite real value required') from exc
    if not math.isfinite(value):
        raise ValueError('finite real value required')
    return value


def _complex(value):
    try:
        value = complex(value)
    except (ValueError, TypeError, OverflowError) as exc:
        raise ValueError('finite complex value required') from exc
    if not (math.isfinite(value.real) and math.isfinite(value.imag)):
        raise ValueError('finite complex value required')
    return value


def _sequence(values, convert=_real):
    try:
        result = [convert(v) for v in values]
    except TypeError as exc:
        raise ValueError('sequence required') from exc
    if not result:
        raise ValueError('nonempty sequence required')
    return result


def _paired(times, weights):
    times, weights = _sequence(times), _sequence(weights)
    if len(times) != len(weights):
        raise ValueError('paired sequences must have equal lengths')
    return times, weights


def quadratic_spectrum(h, s):
    """h S h^H. Full Hermitian PSD matrix validity is a caller precondition.

    Shape/finiteness/Hermitian and output-sign checks catch some violations;
    neither these checks nor all pairwise bounds certify PSD for dimension >2.
    """
    h = _sequence(h, _complex)
    try:
        s = [_sequence(row, _complex) for row in s]
    except TypeError as exc:
        raise ValueError('matrix required') from exc
    if len(s) != len(h) or any(len(row) != len(h) for row in s):
        raise ValueError('incompatible dimensions')
    scale_s = max(abs(v) for row in s for v in row)
    for i in range(len(h)):
        if s[i][i].real < 0:
            raise ValueError('negative diagonal spectrum')
        for j in range(len(h)):
            if abs(s[i][j]-s[j][i].conjugate()) > 1e-12*max(scale_s,1e-300):
                raise ValueError('non-Hermitian spectrum')
    terms = [h[i]*s[i][j]*h[j].conjugate()
             for i in range(len(h)) for j in range(len(h))]
    value = _complex(sum(terms))
    scale = sum(abs(v) for v in terms)
    if abs(value.imag) > 1e-12*max(scale,1e-300):
        raise ValueError('spectrum is not real')
    if value.real < -1e-12*max(scale,1e-300):
        raise ValueError('negative output spectrum')
    return max(0.0,value.real)


def endpoint_psd(f, mismatch_s, common_psd, branch_psd, corner_hz=None):
    """Restricted equal-endpoint/pure-delay case; independent output branches.

    corner=None: shared LO; finite positive corner: equal lowpass reference
    transfer. General unequal/correlated paths use quadratic_spectrum instead.
    """
    f, mismatch_s = _real(f), _real(mismatch_s)
    common_psd, branch_psd = _real(common_psd), _real(branch_psd)
    if min(common_psd,branch_psd) < 0:
        raise ValueError('nonnegative density required')
    if corner_hz is not None:
        corner_hz = _real(corner_hz)
        if corner_hz <= 0:
            raise ValueError('positive corner required')
    g = 1 if corner_hz is None else 1/(1+1j*f/corner_hz)
    return _real(abs(g*(1-cmath.exp(-2j*math.pi*f*mismatch_s)))**2*common_psd+2*branch_psd)


def simpson(func, low, high, intervals=4096):
    low, high = _real(low), _real(high)
    if (isinstance(intervals,bool) or not isinstance(intervals,int)
            or intervals < 2 or intervals % 2 or not low < high):
        raise ValueError('ordered bounds and positive even integer intervals required')
    step = (high-low)/intervals
    total = _real(func(low))+_real(func(high))
    total += sum((4 if k%2 else 2)*_real(func(low+k*step)) for k in range(1,intervals))
    return _real(total*step/3)


def ou_covariance(lag_s, variance, correlation_s):
    """Declared exponential covariance; Gaussianity is a separate assumption."""
    lag_s, variance, correlation_s = map(_real,(lag_s,variance,correlation_s))
    if variance < 0 or correlation_s <= 0:
        raise ValueError('nonnegative variance and positive correlation time required')
    return variance*math.exp(-abs(lag_s)/correlation_s)


def ou_psd(f, variance, correlation_s):
    f, variance, correlation_s = map(_real,(f,variance,correlation_s))
    if variance < 0 or correlation_s <= 0:
        raise ValueError('nonnegative variance and positive correlation time required')
    return 2*variance*correlation_s/(1+(2*math.pi*f*correlation_s)**2)


def linear_variance(times, weights, covariance):
    """Real observation covariance; validity of supplied kernel is precondition."""
    times, weights = _paired(times,weights)
    return _real(sum(a*b*_real(covariance(t-u)) for t,a in zip(times,weights)
                     for u,b in zip(times,weights)))


def observation_gain(f, times, weights):
    f = _real(f)
    times, weights = _paired(times,weights)
    return _complex(sum(a*cmath.exp(2j*math.pi*f*t) for t,a in zip(times,weights)))


def absolute_phase_variance(signal_variance, calibration_variance, covariance=0):
    """Var(X-C), for a declared absolute residual observation, not band variance."""
    vx, vc, cov = map(_real,(signal_variance,calibration_variance,covariance))
    if vx < 0 or vc < 0 or abs(cov) > math.sqrt(vx)*math.sqrt(vc):
        raise ValueError('invalid two-variable covariance')
    return _real(vx+vc-2*cov)


class PhaseDelayFit(NamedTuple):
    mean_frequency_hz: float
    phase_at_mean_rad: float
    delay_s: float

    def phase_at(self, reference_hz):
        """Locally unwrapped fitted phase at the explicitly requested frequency."""
        return _real(self.phase_at_mean_rad-2*math.pi*
                     (_real(reference_hz)-self.mean_frequency_hz)*self.delay_s)


def fit_phase_delay(frequencies, phases, *, unwrapped=True, state_ids=None):
    """OLS phase = b_mean - 2π(f-fmean) delay; returns PhaseDelayFit.

    Input phases must already be locally unwrapped in one known common phase
    state, with fixture correction or its ambiguity explicitly retained. No wrap
    resolution, hidden state detection, calibration algorithm or uncertainty fit.
    False unwrapped or supplied missing/mixed state IDs are rejected. Omitting
    state_ids asserts a common state; this cannot be inferred from phase data.
    """
    frequencies, phases = _paired(frequencies,phases)
    if len(phases) < 2 or unwrapped is not True:
        raise ValueError('need at least two locally unwrapped common-state phases')
    if state_ids is not None:
        try:
            state_ids = list(state_ids)
        except TypeError as exc:
            raise ValueError('state sequence required') from exc
        for state in state_ids:
            if isinstance(state,(int,float,complex)):
                _complex(state)
        if (len(state_ids) != len(phases) or any(v is None for v in state_ids)
                or any(v != state_ids[0] for v in state_ids)):
            raise ValueError('known common phase state required')
    fm, pm = sum(frequencies)/len(frequencies), sum(phases)/len(phases)
    denominator = sum((f-fm)**2 for f in frequencies)
    if denominator == 0:
        raise ValueError('delay unobservable at a single frequency')
    slope = sum((f-fm)*(p-pm) for f,p in zip(frequencies,phases))/denominator
    return PhaseDelayFit(_real(fm),_real(pm),_real(-slope/(2*math.pi)))


def gaussian_accumulation(times, weights, covariance):
    """E|sum w exp(j phi)|²; real jointly Gaussian stationary phase is assumed.

    Valid covariance is a precondition; finiteness checks do not establish it.
    """
    times, weights = _paired(times,weights)
    r0 = _real(covariance(0))
    return _real(sum(a*b*math.exp(-(r0-_real(covariance(t-u))))
                     for t,a in zip(times,weights) for u,b in zip(times,weights)))
