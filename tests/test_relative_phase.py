"""Independent mathematical checks; executable with unittest or pytest."""
import cmath
import math
import random
import unittest
from coherent_receiver.relative_phase import (
    quadratic_spectrum, endpoint_psd, simpson, ou_covariance, ou_psd,
    linear_variance, observation_gain, fit_phase_delay, gaussian_accumulation,
    absolute_phase_variance,
)


class RelativePhaseTests(unittest.TestCase):
    def test_cross_spectral_order_against_constructed_sources(self):
        # x=a*u+b*v; compare physical coefficients with covariance propagation.
        a, b = 1+2j, -0.3+0.7j
        h = [0.6-0.4j, -1+0.2j]
        s = [[1, a.conjugate()], [a, abs(a)**2+abs(b)**2]]
        expected = abs(h[0]+h[1]*a)**2+abs(h[1]*b)**2
        self.assertAlmostEqual(quadratic_spectrum(h, s), expected, places=12)

    def test_delay_and_lowpass_limits(self):
        for f in [0, 3, 300, 10000]:
            dt = 1e-5
            self.assertAlmostEqual(endpoint_psd(f, dt, 1, 0),
                                   4*math.sin(math.pi*f*dt)**2, places=12)
            self.assertEqual(endpoint_psd(f, 0, 1, 0), 0)
            self.assertAlmostEqual(endpoint_psd(f, dt, 1, 0, 100),
                                   endpoint_psd(f, dt, 1, 0)/(1+(f/100)**2))

    def test_observation_covariance_spectrum(self):
        # Integrate Fourier transform of exponential covariance; unequal weights
        # exercise the sign/order without using the covariance implementation.
        ts, ws = [0, .1, .7], [-1, .3, .7]
        c = lambda t: ou_covariance(t, .04, .2)
        exact = linear_variance(ts, ws, c)
        values = [2*simpson(lambda f: ou_psd(f,.04,.2)*abs(observation_gain(f,ts,ws))**2,
                            0, 1000, n) for n in [32768, 65536]]
        self.assertLess(abs(values[1]-values[0]), 2e-6)
        # Finite 1/f² tail, bounded by (sum |w|)² times PSD tail.
        tail = 4*.04*(1-2/math.pi*math.atan(2*math.pi*1000*.2))
        self.assertLess(abs(exact-values[1]), tail+2e-6)

    def test_architecture_preference_reversal(self):
        def v(dt, local, shared=1e-9):
            return 2*simpson(lambda f: endpoint_psd(f,dt,1e-6,1e-8 if local else shared,
                                                   100 if local else None),1,10000)
        self.assertLess(v(1e-8,False),v(1e-8,True))
        self.assertGreater(v(1e-7,False,1e-7),v(1e-7,True))

    def test_symmetric_fit_holdout(self):
        fs = [9.99e8,1e9,1.001e9]
        ph = [.3-2*math.pi*(f-1e9)*2e-9 for f in fs]
        fm,p,delay = fit_phase_delay(fs,ph)
        self.assertAlmostEqual(delay,2e-9,places=18)
        self.assertAlmostEqual(p-2*math.pi*(1.0005e9-fm)*delay,
                               .3-2*math.pi*.0005e9*2e-9)
        with self.assertRaises(ValueError): fit_phase_delay([1,1],[0,0])

    def test_gaussian_simulation_and_distinct_statistics(self):
        rng = random.Random(20261029)
        times = [i*.1 for i in range(20)]
        w = [1/20]*20
        var, tc = .25, .2
        rho = math.exp(-.1/tc)
        c = lambda t: ou_covariance(t,var,tc)
        expected = gaussian_accumulation(times,w,c)
        samples, real_parts, residuals = [], [], []
        for _ in range(12000):
            phase = rng.gauss(0,math.sqrt(var))
            path = [phase]
            for _ in times[1:]:
                phase = rho*phase+rng.gauss(0,math.sqrt(var*(1-rho*rho)))
                path.append(phase)
            z = sum(cmath.exp(1j*p) for p in path)/20
            samples.append(abs(z)**2)
            real_parts.append(z.real)
            residuals.append(path[-1]-path[0])
        mean = sum(samples)/len(samples)
        se = math.sqrt(sum((x-mean)**2 for x in samples)/(len(samples)-1)/len(samples))
        self.assertLess(abs(mean-expected),5*se)
        self.assertLess(abs(sum(real_parts)/len(samples)-math.exp(-var/2)),.012)
        self.assertLess(abs(sum(x*x for x in residuals)/len(samples)-2*(var-c(1.9))),.025)
        # Frozen Gaussian phase has same marginal variance, but |average|²=1.
        self.assertAlmostEqual(gaussian_accumulation(times,w,lambda t:var),1)
        self.assertLess(expected, .95)

    def test_allocation_closed_integral_and_precision(self):
        # Integrate 2-2cos(2π f dt) analytically, avoiding the spectral code.
        dt, lo, hi = 1e-7, 1, 10000
        k = 2*math.pi*dt
        exact = 2e-6*(2*(hi-lo)-2*(math.sin(k*hi)-math.sin(k*lo))/k)
        numeric = 2*simpson(lambda f: endpoint_psd(f,dt,1e-6,0),lo,hi,8192)
        self.assertAlmostEqual(numeric,exact,delta=2e-17)
        # Near zero: direct sine is stable where subtractive closed form is not.
        dt = 1e-12
        small = 2e-6*(2*math.pi*dt)**2*(hi**3-lo**3)/3
        result = 2*simpson(lambda f: endpoint_psd(f,dt,1e-6,0),lo,hi)
        self.assertAlmostEqual(result/small,1,places=12)

    def test_residual_covariance_and_fixed_correction_identity(self):
        times = [0,.1,1,1.1]
        weights = [-.5,-.5,.5,.5]
        c = lambda t: ou_covariance(t,.01,.2)
        v = linear_variance(times,weights,c)
        direct = .01+c(.1)-c(1)-.5*(c(.9)+c(1.1))
        self.assertAlmostEqual(v,direct,places=14)
        # Scalar arithmetic identity, not an implemented calibration procedure.
        offset, wanted = .3,.04
        corrected = cmath.exp(1j*(offset+wanted))*cmath.exp(-1j*offset)
        self.assertAlmostEqual(cmath.phase(corrected),wanted)
        # A blind per-sample correction destroys exactly that wanted information.
        blind = cmath.exp(1j*(offset+wanted))*cmath.exp(-1j*(offset+wanted))
        self.assertAlmostEqual(cmath.phase(blind),0)

    def test_static_calibration_dc_rejection_and_absolute_covariance(self):
        times, weights = [0,.2,.5], [-.5,-.5,1]
        r=lambda t: ou_covariance(t,.04,.3)
        baseline=linear_variance(times,weights,r)
        # C=x(0)+epsilon: includes nonzero use/calibration covariance.
        vc=.04+.01
        cov_lc=sum(w*r(t) for t,w in zip(times,weights))
        residual=baseline+sum(weights)**2*vc-2*sum(weights)*cov_lc
        self.assertAlmostEqual(residual,baseline)
        self.assertEqual(observation_gain(0,times,weights),0)
        x=[.1,.2,-.4]
        self.assertAlmostEqual(sum(w*(v-3) for w,v in zip(weights,x)),
                               sum(w*v for w,v in zip(weights,x)))
        # Absolute phase at .5 s minus prior x(0)+epsilon has covariance.
        self.assertAlmostEqual(absolute_phase_variance(.04,vc,r(.5)),
                               2*.04*(1-math.exp(-.5/.3))+.01)
        self.assertAlmostEqual(absolute_phase_variance(.04,.01,.01),.03)

    def test_update_error_hold_spectrum_and_dc_rejection(self):
        # Independent holds straddling a boundary, unlike one static offset,
        # survive a two-sample difference. No stationarity is assumed here.
        self.assertEqual(linear_variance([0,1],[-1,1],lambda t: .01),0)
        self.assertEqual(linear_variance([0,1],[-1,1],
                                         lambda t: .01 if t==0 else 0),.02)
        P,v=2,.03
        for f in [0,.1,.5,1.3]:
            transformed=simpson(lambda lag:
                v*(1-abs(lag)/P)*math.cos(2*math.pi*f*lag),-P,P,8192)
            sinc=1 if f==0 else math.sin(math.pi*f*P)/(math.pi*f*P)
            self.assertAlmostEqual(transformed,v*P*sinc*sinc,delta=2e-13)

    def test_asymmetric_fit_reference_and_holdout(self):
        fs=[999e6,1000e6,1001.5e6]
        phases=[.3-2*math.pi*(f-1e9)*2e-9 for f in fs]
        fit=fit_phase_delay(fs,phases,state_ids=[7,7,7])
        self.assertAlmostEqual(fit.mean_frequency_hz, sum(fs)/3)
        self.assertAlmostEqual(fit.phase_at_mean_rad,
                               .3-2*math.pi*(fit.mean_frequency_hz-1e9)*2e-9)
        self.assertGreater(abs(fit.phase_at_mean_rad-.3),.002)
        self.assertAlmostEqual(fit.phase_at(1e9),.3)
        self.assertAlmostEqual(fit.phase_at(1000.5e6),.3-2*math.pi*.5e6*2e-9)
        self.assertAlmostEqual(fit.delay_s,2e-9,places=18)

    def test_wrapped_delay_ambiguity_and_unknown_state(self):
        fs=[999e6,1000e6,1001.5e6]
        phases=[.3-2*math.pi*(f-1e9)*2e-9 for f in fs]
        alternative=[p-2*math.pi*(f-1e9)*2e-6 for f,p in zip(fs,phases)]
        for p,q in zip(phases,alternative):
            self.assertLess(abs(cmath.exp(1j*p)-cmath.exp(1j*q)),1e-12)
        with self.assertRaises(ValueError):
            fit_phase_delay(fs,phases,unwrapped=False)
        for states in [[1,2,1],[None]*3,[1,1],[float("nan")]*3,[float("inf")]*3]:
            with self.assertRaises(ValueError):
                fit_phase_delay(fs,phases,state_ids=states)
        # Unknown per-tone offsets exactly absorb any proposed delay change.
        offsets=[q-p for p,q in zip(phases,alternative)]
        self.assertEqual([p+o for p,o in zip(phases,offsets)],alternative)
        # Reallocate receiver/fixture phase AND slope: the measurement is unchanged.
        receiver=[.3-2*math.pi*(f-1e9)*2e-9 for f in fs]
        fixture=[.1-2*math.pi*(f-1e9)*3e-9 for f in fs]
        measured=[r+c for r,c in zip(receiver,fixture)]
        shifted=[r+.2-2*math.pi*(f-1e9)*1e-9+
                 c-.2+2*math.pi*(f-1e9)*1e-9
                 for f,r,c in zip(fs,receiver,fixture)]
        for a,b in zip(measured,shifted): self.assertAlmostEqual(a,b)

    def test_unequal_endpoints_and_reference_branch_correlation(self):
        # r=u; v1=a*u+b*v; v2=c*u+d*v+e*w; unit independent sources.
        a,b,c,d,e=.2+.1j,.3,-.1+.4j,.1-.2j,.5
        rows=[[1,0,0],[a,b,0],[c,d,e]]
        S=[[sum(x*y.conjugate() for x,y in zip(map(complex,ri),map(complex,rj)))
            for rj in rows] for ri in rows]
        G1=cmath.exp(-.2j)/(1+.3j)
        G2=.8*cmath.exp(-.6j)/(1+.8j)
        result=quadratic_spectrum([G2-G1,-1,1],S)
        expected=abs(G2-G1+c-a)**2+abs(d-b)**2+abs(e)**2
        self.assertAlmostEqual(result,expected)
        # Demonstrate the cross term explicitly; zeroing it changes prediction.
        branch=abs(c-a)**2+abs(d-b)**2+abs(e)**2
        cross=2*((G2-G1)*(c-a).conjugate()).real
        self.assertAlmostEqual(result,abs(G2-G1)**2+branch+cross)

    def test_complex_filter_phase_bridge(self):
        h=[.5+.2j,.5-.2j]  # sum=1 but complex impulse causes AM-to-PM
        def error(eps):
            alpha=[eps,-eps]
            phi=[.3*eps,-.4*eps]
            exact=sum(g*(1+a)*cmath.exp(1j*p) for g,a,p in zip(h,alpha,phi))
            first=sum(g.imag*a+g.real*p for g,a,p in zip(h,alpha,phi))
            naive=sum(g.real*p for g,p in zip(h,phi))
            self.assertGreater(abs(first-naive),.3*eps)
            return abs(cmath.phase(exact)-first)
        self.assertLess(error(.001),error(.01)/50)

    def test_covariance_sum_condition_for_mean(self):
        # Nonzero pair correlations cancel in aggregate; independence is not needed.
        S=[[1,.2,-.1],[.2,1,-.1],[-.1,-.1,1]]
        self.assertAlmostEqual(quadratic_spectrum([1/3]*3,S),1/3)
        # Pairwise bounds do not certify a larger matrix.
        invalid=[[1,-.9,-.9],[-.9,1,-.9],[-.9,-.9,1]]
        self.assertEqual(quadratic_spectrum([1,0,0],invalid),1)
        with self.assertRaises(ValueError): quadratic_spectrum([1,1,1],invalid)

    def test_malformed_and_nonfinite_inputs(self):
        for bad in [float('nan'),float('inf'),-float('inf')]:
            calls=[
                lambda: endpoint_psd(bad,1,1,1),
                lambda: endpoint_psd(1,bad,1,1),
                lambda: endpoint_psd(1,1,bad,1),
                lambda: endpoint_psd(1,1,1,bad),
                lambda: endpoint_psd(1,1,1,1,bad),
                lambda: simpson(lambda f: bad,0,1),
                lambda: simpson(lambda f: f,0,bad),
                lambda: ou_covariance(bad,1,1),
                lambda: ou_psd(1,bad,1),
                lambda: ou_psd(1,1,bad),
                lambda: linear_variance([0],[bad],lambda t:1),
                lambda: linear_variance([0],[1],lambda t:bad),
                lambda: observation_gain(1,[bad],[1]),
                lambda: observation_gain(bad,[0],[1]),
                lambda: fit_phase_delay([0,1],[0,bad]),
                lambda: fit_phase_delay([0,bad],[0,1]),
                lambda: gaussian_accumulation([0],[1],lambda t:bad),
                lambda: quadratic_spectrum([bad],[[1]]),
                lambda: quadratic_spectrum([1],[[complex(1,bad)]]),
                lambda: absolute_phase_variance(1,1,bad),
                lambda: fit_phase_delay([0,1],[0,1]).phase_at(bad)]
            for call in calls:
                with self.subTest(value=bad,call=call):
                    with self.assertRaises(ValueError): call()
        calls=[
            lambda: observation_gain(1,[0,1],[1]),
            lambda: gaussian_accumulation([0],[1,1],lambda t:1),
            lambda: linear_variance([],[],lambda t:1),
            lambda: fit_phase_delay([0,1],[0]),
            lambda: quadratic_spectrum([1,1],[[1]]),
            lambda: quadratic_spectrum([1,1],[[1,1j],[1j,1]]),
            lambda: endpoint_psd(1,1,-1,1),
            lambda: endpoint_psd(1,1,1,1,0),
            lambda: ou_covariance(0,-1,1),
            lambda: ou_psd(0,1,0),
            lambda: absolute_phase_variance(1,1,2),
            lambda: simpson(lambda t:t,0,1,2.5)]
        for call in calls:
            with self.assertRaises(ValueError): call()

    def test_snapshot_precision_and_timing(self):
        cases=[(1e-8,1e-9,None,.01,.0253528377804),
               (1e-7,1e-8,100,.01,.0801727056214),
               (1e-7,1e-8,100,.05,.0343788232821)]
        for dt,b,corner,T,sd in cases:
            integrand=lambda f: endpoint_psd(f,dt,1e-6,b,corner)*(
                math.sin(math.pi*f*T)/(math.pi*f*T))**2
            vs=[2*simpson(integrand,1,10000,n) for n in [65536,131072]]
            self.assertLess(abs(vs[-1]-vs[0]),1e-13)
            self.assertAlmostEqual(math.sqrt(vs[-1])*180/math.pi,sd,places=10)
        # The delivered local 10 ms prediction violates the snapshot allocation.
        self.assertGreater(cases[1][-1],.04)
        for T in [.01,.05]:
            period=.5/.216-(.75*T+.1)
            self.assertAlmostEqual(.216*(period+.75*T+.1),.5)
            self.assertLess(.216*(2+.75*T+.1),.5)

    def test_rectangular_snapshot_spectrum_against_time_covariance(self):
        density,lo,hi=2e-8,1,10000
        def covariance(lag):
            if lag==0: return 2*density*(hi-lo)
            return density*(math.sin(2*math.pi*hi*lag)-
                            math.sin(2*math.pi*lo*lag))/(math.pi*lag)
        for T in [.01,.05]:
            spectral=2*simpson(lambda f: density*(
                math.sin(math.pi*f*T)/(math.pi*f*T))**2,lo,hi,131072)
            # Integrate over a rectangle by lag: independent time-domain form.
            temporal=2/T**2*simpson(lambda u:(T-u)*covariance(u),0,T,65536)
            self.assertAlmostEqual(spectral,temporal,delta=1e-15)

    def test_fixed_lo_vs_fixed_if_phase_slope(self):
        # A nondispersive waveform path, including mixer subtraction.
        f0,l0=1e9,990e6
        rf,fixture,if_delay,lo=2e-9,3e-9,4e-9,1e-9
        fs=[999e6,1000e6,1001.5e6]
        def phase(F,L):
            return (.3-2*math.pi*(F-f0)*(rf+fixture)
                    +2*math.pi*(L-l0)*lo
                    -2*math.pi*((F-L)-(f0-l0))*if_delay)
        fixed_lo=fit_phase_delay(fs,[phase(f,l0) for f in fs])
        fixed_if=fit_phase_delay(fs,[phase(f,l0+f-f0) for f in fs])
        self.assertAlmostEqual(fixed_lo.delay_s,rf+fixture+if_delay,places=18)
        self.assertAlmostEqual(fixed_if.delay_s,rf+fixture-lo,places=18)
        self.assertAlmostEqual(fixed_lo.phase_at(f0),.3)
        self.assertAlmostEqual(fixed_if.phase_at(f0),.3)
