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
        self.assertAlmostEqual(abs(v)**2/(2*50),12.625e-12)
        self.assertAlmostEqual(math.degrees(cmath.phase(v/v1)),5.7105931375,places=9)
        self.assertAlmostEqual(20*math.log10(abs(v/v1)),.0432137378,places=9)
        a=.73; U=[[math.cos(a),-math.sin(a)],[math.sin(a),math.cos(a)]]
        hp=[sum(h[i]*U[i][j] for i in range(2)) for j in range(2)]
        Ep=[sum(U[i][j]*E[i] for i in range(2)) for j in range(2)]
        self.assertAlmostEqual(sum(hp[i]*Ep[i] for i in range(2)),2*v)

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
        self.assertAlmostEqual(10**((-115-30)/10)/(pb*B),3.16227766017e-13)

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



if __name__=='__main__':
    unittest.main()
