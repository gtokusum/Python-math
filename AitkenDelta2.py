import math

def getPs(p0,pn):
    p1 = pn(p0)
    p2 = pn(p1)
    return p1,p2


def delta(p0,p1,p2,pn,n):
    if n == 0:
        return
    else:
        p1,p2=getPs(p0,pn)
        q = p0 - (p1-p0)**2 /(p2 -2*p1 +p0)
        print(q)
        delta(p1,0,0,pn,n-1)
    return 


f = lambda x: (2-math.e**(x) +x**2)/3
f2 = lambda x: (math.e**x/3)**(1/2)

# print(delta(0.5,0,0,f,5))
print(delta(0.75,0,0,f2,5))
