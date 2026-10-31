"""Distinct waveform/source/history checks for synthetic subsystem treatments."""
import unittest,sys,math,cmath
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
import subsystem_models as m


class AnalogModels(unittest.TestCase):
    def test_complete_real_waveform_peak_and_thresholds(self):
        for rejection in [43,46,49,52]:
            # Normalize real output volts by sqrt(2R*1mW).
            weak=10**(-56/20);block=10**((26-rejection)/20)
            wave=[weak*math.cos(2*math.pi*100*t/10000)+block*(math.cos(2*math.pi*101*t/10000)+math.cos(2*math.pi*102*t/10000)) for t in range(10001)]
            actual=20*math.log10(max(map(abs,wave)))
            self.assertAlmostEqual(actual,m.analog_case(rejection)['peak'],places=12)
        for limit in [-10,-13,-16]:
            rejection=26-20*math.log10((10**(limit/20)-10**(-56/20))/2)
            self.assertAlmostEqual(m.analog_case(rejection)['peak'],limit,places=12)

    def test_noise_by_output_referred_source_sum(self):
        # Each independent matched source contributes normalized kT0 at its port.
        for order in ['early','late']:
            stages=[(10**(-.2),10**.2),(100,10**.2)]
            if order=='late':stages.reverse()
            stages += [(10**.6,10**.8),(100,10**.6)]
            signal_gain=math.prod(g for g,f in stages)
            output=signal_gain
            for i,(g,f) in enumerate(stages):output+=(f-1)*math.prod(gg for gg,ff in stages[i:])
            result=10*math.log10(output/signal_gain)
            self.assertAlmostEqual(result,m.analog_case()[order+'_nf'],places=12)

    def test_real_cubic_and_complex_cascade(self):
        # Real polynomial product coefficient, independently by Fourier projection.
        n=8192;A=.03;a1=2.;a3=-.5
        vals=[]
        for i in range(n):
            t=i/n;x=A*(math.cos(2*math.pi*11*t)+math.cos(2*math.pi*12*t));vals.append(a1*x+a3*x**3)
        product=2*sum(y*cmath.exp(-2j*math.pi*10*i/n) for i,y in enumerate(vals))/n
        self.assertAlmostEqual(product/(.75*a3*A**3),1,places=9)
        weak=10**(-102/20);block=10**(-69/20);values=[]
        for i in range(n):
            z=weak+block*(cmath.exp(2j*math.pi*i/n)+cmath.exp(4j*math.pi*i/n))
            for gain,intercept in [(20,0),(6,20),(20,25)]:
                a=10**(gain/20);z=a*z*(1+1j*abs(z)**2/10**(intercept/10))
            values.append(z)
        actual=sum(values)/n/(weak*10**(46/20))-1
        c=m.analog_case();cross=sum(4*10**((p-ip)/10) for p,ip in zip(c['blocker_inputs'],[0,20,25]))
        self_term=sum(10**((p-ip)/10) for p,ip in zip(c['wanted_inputs'],[0,20,25]))
        self.assertLess(abs(actual),c['phasor_radius']+cross+self_term+1e-10)
        self.assertAlmostEqual(actual.imag,c['phasor_radius']+cross+self_term,delta=1e-10)

    def test_recovery_from_time_integration(self):
        # Explicit Euler is independent of closed-form load/discharge formulas.
        dt=.0005;q=0.
        for _ in range(round(10/dt)):q+=dt*(1-q)/5
        self.assertLess(abs(q-(1-math.exp(-2))),1.4e-5)
        for _ in range(round(176/dt)):q-=dt*q/40
        self.assertLess(abs(q-(1-math.exp(-2))*math.exp(-176/40)),4e-7)
        self.assertLess(8*q,.1)
        self.assertGreater(40*math.log(80),169)
        self.assertGreater(80*math.log(80),180)

    def test_policy_visibility_history_and_fault_gates(self):
        t=m.policy_trace();self.assertEqual(next(x['t'] for x in t if x['state']=='H'),30)
        self.assertEqual(next(x['t'] for x in t if x['valid']),186)
        self.assertTrue(all(x['phase']<=.1 and x['amplitude']<=.01 and x['wanted']>=-60 for x in t if x['valid']))
        self.assertFalse(any(x['valid'] for x in m.policy_trace(46)))
        p=m.GainPolicy();self.assertFalse(p.step(0,calibrated=False)['valid'])
        self.assertFalse(p.step(1,qualified=False)['valid']);self.assertTrue(p.step(1000)['fault'])
        with self.assertRaises(ValueError):p.step(999)
        # Return dwell must restart after a threshold excursion, not only a pulse.
        p=m.GainPolicy(state='L')
        for i in range(39):r=p.step(i,peak_h=-15 if i<19 else -17)
        self.assertEqual(r['state'],'L');self.assertEqual(p.step(39,peak_h=-17)['state'],'H')
        # Renewed exposure invalidates a previously valid observation.
        p=m.GainPolicy()
        for i in range(241):r=p.step(i,pulse=(i<10 or 200<=i<210))
        self.assertFalse(r['valid']);self.assertGreater(r['phase'],.1)

    def test_49db_curve_geometry_by_power_ratios(self):
        import xml.etree.ElementTree as E,re
        root=E.parse(Path(__file__).parents[1]/'book/figures/analog-blocker-region.svg').getroot()
        paths=[p for p in root if p.attrib.get('stroke-width')=='2.8' and len(re.findall('[ML]',p.attrib.get('d','')))>20]
        points=re.findall(r'[ML]([\d.-]+),([\d.-]+)',paths[0].attrib['d'])
        for xx,yy in points[::13]:
            xx=float(xx);yy=float(yy);a=40+(xx-100)*12/780
            pk=10*math.log10((2*math.sqrt(10**((26-a)/10))+math.sqrt(10**(-56/10)))**2)
            self.assertAlmostEqual(yy,167+195-195*(pk+21)/14,delta=.000501)


