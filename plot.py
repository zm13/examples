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

#Use scipy.optimize.curvefit task to fit a linear line

#First define the function you want to fit
def lsq(x, a, b):
    return a + b*x

#Call scipy.optimize
fit_params, covariance_matrix  = opt.curve_fit(lsq, xdata, ydata, p0=(1,1))

#fit_params[0] is intercept, fit_params[1] is slope for data

fit = lsq(xdata, fit_params[0], fit_params[1])

#Now that the data is fit, we can make plot. First set font of axis labels and title to serif

plt.rc('font', family='serif', size=12)

#Use subplot which can be more flexible. In this case we will use it to only make one plot

example_plot, ((ax1)) = plt.subplots(1, 1)

ax1.errorbar(xdata, ydata, yerr=[yerror, yerror], fmt=' ',  color="black", marker='.')
p1, = ax1.plot(xdata, ydata, color="black", marker='.',linewidth=0, ms=10)
p2, = ax1.plot(xdata,  fit, linewidth=1, ls="-",color="blue")

ax1.set_ylabel('X Data')
ax1.set_xlabel('Y Data')

#Change size of axi tick marks and labels
ax1.yaxis.label.set_size(26)
ax1.xaxis.label.set_size(26)
ax1.tick_params(axis='both', which='major', labelsize=20)
ax1.tick_params(axis='both', which='major', labelsize=20)

#Arrange tick marks
ax1.xaxis.set_ticks(np.arange(0, 12, 3)) #Tick marks from 0 to 12 on the axis, with a mark every 3 points
ax1.yaxis.set_ticks(np.arange(0, 12, 2))
ax1.set_ylim(0,11)
ax1.set_xlim(0, 11)

ax1.legend([p1, p2], ['Example Data', 'Example Fit'],loc=2, prop={'size':24}, numpoints=1)

#save plot to pdf if you would like
#example_plot.set_size_inches(5,5)
#example_plot.savefig('example_plot.pdf', bbox_inches='tight')
plt.show()

