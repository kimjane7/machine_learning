import os
import sys
import numpy as np
from numpy import linalg
import sklearn.linear_model as skl
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
matplotlib.rcParams['font.family'] = "serif"


def calc_R2(y,ytilde):

	return 1.0 - np.sum((y-ytilde)**2) / np.sum((y-np.mean(ytilde))**2)

def calc_MSE(y,ytilde):

	return np.sum((y-ytilde)**2)/len(y)


# dictionary to store R2 and MSE
results = {}

# generate n random data points
n = 100
x = np.random.uniform(0.0,1.0,n)

# quadratic polynomial with noise
a0, a1, a2 = np.random.uniform(0.0,5.0,3)
gamma = 10.0
y = a0 - a1*x + a2*x**2 + gamma*np.random.normal(0.0,1.0)

# build design matrix for quadratic polynomial
X = np.zeros((n,3))
X[:,0] = 1
X[:,1] = x
X[:,2] = x**2

# ordinary least squares
beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

# make prediction using OLS
ytilde = X @ beta
R2 = calc_R2(y,ytilde)
MSE = calc_MSE(y,ytilde)
results['my OLS'] = (R2,MSE)

# plot
fig, ax = plt.subplots()
ax.set_xlim([0.0,1.0])
ax.set_xlabel(r'$x$')
ax.set_title(r'Least squares fit of a random quadratic polynomial')
ax.scatter(x,y,c='g',s=100,linewidth=0.0,label=r'data')
ax.scatter(x,ytilde,c='r',s=60,linewidth=0.0,label=r'ordinary linear regression')

# make prediction using scikit-learn and plot
fit = skl.LinearRegression().fit(X,y)
ytilde = fit.predict(X)
R2 = r2_score(y,ytilde)
MSE = mean_squared_error(y,ytilde)
results['skl OLS'] = (R2,MSE)
ax.scatter(x,ytilde,c='b',s=25,linewidth=0.5,label=r'scikit-learn linear regression')

fit = skl.Ridge(alpha=0.1).fit(X,y)
ytilde = fit.predict(X)
R2 = r2_score(y,ytilde)
MSE = mean_squared_error(y,ytilde)
results['skl ridge'] = (R2,MSE)
ax.scatter(x,ytilde,c='purple',s=25,linewidth=0.5,label=r'scikit-learn ridge regression ($\lambda = 0.1$)')

print(results)
ax.legend()
plt.show()



