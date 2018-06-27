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
axes.set_xlim([0,3100])
axes.tick_params(labelsize=12)

file = np.loadtxt("energy_bins.dat",unpack=True)
bars = axes.bar(file[0], file[1], 10, color='darkcyan',edgecolor='k',linewidth=0.3)

plt.legend(loc=1, shadow=True, fontsize=12)
plt.xlabel('Total Energy of Event (keV)', fontsize=12, weight='normal', family='serif')
plt.ylabel('Count', fontsize=12, weight='normal', family='serif')
plt.title('Energy Distribution', fontsize=12, weight='normal', family='serif')
plt.tight_layout()

figname = 'energy_distribution'+'.png'
plt.savefig(figname, format='png')
os.system('okular '+figname)
plt.clf()

plt.figure(figsize=(6,6))
fig = plt.figure(1)
axes = plt.gca()
axes.set_xlim([0,3100])
axes.tick_params(labelsize=12)
plt.plot(file[0], file[2]*100, linewidth=2, color='darkcyan')

plt.legend(loc=1, shadow=True, fontsize=12)
plt.xlabel('Total Energy of Event (keV)', fontsize=12, weight='normal', family='serif')
plt.ylabel('Percentage (%)', fontsize=12, weight='normal', family='serif')
plt.title('Cumulative Energy Distribution', fontsize=12, weight='normal', family='serif')
plt.grid(True)
plt.tight_layout()

figname = 'percentile'+'.png'
plt.savefig(figname, format='png')
os.system('okular '+figname)
plt.clf()