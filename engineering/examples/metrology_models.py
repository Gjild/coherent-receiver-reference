"""Supplied phase readings, loading, correlated records and conditional uncertainty."""
from math import *
import cmath,csv,io
from pathlib import Path
from visual_foundations import SVG,lin,log as logspace


def mean_factor(n,rho=.9):
    return (n+2*sum((n-k)*rho**k for k in range(1,n)))/n**2


def variance_dof(n,rho=.9):
    if n<2:raise ValueError('at least two observations for centered quadratic form')
    S=n*n*mean_factor(n,rho)
    rows=[sum(rho**abs(i-j) for j in range(n)) for i in range(n)]
    tr=n-S/n
    tr2=n+2*sum((n-k)*rho**(2*k) for k in range(1,n))-2*sum(v*v for v in rows)/n+(S/n)**2
    return max(1.,tr*tr/tr2)


def loading(z=45+5j,zs=50):
    return z/(zs+z)


def loading_correction(z=45+5j,zs=50,target=50):
    return cmath.phase(loading(z,zs)/loading(target,zs))


def loading_uncertainty(z=45+5j,uz=.2):
    d=1/z-1/(50+z)
    return uz*abs(d)  # independent equal real/imaginary standard uncertainties


def supplied_records():
    import numpy as np
    rng=np.random.default_rng(2201);n=100
    def ar(sig):
        x=np.empty(n);x[0]=sig*rng.normal()
        for k in range(1,n):x[k]=.9*x[k-1]+sig*sqrt(1-.9**2)*rng.normal()
        return x
    records=[];theta=.1;load=loading_correction();inst=-.004
    for sign in [1,-1]:
        ref=ar(.02);ea=ar(.006);eb=ar(.006)
        pa=-ref+ea;pb=theta+load+sign*.015+inst-ref+eb
        records.append((sign,pa,pb))
    return records


def records_csv():
    out=io.StringIO(newline='');w=csv.writer(out,lineterminator='\n')
    w.writerow(['fixture_sign','index','time_s','phase_A_rad','phase_B_rad'])
    for sign,a,b in supplied_records():
        for k,(aa,bb) in enumerate(zip(a,b)):w.writerow([sign,k,f'{k*.001:.3f}',f'{aa:.12g}',f'{bb:.12g}'])
    return out.getvalue()


def metrology_case():
    import numpy as np
    records=supplied_records();load=loading_correction();means=[];est=[]
    n=100;rho=.9;R=rho**abs(np.arange(n)[:,None]-np.arange(n)[None,:]);P=np.eye(n)-np.ones((n,n))/n
    for sign,a,b in records:
        x=b-a;means.append(float(np.mean(x)));est.append(float(x@P@x/np.trace(P@R)))
    F=mean_factor(n);repeat=sqrt(2)*.006*sqrt(F);uL=loading_uncertainty()
    uc=sqrt(repeat**2+.002**2+.001**2+uL**2)
    indep=sqrt((2*.006**2+2*.02**2)*F+.002**2+.001**2+uL**2)
    swap=(means[0]+means[1])/2-(-.004)-load
    # Independent records reduce reading noise, not common instrument/loading knowledge.
    swapu=sqrt(repeat**2/2+.001**2+uL**2+.0015**2)
    return dict(loading_gain=[loading().real,loading().imag],loading_phase_rad=load,
        loading_standard_uncertainty_rad=uL,raw_difference_means_rad=means,
        corrected_phase_rad=means[0]-.015-(-.004)-load,
        mean_factor=F,effective_mean_samples=1/F,variance_dof=variance_dof(n),
        supplied_variance_estimates=est,repeat_standard_uncertainty_rad=repeat,
        combined_standard_uncertainty_rad=uc,independent_refs_standard_uncertainty_rad=indep,
        swap_phase_rad=swap,swap_fixture_phase_rad=(means[0]-means[1])/2,
        swap_standard_uncertainty_rad=swapu,
        floor_bound_20mV_rad=asin(.0002/.02),floor_bound_120mV_rad=asin(.0002/.12),
        minimum_amplitude_for_2mrad_V=.0002/sin(.002))


