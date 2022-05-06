# FCP-project-1
Hospital admissions across the UK over the period of COVID-19. 

## Introduction
Our project simulates covid hospital admissions through inputing populations and the initial infection values. We have used NHS data to compare our simulation to the real time values.

## Libraries
import Pandas <br />
import Matplotlip <br />
import Numpy <br />
import Scipy <br />

## Set up:
clone the repository

### For the simulation and its animated graphs: (animation.py)
Open a terminal, <br />
Run python animation.py, <br />
Follow the instructions, inputting your desired size of inital population and number of infected people for a general animation of the simulation. <br />
In order to compare with the graphs produced by the creatingplot.py, there are specific values to input: <br />
To compare to the total England population input N = 5600 and I0 = 52 (this correlates with the data sourced in the dataframe) <br />
To compare to the South West region, to specifically observe Bristol area, input N = 560 and I0 = 1 <br />
The values that are requested by user input are used to simulate data plots as an isolated scenario, using averages of values for the rate of infection and recovery to present a controllable estimation of how certain values would affect the virus spread over a period of 150 days.

### For the NHS data line graph: (creatingplot.py)
Open a terminal <br />
Run python creatingplot.py <br />
This will produce 3 seperate graphs: 1) A single graph of multiple plots correlating to the different regions in England, each identified using the colour coordinated legend. 2) A graph showing the accumulation of all hospital admissions across England. and 3) Specifically showing the hospital admissions in the South West region (Bristol). The third graph will save in order to view later and be compared to our simulation. <br />
This file has no oppurtunity for inputted values as it just reads data from official csv files. The code merges the 4 seperate files the raw data is stored as into a single pandas dataframe in order to be more easily accessed and used. The code also saves this merged df as a csv file. <br /> 
It then follows to exctract the specific data from the different rows (Names of region) and plots them as individual lines on the same graph. 

### For the pie chart visualisation of data: (piechart.py)
Open a terminal
Run python piechart.py
This will produe 4 pie charts which represents total number of hospitalizations from Covid-19 in England across 4 time periods: a) April 2020 to August 2020, b) August 2020 to April 2021, c) April 2021 to August 2021 and d) August 2021 to April 2022.
A 5th graph will be produced which is in the form of a nested piechart and represents yearly hospitalizations from Covid-19 across 2 time periods: a) 2020 to 2021 and b) 2021 to 2022. The outer piechart represents total number of hospitalizations from Covid-19 in England for that year while the inner piechart reflects total hospitalizations from Covid-19 by region for that year.
The data used in these graphs is a result of summing up daily hospitalization data in order to calculate, and later graph, monthly and yearly hospitalizations. In our data, the data is split into total data for England and data by region.
This file consists of imported data and thus, has no opportunity for inputted values. The code extracts the data, analyzes it and sums it in order to produce the graphs.

### merged_data.csv
This is the merged data frame of the 4 individual csv files 'Apr20-Aug20.csv','Aug20-Apr21.csv', 'Ap21-Aug21.csv', 'Aug21-Apr22.csv' (which can all be accessed on the repository) that has been converted into a csv file. 

### southwest_data.pdf
This is the saved graph plotting only the hospital admissions in the South West region. 
