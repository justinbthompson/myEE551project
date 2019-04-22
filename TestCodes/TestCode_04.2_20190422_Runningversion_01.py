#TestCode_04.1
#TestCode to check speed of possible methods for total consumption calculations
#Conclusion - Method from TestCode_04 is faster than new method from TestCode_04.1 (see trial below)
#However, using built in pandas functions is much much faster than either
#As for now, I will continue to use my functions to represent knowledge learned in this course

#External libraries needed, must be installed
import pandas as pd #Python Data Analysis Library
#Python built-in libraries needed
from urllib.request import urlopen #To request data from URL
from io import BytesIO #To obtain zip file from URL
from zipfile import ZipFile #To open items in zip file
import time

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


dt = {}
dp = {}

def Energysum1():
    global dt, dp
    #Reset dt and dp for new data set
    dt = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    dp = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
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
            dt['Other Fossil Fuels'] += data['Gen MW'][i]
        if (data['Fuel Category'][i] == 'Other Renewables'):
            dt['Other Renewables'] += data['Gen MW'][i]
        if (data['Fuel Category'][i] == 'Wind'):
            dt['Wind'] += data['Gen MW'][i]
        if (data['Fuel Category'][i] == 'Hydro'):
            dt['Hydro'] += data['Gen MW'][i]
        i += 1
    for x in dp:
        dp[x] = round(100*dt[x]/dt['All Sources'],2)
    return dt, dp

def Energysumprint():
    print('Daily Total Energy Usage for ' + str(inputyear) + '-' + str(inputmonth) + '-' + str(inputday) + ': \n')
    #print(str(dt['All Sources']) + " MW \n")
    print('Daily Total Energy Usage Per Energy Source: \n')
    for x, y in dt.items():
        if x not in 'Daily Total All Sources':
            print(x + ": " + str(y) + " MW (" + str(dp[x]) + "%)")




#Curious to find quicker method, less if statements

def Energysum2():
    #Same method for total energy consumption of day
    global dt, dp
    #Reset dt and dp for new data set
    dt = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    dp = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    i = 0
    while i < data.shape[0]: #data.shape[0] = number of rows in data, data.shape[1] = number of columns
        #Total Daily Energy Comsumption
        dt['All Sources'] += data['Gen MW'][i]

    #Different method by generation source
        for x in dt:
            if (data['Fuel Category'][i] == x):
                dt[x] += data['Gen MW'][i]

        i += 1

    for x in dp:
        dp[x] = round(100*dt[x]/dt['All Sources'],2)
    return dt, dp

#Energysumprint()

i = 0
start_time = time.time()
while i < 100:
    Energysum1()
    i += 1
end_time = time.time()
elapsed = end_time - start_time
print("Elapsed time for Energysum1 ", '{0:4f}'.format(elapsed))

i = 0
start_time = time.time()
while i < 100:
    Energysum2()
    i += 1
end_time = time.time()
elapsed = end_time - start_time
print("Elapsed time for Energysum2 ", '{0:4f}'.format(elapsed))

#Results
#Energysum1 ran 101 times = 26.36 seconds
#Energysum2 ran 101 times = 29.25 seconds
#So first method is faster

#Let's check pandas library and times

def Energysum3():
    dt['All Sources'] = data['Gen MW'].sum()
    for x in dt:
        if x != 'All Sources':
            dt[x] = data.loc[data['Fuel Category'] == x, 'Gen MW'].sum()

#print newest method just to check it works
#Energysum3()
#Energysumprint()

#Check time for method 3

i = 0
start_time = time.time()
while i < 100:
    Energysum3()
    i += 1
end_time = time.time()
elapsed = end_time - start_time
print("Elapsed time for Energysum3 ", '{0:4f}'.format(elapsed))

#Energysum3 ran 101 times = 0.53 seconds
#The pandas library is much faster than my code, but I will still use mine
