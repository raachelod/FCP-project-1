#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:11:57 2022

@author: rachelodwyer
"""

import pandas as pd


#importing data from 4 seperate raw files
APR20AUG20 = pd.read_csv('Ap20-Au20-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')
AUG20APR21 = pd.read_csv('Au20-Ap21-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')
APR21NOV21 = pd.read_csv('Ap21-No21-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')
NOV21APR22 = pd.read_csv('No21-Ap22-Table.csv', index_col = 'Name', parse_dates= True, thousands= ',')



#Merging datasets 
APR20APR21 = pd.merge(APR20AUG20, AUG20APR21, on= 'Name')
APR21APR22 = pd.merge(APR21NOV21, NOV21APR22, on= 'Name')
APR20APR22 =pd.merge(APR20APR21,APR21APR22, on = 'Name' ) #single data frame over 2 years

print(APR20APR22)

#saving data frame created on python as csv file to use in seperate scripts and view as file
#APR20APR22.to_csv('/Users/rachelodwyer/Desktop/year1.2/FurtherComputing/FCP-project-1/merged_data.csv')
 







