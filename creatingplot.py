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

#reading csv files 
APR20AUG20 = pd.read_excel('Apr20-Aug20.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')
AUG20APR21 = pd.read_excel('Aug20-Apr21.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')
APR21NOV21 = pd.read_excel('Ap21-Aug21.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')
NOV21APR22 = pd.read_excel('Aug21-Apr22.xlsx', index_col = 'Name', parse_dates= True, thousands= ',')



#pie chart of data (england)

#APR20AUG20

data_1 = APR20AUG20
data_MAR20 = [d[1:13] for d in APR20AUG20[2]]
data_APR20 = [d[14:43] for d in APR20AUG20[2]]
data_MAY20 = [d[44:74] for d in APR20AUG20[2]]
data_JUN20 = [d[75:104] for d in APR20AUG20[2]]
data_JUL20 = [d[105:135] for d in APR20AUG20[2]]
data_1 = [data_MAR20, data_APR20, data_MAY20, data_JUN20, data_JUL20]

months = ['March 2020', 'April 2020', 'May 2020', 'June 2020', 'July 2020']

colors = ("orange", "cyan", "brown", "indigo", "beige")
fig_1 = plt.figure(figsize = (10,7))
plt.pie(data_1, labels = months)
plt.legend(title = "Month",
           loc = "centre left")
plt.title("Hospitalizations by Month in England from April 2020 to August 2020")
plt.show()



#AUG20APR21

data_2 = AUG20APR21
data_AUG20 = [d[1:30] for d in AUG20APR21[2]]
data_SEPT20 = [d[31:60] for d in AUG20APR21[2]]
data_OCT20 = [d[61:91] for d in AUG20APR21[2]]
data_NOV20 = [d[92:121] for d in AUG20APR21[2]]
data_DEC20 = [d[122:152] for d in AUG20APR21[2]]
data_JAN21 = [d[152:183] for d in AUG20APR21[2]]
data_FEB21 = [d[184:201] for d in AUG20APR21[2]]
data_MAR21 = [d[202:232] for d in AUG20APR21[2]]
data_APR21 = [d[233:262] for d in AUG20APR21[2]]
data_2 = [data_AUG20, data_SEPT20, data_OCT20, data_NOV20, data_DEC20, data_JAN21, data_FEB21, data_MAR21, data_APR21]

months = ['August 2020', 'September 2020', 'October 2020', 'November 2020', 'December 2020', 'January 2021', 'February 2021', 'March 2021', 'April 2021']

colors = pplt.colors()
colors = ("pink2", "violet2", "blue2", "lime3", "indigo2", "peach", "pastel blue", "light violet", "lime olive")
fig_2 = plt.figure(figsize = (10,7))
plt.pie(data_2, labels = months)
plt.legend(title = "Month",
           loc = "centre left")
plt.title("Hospitalizations by Month in England from August 2020 to April 2021")
plt.show()




#merging data 
APR20APR21 = pd.merge(APR20AUG20, AUG20APR21, on= 'Name')
APR21APR22 = pd.merge(APR21NOV21, NOV21APR22, on= 'Name')
APR20APR22 =pd.merge(APR20APR21,APR21APR22, on = 'Name')

print(APR20APR22)

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
plt.title('Hospital admissions during COVID-19 across UK')
plt.xlabel('Months during COVID-19')
plt.ylabel('Number of hospital admissions')
plt.legend()
    
#def animate():
 #   england_series.append()

#make this an option to save figure
#parser = argparse.ArgumentParser(description='Animate an epidemic')
#parser.add_argument('--file', metavar='N', type=str, default=None,
 #                       help='Filename to save to instead of showing on screen')

#plt.savefig('linegraph.png', format = 'png', dpi = 100)

