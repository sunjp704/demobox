
from scipy import fft
import numpy as np
import matplotlib.pyplot as plt


N=128
h=2*np.pi/N
x=np.arange(1,N+1)*h
t=0
dt=h/4
c=0.2+np.sin(x-1)**2
v=np.exp(-100*(x-1)**2)
vold=np.exp(-100*(x-0.2*dt-1)**2)

# time stepping
tmax=8
tplot=0.15
dt=tplot
plotgap=round(tplot/dt)
dt=tplot/plotgap
nplots=round(tmax/tplot)
data=np.hstack(v,np.zeros((nplots,N)))
tdata=t
for i in range(nplots):
    for n in range(plotgap):
        t+=dt
        v_hat= fft.fft(v)
        w_hat=1j*