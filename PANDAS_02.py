# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:28:51 2019

@author: GERALD
"""

import pandas as pd

cars = pd.read_csv('cars.csv')
X = cars[cars['Model'] == 'Mazda RX4']
Y = cars.loc[cars['Model'] == 'Camaro Z28' , ['cyl'] ]
Z = cars.loc[(cars['Model'] == 'Mazda RX4 Wag') | (cars['Model'] == 'Ford Pantera L') | 
        (cars['Model'] == 'Honda Civic'), ['cyl','gear'] ]