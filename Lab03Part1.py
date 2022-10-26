#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 12:09:38 2022

@author: keithcheng
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
car = pd.read_csv('accord_sedan.csv')
#plt.scatter(car.price, car.mileage)
#plt.boxplot(car.price)
#plt.boxplot(car.mileage)

pm = np.mean(car.price)#mean of price
psd = np.std(car.price)#standard deviation of price
mm = np.mean(car.mileage)#mean of mileage
msd = np.std(car.mileage)#standard deviation of mileage

car['isOutlierPrice']=np.where(abs((car.price - pm)/psd)>2,1,0)
car['isOutlierMileage']=np.where(abs((car.mileage - mm)/msd)>2,1,0)

import collections as cd
print(cd.Counter(car['isOutlierPrice']))
print(cd.Counter(car['isOutlierMileage']))

colorcol=[]

for i in range(len(car)):
    if car['isOutlierPrice'][i]==1:
        colorcol.append("orange")
    elif car['isOutlierMileage'][i]==1:
        colorcol.append("red")
    else:
        colorcol.append("lightblue")
        
plt.scatter(car.price, car.mileage,color=colorcol)

# =============================================================================
# threshold = 2
# outlier = []
# for i in car.price:
#     z = (i-pm)/psd
#     if z > threshold:
#         outlier.append(i)
# print('outlier in dataset is', outlier)
# =============================================================================

# =============================================================================
# threshold = 2
# outlier = []
# for i in car.price:
#     z = (i-pm)/psd
#     if z > threshold:
#         outlier.append(1)
#     elif z < threshold:
#         outlier.append(0)
# isOutlierPrice = pd.DataFrame(outlier)
# car=car.append(isOutlierPrice)
# =============================================================================

