from operator import sub #the subtraction function
import math
import mpmath
import RKeuler
import smartEuler

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
    
