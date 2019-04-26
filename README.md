# Power Demand Data Collection <br />
### [EE551 Course](https://github.com/sergulaydore/EE-551-Spring-2019 "Course Website") Project Spring 2019 <br />
Justin Thompson <br />

I pledge my honor that I have abided by the Stevens Honor System -Justin Thompson

## Introduction <br /> 

United States electricity consumption is continuously updated on government and utility websites.
This program takes data from the New York Independent System Operator [Real-Time Dashboard](https://www.nyiso.com/real-time-dashboard) [archive](http://mis.nyiso.com/public/P-63list.htm) and analyzes it. 

When the program starts, the command window will prompt the user to type in a date. This date will be the date in which data is analyzed, and it will be used to access the data. 

The program will then output: <br />
* Total energy consumption for the given date
* Energy consumption per generation source: dual fuel, natural gas, nuclear, other fossil fuels, other renewables, wind, and hydro
* Energy consumption per generation source as a percentage of total energy consumption
* Peak minute and hour energy consumption

An example output is below:

Daily Total Energy Usage for 2019-04-20: 

3499585.0 MW 

Daily Total Energy Usage Per Energy Source: 

Dual Fuel: 569157.0 MW (16.26%) <br />
Natural Gas: 557019.0 MW (15.92%) <br />
Nuclear: 1393077.0 MW (39.81%) <br />
Other Fossil Fuels: 43723.0 MW (1.25%) <br />
Other Renewables: 52199.0 MW (1.49%) <br />
Wind: 117148.0 MW (3.35%) <br />
Hydro: 767262.0 MW (21.92%) <br />

Peak Energy Consumption occurred at 11:06, with 13241.0 MW <br />
Peak Energy Consumption over an hour occured at hour 20, with 179357.0 MW

## Installation and Use <br />
* To download this program, git clone this repository
* Install external library [pandas](https://pandas.pydata.org/). This is used to compile CSV file data into an array.
* Run the program NewYorkStateEnergyConsumptionDataAnalyzer.py
* Input year, month, and day.
* Read the data and continue entering more dates for more data
* Note, internet connection is required

## What to find in this repository
* The ProgressCodes folder shows several early iterations of the code as it was being developed
* The ProjectFinalCode folder contains the final program to run and functions behind it
* The TestCodes folder contains a script to test correct data collection from the main functions
* Proposal.md is the original proposal
