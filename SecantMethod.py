import math


def Secant(f,a,b,tau):
    p0 = a
    p1 = b
    n = 1
    while abs(p1-p0) > tau:
        tmp = p1
        p1 = p1 - f(p1)*((p1-p0)/(f(p1)-f(p0)))
        p0 = tmp
        n += 1
        print(n,p1)
    return (n,p1)


f = lambda x: (x-2)**2 - math.log(x)

print(Secant(f,1,2,10**-5))
