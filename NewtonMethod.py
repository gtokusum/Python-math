import math
from scipy.misc import derivative


def getPs(f,fprime,a):
    p = a
    p1 = p - (f(p) /fprime(p))
    return p1


def Newton(f,fprime,a,tau=10**-5):
    n = 1
    p = 0
    p1 = a
    while abs(p-p1) > tau:
        # print(abs(p-p1))
        p = p1
        p1 = p - f(p)/fprime(p)
        # print(n,p1)
        n+=1
    return n,p1

e = math.e
ln = math.log



f = lambda x: e**(6*x) + 3*(ln(2))**2 * e**(2*x) - ln(8)*e**(4*x) - (ln(2))**3
fprime = lambda x: 6*e**(6*x) + 6*(ln(2))**2*e**(2*x) - 12*(ln(2))*e**(4*x)
# print(Newton(f,fprime,-0.05113676593,0.0002)) 
# po = [-1,0,1,3,5,10]
# print(abs(-0.18288825721176558+0.18288825721176558))
# for i in po:
#     print(i)
#     print(Newton(f,fprime,i))
#     print("\n\n")