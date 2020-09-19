# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 12:47:37 2020

@author: HETSHAH
"""

from sklearn import datasets, linear_model
import pandas as pd
import matplotlib.pyplot as plt
import seaborn.apionly as sns

iris = sns.load_dataset('iris')
fit_data = iris[["petal_length", "petal_width"]].values
x_data = fit_data[:,0].reshape(-1,1)
y_data = fit_data[:,1].reshape(-1,1)
 
# Create linear regression object
regr = linear_model.LinearRegression()
# once the data is reshaped, running the fit is simple
regr.fit(x_data, y_data)
 
# we can then plot the data and out fit
axes = iris.plot(x="petal_length", y="petal_width", kind="scatter")
plt.plot(x_data, regr.predict(x_data), color='black', linewidth=3)
plt.show()