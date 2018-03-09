# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 05:13:11 2018

@author: Jie Lu
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

#read data
df = pd.read_csv('task31_data.csv', sep = ',')

#get title and axis
title = "Divorce vs margarine (US)"
yaxis_1 = list(df)[1]
yaxis_2 = list(df)[2]

#get data
divorce = np.array(df["Divorce rate in Maine"])
margarine = np.array(df["Per capita consumption of margarine (US)"])
year = np.array(df["year"])

#save the image
plt.figure()
ax1 = plt.gca()
plt.xticks(year)
line1, = ax1.plot(year, divorce, c = 'b')
ax2 = ax1.twinx()
line2, = ax2.plot(year, margarine, c = 'y')
plt.legend((line1, line2),('Divorce rate in Maine',
                           'Per capita consumption of margarine (US)'))
ax1.set_ylabel(yaxis_1)
ax2.set_ylabel(yaxis_2)
plt.suptitle(title)
plt.savefig("task31_graph.png")