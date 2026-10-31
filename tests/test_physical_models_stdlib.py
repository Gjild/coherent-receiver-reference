"""Independent physical-model algebra, numerical limits and SVG coordinate checks.

These checks establish consistency under declared models, not hardware validity.
"""
import cmath
import math
import unittest
from pathlib import Path
import xml.etree.ElementTree as ET


class FieldModels(unittest.TestCase):
    def test_geometry_from_exact_spherical_distance(self):
        # Exact range difference converges to the sourceward projection.
        c=3e8; fc=1e9; b=.15; ellx=.5
        for R in (100.,1000.):
            r2=math.sqrt(R*R-2*R*ellx*b+b*b)
            delay=(r2-R)/c
            self.assertLess(abs(delay-(-ellx*b/c)),b*b/(2*R*c)*1.01)
        self.assertAlmostEqual(-2*math.pi*fc*(-ellx*b/c),math.pi/2)
        # Receding round-trip path: differentiate complex phase numerically.
        phase=lambda R:cmath.exp(-4j*math.pi*fc*R/c)
        step=1e-5
        self.assertAlmostEqual(cmath.phase(phase(10+step)/phase(10))/step,
                               -4*math.pi*fc/c,places=7)

    def test_loaded_voltage_and_polarization_basis(self):
        E=[1e-3/math.sqrt(2)]*2; h=[.1,.01j]
        v=sum(a*b for a,b in zip(h,E))*.5
        v1=.1*E[0]*.5
        self.assertAlmostEqual((abs(v)**2/(2*50))/12.625e-12,1,places=12)
        self.assertAlmostEqual(math.degrees(cmath.phase(v/v1)),5.7105931375,places=9)
        self.assertAlmostEqual(20*math.log10(abs(v/v1)),.0432137378,places=9)
        a=.73; U=[[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]]
        hp=[sum(h[i]*U[i][j] for i in range(2)) for j in range(2)]
        Ep=[sum(U[i][j]*E[i] for i in range(2)) for j in range(2)]
        self.assertAlmostEqual(sum(hp[i]*Ep[i] for i in range(2))/(2*v),1,places=12)

    def test_curve_coordinates_against_complex_voltage(self):
        # Read blue phase curve and invert the SVG axis transform. Reference
        # values come from complex loaded voltages, not the generator's atan.
        root=ET.parse(Path(__file__).parents[1]/'book/figures/polarization-error.svg').getroot()
        paths=[p for p in root.findall('{http://www.w3.org/2000/svg}path')
               if p.attrib.get('stroke')=='#125b86']
        data=[p for p in paths if len(p.attrib['d'])>1000][0].attrib['d'].split()
        for token in data[::30]:
            px,py=map(float,token[1:].split(','))
            psi=-60+(px-100)/780*120
            y=11-(py-162)/195*22
            z2=math.cos(math.radians(psi))+1j*.1*math.sin(math.radians(psi))
            self.assertAlmostEqual(y,math.degrees(cmath.phase(z2)),delta=.0001)

    def test_sensing_linearization_and_ambiguity(self):
        k=4*math.pi*1e10/3e8
        self.assertAlmostEqual(-k*.0001,-.0418879020479)
        self.assertAlmostEqual(cmath.exp(-1j*k*(1+.0001)),
                               cmath.exp(-1j*k*(1.0001*1)))
        self.assertAlmostEqual(cmath.exp(-1j*k*.015),1)


