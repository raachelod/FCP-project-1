#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:13:07 2022

@author: rachelodwyer
"""
import pandas as pd
import matplotlib.pyplot as plt
import proplot as pplt
#import argparse 

#reading excel files 
APR20AUG20 = pd.read_excel('Apr20-Aug20.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')
AUG20APR21 = pd.read_excel('Aug20-Apr21.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')
APR21AUG21 = pd.read_excel('Ap21-Aug21.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')
AUG21APR22 = pd.read_excel('Aug21-Apr22.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')
                     
                     
#merging data by year
APR20APR21 = pd.merge(APR20AUG20, AUG20APR21, on= 'Name')
APR21APR22 = pd.merge(APR21NOV21, NOV21APR22, on= 'Name')
APR20APR22 =pd.merge(APR20APR21,APR21APR22, on = 'Name')

print(APR20APR22)

#saving the merged data file to reuse and/or view seperately 
#APR20APR22.to_csv('merged_data.csv')

#make this a class - different types of plots
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
plot1 = plt.figure(1)
plt.title('Hospital admissions during COVID-19 across UK')
plt.xlabel('Months during COVID-19')
plt.ylabel('Number of hospital admissions')
plt.legend()
   

<<<<<<< HEAD

plot2 = plt.figure(2)
plt.plot(southwest, color = 'grey' )
plt.title('Hospital admissions during COVID-19 in South West England')
plt.xlabel('Months during COVID-19')
plt.ylabel('Number of hospital admissions')
plt.savefig('southwest_data.pdf')
=======
>>>>>>> 947f76c5cce6c3897f95ec63f1b3d1de6ce2c938

plt.show()