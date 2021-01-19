# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 01:40:28 2020

@author: Gaku
"""

import numpy as np
import matplotlib.pyplot as plt


# repeat the definition of the test criterion:

def pass_test( x, y ):
  d = y**2 + x**2
  return d<=1

# this function will perform a single "experiment"
# with N trials, the return value of the experiment
# will be the number of trials that passed the
# test criterion defined above

def experiment( N ):

  randX = (np.random.random(N)-0.5)*2
  randY = (np.random.random(N)-0.5)*2

  N_pass = 0

  for i in range( N ):
    if pass_test( randX[i], randY[i] ):
      N_pass += 1

  return N_pass / N

# here you can define the number of experiments to conduct
# and the number of trials for each experiment

N_experiments = 10
N_trials = 1000



# store the results of each experiment in an list called results
results = []
for exp in range( N_experiments ):
  results.append(experiment(N_trials))

# now make a histogram of the results for each experiment
plt.figure(figsize=(10,8))
plt.xlabel('Measured Probability')
plt.ylabel('Number of Experiments')
bin_contents, bin_edges, patch = plt.hist( results, bins=101, range=(-0.005,1.005) )

pie = np.mean(results)*4
uncertainty = np.std(results,ddof=1)/(10**6)**.5
# print some useful information:
print( "Number of experiments conducted:  ", N_experiments )
print( "  Average probability:  ", np.mean(results) )
print( "  Standard deviation:  ", np.std(results,ddof=1) )
print( "Estimated value for pi: ", pie)
print( "Uncertainty of estimate: ", uncertainty)
plt.show()