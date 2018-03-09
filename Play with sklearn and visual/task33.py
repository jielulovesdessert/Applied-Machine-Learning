# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:29:11 2018

@author: Jie Lu
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_boston

#load x y data and the feature
boston_data = load_boston()
MEVD = boston_data['target']
data = boston_data['data']
feature = boston_data['feature_names']

#draw and save
fig, axes = plt.subplots(3,5,figsize=(15,10))
k=0
for i in range(3):
    for j in range(5):
        axes[i,j].scatter(data[:,k], MEVD, c = np.random.rand(3,), alpha=0.33)
        axes[i,j].set_xlabel(feature[k])
        if j==0:
             axes[i,j].set_ylabel('MEVD')        
        k+=1
        if k == 13:
            break

plt.savefig("task33.png")