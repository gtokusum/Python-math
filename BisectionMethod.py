import math
import numpy as np

def bisection(f,a,b,tau,n):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Root not in interval")
    m = (a+b)/2
    if np.abs(f(m)) < tau:
        return m,n
    elif np.sign(f(a)) == np.sign(f(m)):
        return bisection(f, m, b, tau,n+1)
    else:
        return bisection(f,a,m,tau,n+1)

if __name__ == "__main__":
    fx = lambda x:x - 2*math.sin(x)
    ans = bisection(fx,1.5,2.5,10**(-5),0)
    print(ans)