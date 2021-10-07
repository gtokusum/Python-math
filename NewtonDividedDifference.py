import numpy as np
import math

def NewtonDivDiff(x,y):
    n = len(x)
    f = np.zeros((n,n),dtype=np.float64)
    f[:,0] = y
    for i in range(1,n):
        for j in range(1,i+1):
            f[i,j] = (f[i,j-1] - f[i-1,j-1])/(x[i] - x[i-j])
    return f

def xterms(x,x0,i):
    lastP = 1
    for j in range(i+1):
        # print(x[j])
        lastP *= (x0 - x[j])
    return lastP


def poly(f,x,y,x0):
    n = len(x) - 1
    p = []
    p.append(y[0] + f[1,1]*(x0-x[0]))
    for i in range(1,n):
        p.append(p[i-1]+ f[i+1,i+1]*xterms(x,x0,i))
    return p
    




xa = [0.6,0.7,0.8,1.0]
x = np.asarray(xa)
ya =[-0.17694460,0.013775227,0.22363362,0.65809197]
y = np.asarray(ya)
f = NewtonDivDiff(x,y)
print(f)
print(poly(f,x,y,0.9))