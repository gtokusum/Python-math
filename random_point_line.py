import random as rn 
import matplotlib.pyplot as plt
import numpy as np 
import math 

def get_points(n):
	x = []
	for _ in range(n):
		x.append(rn.random())
	return x



def plot(n):
	x = get_points(n)
	y = get_points(n)

	under_line = []
	for i in range(n):
		if y[i] < x[i]:
			under_line.append((x[i],y[i]))
	# fig,ax = plt.subplots()
	# ax.set(xlabel='x-axis',ylabel='y-axis',title='ration of points under y=x == {}'.format(len(under_line)/n))
	# plt.plot(x,y,'r *')
	# z = np.linspace(0,1,100)
	# plt.plot(z,z)
	# plt.show()
	return len(under_line)/n

if __name__ == '__main__':
	print(plot(10000))