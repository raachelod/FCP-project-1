#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:13:07 2022

@author: rachelodwyer
"""
import pandas as pd
import matplotlib.pyplot as plt

#reading csv files 
APR20AUG20 = pd.read_csv('Ap20-Au20-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')
AUG20APR21 = pd.read_csv('Au20-Ap21-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')
APR21NOV21 = pd.read_csv('Ap21-No21-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')
NOV21APR22 = pd.read_csv('No21-Ap22-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')



#merging data 
APR20APR21 = pd.merge(APR20AUG20, AUG20APR21, on= 'Name')
APR21APR22 = pd.merge(APR21NOV21, NOV21APR22, on= 'Name')
APR20APR22 =pd.merge(APR20APR21,APR21APR22, on = 'Name')

print(APR20APR22)

#plotting data
APR20APR22 = APR20APR22.T
england_series = APR20APR22['ENGLAND']
england_series.plot(label = 'England (total)')
east_england = APR20APR22['East of England']
east_england.plot(label = 'East England')
london = APR20APR22['London']
london.plot(label = 'London')
midlands = APR20APR22['Midlands']
midlands.plot(label = 'Midlands')
ne_yorkshire = APR20APR22['North East and Yorkshire' ]
ne_yorkshire.plot(label = 'North East and Yorkshire')
northwest = APR20APR22['North West']
northwest.plot(label = 'North West')
southeast = APR20APR22['South East']
southeast.plot(label = 'South East')
southwest = APR20APR22['South West']
southwest.plot(label = 'South West')
plt.xlabel('Months during COVID-19')
plt.ylabel('Number of hospital admissions')
plt.title('Hospital admissions during COVID-19 across UK')
plt.legend()
plt.show()

#make this an option to save figure
#plt.savefig('linegraph.png')

