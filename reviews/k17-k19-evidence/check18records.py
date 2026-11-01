from pathlib import Path
import sys,json,math,numpy as np
sys.path.insert(0,str(Path('engineering/examples').resolve()));import sampled_models as m
r={};r['fit']=m.iq_fit_cached();fs=16e6;N=4096;t=np.arange(N)/fs;dc=.005+.003j
f=[.375e6,-.625e6,1.375e6];amp=[.009,.007,.004];phase=[.1,-.4,.8];tones=[(ff,a*np.exp(1j*p)) for ff,a,p in zip(f,amp,phase)]
w=dc+sum(a*np.exp(1j*2*np.pi*ff*(t-20e-9)) for ff,a in tones);v=m.iq_wave(t,tones,dc)
r['modulation']={}
for mode in [False,True]:
 y=m.iq_apply_periodic(v,fs,flat=mode)
 r['modulation']['flat' if mode else 'matched']={'error':float(np.linalg.norm(y-w)/np.linalg.norm(w-dc)),'dc_error_real':float(np.mean(y).real-dc.real),'dc_error_imag':float(np.mean(y).imag-dc.imag)}
t=np.arange(1000)/1000;w=dc+.01*np.exp(2j*np.pi*10*(t-20e-9));v=m.iq_wave(t,[(10,.01)],dc);y=m.iq_apply_periodic(v,1000)
r['near_dc']={'error':float(np.linalg.norm(y-w)/np.linalg.norm(w-dc)),'dc_error':str(np.mean(y)-dc)}
r['sweep']=[]
for f in [q*125000 for q in range(-15,16,2)]:
 a,b=m.iq_response(f,'matched',.01);target=np.exp(-2j*np.pi*f*20e-9)
 r['sweep'].append({'f':f,'gain_db':20*math.log10(abs(a)),'phase_deg':math.degrees(np.angle(a/target)),'image_db':-20*math.log10(abs(b/a))})
print(json.dumps(r,indent=2));Path('/tmp/k1719/k18-records.json').write_text(json.dumps(r,indent=2)+'\n')
# Held-out synthetic data: actual physical real-path records, both input signs.
t=np.arange(N)/fs; r['swept_records']=[]
for f in [q*125000 for q in range(-15,16,2)]:
 responses=[]
 for inp,phi in [(f,.31),(-f,-.7)]:
  amp=.01*np.exp(1j*phi);v=m.iq_wave(t,[(inp,amp)]);y=m.iq_apply_periodic(v,fs)
  z=np.mean(y*np.exp(-2j*np.pi*f*t))/(amp if inp==f else amp.conjugate());responses.append(z)
 a,b=responses;aa,bb=m.iq_response(f)
 assert abs(a-aa)<1e-13 and abs(b-bb)<1e-13
 r['swept_records'].append({'f':f,'desired':str(a),'conjugate':str(b),'image_db':-20*math.log10(abs(b/a))})
r['level_state']=[]
for amp,state,g,e,delay,off in [(.2,'A',1.05,np.pi/60,20e-9,.003-.002j),(.02,'B',1.07,np.pi/45,24e-9,.004-.001j)]:
 f=.375e6;v=m.iq_wave(t,[(f,amp)],g=g,epsilon=e,delay=delay,offset=off);y=m.iq_apply_periodic(v,fs)
 w=amp*np.exp(2j*np.pi*f*(t-20e-9));a=np.mean(y*np.exp(-2j*np.pi*f*t))/amp;b=np.mean(y*np.exp(2j*np.pi*f*t))/amp
 r['level_state'].append({'amplitude':amp,'state':state,'gain_db':20*math.log10(abs(a)),'phase_deg':math.degrees(np.angle(a*np.exp(2j*np.pi*f*20e-9))),'image_db':-20*math.log10(abs(b/a)),'waveform_error':float(np.linalg.norm(y-w)/np.linalg.norm(w)),'mean':str(np.mean(y))})
Path('/tmp/k1719/k18-records.json').write_text(json.dumps(r,indent=2)+'\n');print('actual swept records:',len(r['swept_records']),'level/state:',r['level_state'])
