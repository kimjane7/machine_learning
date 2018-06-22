import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os
import sys
from pylab import *
matplotlib.rcParams['font.family'] = "serif"
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter


plt.figure(figsize=(6,6))
fig = plt.figure(1)
axes = plt.gca()
axes.set_xlim([-24,24])
axes.set_ylim([-24,24])
axes.tick_params(labelsize=12)

file = np.loadtxt("cell_stats.dat",unpack=True)
#axes.scatter(file[1], file[3], alpha= 0.5, color='darkcyan',edgecolor='k',linewidth=0.3)
axes.errorbar(file[1],file[3],yerr=file[6],fmt='o',mfc='darkcyan',alpha=0.5,mew=0.3, mec='k',ms='4')

X = [-24,24]
left_bound = [-15,-15]
right_bound = [15,15]
plt.plot(X, X, color='k',linewidth=1)
plt.plot(left_bound, X, color='k',linewidth=1,linestyle='--')
plt.plot(right_bound, X, color='k',linewidth=1,linestyle='--')
plt.plot(X, left_bound, color='k',linewidth=1,linestyle='--')
plt.plot(X, right_bound, color='k',linewidth=1,linestyle='--')

plt.legend(loc=1, shadow=True, fontsize=12)
plt.xlabel(r'$x_{center}$ (mm)', fontsize=12, weight='normal', family='serif')
plt.ylabel(r'$x_{avg}$ (mm)', fontsize=12, weight='normal', family='serif')
plt.title(r'$x_{center}$ vs. $x_{avg}$', fontsize=12, weight='normal', family='serif')
plt.tight_layout()

figname = 'X_stats'+'.png'
plt.savefig(figname, format='png')
os.system('okular '+figname)
plt.clf()



plt.figure(figsize=(6,6))
fig = plt.figure(1)
axes = plt.gca()
axes.set_xlim([-24,24])
axes.set_ylim([-24,24])
axes.tick_params(labelsize=12)

axes.scatter(file[2], file[4], alpha= 0.5, color='darkcyan',edgecolor='k',linewidth=0.3)

X = [-24,24]
left_bound = [-15,-15]
right_bound = [15,15]
plt.plot(X, X, color='k',linewidth=1)
plt.plot(left_bound, X, color='k',linewidth=1,linestyle='--')
plt.plot(right_bound, X, color='k',linewidth=1,linestyle='--')
plt.plot(X, left_bound, color='k',linewidth=1,linestyle='--')
plt.plot(X, right_bound, color='k',linewidth=1,linestyle='--')

plt.legend(loc=1, shadow=True, fontsize=12)
plt.xlabel(r'$y_{center}$ (mm)', fontsize=12, weight='normal', family='serif')
plt.ylabel(r'$y_{avg}$ (mm)', fontsize=12, weight='normal', family='serif')
plt.title(r'$y_{center}$ vs. $y_{avg}$', fontsize=12, weight='normal', family='serif')
plt.tight_layout()

figname = 'Y_stats'+'.png'
plt.savefig(figname, format='png')
os.system('okular '+figname)
plt.clf()