#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  5 14:37:39 2022

@author: rachelodwyer
"""


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
fig_1, x = plt.plot(figsize = (10,7))
fig_1 = x.pie(data_1
              labels = months
              colors = colors)
x.legend(title = "Month",
           loc = "centre left")
x.title("Hospitalizations by Month in England from April 2020 to August 2020")
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
fig_2, y = plt.plot(figsize = (10,7))
fig_2 = y.pie(data_2,
              label = 'months',
              color = colors)
y.legend(title = "Month",
           loc = "centre left")
y.title("Hospitalizations by Month in England from August 2020 to April 2021")
plt.show()



#APR21AUG21

data_3 = APR20AUG20
data_APR21 = [d[1:13] for d in APR21AUG21[2]]
data_MAY21 = [d[14:43] for d in APR21AUG21[2]]
data_JUN21 = [d[44:74] for d in APR21AUG21[2]]
data_JUL21 = [d[75:104] for d in APR21AUG21[2]]
data_AUG21 = [d[105:135] for d in APR21AUG21[2]]
data_SEPT21 = [d[105:135] for d in APR21AUG21[2]]
data_3 = [data_APR21, data_MAY21, data_JUN21, data_JUL21, data_AUG21, data_SEPT21]

months = ['April 2021', 'May 2021', 'June 2021', 'July 2021', 'August 2021', 'September 2021']

colors = pplt.colors()
colors = ("pink2", "violet2", "blue2", "lime3", "indigo2", "peach")
fig_3, z = plt.plot(figsize = (10,7))
fig_3 = z.pie(data_3
              labels = months
              colors = colors)
z.legend(title = "Month",
           loc = "centre left")
z.title("Hospitalizations by Month in England from April 2021 to September 2021")
plt.show()



#AUG21APR22

data_4 = AUG21APR22
data_OCT21 = [d[1:31] for d in AUG21APR22[2]]
data_NOV21 = [d[32:61] for d in AUG21APR22[2]]
data_DEC21 = [d[62:92] for d in AUG21APR22[2]]
data_JAN22 = [d[93:132] for d in AUG21APR22[2]]
data_FEB22 = [d[133:160] for d in AUG21APR22[2]]
data_MAR22 = [d[161:191] for d in AUG21APR22[2]]
data_APR22 = [d[192:221] for d in AUG21APR22[2]]
data_3 = [data_OCT21, data_NOV21, data_DEC21, data_JAN22, data_FEB22, data_MAR22, data_APR22]

months = ['August 2021', 'September 2021', 'October 2021', 'November 2021', 'December 2021', 'January 2022']

colors = pplt.colors()
colors = ("pink2", "violet2", "blue2", "lime3", "indigo2", "peach", "pastel blue")
fig_4, zz = plt.plot(figsize = (10,7))
fig_4 = zz.pie(data_4
              labels = months
              colors = colors)
zz.legend(title = "Month",
           loc = "centre left")
zz.title("Hospitalizations by Month in England from April 2021 to September 2021")
plt.show()






#nested pie chart by year

APR20APR21 = pd.merge(APR20AUG20, AUG20APR21, on= 'Name')
APR21APR22 = pd.merge(APR21NOV21, NOV21APR22, on= 'Name')

#data

england2021_total = [d[1:] for d in APR20APR21[2]]
east2021_total = [d[1:] for d in APR20APR21[4]]
london2021_total = [d[1:] for d in APR20APR21[5]]
midlands2021_total = [d[1:] for d in APR20APR21[6]]
neyork2021_total = [d[1:] for d in APR20APR21[7]]
nw2021_total = [d[1:] for d in APR20APR21[8]]
se2021_total = [d[1:] for d in APR20APR21[9]]
sw2021_total = [d[1:] for d in APR20APR21[10]]


england2122_total = [d[1:] for d in APR21APR22[2]]
east2122_total = [d[1:] for d in APR21APR22[4]]
london2122_total = [d[1:] for d in APR21APR22[5]]
midlands2122_total = [d[1:] for d in APR21APR22[6]]
neyork2122_total = [d[1:] for d in APR21APR22[7]]
nw2122_total = [d[1:] for d in APR21APR22[8]]
se2122_total = [d[1:] for d in APR21APR22[9]]
sw2122_total = [d[1:] for d in APR21APR22[10]]

#data array

regions = ['East England', 'London', 'Midlands', 'Northeast Yorkshire', 'Northwest', 'Southeast', 'Southwest']

a2021 = east2021_total, london2021_total, midlands2021_total,
    neyork2021_total, nw2021_total, se2021_total, sw2021_total

b2122 = east2122_total, london2122_total, midlands2122_total,
        neyork2122_total, nw2122_total, se2122_total, sw2122_total
           
data_nest = np.array([a2021], [b2122])

#color scale

cmap1 = plt.cm.Set1
cmap2 = plt.cm.Pastel1                     
                     
outer_colors = cmap1
inner_colors = cmap2
                     
#creating plot

fig_5, zzz = plt.plot(figsize = (10,7))
zzz.pie(a2021, radius=1, labels = regions, colors = outer_colors, wedgeprops=dict(width=0.3, edgecolor='w'))
zzz.pie(b2122, radius=0.65, labels = regions, colors = inner_colors, wedgeprops=dict(width=0.3, edgecolor='w'))
zzz.title("Hospitalizations by Month by Region in England from April 2020 to April 2020")
plt.show() 