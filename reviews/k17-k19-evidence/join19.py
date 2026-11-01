from pathlib import Path
p=Path('engineering/examples/sampled_models.py');s=p.read_text();i=s.index('\ndef processing_case(')
s=s[:i]+'''
def joined_processing_case():
    """Actual integer NCO/FIR/decimation then finite fractional interpolation."""
    import numpy as np
    count=8192;t=np.arange(count)/128e6;c=converter_case();a=c['wanted'];b=c['blocker']
    env=a*(.4*np.exp(.3j)+.3*np.exp(2j*pi*.5e6*t+.1j)+.2*np.exp(-2j*pi*1e6*t-.4j)+.1*np.exp(2j*pi*1.5e6*t+.8j))
    raw=np.real(env*np.exp(2j*pi*20e6*t))+b*(np.cos(2*pi*30e6*t+1.1)+np.cos(2*pi*40e6*t-.7))
    words=np.clip(np.rint(raw*2**15),-32768,32767).astype(np.int64)
    ix,ref=ddc_reference(words/2**15);_,fixed,flags=ddc_integer(words)
    first=next(i for i,n in enumerate(ix) if n>=256)
    rf=ref[first:];fx=fixed[first:];positions=np.arange(4,len(rf)-4)-.32
    ideal=resample_finite(rf,positions)
    actual=resample_finite(fx,positions,phase_bits=15,coefficient_fraction=29,integer=True)
    origin=(ix[first]-128)/128e6;epochs=origin+positions/16e6
    gain=np.vdot(ideal,actual)/np.vdot(ideal,ideal)
    result=dict(error_pct=float(np.linalg.norm(actual-ideal)/np.linalg.norm(ideal)*100),
                phase_deg=degrees(cmath.phase(gain)),first_epoch_s=float(epochs[0]),
                last_epoch_s=float(epochs[-1]),samples=len(actual),**flags)
    return result,words,positions,ideal,actual,epochs

'''+s[i:];p.write_text(s)
