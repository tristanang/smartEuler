import numpy as np
import math

def eulerStep(y_1,f1,dt):
    return y_1+f1*dt

def rkStep(y_1,t_1,f,dt):
    k1 = f(t_1,y_1)
    k2 = f(t_1+(dt/2),y_1+(dt/2)*(k1/2))
    k3 = f(t_1+(dt/2),y_1+(dt/2)*(k2/2))
    k4 = f(t_1+dt, y_1 + dt*k3)
    
    return y_1 + (dt/6) * (k1 + 2*(k2+k3) + k4)

def genTime(tstart,tend,dt):
    datapoints = (tend - tstart) / dt
    timelst = np.linspace(tstart,tend,datapoints+1,endpoint=True)
    return timelst

def eulerMethod(f,tstart,tend,yinitial,dt):
    timelst = genTime(tstart,tend,dt)
    ylst = [yinitial]

    dt = timelst[1] - timelst[0]
    
    for i in range(len(timelst)-1):
        y_next = eulerStep(ylst[-1],f(timelst[i],ylst[-1]),dt)
        ylst.append(y_next)
    
    return timelst,ylst

def RK4(f,tstart,tend,yinitial,dt):
    timelst = genTime(tstart,tend,dt)
    ylst = [yinitial]

    for i in range(len(timelst)-1):
        y_next = rkStep(ylst[-1],timelst[i],f,dt)
        ylst.append(y_next)
    
    return timelst,ylst


def test():
    tstart = 0.0
    tend = 1.
    yinitial = 1.
    dt = 0.1
    t,y = eulerMethod(f2,tstart,tend,yinitial,dt)
    return t,y

def f1(t,y): return t-y

def f2(t,y): return math.exp(t)


