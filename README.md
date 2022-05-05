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


