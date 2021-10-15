import numpy as np
import math

def hermite(x,f,fx):
    n = len(x)
    q = np.zeros((2*n,2*n),dtype=np.float64)
    z = [0 for i in range(2*n)]
    for i in range(n):
        z[2*i] = x[i]
        z[2*i+1] = x[i]
        q[2*i,0] = f[i]
        q[2*i+1,0] = f[i]
        q[2*i+1,1] = fx[[i]]
        if i > 0:
            q[2*i,1] = (q[2*i,0]-q[2*i-1,0])/(z[2*i]-z[2*i-1])
    print(z)
    for i in range(2,2*n):
        for j in range(2,i+1):
            q[i,j] = (q[i,j-1]-q[i-1,j-1])/(z[i]-z[i-j])
    return q


x = np.asarray([8.3,8.6])
f = np.asarray([17.56492,18.50515])
fp = np.asarray([3.116256,3.151762])

print(hermite(x,f,fp))

