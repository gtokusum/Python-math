import numpy as np
import math
def neville(x,y,x0):
    n = len(x)
    q = np.zeros((n,n),dtype=np.float64)
    q[:,0] = y
    for i in range(1,n):
        for j in range(1,i+1):
            q[i, j] = ((x0 - x[i-j])*q[i,j-1] - (x0-x[i])*q[i-1,j-1]) / (x[i]-x[i-j])
    return q

xa = [0,1,2,4,5]
x =  np.asarray(xa)
f = lambda z: math.sqrt(z)
y = np.asarray([f(i) for i in xa])
x0 = 3
print(neville(x,y,x0))