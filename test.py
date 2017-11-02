from operator import sub #the subtraction function
import math
import mpmath
from RKeuler import *
from smartEuler import *
import matplotlib.pyplot as plt

def f_d(t,y):
    return math.exp(t) * math.sin(y)
    
def f(t): #f(0) = 1
    return 2*mpmath.acot(
        math.exp(1-math.exp(t))*mpmath.cot(0.5)
        )
    
def calcSquareError(f,tlst,ylst):
    y_actual = list(map(f,tlst))
    errorlst = list(map(sub, y_actual, ylst)) 
    errorlst = list(map(lambda x: x**2, errorlst))
    return sum(errorlst)/len(tlst)

#Visual Tests

def visualtest(f,df,initial,tstart,tend,dt,method):
    x,y = method(df,tstart,tend,initial,dt)
    y_act = list(map(f,x))
    plt.plot(x,y,label='n_int')
    plt.plot(x,y_act,label='act')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

#function to display twolists in image or ?... columns with the actual.

#visualtest(f,f_d,1,0,10,1,adaptiveEuler)
    
#Quantitative Tests
