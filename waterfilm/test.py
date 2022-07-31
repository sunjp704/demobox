from scipy import fft
import numpy as np

N=128
h=2*np.pi/N
x=np.arange(1,N+1)*h
t=0
dt=h/4
c=0.2+np.sin(x-1)**2
v=np.exp(-100*(x-1)**2)
vold=np.exp(-100*(x-0.2*dt-1)**2)

t=fft.fft(v)