def unit22():
    s=SVG('metrology-planes','Trace loading, fixtures and reference paths into the reported phase',850)
    for y,channel in [(140,'A'),(340,'B')]:
        s.box(35,y,220,90,['DUT '+channel+': source plane','source impedance Zs'])
        s.box(350,y,235,90,['Fixture + loaded port','ZL; phase correction'])
        s.box(700,y,210,90,['Phase reading p'+channel,'subtract reference r'])
        s.path([(255,y+45),(350,y+45)],arrow=True);s.path([(585,y+45),(700,y+45)],arrow=True)
    s.box(375,550,280,90,['Common reference r(t)','same phase sensitivity'])
    s.path([(655,595),(940,595),(940,455),(805,455),(805,430)],arrow=True)
    s.path([(940,455),(940,255),(805,255),(805,230)],arrow=True)
    s.text(40,700,'Difference pB − pA cancels r only with matched timing, signs and transfer.',19)
    s.text(40,755,'Changing the reference topology changes test sensitivity and its uncertainty.',19);s.save()
    ns=sorted(set(round(x) for x in logspace(2,1000)))
    uL=loading_uncertainty();floor=.002**2+.001**2+uL**2
    s=SVG('metrology-records','Correlated records limit averaging and uncertainty of the variance estimate',1080)
    s.plot(70,'Per-channel phase RMS 0.006 rad; sampled correlation ρ=0.9',(2,1000),(0,.012),
        'Number of phase readings N (log scale)','Standard uncertainty of reported phase (rad)',[
        ('correlated reading contribution',ns,[sqrt(2)*.006*sqrt(mean_factor(n)) for n in ns]),
        ('incorrect independent reading model',ns,[sqrt(2)*.006/sqrt(n) for n in ns]),
        ('combined incl. fixed knowledge terms',ns,[sqrt(2*.006**2*mean_factor(n)+floor) for n in ns])],True,False)
    s.plot(520,'Known Gaussian correlation shape; variance uses centered quadratic form',(2,1000),(1,1000),
        'Number of phase readings N (log scale)','Effective count / moment-matched degrees of freedom',[
        ('effective mean count Neff',ns,[1/mean_factor(n) for n in ns]),
        ('variance moment DOF ν',ns,[variance_dof(n) for n in ns]),
        ('independent variance DOF N−1',ns,[n-1 for n in ns])],True,True)
    s.text(40,940,'Neff controls variance of the mean; ν describes variance-estimate uncertainty.',18)
    s.text(40,995,'Neither supplies an exact Student-t interval for these correlated records.',18);s.save()
    amps=logspace(.005,.15)
    s=SVG('metrology-level-floor','Level changes distinguish a fixed leakage floor from proportional leakage',660)
    s.plot(70,'Coherent additive phasor leakage; declared admissible amplitude ≤ 0.15 V',(.005,.15),(.0005,.05),
        'Desired phasor magnitude A (V; log scale)','Worst phase bias magnitude (rad; log scale)',[
        ('fixed |b|≤0.2mV: arcsin(B/A)',amps,[asin(.0002/a) for a in amps]),
        ('proportional |b|≤0.01A',amps,[asin(.01)]*len(amps)),
        ('illustrative 0.002rad bias limit',amps,[.002]*len(amps))],True,True)
    s.text(40,495,'20 mV: bound 0.0100002 rad; 120 mV: 0.00166667 rad; 200 mV exceeds range.',18)
    s.text(40,555,'Raising level is conditional on loaded response, linearity and phase-state evidence.',18)
    s.text(40,610,'Time averaging alone does not remove a coherent offset.',18);s.save()

    s=SVG('metrology-phase-disk','Geometry alone does not determine phase uncertainty',1120)
    s.path([(100,290),(600,290)],'#9aaab3',width=1.5,arrow=True)
    s.path([(160,515),(160,75)],'#9aaab3',width=1.5,arrow=True)
    for radius,color,dash in [(209,'#b34719','8 4'),(190,'#125b86','')]:
        s.s.append(f'<circle cx="350" cy="290" r="{radius}" fill="none" stroke="{color}" stroke-width="2.8" stroke-dasharray="{dash}"/>')
    s.dot(160,290,5,'#263c49');s.dot(350,290,4)
    phi=.6;r=2*cos(phi)
    s.path([(160,290),(160+190*r*cos(phi),290-190*r*sin(phi))],arrow=True)
    s.text(130,322,'0',18);s.text(345,322,'1',18);s.text(535,322,'2',18)
    s.text(545,350,'Re z',18);s.text(180,90,'Im z',18)
    s.text(245,155,'r = 2 cos φ',18)
    s.text(610,130,'Blue: |z − 1| ≤ 1',21)
    s.text(610,180,'Zero touches the boundary.',18)
    s.text(610,235,'Orange: radius 1.1',21,'#b34719')
    s.text(610,285,'Zero is strictly inside.',18)
    s.text(610,365,'Both axes: normalized',18)
    s.text(610,395,'complex coordinates.',18)
    pp=lin(-pi/2,pi/2)
    s.plot(620,'Blue disk only: uniform area, no probability mass at zero',(-pi/2,pi/2),(0,.7),
        'Principal phase φ (rad)','Phase probability density (rad^-1)',[
        ('p(φ) = 2 cos²φ / π',pp,[2*cos(x)**2/pi for x in pp])])
    s.text(40,1000,'Uniform touching disk: phase RMS = sqrt(π²/12 − 1/2) = 0.56786181 rad.',18)
    s.text(40,1060,'The orange outline specifies admissible geometry, not a probability distribution.',18);s.save()

if __name__=='__main__':
    unit22()
    import sys
    if '--records' in sys.argv:
        p=Path(__file__).resolve().parents[2]/'book/data/metrology-phase.csv';p.parent.mkdir(exist_ok=True);p.write_text(records_csv())
