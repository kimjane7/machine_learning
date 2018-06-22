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
axes.set_xlim([0,40])
axes.tick_params(labelsize=12)

for i in range(0,256):
	file = np.loadtxt("celldata/cell"+str(i)+".dat",unpack=True)
	avg_x = np.mean(file[0]);
	avg_y = np.mean(file[1]);
	r = ((file[0]-avg_x)**2+(file[1]-avg_y)**2)**0.5
	n, bins, patches = plt.hist(r, 40, linewidth=1, facecolor='darkcyan', alpha=0.75)

	plt.legend(loc=1, shadow=True, fontsize=12)
	plt.xlabel('Radial Distance from Average (mm)', fontsize=12, weight='normal', family='serif')
	plt.ylabel('Count', fontsize=12, weight='normal', family='serif')
	plt.title('Cell '+str(i), fontsize=12, weight='normal', family='serif')
	plt.tight_layout()

	figname = 'cell'+str(i)+'.png'
	plt.savefig(figname, format='png')
	#os.system('okular '+figname)
	plt.clf()

