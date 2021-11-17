import numpy as np
import random
import matplotlib.pyplot as plt

#Function that produces either -1 or 1 with equal chance
def randstep(e):
    return e if random.random() < 0.5 else -e

#Variables
N = np.arange(100,10000,100)
e = 2
R = []

#Looping over all values of N
for n in N:
    r_array = []
    
    #Taking 100 tries
    for i in range(100):
      r = 0

      #Taking n steps
      for _ in range(n):
        r += randstep(e)
      r_array.append(np.abs(r))

    #Calculating RMS
    r_array = np.array(r_array)  
    R.append(np.sqrt(np.mean(r_array**2)))

#Plotting
plt.plot(N,R,label="Measurement")
plt.plot(N,e*np.sqrt(N),label="Theory")
plt.legend()
plt.xlabel("N")
plt.ylabel("R")
plt.show()
    
