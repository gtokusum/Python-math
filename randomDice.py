import random as rn
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
'''
program to show distribution of dice rolls
'''
def getint(n): #n = the number of sides of the die
    return rn.randint(1,n) + rn.randint(1,n)

#dice = number of sides, exp = number of rolls 
def plot(dice,exp):
    #get random dice rolls
    y = [getint(dice) for i in range(exp)]

    #calculate occurence of each value and add to dict
    z = {}
    for i in range(2,dice*2+1):
        if i not in z:
            z[i] = round(y.count(i)/exp *100,2)
    for i in z:
        print(i,z[i])
    
    #set histogram
    Nbins = dice*2-1
    plt.hist(y,bins=Nbins,density=True,alpha=0.5,color='b')
    mu,std = norm.fit(y)
    xmin,xmax = plt.xlim()
    x = np.linspace(xmin,xmax,100)
    p = norm.pdf(x,mu,std)
    plt.plot(x,p,'k',linewidth=2)
    plt.xlabel('rolled values')
    plt.ylabel('rolled percentage')
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)
    plt.show()
    
plot(6,100000)


