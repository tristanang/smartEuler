from operator import sub

def calcSquareError(f,tlst,ylst):
    y_actual = list(map(f,tlst))
    errorlst = list(map(sub, y_actual, ylst)) 
    errorlst = list(map(lambda x: x**2, errorlst))
    return sum(errorlst)
    
