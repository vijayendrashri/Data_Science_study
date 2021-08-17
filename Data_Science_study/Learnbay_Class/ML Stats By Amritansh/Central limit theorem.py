#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani

# 2000 simulation for Die roll
n=1000

# In each simulation there is one  trial
avg=[]
for i in range(2,n):
    a = np.random.randint(1,7,n)
    avg.append(np.average(a))
    
print(avg[:3])
#function that plot the histogram
def clt(current):
    plt.cla()
    if current==1000:
        a.event_source.stop()
    plt.hist(avg[0:current])
    plt.gca().set_title('Expected value of die roll')
    plt.gca().set_xlabel('Avg from die roll')
    plt.gca().set_ylabel('Frequency')
    plt.annotate('Die roll ={}'.format(current),[3,27])

fig=plt.figure()
a = ani.FuncAnimation(fig,clt,interval=5)
plt.show()
