import math
from scipy.misc import derivative



def Newton(f,fprime,a,b,tau=10**-5):
    n = 1
    p = 0
    p1 = a
    while abs(p-p1) > tau:
        p = p1
        p1 = p - f(p)/fprime(p)
        print(n,p1)
        n+=1
    return n,p1

f = lambda x: math.e**x + 2**(-x) + 2*math.cos(x)-6
fprime = lambda x: math.e**x - math.log(x)*2**(-2) - 2*math.sin(x)
print(Newton(f,fprime,1,2)) 

    