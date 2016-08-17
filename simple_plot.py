import numpy as np
import scipy as scy
import scipy.integrate
import matplotlib as mpl
import pylab as plt
import matplotlib.cm as cm
import scipy.optimize as opt
from matplotlib import rc
import matplotlib.gridspec as gridspec
import matplotlib.cm as cm
import matplotlib.ticker as mtick

# First use numpy to read in a text file with data. Skiprows=1 skips the first line
xdata, ydata, yerror = np.loadtxt("test.dat", skiprows=1, unpack=True)


#Plot using matplotlib and pylab
plt.plot(xdata,ydata, linewidth=0, color='black', marker="o")
plt.axis([0, 11, 0, 11])
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Title")
plt.show()

