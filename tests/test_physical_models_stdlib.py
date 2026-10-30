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


if __name__=='__main__':
    unittest.main()