class NoiseModels(unittest.TestCase):
    def test_thermal_power_real_and_envelope_domains(self):
        k=1.380649e-23;T=290;R=50;B=1e5
        real_s=2*k*T*R*(.5**2)
        real_power=2*B*real_s/R
        envelope_power=B*(4*real_s)/(2*R)
        self.assertAlmostEqual(real_power/envelope_power,1)
        self.assertAlmostEqual(10*math.log10(real_power/.001),-123.9751871942,places=8)
        self.assertAlmostEqual((2*k*T*R*(.8**2)/(4*R))/(real_s/R),.64)

    def test_coupled_resistor_circuit_by_source_ensemble(self):
        import itertools
        # Solve three-node KCL directly for each independent unit-variance
        # resistor source. Scale source variance by 2kBT afterwards.
        values=[]
        for signs in itertools.product([-1,1],repeat=3):
            e0,e1,e2=[math.sqrt(10)*v for v in signs]
            # Equations at the common node and loaded port nodes:
            # port: v_i=(v_common+e_i)/(1+10/50)
            # common: (vc-e0)/10+(vc-v1+e1)/10+(vc-v2+e2)/10=0
            vc=(6*e0-e1-e2)/8
            v1=(vc+e1)/1.2;v2=(vc+e2)/1.2
            values.append((v1,v2))
        C=[[sum(v[i]*v[j] for v in values)/8 for j in range(2)] for i in range(2)]
        self.assertAlmostEqual(C[0][0],9.33159722222222)
        self.assertAlmostEqual(C[0][1],2.38715277777778)
        diff=sum((v[1]-v[0])**2 for v in values)/8
        self.assertAlmostEqual(diff,2*10*(5/6)**2)
        self.assertAlmostEqual((C[0][0]+C[1][1])/diff-1,.34375)
        # A valid source matrix remains PSD; a reverse sign without sources
        # cannot be introduced merely to improve the differential budget.
        self.assertGreater(C[0][0]*C[1][1]-C[0][1]**2,0)
        cold=[]
        for signs in itertools.product([-1,1],repeat=3):
            e0=signs[0];e1=math.sqrt(10)*signs[1];e2=math.sqrt(10)*signs[2]
            vc=(6*e0-e1-e2)/8
            cold.append(((vc+e1)/1.2,(vc+e2)/1.2))
        self.assertAlmostEqual(sum(a*b for a,b in cold)/8,-1.12847222222)


    def test_reciprocal_integral_by_overlap_and_quadrature(self):
        # Independent midpoint integration of the finite blocker. Use kHz
        # coordinates; uniform source normalization cancels the kHz unit.
        n=8000;delta=1000;halfwidth=200
        for f in (-50,-13,0,27,50):
            integrated=sum(1 if abs(f-(-halfwidth+(i+.5)*400/n))<=100 else 4
                           for i in range(n))/n
            self.assertAlmostEqual(integrated,2.5,delta=.001)
        pb=1e-7;s0=1e-12;B=1e5
        self.assertAlmostEqual(10*math.log10(pb*s0*B/.001),-110)
        self.assertAlmostEqual(10*math.log10(2.5),3.97940008672)
        self.assertAlmostEqual((10**((-115-30)/10)/(pb*B))/3.16227766017e-13,1,places=10)

    def test_timing_error_from_direct_sampled_waveform(self):
        # Exact perturbed samples, not the generator's slope-RMS formula.
        fs=500e6;n=5000;sd=1e-12;err=[];lower=[]
        x=lambda t:.01*math.cos(2*math.pi*1e7*t+.31)+math.cos(2*math.pi*1e8*t+.7)
        for i in range(n):
            t=i/fs;dt=math.sqrt(2)*sd*math.cos(2*math.pi*90e6*t+.29)
            err.append(x(t+dt)-x(t))
        rms=math.sqrt(sum(e*e for e in err)/n)
        expected=sd/math.sqrt(2)*math.sqrt((2*math.pi*1e7*.01)**2+(2*math.pi*1e8)**2)
        self.assertAlmostEqual(rms,expected,delta=1e-10)
        amplitude=2*abs(sum(e*cmath.exp(-2j*math.pi*1e7*i/fs) for i,e in enumerate(err)))/n
        expected_peak=2*math.pi*1e8*sd/math.sqrt(2)
        self.assertAlmostEqual(amplitude,expected_peak,delta=3e-10)
        snr=20*math.log10((.01/math.sqrt(2))/(expected_peak/math.sqrt(2)))
        self.assertAlmostEqual(snr,27.0467025895,places=8)
        required_dt=math.sqrt(2)*.01/(2*math.pi*1e8*100)
        self.assertAlmostEqual(required_dt*1e12,.225079079039,places=10)



