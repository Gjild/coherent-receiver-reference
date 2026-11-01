from pathlib import Path
import sys,json,math,cmath,time,platform,statistics
import numpy as np
sys.path.insert(0,str(Path('engineering/examples').resolve()));import sampled_models as m
r={'filter':{str(b):m.fir_metrics(fraction=b) for b in [17,23,29]},'processing':m.processing_case()}
# Different input identity / NCO faults; phase compared with unchanged baseline.
x=m.digital_input()/2**15;idx,base=m.ddc_reference(x);keep=idx>=256
fault=2048;_,nco=m.ddc_reference(x,fault_index=fault);di,drop=m.ddc_reference(np.delete(x,fault));bf=base[:len(drop)]
a=(idx>=fault+256);b=(di>=fault+256)
r['faults']={'nco_phase_deg':math.degrees(np.angle(np.mean(nco[a])/np.mean(base[a]))),'drop_phase_deg':math.degrees(np.angle(np.mean(drop[b])/np.mean(bf[b]))),'known_missing_output_indices':list(map(int,idx[(idx>=fault)&(idx<=fault+256)]))}
# Pure tones / modulation: finite filter response including both real images.
h=m.fir_coeff();n=np.arange(8192);t=n/128e6
r['rate']=[]
for dec,f in [(8,20.5e6),(16,20.5e6),(32,24e6)]:
 yidx,y=m.ddc_reference(np.cos(2*np.pi*f*t+.31),decimation=dec);nvalid=yidx>=256;w=2*np.pi*(f-20e6)/128e6
 H=np.sum(h*np.exp(-1j*w*np.arange(len(h))))
 # Desired plus negative-frequency mirror, both computed through the actual FIR.
 wn=-2*np.pi*(f+20e6)/128e6;Hn=np.sum(h*np.exp(-1j*wn*np.arange(len(h))))
 expected=H*np.exp(1j*(w*yidx+.31))+Hn*np.exp(1j*(wn*yidx-.31))
 assert np.max(abs(y[nvalid]-expected[nvalid]))<2e-12
 r['rate'].append({'M':dec,'analog_MHz':f/1e6,'wanted_transfer':float(abs(H)),'error':float(np.max(abs(y[nvalid]-expected[nvalid]))),'effective_epoch_first':float((yidx[nvalid][0]-128)/128e6)})
# Fractional resampling with the supplied affine remote-clock coordinates.
fb=16e6;alpha=1+20e-6;beta=10e-9;ns=np.arange(32768);source_times=(ns/fb-beta)/alpha
target=np.arange(16,32750)/fb
wave=lambda t: .004*np.exp(2j*np.pi*2e6*t+.2j)+.003*np.exp(-2j*np.pi*.75e6*t-.3j)
source=wave(source_times);q=fb*(alpha*target+beta);truth=wave(target)
out=m.resample_finite(source,q);quant=m.resample_finite(source,q,phase_bits=15,coefficient_fraction=29)
sourceq=(np.rint(source.real*2**21)+1j*np.rint(source.imag*2**21))/2**21
fixed=m.resample_finite(sourceq,q,phase_bits=15,coefficient_fraction=29,integer=True)
r['resampling']={'floating_error_pct':float(np.linalg.norm(out-truth)/np.linalg.norm(truth)*100),'coefficient_phase_error_pct':float(np.linalg.norm(quant-truth)/np.linalg.norm(truth)*100),'integer_error_pct':float(np.linalg.norm(fixed-truth)/np.linalg.norm(truth)*100),'max_integer_vs_float_uv':float(max(abs(fixed-out))*1e6)}
# Needed coefficient/table/range bounds, eight-node uniform approximation theorem.
prod=np.prod([.5-j for j in range(-3,5)]);bound=abs(prod)*(np.pi/4)**8/math.factorial(8)
nodes,w=m.lagrange_weights(.5);r['interpolation_bound']={'complex':bound,'phase_deg':math.degrees(math.asin(bound)),'gain_loss_db':-20*math.log10(1-bound),'l1_center':sum(abs(np.array(w))),'white_noise_center':sum(np.array(w)**2)}
r['resources']={'unsymmetric_ops':2*2*257*16e6+2*2*128e6+2*2*8*16e6,'symmetric_ops':2*2*129*16e6+2*2*128e6+2*2*8*16e6,'arrival_Bps':192e6+48*16e6/1024,'outage_bytes':(192e6+48*16e6/1024)*.0005,'after_outage_bytes':131072+(192e6+48*16e6/1024)*.0005,'recovery_s':(192e6+48*16e6/1024)*.0005/(240e6-192e6-48*16e6/1024),'clock_mismatch_fill_s':131072/((192e6+48*16e6/1024)*20e-6)}
# Record actual software execution time: not receiver measurements / real-time guarantee.
words=m.digital_input();times=[]
for _ in range(5):
 start=time.perf_counter();m.ddc_integer(words);times.append(time.perf_counter()-start)
cpu='unknown'
for line in Path('/proc/cpuinfo').read_text().splitlines():
 if line.startswith('model name'):cpu=line.split(':',1)[1].strip();break
r['software_execution']={'platform':platform.platform(),'cpu':cpu,'python':platform.python_version(),'numpy':np.__version__,'input_samples':len(words),'runs_s':times,'median_s':statistics.median(times),'required_input_interval_s':len(words)/128e6,'median_input_samples_per_s':len(words)/statistics.median(times)}
Path('/tmp/k1719/k19-records.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
