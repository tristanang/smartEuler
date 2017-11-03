def adaptiveEuler(f,tstart,tend,yinitial,h): #h instead of dt used because it is no longer a fixed quantity
    tol = 0.005
    saf = 0.9
    
    timelst = [tstart]
    ylst = [yinitial]
    
    while timelst[-1] < tend:
        df =  f(timelst[-1],ylst[-1])
        y_one = ylst[-1] + (h * df)
        y_half = ylst[-1] + (h/2)*(df)
        y_twohalf = y_half + (h/2) * (f(timelst[-1]+(h/2),y_half))
        error = abs(y_twohalf - y_one)
        
        if error == 0: #might occur due to small close to zero errors and floating point rounding
            h = saf * h * min(max(tol/error,0.3),2)
        else:
            h = saf * h * 2
       
        timelst.append(timelst[-1]+h)
        y_next = ylst[-1] + h * df
        ylst.append(y_next)
    
    return timelst,ylst

def adaptiveRK45():
    return