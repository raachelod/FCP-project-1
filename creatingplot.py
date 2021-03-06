#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 18:13:07 2022

@author: rachelodwyer
"""
import pandas as pd
import matplotlib.pyplot as plt


#reading excel files 
APR20AUG20 = pd.read_csv('Apr20-Aug20.csv', index_col = 'Name', parse_dates= True, thousands= ',')
AUG20APR21 = pd.read_csv('Aug20-Apr21.csv', index_col = 'Name', parse_dates= True, thousands= ',')
APR21AUG21 = pd.read_csv('Ap21-Aug21.csv', index_col = 'Name', parse_dates= True, thousands= ',')
AUG21APR22 = pd.read_csv('Aug21-Apr22.csv', index_col = 'Name', parse_dates= True, thousands= ',')
                                          
#merging data by year
APR20APR21 = pd.merge(APR20AUG20, AUG20APR21, on= 'Name')
APR21APR22 = pd.merge(APR21AUG21, AUG21APR22, on= 'Name')
APR20APR22 =pd.merge(APR20APR21,APR21APR22, on = 'Name')

#print(APR20APR22)

#saving the merged data file to reuse and/or view seperately 
#APR20APR22.to_csv('merged_data.csv')

#make this a class - different types of plots
#plotting data
APR20APR22 = APR20APR22.T
england = APR20APR22['ENGLAND']
east_england = APR20APR22['East of England']
east_england.plot(label = 'East England', lw = 1 )
london = APR20APR22['London']
london.plot(label = 'London', lw = 1 )
midlands = APR20APR22['Midlands']
midlands.plot(label = 'Midlands', lw = 1 )
ne_yorkshire = APR20APR22['North East and Yorkshire' ]
ne_yorkshire.plot(label = 'North East and Yorkshire', lw = 1 )
northwest = APR20APR22['North West']
northwest.plot(label = 'North West', lw = 1 )
southeast = APR20APR22['South East']
southeast.plot(label = 'South East', lw = 1 )
southwest = APR20APR22['South West']
southwest.plot(label = 'South West', lw = 1 )
plot1 = plt.figure(1)
plt.title('Hospital admissions during COVID-19 across UK')
plt.xlabel('Months during COVID-19')
plt.ylabel('Number of hospital admissions')
plt.legend()

plot2 = plt.figure(2)
plt.plot(england, color = 'blue', lw = 1)
plt.title('Hospital admissions during COVID-19 in England')
plt.xlabel('Months during COVID-19')
plt.ylabel('Number of hospital admissions')
   
plot3 = plt.figure(3)
plt.plot(southwest, color = 'grey', lw = 1)
plt.title('Hospital admissions during COVID-19 in South West England')
plt.xlabel('Months during COVID-19')
plt.ylabel('Number of hospital admissions')
#plt.savefig('southwest_data.pdf')


plt.show()



