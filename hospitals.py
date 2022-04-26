#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 15:11:57 2022

@author: rachelodwyer
"""

import pandas as pd
#import numpy as np
#import argparse
import matplotlib.pyplot as plt
#from matplotlib.animaion import FuncAnimation


#importing data from files
APR20AUG20 = pd.read_csv('Ap20-Au20-Table.csv')
AUG20APR21 = pd.read_csv('Au20-Ap21-Table.csv')
APR21NOV21 = pd.read_csv('Ap21-No21-Table.csv')
NOV21APR22 = pd.read_csv('No21-Ap22-Table.csv')

#Selecting data from only 20th of every month 
APR20AUG20 = APR20AUG20[['Name', '20-Mar-20','20-Apr-20', '20-May-20', '20-Jun-20', '20-Jul-20', ]]
AUG20APR21 = AUG20APR21[['Name', '20-Aug-20','20-Sep-20', '20-Oct-20', '20-Nov-20', '20-Dec-20','20-Jan-21', '20-Feb-21', '20-Mar-21' ]]
APR21NOV21= APR21NOV21[['Name', '20-Apr-21', '20-May-21', '20-Jun-21', '20-Jul-21', '20-Aug-21','20-Sep-21']]
NOV21APR22 = NOV21APR22[['Name','20-Oct-21', '20-Nov-21', '20-Dec-21','20-Jan-22', '20-Feb-22', '20-Mar-22' ]]

#Merging datasets 
APR20APR21 = pd.merge(APR20AUG20, AUG20APR21, on= 'Name')
APR21APR22 = pd.merge(APR21NOV21, NOV21APR22, on= 'Name')


APR20APR22 =pd.merge(APR20APR21,APR21APR22, on = 'Name' ) #single data frame over 2 years
print(APR20APR22)

x = APR20APR22[['Name']]
y = APR20APR22[['20-Mar-20']]
fig1, ax1 = plt.subplots()
ax1.plot(x, y)


#hospitalAdmissions = 
#def main(args):
#    parser = argparse.ArgumentParser(description= 'Animate UK hospital admissions')
#   parser.add_argument('--region', metavar = 'R', type=str, default = None, help = 'Hospital admissions in R region')
 #   parser.add_argument('--plot', action = 'store_true', help = 'Generate plots instead of animation')
  #  parser.add_argument('--file', metavar = 'N', type=str, default=None, help='Filename to save to instead of showing on screen')
   # args = parser.parse_args(args)
    

    







