import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.patches as patches
import numpy as np
import scipy.stats as stats
import os
import sys
from pylab import *
matplotlib.rcParams['font.family'] = "serif"
from matplotlib import ticker
from matplotlib.ticker import ScalarFormatter
 

for i in range(0,256):

	print(i)
	file = np.loadtxt("celldata/cell"+str(i)+".dat",unpack=True)

	#HISTOGRAMS OF RADIAL DISTANCES FROM AVERAGE

	'''
	plt.figure(figsize=(6,6))
	fig = plt.figure(1)
	axes = plt.gca()
	axes.set_xlim([0,30])
	axes.tick_params(labelsize=12)

	avg_x = np.mean(file[0]);
	avg_y = np.mean(file[1]);
	r = ((file[0]-avg_x)**2+(file[1]-avg_y)**2)**0.5
	n, bins, patches = plt.hist(r, 60, linewidth=1, facecolor='darkcyan', alpha=0.75)

	plt.legend(loc=1, shadow=True, fontsize=12)
	plt.xlabel('Radial Distance from Average (mm)', fontsize=12, weight='normal', family='serif')
	plt.ylabel('Count', fontsize=12, weight='normal', family='serif')
	plt.title('Cell '+str(i), fontsize=12, weight='normal', family='serif')
	plt.tight_layout()

	figname = 'histogram'+str(i)+'.png'
	plt.savefig(figname, format='png')
	#os.system('okular '+figname)
	plt.clf()
	'''


	#PROBABILITY DENSITY OF RADIAL DISTANCE FROM CENTER
	'''
	
	plt.figure(figsize=(6,6))
	fig = plt.figure(1)
	axes = plt.gca()
	axes.set_xlim([0,30])
	axes.set_ylim([0,1])
	axes.tick_params(labelsize=12)

	center_x = 3.0*floor(i/16.0)-22.5
	center_y = 3.0*(i%16)-22.5
	r = ((file[0]-center_x)**2+(file[1]-center_y)**2)**0.5

	plt.hist(r, bins=np.arange(0.0, 20.1, 0.1), normed=True, edgecolor='k',linewidth=0.5, facecolor='k', alpha=0.3)
	xt = plt.xticks()[0]
	xmin, xmax = min(xt), max(xt)
	lnspc = np.linspace(xmin, xmax, len(r))

	a,b,c = stats.fisk.fit(r)
	pdf_norm = stats.fisk.pdf(lnspc,a,b,c)
	plt.plot(lnspc, pdf_norm, linewidth=1, color='b', label='fisk')

	cellx = int(np.floor(i/16.0)+1)
	celly = int((i%16)+1)

	plt.legend(loc=1, shadow=True, fontsize=12)
	plt.xlabel('Radial Distance from Center (mm)', fontsize=12, weight='normal', family='serif')
	plt.ylabel('Probability', fontsize=12, weight='normal', family='serif')
	plt.title('Cell ['+str(cellx)+','+str(celly)+']', fontsize=12, weight='normal', family='serif')
	plt.tight_layout()

	figname = 'probdens'+str(i)+'.png'
	plt.savefig(figname, format='png')
	#os.system('okular '+figname)
	plt.clf()
	'''


	#SCATTER PLOTS OF INITIAL POSITIONS WITH PROJECTED HISTOGRAMS

	
	left, width = 0.1, 0.65
	bottom, height = 0.1, 0.65
	bottom_h = left_h = left + width + 0.02

	rect_scatter = [left, bottom, width, height]
	rect_histx = [left, bottom_h, width, 0.2]
	rect_histy = [left_h, bottom, 0.2, height]

	plt.figure(1, figsize=(8, 8))

	axScatter = plt.axes(rect_scatter)
	axHistx = plt.axes(rect_histx)
	axHisty = plt.axes(rect_histy)

	axScatter.scatter(file[0], file[1], c=file[2], cmap='cool', vmin=0.0, vmax=3060.0, alpha=0.3, linewidth=0.5)
	axScatter.set_xlim([-24,24])
	axScatter.set_xlim([-24,24])

	binwidth = 0.1
	xymax = np.max([np.max(np.fabs(file[0])), np.max(np.fabs(file[1]))])
	lim = 15

	axScatter.set_xlim((-lim, lim))
	axScatter.set_ylim((-lim, lim))

	bins = np.arange(-lim, lim + binwidth, binwidth)
	axHistx.hist(file[0], bins=bins, normed=True, facecolor='darkcyan', alpha=0.5, linewidth=0.0)
	axHisty.hist(file[1], bins=bins, normed=True, facecolor='darkcyan', alpha=0.5, linewidth=0.0,orientation='horizontal')

	axHistx.set_xlim(axScatter.get_xlim())
	axHisty.set_ylim(axScatter.get_ylim())

	nullfmt = NullFormatter() 
	axHistx.xaxis.set_major_formatter(nullfmt)
	axHisty.yaxis.set_major_formatter(nullfmt)
	axHisty.locator_params(axis='x',nbins=5)
	axHistx.locator_params(axis='y',nbins=5)

	
	
	#lnspc = np.linspace(-lim, lim, 1000)
	#a,b,c = stats.gennorm.fit(file[0])
	#pdf_norm = stats.gennorm.pdf(lnspc,a*2,b,c*1.3)
	#axHistx.plot(lnspc, pdf_norm, linewidth=1, color='k')
	#a,b,c = stats.gennorm.fit(file[1])
	#pdf_norm = stats.gennorm.pdf(lnspc,a*2,b,c*1.3)
	#axHisty.plot(pdf_norm, lnspc, linewidth=1, color='k')


	axScatter.set_xlabel(r'$x_0$ (mm)')
	axScatter.set_ylabel(r'$y_0$ (mm)')
	axHisty.set_xlabel('Probability')
	axHistx.set_ylabel('Probability')

	axHistx.tick_params(labelsize=9)
	axHisty.tick_params(labelsize=9)
	axScatter.tick_params(labelsize=9)
	rect = patches.Rectangle((-24+floor(i/16.0)*3,-24+(i%16)*3),3,3,linewidth=1.5,edgecolor='k',facecolor='None')
	axScatter.add_patch(rect)

	cellx = int(np.floor(i/16.0)+1)
	celly = int((i%16)+1)

	axScatter.text(19, 20, '['+str(cellx)+','+str(celly)+']',fontsize=20,verticalalignment='center',horizontalalignment='left')
	figname = 'cell'+str(i)+'.png'
	plt.savefig(figname, format='png')
	#os.system('okular '+figname)
	plt.clf()
	
	''' RADIAL DISTANCE VS ENERGY DEPOSITED HEXBIN

	plt.figure(figsize=(8,6))
	fig = plt.figure(1)
	axes = plt.gca()
	axes.set_xlim([0,3060])
	#axes.set_ylim([0,30])
	axes.tick_params(labelsize=12)

	center_x = 3.0*floor(i/16.0)-22.5
	center_y = 3.0*(i%16)-22.5
	r = ((file[0]-center_x)**2+(file[1]-center_y)**2)**0.5

	hb = axes.hexbin(file[2],r,gridsize=100,cmap='inferno',vmin=0.0, vmax=2.5, bins='log')
	cb = plt.colorbar(hb,ax=axes)
	cb.set_label('log(Count)')


	cellx = int(np.floor(i/16.0)+1)
	celly = int((i%16)+1)

	plt.legend(loc=1, shadow=True, fontsize=12)
	plt.xlabel('Energy Deposited (keV)', fontsize=12, weight='normal', family='serif')
	plt.ylabel('Radial Distance from Center (mm)', fontsize=12, weight='normal', family='serif')
	plt.title('Cell ['+str(cellx)+','+str(celly)+']', fontsize=12, weight='normal', family='serif')
	plt.tight_layout()

	figname = 'energy'+str(i)+'.png'
	plt.savefig(figname, format='png')
	#os.system('okular '+figname)
	plt.clf()
	'''