class SynthesisModels(unittest.TestCase):
    def test_pi_loop_by_differential_equation(self):
        # RK4 actual phase/frequency control actions, independently of H/E code.
        fn=20000.;w=2*math.pi*fn;z=2**-.5;dt=1e-8;phase=0.;integ=0.
        def rhs(x,u):return 2*z*w*(1-x)+u,w*w*(1-x)
        for i in range(12000):
            a,b=rhs(phase,integ);c,d=rhs(phase+a*dt/2,integ+b*dt/2)
            e,f=rhs(phase+c*dt/2,integ+d*dt/2);g,h=rhs(phase+e*dt,integ+f*dt)
            phase+=dt*(a+2*c+2*e+g)/6;integ+=dt*(b+2*d+2*f+h)/6
            if i in [999,3999,9999]:
                t=(i+1)*dt;expected=math.exp(-z*w*t)*(math.cos(w*z*t)-math.sin(w*z*t))
                self.assertAlmostEqual(1-phase,expected,delta=2e-12)
        for f in [0,100,20000,1e6]:
            H,E=m.pll_transfer(f);s=2j*math.pi*f
            if f:
                L=(2*z*w*s+w*w)/(s*s)
                self.assertAlmostEqual(H,L/(1+L),places=13)
            self.assertAlmostEqual(H+E,1,places=13)

    def test_noise_integral_by_rational_spectrum(self):
        from visual_foundations import quad
        for fn in [2000,10000,20000,40000]:
            def ps(f):
                denom=fn**4+f**4
                return 102**2*1e-16*(fn**4+2*fn*fn*f*f)/denom+1e-3*f**4/((f*f+1)*denom)
            bands=[10,100,1000,10000,100000,1e6]
            value=2*sum(quad(ps,a,b,4096) for a,b in zip(bands,bands[1:]))
            self.assertAlmostEqual(value/m.pll_case(fn)['variance'],1,places=9)
        self.assertLess(m.pll_case()['sigma_degrees'],.03)
        self.assertGreater(m.pll_case(40000)['sigma_degrees'],.03)
        self.assertGreater(m.pll_case(10000)['wait_us'],100)

    def test_real_mixer_spur_and_witness_blindness(self):
        n=65536;beta=2e-4;converted=0j;reading=0.
        for i in range(n):
            t=i/n;pm=beta*math.cos(2*math.pi*t)
            rf=math.cos(2*math.pi*101*t);lo=math.cos(2*math.pi*102*t+pm)
            converted+=2*rf*lo*cmath.exp(-4j*math.pi*t)*2/n
            reading+=(pm-pm)**2
        self.assertAlmostEqual(abs(converted)/(beta/2),1,places=7)
        self.assertEqual(reading,0)
        self.assertGreater(m.lo_contract()['phase_spur_degrees'],.7)
        limited=m.lo_contract(beta=m.lo_contract()['beta_limit'])
        self.assertAlmostEqual(limited['phase_spur_degrees'],.02,places=13)

    def test_window_difference_source_energy(self):
        # White source mapped through actual difference of shifted rectangles.
        n=1000;shift=3;dt=.002/n;S=5e-12
        weights=[(int(shift<=i<shift+n)-int(0<=i<n))/n for i in range(n+shift)]
        actual=sum(x*x for x in weights)*S/dt
        self.assertAlmostEqual(actual/(2*S*(shift*dt)/.002**2),1,places=13)
        self.assertLess(m.lo_contract()['endpoint'],m.lo_contract()['mask'])
        bad=m.lo_contract(1e-10);self.assertGreater(bad['endpoint'],bad['mask'])
        self.assertLess(bad['average_sigma_degrees'],.02)
        # Global source-density bound used by the continuous-time window bound.
        for i in range(4000):
            f=10**(-3+11*i/3999)
            self.assertLessEqual(m.pll_density(f)+ (2e-12 if f<=20e6 else 0),5e-12)

    def test_loading_thermal_and_power_interfaces(self):
        r=.001
        maximum=max(abs(cmath.phase(1+r*cmath.exp(2j*math.pi*i/30000))) for i in range(30001))
        self.assertAlmostEqual(maximum,math.asin(r),delta=1e-11)
        delay=.08e-12*2;carrier=1.02e9
        self.assertAlmostEqual(math.degrees(cmath.phase(cmath.exp(-2j*math.pi*carrier*delay))),-.058752,places=12)
        required=sum(1e-3/10**(-6/10) for _ in range(3))/10**(-2/10)
        self.assertAlmostEqual(required,.0189287203344058,places=15)
        # Controller gains and delay budget recovered directly from open-loop unity.
        w=2*math.pi*20000;z=2**-.5;kv=2*math.pi*20e6;N=102
        kp=2*z*w*N/kv;ki=w*w*N/kv;wc=w*math.sqrt(1+math.sqrt(2))
        L=kv/N*(kp+ki/(1j*wc))/(1j*wc)
        self.assertAlmostEqual(abs(L),1,places=13)
        tau=(math.pi+cmath.phase(L)-math.pi/4)/wc
        self.assertAlmostEqual(tau*1e6,1.83515533276,places=10)
