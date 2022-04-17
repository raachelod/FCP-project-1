#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 12:10:42 2022

@author: rachelodwyer
"""

import pandas as pd
#hosptial admissions across UK hospitals every month 
DEC2019 = pd.read_csv('dec-2019.csv')
DEC2019 = DEC2019[['Org Code', 'Parent Org', 'Org name', 'Number of A&E attendances Other A&E Department']]
DEC2019 = DEC2019.sort_values(by = 'Org Code')

JAN2020= pd.read_csv('jan-2020.csv')
JAN2020 = JAN2020[['Org Code', 'Parent Org', 'Org name', 'Number of A&E attendances Other A&E Department']]
JAN2020 = JAN2020.sort_values(by = 'Org Code')

FEB2020= pd.read_csv('feb-2020.csv')
FEB2020 = FEB2020[['Org Code', 'Parent Org', 'Org name', 'Number of A&E attendances Other A&E Department']]
FEB2020 = FEB2020.sort_values(by = 'Org Code')

MAR2020= pd.read_csv('mar-2020.csv')
MAR2020 = MAR2020[['Org Code', 'Parent Org', 'Org name', 'Number of A&E attendances Other A&E Department']]
MAR2020 = MAR2020.sort_values(by = 'Org Code')

APR2020= pd.read_csv('apr-2020.csv')
APR2020 = APR2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
APR2020 = APR2020.sort_values(by = 'Org Code')

MAY2020= pd.read_csv('may-2020.csv')
MAY2020 = MAY2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
MAY2020 = MAY2020.sort_values(by = 'Org Code')

JUN2020= pd.read_csv('jun-2020.csv')
JUN2020 = JUN2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
JUN2020 = JUN2020.sort_values(by = 'Org Code')

JUL2020= pd.read_csv('jul-2020.csv')
JUL2020 = JUL2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
JUL2020 = JUL2020.sort_values(by = 'Org Code')

AUG2020= pd.read_csv('aug-2020.csv')
AUG2020 = AUG2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
AUG2020 = AUG2020.sort_values(by = 'Org Code')

SEP2020= pd.read_csv('sep-2020.csv')
SEP2020 = SEP2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
SEP2020 = SEP2020.sort_values(by = 'Org Code')

OCT2020= pd.read_csv('oct-2020.csv')
OCT2020 = OCT2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
OCT2020 = OCT2020.sort_values(by = 'Org Code')

NOV2020= pd.read_csv('nov-2020.csv')
NOV2020 = NOV2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
NOV2020 = NOV2020.sort_values(by = 'Org Code')

DEC2020= pd.read_csv('dec-2020.csv')
DEC2020 = DEC2020[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
DEC2020 = DEC2020.sort_values(by = 'Org Code')

JAN2021= pd.read_csv('jan-2021.csv')
JAN2021 = JAN2021[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
JAN2021 = JAN2021.sort_values(by = 'Org Code')

FEB2021= pd.read_csv('feb-2021.csv')
FEB2021 = FEB2021[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
FEB2021 = FEB2021.sort_values(by = 'Org Code')

MAR2021= pd.read_csv('mar-2021.csv')
MAR2021 = MAR2021[['Org Code', 'Parent Org', 'Org name', 'A&E attendances Other A&E Department']]
MAR2021 = MAR2021.sort_values(by = 'Org Code')

print(DEC2019.head())

print(JAN2020.head())


