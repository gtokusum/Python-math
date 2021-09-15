from sympy import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')


def singDeriv(fx):
    # x = Symbol('x')
    return fx.diff(x)


def multiDeriv(fx, wrF, wrS):
    fxPrime = fx.diff(wrF)
    fxPrime = fxPrime.diff(wrS)
    return fxPrime

# print(multiDeriv(x**4+x*y**4,x,y))

