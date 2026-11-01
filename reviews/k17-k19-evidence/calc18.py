import numpy as np, math, cmath
G=1.05;E=math.radians(3);tau=20e-9;gamma=.5;A=.02
cy=G*math.cos(E)+.75*gamma*A*A;cx=G*math.sin(E);gh=math.hypot(cy,cx);eh=math.atan2(cx,cy)
print('fit',gh,math.degrees(eh),tau)
def matrix(f,g=G,e=E,t=tau):
 h=cmath.exp(-2j*math.pi*f*t);a=(1+g*cmath.exp(-1j*e)*h)/2;b=(1-g*cmath.exp(1j*e)*h)/2
 am=(1+g*cmath.exp(1j*e)*h)/2;bm=(1-g*cmath.exp(-1j*e)*h)/2
 return np.array([[a,b],[bm,am]])
def corrmat(f,delay=tau):
 # input [z(f),z*(-f)] -> corrected output at target delayed plane
 H=cmath.exp(-2j*math.pi*f*delay);q=1/(gh*math.cos(eh));t=math.tan(eh)
 return np.array([[H*(1+1j*t)/2+q/2,H*(1+1j*t)/2-q/2], [H*(1-1j*t)/2-q/2,H*(1-1j*t)/2+q/2]])
for f in [0,.125e6,1e6,1.875e6,2e6]:
 for typ,c in [('raw',np.eye(2)),('flat',corrmat(0)),('delay',corrmat(f))]:
  m=c@matrix(f);tar=cmath.exp(-2j*math.pi*f*tau)
  print(f,typ,'desired amp/ph',20*math.log10(abs(m[0,0])),math.degrees(cmath.phase(m[0,0]/tar)),'leak',20*math.log10(max(abs(m[0,1]/m[0,0]),1e-16)))
print('noise', (1+1/gh**2)/(2*math.cos(eh)**2))
# time construction, FFT delayed I, static cross feed, independent waveform
fs=16e6;N=4096;n=np.arange(N);t=n/fs
freqs=[.375e6,-.625e6,1.375e6];amps=[.009,.007,.004];ph=[.1,-.4,.8];dc=.005+.003j
s=dc+sum(a*np.exp(1j*(2*np.pi*f*t+p)) for f,a,p in zip(freqs,amps,ph))
sd=dc+sum(a*np.exp(1j*(2*np.pi*f*(t-tau)+p)) for f,a,p in zip(freqs,amps,ph))
d=.003-.002j
v=s.real+1j*(G*(sd.imag*np.cos(E)-sd.real*np.sin(E))+gamma*sd.imag**3)+d
ff=np.fft.fftfreq(N,1/fs)
def apply(v,delay=tau):
 i=np.fft.ifft(np.fft.fft((v-d).real)*np.exp(-2j*np.pi*ff*delay)).real
 q=(v-d).imag/(gh*np.cos(eh))+np.tan(eh)*i
 return i+1j*q
for typ,x in [('raw',v-d),('flat',apply(v,0)),('delayed',apply(v))]:
 print('mod',typ,np.linalg.norm(x-sd)/np.linalg.norm(s-dc), 'dcerr',np.mean(x)-dc)
for aa in [.02,.2]:
 for gg,ee,tt,dd in [(G,E,tau,d),(1.07,math.radians(4),24e-9,.004-.001j)]:
  f=.375e6;ss=aa*np.exp(1j*2*np.pi*f*t);ssdel=aa*np.exp(1j*2*np.pi*f*(t-tt));want=aa*np.exp(1j*2*np.pi*f*(t-tau)); vv=ss.real+1j*(gg*(ssdel.imag*np.cos(ee)-ssdel.real*np.sin(ee))+gamma*ssdel.imag**3)+dd
  yy=apply(vv);z=np.mean(yy*np.exp(-2j*np.pi*f*t))/aa;im=np.mean(yy*np.exp(2j*np.pi*f*t))/aa;print('level',aa,gg,'amp/ph',20*math.log10(abs(z)),math.degrees(cmath.phase(z*np.exp(2j*np.pi*f*tau))),'leak',20*math.log10(abs(im/z)),'err',np.linalg.norm(yy-want)/np.linalg.norm(want),'dc',np.mean(yy))
print('HP10Hz',20*np.log10(10/math.hypot(10,100)),math.degrees(math.atan2(100,10)))
