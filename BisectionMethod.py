import math
import numpy as np

def bisection(f,a,b,tau,n):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Root not in interval")
    m = (a+b)/2
    if np.abs(f(m)) < tau:
        return m,n
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection(f, m, b, tau,n+1)
    else:
        return bisection(f,a,m,tau,n+1)

def fixedPoint(p0,f,n,stop):
    newP = p0
    while n != stop:
        newP = f(newP)
        print(newP, n)
        n += 1
    return

def fixedIteration(p0,f,n,tau):
    newP = f(p0)
    print(newP,n)
    while abs(newP - p0) > tau:
        n += 1
        p0 = newP
        newP = f(newP)
        print(newP,n)
    return
        


if __name__ == "__main__":
    # fx = lambda x:math.sqrt((2-x**4)/3)
    # ans = bisection(fx,1.5,2.5,10**(-5),0)
    # print(ans)
    
    fx = lambda x: 2+math.sin(x)
    fixedIteration(2.5,fx,1,10**-5)
    print(abs(2.5541921027478667-2.5542005781937362))