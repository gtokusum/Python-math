import scipy.integrate as integrate
#py -m pip install 'package'



def get_integral(f, a, b):
	return integrate.quad(f,a,b)

# print(get_integral())

def double_int():
	f = lambda x,y:x*y**2
	return integrate.dblquad(f,0,2,lambda x:0,lambda x:1)

if __name__ == '__main__':
	print(get_integral(lambda x:x**2,0,1))
	print(double_int())