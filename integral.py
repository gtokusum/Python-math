import scipy.integrate as integrate
#py -m pip install 'package'



def get_integral():
	e = input("input eq: ")
	eq = lambda x:eval(e)
	a = int(input("input lower value: "))
	b = int(input("input upper value: "))
	return integrate.quad(eq,a,b)

# print(get_integral())

def double_int():
	f = lambda x,y:x*y**2
	return integrate.dblquad(f,0,2,lambda x:0,lambda x:1)

if __name__ == '__main__':
	#print(get_integral())
	print(double_int())