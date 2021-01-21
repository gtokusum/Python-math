from scipy.misc import derivative

def f(x):
    return x**2

print(derivative(f,1))