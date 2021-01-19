import random as rn
import matplotlib.pyplot as plt
import math

def get_random(n):
	x = []
	for _ in range(n):
		x.append(rn.random())
	return x


def plot(n):
	x = get_random(n)
	y = get_random(n)
	in_circ = []
	for i in range(n):
		if math.sqrt(y[i]**2 + x[i]**2) < 1:
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
	print('estimated value of pi =',plot(1000000))