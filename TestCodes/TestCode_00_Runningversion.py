#TestCode_00
#Running version of final code
#Last updated 2019-04-22 4:30 PM


#--------------------------------------------------------------------------------
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


#--------------------------------------------------------------------------------
#Fucntions

def access_data(): #Access data from NY ISO
    url = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + str(inputyear)+str(inputmonth).zfill(2)+str(inputday).zfill(2) + 'rtfuelmix.csv'
    try:
        urlopen(url) #That date exists as csv file in database
        data = pd.read_csv(url)
    except: #We need to go through zipfile if that csv file is no longer posted on database
        filetoread = str(inputyear)+str(inputmonth).zfill(2)+str(inputday).zfill(2) + 'rtfuelmix.csv'
        url2 = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + str(inputyear)+str(inputmonth).zfill(2) + '01rtfuelmix_csv.zip'
        resp = urlopen(url2)
        zf = ZipFile(BytesIO(resp.read()))
        data = pd.read_csv(zf.open(filetoread))
    return data


def energy_sum1(): #Find Daily Total Energy Usage, both full and per generation source, and percentage by source
    global dt, dp, data
    #Reset dt and dp for new data set
    dt = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    dp = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    i = 0
    while i < data.shape[0]: #data.shape[0] = number of rows in data, data.shape[1] = number of columns
        #Total Daily Energy Consumption
        dt['All Sources'] += data['Gen MW'][i]
        #Daily Energy Consumption Per Generation Source
        if data['Fuel Category'][i] == 'Dual Fuel':
            dt['Dual Fuel'] += data['Gen MW'][i]
        if data['Fuel Category'][i] == 'Natural Gas':
            dt['Natural Gas'] += data['Gen MW'][i]
        if data['Fuel Category'][i] == 'Nuclear':
            dt['Nuclear'] += data['Gen MW'][i]
        if data['Fuel Category'][i] == 'Other Fossil Fuels':
            dt['Other Fossil Fuels'] += data['Gen MW'][i]
        if data['Fuel Category'][i] == 'Other Renewables':
            dt['Other Renewables'] += data['Gen MW'][i]
        if data['Fuel Category'][i] == 'Wind':
            dt['Wind'] += data['Gen MW'][i]
        if data['Fuel Category'][i] == 'Hydro':
            dt['Hydro'] += data['Gen MW'][i]
        i += 1
    for x in dp: #Find percentage of total energy usage for generation source
        dp[x] = round(100*dt[x]/dt['All Sources'],2)

def energy_sum3():  #Quicker way find Daily Total Energy usage, using pandas library. Not in use.
                    #Using method with loops and if statements to show concepts learned in this course.
    dt['All Sources'] = data['Gen MW'].sum()
    for x in dt:
        if x != 'All Sources':
            dt[x] = data.loc[data['Fuel Category'] == x, 'Gen MW'].sum()

def energy_sum_print(): #Print Daily Total Energy Usage, both full and per generation source, and percentage by source
    print('Daily Total Energy Usage for ' + str(inputyear) + '-' + str(inputmonth) + '-' + str(inputday) + ': \n')
    print(str(dt['All Sources']) + " MW \n")
    print('Daily Total Energy Usage Per Energy Source: \n')
    for x, y in dt.items():
        if x not in 'Daily Total All Sources':
            print(x + ": " + str(y) + " MW (" + str(dp[x]) + "%)")




#--------------------------------------------------------------------------------
#Program
data = access_data()
energy_sum1()
energy_sum_print()
