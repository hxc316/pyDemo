import matplotlib
from numpy import *
import matplotlib.pylab as plt

data=arange(30).reshape(10,3)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(data[:,1],data[:,2])
plt.show()
