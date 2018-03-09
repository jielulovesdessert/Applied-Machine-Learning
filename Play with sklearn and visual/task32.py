# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 06:51:50 2018

@author: Jie Lu
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris

#read and get data
iris_dataset = load_iris()
setosa = iris_dataset.data[iris_dataset.target == 0]
versicolor = iris_dataset.data[iris_dataset.target == 1]
virginica = iris_dataset.data[iris_dataset.target == 2]

#draw the graph
fig, ax = plt.subplots(4, 4, figsize = (15,15))
for i in range(0,4):
    for j in range(0,4):
        if i == j:
            ax[i,j].hist(np.append(setosa[:,i],[versicolor[:,i],virginica[:,i]]),bins=20)
        else:
            ax[j,i].scatter(setosa[:,i], setosa[:,j])
            ax[j,i].scatter(versicolor[:,i], versicolor[:,j])
            ax[j,i].scatter(virginica[:,i], virginica[:,j])
            ax[j,i].legend(('setosa','versicolor','virginica'))

#set labels
for i in range(0,4):            
    ax[i,0].set_ylabel(iris_dataset['feature_names'][i])
    ax[3,i].set_xlabel(iris_dataset['feature_names'][i])

plt.savefig("task32_graph.png")