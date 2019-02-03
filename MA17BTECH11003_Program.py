import itertools
import numpy as np
import matplotlib.pyplot as plt
from math import *
from tkinter import *
from scipy.stats import bernoulli
epsilon=0.075; n=100; Pn_found = []
H=(0.25*log(1/0.25,2))+(0.75*log(1/0.75,2))																				#this is the entropy H(X)
while n<=700:	
	non_epsilon_typical_vectors_found = 0
	for _ in itertools.repeat(None,2000000):		
		random_vector = np.array(bernoulli.rvs(0.25, size =n))															#generated n length binary random variable with prob(0)=0.75
		d1 = random_vector.sum()
		d0 = n-d1																										#d0 and d1 are the number of 0s and 1s respectively in random_vector
		cmp = ((d0*log(0.75,2)+(d1*log(0.25,2))))*(-1/n*1.0)
		if H-epsilon>cmp  or cmp>H+epsilon:	non_epsilon_typical_vectors_found=non_epsilon_typical_vectors_found+1		#if this happens then random_vector is not epsilon typical
	Pn = non_epsilon_typical_vectors_found/2000000.0																	#Pn is the probability that a randomly drawn random_vector is not epsilon typical	
	print ("n=",n,"Pn=",Pn)
	Pn_found.append(Pn)		
	n=n+100																												#incrementing n for next iteration
y = Pn_found
plt.yscale('log')
x = [100,200,300,400,500,600,700]
plt.scatter(x, y)
plt.ylabel('y axis: P(n) ')
plt.xlabel('x axis: n ')
plt.grid(True)
plt.title("Harsh Raj : MA17BTECH11003\n\nVariation of P(n) with n for Epsilon = 0.075\n")
plt.tight_layout()
for i, txt in enumerate(y):
    plt.annotate("("+str(100*(i+1))+","+((str(txt)))+")", (x[i]+6, y[i]))
plt.show()