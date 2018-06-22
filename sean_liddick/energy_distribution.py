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

for j in range(0,12):
	file = np.loadtxt("total_energies.dat",unpack=True)
	n, bins, patches = plt.hist(file[1], 150, linewidth=1, facecolor='darkcyan', alpha=0.75)

plt.legend(loc=1, shadow=True, fontsize=12)
plt.xlabel('Total Energy of Event (keV)', fontsize=12, weight='normal', family='serif')
plt.ylabel('Count', fontsize=12, weight='normal', family='serif')
plt.title('Energy Distribution', fontsize=12, weight='normal', family='serif')
plt.tight_layout()

figname = 'energy_distribution'+'.png'
plt.savefig(figname, format='png')
os.system('okular '+figname)
plt.clf()


