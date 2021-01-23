import random as rn
import matplotlib.pyplot as plt
import math

#getting random floats from 0-1
def get_random(n):
	x = []
	for _ in range(n):
		x.append(rn.random())
	return x

#n = number of points
def plot(n):
	x = get_random(n)
	y = get_random(n)
	in_circ = []
	
	#calculates if the point is inside the unit circle
	for i in range(n):
		if math.sqrt(y[i]**2 + x[i]**2) <= 1:
			in_circ.append((x[i],y[i]))
	pi_est = 4*len(in_circ) / n
	# pi_error = abs(pi_est/math.pi - 1)
	# print('error: ',pi_error)
	# fig,ax = plt.subplots()
	# ax.set(xlabel = 'x-axis',ylabel='y-axis',title='pi estimate = {}'.format(pi_est))
	# plt.plot(x,y,'r *')
	# plt.show()
	return pi_est

if __name__ == '__main__':
	data = []
	for i in range(10):
		pi = plot(1000000)
		print('estimated value of pi =',pi)
		data.append(pi)
	print('Average value of pi =',sum(data)/len(data))