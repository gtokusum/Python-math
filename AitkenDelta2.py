import math
import numpy as np
import NewtonMethod

def getPs(p0,pn):
    p1 = pn(p0)
    p2 = pn(p1)
    return p1,p2


def delta(p0,p1,p2,pn,n):
    if n == 0:
        return
    else:
        p1,p2=getPs(p0,pn)
        # print(p1,p2,p0)
        q = p0 - (p1-p0)**2 /(p2 -2*p1 +p0)
        print(q)
        delta(p1,0,0,pn,n-1)
    return 
e = math.e
ln = math.log


def deltaNewton(p0,q,f,fprime,tau,n=0):
    p1 = NewtonMethod.getPs(f,fprime,p0)
    p2 = NewtonMethod.getPs(f,fprime,p1)
    q0 = p0 - (p1-p0)**2/(p2-2*p1+p0)
    print(n,q0)
    if abs(q-q0) > tau:
        n += 1
        deltaNewton(p1,q0,f,fprime,tau,n)
    
    return



# f = lambda x: (2-math.e**(x) +x**2)/3
# f2 = lambda x: (math.e**x/3)**(1/2)
f = lambda x: e**(6*x) + 3*(ln(2))**2 * e**(2*x) - ln(8)*e**(4*x) - (ln(2))**3
fprime = lambda x: 6*e**(6*x) + 6*(ln(2))**2*e**(2*x) - 12*(ln(2))*e**(4*x)
# print(delta(0.5,0,0,f,5))

deltaNewton(0,0,f,fprime,0.0002)