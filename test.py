from operator import sub #the subtraction function
import math
import mpmath
from RKeuler import *
from smartEuler import *
import matplotlib.pyplot as plt
from timeit import timeit
from time import sleep

# The functions in the list
def f_d(t,y):
    return math.exp(t) * math.sin(y)
    
def f(t): #f(0) = 1
    return 2*mpmath.acot(
        math.exp(1-math.exp(t))*mpmath.cot(0.5)
        )

def f1(t):
    return math.exp(t)

def f2(t):
    return math.sin(t)

def f2_d(t,y=0):
    return math.cos(t)

def f3(t): #y(0) = 1
    return math.exp(math.exp(t)-1)

def f3_d(t,y):
    return y*math.exp(t)

def f4(t): #y(0) = 1
    return 1/(1-t)
def f4_d(t,y):
    return y**2

# List of Functions
functions = [f,f1,f2,f3,f4]
diffEQs = [f_d,f1,f2_d,f3_d,f4_d]

#
def calcSquareError(f,method):
    tlst,ylst = method
    y_actual = list(map(f,tlst))
    errorlst = list(map(sub, y_actual, ylst)) 
    errorlst = list(map(lambda x: x**2, errorlst))
    return float(sum(errorlst)/len(tlst))

#Visual Tests
def visualTest(f,df,initial,tstart,tend,dt,method=adaptiveEuler):
    plt.close()
    x,y = method(df,tstart,tend,initial,dt)
    y_act = list(map(f,x))
    plt.plot(x,y,label='n_int')
    plt.plot(x,y_act,label='act')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
           ncol=2, mode="expand", borderaxespad=0.)
    plt.show()

#Time Tests
def wrapper(df,initial,tstart,tend,dt,method=adaptiveEuler):
    def wrapped():
        return method(df,tstart,tend,initial,dt)
    return wrapped

def timeWrapper(df,initial,tstart,tend,dt,method=adaptiveEuler):
    #global wrapped
    wrapped = wrapper(df,initial,tstart,tend,dt,method=adaptiveEuler)
    
    return timeit(wrapped,number=10000)

def time1():
    return eulerMethod(f_d,0,5,1,0.05)

def time2():
    return adaptiveEuler(f_d,0,5,1,1)

def time3():
    return eulerMethod(f_d,0,5,1,0.05)



#timeit('time1()',setup='from test import time1', number=10000)
#timeit('time2()',setup='from test import time2', number=10000)

#function to display twolists in image or ?... columns with the actual.

#visualTest(f,f_d,1,0,10,1,adaptiveEuler)
