# Power Demand Data Collection <br />
### [EE551 Course](https://github.com/sergulaydore/EE-551-Spring-2019 "Course Website") Project Spring 2019 <br />
Justin Thompson <br />

I pledge my honor that I have abided by the Stevens Honor System -Justin Thompson

## 2/15/2019 Introduction <br /> 

United States electricity consumption is continuously updated on government and utility websites.
This program takes archived data from New York Independent System Operator [Real-Time Dashboard](https://www.nyiso.com/real-time-dashboard) set of archived [data](http://mis.nyiso.com/public/P-63list.htm) and analyzes it. 

When the program starts, the command window will prompt the user to type in a date. This date will be the date in which data is analyzed, and it will be used to access the data. 

The program will then output: <br />
* Total energy consumption for the given date
* Energy consumption per generation source: dual fuel, natural gas, nuclear, other fossil fuels, other renewables, wind, and hydro
* Energy consumption per generation source as a percentage of total energy consumption
* Peak minute and hour energy consumption

An example output is below:

Daily Total Energy Usage for 2019-04-24: 

3601545.0 MW 

Daily Total Energy Usage Per Energy Source: 

Dual Fuel: 565914.0 MW (15.71%)
Natural Gas: 438544.0 MW (12.18%)
Nuclear: 1326488.0 MW (36.83%)
Other Fossil Fuels: 345.0 MW (0.01%)
Other Renewables: 55312.0 MW (1.54%)
Wind: 275348.0 MW (7.65%)
Hydro: 939594.0 MW (26.09%)

## Requirments <br />

External library [pandas](https://pandas.pydata.org/) will need to be installed. This is used to compile CSV file data into an array.
All other libraries are python libraries. 

Internet connection is also required to access the data.
