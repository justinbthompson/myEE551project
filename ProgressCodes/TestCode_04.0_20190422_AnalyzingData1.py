#TestCode_04
#TestCode to analyze data. Total daily energy for a given day, energy for day split between generation sources (value and percentage)

#External libraries needed, must be installed
import pandas as pd #Python Data Analysis Library
#Python built-in libraries needed
from urllib.request import urlopen #To request data from URL
from io import BytesIO #To obtain zip file from URL
from zipfile import ZipFile #To open items in zip file

#For now, will choose inputs in python
inputyear = 2019
inputmonth = 4
inputday = 20

#Access data
url = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + str(inputyear)+str(inputmonth).zfill(2)+str(inputday).zfill(2) + 'rtfuelmix.csv'
#print(url)
try:
    urlopen(url) #That date exists as csv file in database
    data = pd.read_csv(url)
    #print(data)
except: #We need to go through zipfile
    filetoread = str(inputyear)+str(inputmonth).zfill(2)+str(inputday).zfill(2) + 'rtfuelmix.csv'
    url2 = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + str(inputyear)+str(inputmonth).zfill(2) + '01rtfuelmix_csv.zip'
    #print(url2)
    resp = urlopen(url2)
    zf = ZipFile(BytesIO(resp.read()))
    data = pd.read_csv(zf.open(filetoread))
    #print(data)

#Now let's analyze data
#Let's get daily totals, totals per generation source, percentage of each generation source

#Read excel sheet
#print(data['Gen MW'][0]) #Reads first MW number, 1594 - works

#Daily total generated output in Megawatts
#dt = data['Gen MW'].sum() #Way to find total using pandas library.
#However, I would like to use a loop to represent topics learned in class.
#dt = 0; i = 0
#while i < data.shape[0]: #data.shape[0] = number of rows in data, data.shape[1] = number of columns
#    dt += data['Gen MW'][i]
#    i += 1
#print(dt) #This worked, but I want to put everythin in one loop

#Total per generation source
#Let's use same loop
#Also let's use a dictionary to show another concept from class, keep daily total data together
dt = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
      'Fossil Fuel':0, 'Other Renewable':0, 'Wind':0, 'Hydro':0}
#dt = 0; dtduelfuel = 0; dtnatgas = 0; dtnuclear = 0; dtfossil = 0; dtrenew = 0; dtwind = 0;
dp = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
      'Fossil Fuel':0, 'Other Renewable':0, 'Wind':0, 'Hydro':0}
i = 0
while i < data.shape[0]: #data.shape[0] = number of rows in data, data.shape[1] = number of columns
    #Total Daily Energy Comsumption
    dt['All Sources'] += data['Gen MW'][i]
    #Daily Energy Consumption Per Generation Source
    if (data['Fuel Category'][i] == 'Dual Fuel'):
        dt['Dual Fuel'] += data['Gen MW'][i]
    if (data['Fuel Category'][i] == 'Natural Gas'):
        dt['Natural Gas'] += data['Gen MW'][i]
    if (data['Fuel Category'][i] == 'Nuclear'):
        dt['Nuclear'] += data['Gen MW'][i]
    if (data['Fuel Category'][i] == 'Other Fossil Fuels'):
        dt['Fossil Fuel'] += data['Gen MW'][i]
    if (data['Fuel Category'][i] == 'Other Renewables'):
        dt['Other Renewable'] += data['Gen MW'][i]
    if (data['Fuel Category'][i] == 'Wind'):
        dt['Wind'] += data['Gen MW'][i]
    if (data['Fuel Category'][i] == 'Hydro'):
        dt['Hydro'] += data['Gen MW'][i]
    i += 1


#Find Percentage of Total Energy Consumption Per Generation Source
for x in dp:
    dp[x] = round(100*dt[x]/dt['All Sources'],2)
    #print(str(dp[x]) + "%")



#print(dt["Daily Total All Sources"])
print('Daily Total Energy Usage for ' + str(inputyear) + '-' + str(inputmonth) + '-' + str(inputday) + ': \n')
print(str(dt['All Sources']) + " MW \n")
print('Daily Total Energy Usage Per Energy Source: \n')
for x, y in dt.items():
  if x not in 'Daily Total All Sources':
    print(x + ": " + str(y) + " MW (" + str(dp[x]) + "%)")



