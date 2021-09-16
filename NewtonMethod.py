import math
from scipy.misc import derivative



def Newton(f,fprime,a,tau=10**-5):
    n = 1
    p = 0
    p1 = a
    while abs(p-p1) > tau:
        p = p1
        p1 = p - f(p)/fprime(p)
        # print(n,p1)
        n+=1
    return n,p1

f = lambda x: 4*(x**2) - math.e**x - math.e**(-x)
fprime = lambda x: 8*x -math.e**x + math.e**(-x)
# print(Newton(f,fprime,-3)) 
po = [-1,0,1,3,5,10]

for i in po:
    print(i)
    print(Newton(f,fprime,i))
    print("\n\n")