class ExtractionModels(unittest.TestCase):
    def test_invalid_frames_and_parameters_are_not_nondetections(self):
        import sys
        sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
        import physical_models as p
        for x in [[],[0],[0,0,0],[float('nan'),0],[0,complex(0,float('inf'))],None]:
            with self.assertRaises(ValueError):p.bounded_extract(x)
        for params in [{'theta':float('nan')},{'theta':float('inf')},
                       {'jammer_variance':-1},{'jammer_variance':float('inf')},
                       {'p_fa':0},{'p_fa':1},{'p_fa':float('nan')}]:
            with self.assertRaises(ValueError):p.bounded_extract([0,0],**params)
        self.assertFalse(p.bounded_extract([0,0])['decision'])
        self.assertTrue(math.isfinite(p.bounded_extract([0,0],p_fa=1e-100)['threshold']))

    def test_record_reader_is_bounded_and_failures_are_invalid(self):
        import sys
        sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
        import physical_models as p
        consumed=[]
        def unlimited():
            while True:
                consumed.append(0)
                yield 0
        with self.assertRaises(ValueError):p.bounded_extract(unlimited())
        self.assertEqual(len(consumed),3)
        def failed_reader():
            yield 0
            raise RuntimeError('Acquisition failed')
        with self.assertRaises(ValueError) as caught:p.bounded_extract(failed_reader())
        self.assertIsInstance(caught.exception.__cause__,RuntimeError)
        self.assertFalse(p.bounded_extract(iter([0,0]))['decision'])

    def test_energy_detector_probability_by_independent_gaussian_draws(self):
        import sys,random
        sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
        import physical_models as p
        eta=13.06224077918807;rho=16*26/101
        self.assertAlmostEqual(p.gamma_tail_integer(4,eta),.001,places=13)
        predicted=p.energy_detection_probability(4,4*rho,eta)
        self.assertAlmostEqual(predicted,.8994733481863,places=12)
        rng=random.Random(101031);trials=50000;detected=0
        for _ in range(trials):
            q=sum(abs(math.sqrt(rho)+complex(rng.gauss(0,1),rng.gauss(0,1))/math.sqrt(2))**2 for _ in range(4))
            detected+=q>eta
        self.assertLess(abs(detected/trials-predicted),.006)

    def test_mismatched_reference_energy_and_real_decision(self):
        inv=[[26/101,-25*math.sqrt(3)/101],[-25*math.sqrt(3)/101,76/101]]
        inner=lambda x,y:sum(x[i].conjugate()*inv[i][j]*y[j] for i in range(2) for j in range(2))
        a=[1+0j,0j];q=inner(a,a).real
        for psi in (0,math.pi/3,math.pi/2,math.pi):
            ar=[cmath.exp(1j*psi),0j];qr=inner(ar,ar).real
            self.assertAlmostEqual(abs(inner(ar,a))**2/(qr*q),1)
            mean=math.sqrt(2)*4*inner(ar,a).real/math.sqrt(qr)
            self.assertAlmostEqual(mean,math.sqrt(32*q)*math.cos(psi))
        for ar in [[1+1j,2-.1j],[.3-.7j,-1j]]:
            self.assertLessEqual(abs(inner(ar,a))**2/(inner(ar,ar).real*q),1+1e-14)

    def test_weight_from_direct_covariance_inverse_and_likelihood(self):
        import sys
        sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
        import physical_models as p
        C=[[76,25*math.sqrt(3)],[25*math.sqrt(3),26]]
        det=C[0][0]*C[1][1]-C[0][1]*C[1][0]
        inv=[[C[1][1]/det,-C[0][1]/det],[-C[1][0]/det,C[0][0]/det]]
        w,q,v=p.extraction_weights()
        self.assertAlmostEqual(q,inv[0][0])
        for i in range(2):self.assertAlmostEqual(w[i],inv[i][0]/q)
        self.assertAlmostEqual(v,sum(w[i]*C[i][j]*w[j] for i in range(2) for j in range(2)))
        x=[2.1+.7j,-.2+1.3j];A=1.7
        cost=lambda mu:sum((x[i]-mu[i]).conjugate()*inv[i][j]*(x[j]-mu[j]) for i in range(2) for j in range(2)).real
        t=sum(inv[0][j]*x[j] for j in range(2))
        self.assertAlmostEqual(cost([0,0])-cost([A,0]),2*A*t.real-A*A*q)
        result=p.bounded_extract(x)
        self.assertAlmostEqual(result['amplitude'],t/q)

    def test_source_draw_detector_false_alarm_and_detection(self):
        import sys,random
        from statistics import NormalDist
        sys.path.insert(0,str(Path(__file__).parents[1]/'engineering/examples'))
        import physical_models as p
        rng=random.Random(101030);N=100000;fa=det=0
        # Source-level draws, rather than drawing the asserted output Gaussian.
        w,q,v=p.extraction_weights();gamma=NormalDist().inv_cdf(.999)
        for _ in range(N):
            u=complex(rng.gauss(0,1),rng.gauss(0,1))/math.sqrt(2)
            n=[complex(rng.gauss(0,1),rng.gauss(0,1))/math.sqrt(2) for _ in range(2)]
            x=[10*math.sqrt(3)/2*u+n[0],5*u+n[1]]
            z=math.sqrt(2)*(w[0]*x[0]+w[1]*x[1]).real/math.sqrt(v)
            fa+=z>gamma;det+=z+math.sqrt(2)*4/math.sqrt(v)>gamma
        expected=NormalDist().cdf(math.sqrt(2*16*q)-gamma)
        self.assertLess(abs(fa/N-.001),.0005)
        self.assertLess(abs(det/N-expected),.006)
        self.assertAlmostEqual(expected,.41289421617,places=10)
        # The executable rule is checked on asymmetric complex source samples.
        self.assertAlmostEqual(p.bounded_extract(x)['z'],z)

    def test_coherent_and_noncoherent_phase_counterexample(self):
        terms=[cmath.exp(1j*m*math.pi/2) for m in range(4)]
        self.assertAlmostEqual(abs(sum(terms)),0,places=13)
        self.assertAlmostEqual(sum(abs(t)**2 for t in terms),4)
        fixed=[t*cmath.exp(-1j*m*math.pi/2) for m,t in enumerate(terms)]
        self.assertAlmostEqual(abs(sum(fixed)),4)
        # Direct convolution of four unit exponential densities produces q^3e^-q/6.
        # Independently integrate its tail and compare with the finite series.
        h=.001;a=6.;b=50.;n=int((b-a)/h)
        area=sum(((a+(i+.5)*h)**3)*math.exp(-(a+(i+.5)*h))/6*h for i in range(n))
        tail=math.exp(-a)*sum(a**k/math.factorial(k) for k in range(4))
        self.assertAlmostEqual(area,tail,delta=2e-9)

    def test_stochastic_correlation_by_gaussian_quadrature(self):
        import itertools
        # Product three-point Gaussian quadrature integrates the fourth-order
        # moments exactly. No correlation-variance identity is used to generate them.
        nodes=[(-math.sqrt(1.5),1/6),(0,2/3),(math.sqrt(1.5),1/6)]
        mean=complex(0);mse=pseudo=0j
        for choices in itertools.product(nodes,repeat=6):
            z=[a for a,w in choices];weight=math.prod(w for a,w in choices)
            source=.1*complex(z[0],z[1]);n1=complex(z[2],z[3]);n2=complex(z[4],z[5])
            product=(source+n1)*(source+n2).conjugate()
            mean+=weight*product
            mse+=weight*abs(product-.01)**2
            pseudo+=weight*(product-.01)**2
        self.assertAlmostEqual(mean,.01)
        self.assertAlmostEqual(mse.real,1.0201)
        self.assertAlmostEqual(pseudo,.0001)

    def test_projection_preserves_constraint_but_amplifies_noise(self):
        for angle in [0,math.pi/6,math.pi/2]:
            b=[math.cos(angle),math.sin(angle)];dot=b[0]
            a_perp=[1-dot*b[0],-dot*b[1]]
            self.assertAlmostEqual(sum(x*x for x in a_perp),math.sin(angle)**2)
            self.assertAlmostEqual(sum(x*y for x,y in zip(a_perp,b)),0)
        w=[1,-math.sqrt(3)]
        self.assertAlmostEqual(w[0],1)
        self.assertAlmostEqual(sum(x*x for x in w),4)
        self.assertAlmostEqual(w[0]*math.sqrt(3)/2+w[1]/2,0)
        self.assertGreater(1/(1+100),0)  # original finite covariance is not a null.

    def test_shared_record_covariance_and_leakage_bound(self):
        a=[1,0]*4;b=[math.sqrt(3)/2,.5]*4
        C=[[(1 if i==j else 0)+100*b[i]*b[j] for j in range(8)] for i in range(8)]
        dot=sum(x*y for x,y in zip(a,b))
        v=[a[i]-100*b[i]*dot/401 for i in range(8)]
        for i in range(8):self.assertAlmostEqual(sum(C[i][j]*v[j] for j in range(8)),a[i],places=11)
        self.assertAlmostEqual(sum(x*y for x,y in zip(a,v)),404/401)
        h=.7+.2j;ell0=.2-.1j;eps=.15
        bound=max(0,abs(1-h*ell0)-abs(h)*eps)
        for k in range(100):
            ell=ell0+eps*cmath.exp(2j*math.pi*k/100)
            self.assertGreaterEqual(abs(1-h*ell)+1e-14,bound)

    def test_reference_cancellation_signal_and_noise_by_source_ensemble(self):
        import itertools
        h=100/101;outputs=[]
        for j,n,v in itertools.product([1,-1,1j,-1j],repeat=3):
            x=10*j+n;r=10*j+v
            outputs.append(x-h*r)
            signal_on=(1+10*j+n)-h*(1+10*j+v)
            self.assertAlmostEqual(signal_on-(x-h*r),1-h)
        variance=sum(abs(z)**2 for z in outputs)/len(outputs)
        self.assertAlmostEqual(variance,201/101)
        self.assertAlmostEqual(20*math.log10(1-h),-40.08642747565,places=10)
        self.assertAlmostEqual((1-h)**2*101/variance,1/201)


if __name__=='__main__':
    unittest.main()
