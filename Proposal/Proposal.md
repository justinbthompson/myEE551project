# Power Demand Data Collection <br />
### [EE551 Course](https://github.com/sergulaydore/EE-551-Spring-2019 "Course Website") Project Spring 2019 <br />
Justin Thompson <br />

I pledge my honor that I have abided by the Stevens Honor System -Justin Thompson

## 2/15/2019 Proposal <br /> 
The U.S. electrical grid is one of the greatest engineering accomplishments of the twentieth century, but it is now aging and seeing larger demands than ever before. Capital improvements to the grid are necessary, and many believe that the evolution towards a smart grid will bring a better future. A smart grid, powered by the data recording and communication systems of today, will allow generation sources, transmitters, distributors, and end customers to monitor their power usage against demand. This will allow them to make decisions to shave peak demand, stop the disruption of services, and be more efficient with energy usage. The purpose of this project will be to explore possibilities of smart grid applications based on the idea that near real time demand data can be collected and analyzed. <br /> <br />
The scope of this project includes: <br /> 
* Code written in Python
* Organized Github repository
* Inclusion of test code
* Reproducibility
* To find and collect near real time electrical demand data from government or utility information sites
  * Example:  [EIA NYIS Demand](https://www.eia.gov/realtime_grid/#/data/graphs?end=20190212T15&start=20190205T20&bas=000g&regions=0 "EIA NYIS Demand")  
* To organize and present this data such that it is easy to analyze and make decisions based off of it
  * In a base scope this will include at least charts and simple graphs
  * Potentially, other visualization tools will be employed as well
* Additional goals if achievable may include simulation of a microgrid based on real time demand data
* Project completion by 04/26/2019 Friday at 5pm ET

## 4/20/2019 Proposal Update <br />

Data will be collected and analyzed from the New York Independent System Operator [Real-Time Dashboard](https://www.nyiso.com/real-time-dashboard) by accessing Excel and .zip files [available](http://mis.nyiso.com/public/P-63list.htm).

The user of the program will be prompted to choose a day within the past two years. The program will then output the total generated megawatts, percentages of generation between different sources, and other information. 

## Required Installations <br />

External library [pandas](https://pandas.pydata.org/) will need to be installed. This is used to compile CSV file data into an array.
All other libraries are python libraries. 
