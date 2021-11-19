import numpy as np
import random
import matplotlib.pyplot as plt

def gauss(x,mu,sigma):
  return (1/np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

mu = 0
sigma1 = 1
sigma2 = np.arange(0.1,1.6,0.05)
R = [1000,10000,100000]
z_vals = []
var_vals= []

for r in R:
  for sigma in sigma2:
   x = np.random.normal(mu,sigma,r)
   P = gauss(x,mu,sigma1)
   Q = gauss(x,mu,sigma) 
   Z = np.mean(P/Q)
   var = np.var(P/Q)
   z_vals.append(Z)
   var_vals.append(np.sqrt(var))


plt.plot(sigma2,z_vals[:len(sigma2)],label="1000")
plt.plot(sigma2,z_vals[len(sigma2):2*len(sigma2)],label="10000")
plt.plot(sigma2,z_vals[2*len(sigma2):],label="100000")
plt.legend()
plt.show()

plt.plot(sigma2,var_vals[:len(sigma2)],label="1000")
plt.plot(sigma2,var_vals[len(sigma2):2*len(sigma2)],label="10000")
plt.plot(sigma2,var_vals[2*len(sigma2):],label="100000")
plt.ylim(0,10)
plt.legend()
plt.show()
