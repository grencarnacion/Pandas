# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:26:15 2019

@author: GERALD
"""

import pandas as pd

cars = pd.read_csv('cars.csv')
first = cars.head()
last = cars.tail()

