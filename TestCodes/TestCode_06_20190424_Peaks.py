#TestCode_06
#Peak function added
#Last updated 2019-04-2X

#--------------------------------------------------------------------------------
#External libraries needed, must be installed
import pandas as pd #Python Data Analysis Library
#Python built-in libraries needed
from urllib.request import urlopen #To request data from URL
from io import BytesIO #To obtain zip file from URL
from zipfile import ZipFile #To open items in zip file
import datetime #Will be used to check if inputted day is a real day

#--------------------------------------------------------------------------------
#Fucntions

def user_input():
    global inputyear, inputmonth, inputday
    print("Welcome to the New York State Energy Calculator") #Boot-up message
    #Select Year
    x = True
    while x is True:
        print("Please enter the year of the day you want to examine \n Choose 2018 or 2019")
        inputyear = input("yyyy >")
        if (inputyear == '2018') | (inputyear == '2019'):
            x = False
    #Accept Month
    x = True
    while x is  True:
        print("Please enter the month of " + inputyear +" you want to examine \n"
                "Choose a number between 1 and 12")
        inputmonth = input("mm >")
        try:
            int(x)
            if int(inputmonth) in range(1,12):
                x = False
        except:
            x = True
    inputmonth = inputmonth[-2:].zfill(2)
    x = True
    while x is True:
        print("Please enter the date of " + inputyear + '-' + inputmonth + ' you want to examine \n'
              'Choose an applicable date between 0 and 31 depending on month')
        inputday = input("dd >")
        try:
            int(inputday)
            try:
                datetime.datetime(int(inputyear), int(inputmonth), int(inputday))
                x = False
            except: x = True
        except:
            x = True
    inputday = inputday[-2:].zfill(2)



def access_data(): #Access data from NY ISO
    url = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + inputyear+inputmonth+inputday + 'rtfuelmix.csv'
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

def energy_sum2():  #Quicker way find Daily Total Energy usage, using pandas library. Not in use.
                    #Using method with loops and if statements to show concepts learned in this course.
    global dt, dp
    dt = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    dp = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    dt['All Sources'] = data['Gen MW'].sum()
    for x in dt:
        if x != 'All Sources':
            dt[x] = data.loc[data['Fuel Category'] == x, 'Gen MW'].sum()
    for x in dp: #Find percentage of total energy usage for generation source
        dp[x] = round(100*dt[x]/dt['All Sources'],2)

def energy_sum_print(): #Print Daily Total Energy Usage, both full and per generation source, and percentage by source
    print('Daily Total Energy Usage for ' + str(inputyear) + '-' + str(inputmonth) + '-' + str(inputday) + ': \n')
    print(str(dt['All Sources']) + " MW \n")
    print('Daily Total Energy Usage Per Energy Source: \n')
    for x, y in dt.items():
        if x not in 'Daily Total All Sources':
            print(x + ": " + str(y) + " MW (" + str(dp[x]) + "%)")


def VOIDpeak():
    global inputday, inputmonth, inputyear
    peakhour = 0; peakminute = 0; t = datetime.time(0)
    #CSV files being examined list power every five minutes
    #M/D/YYYY or #MM/DD/YYYY depending on which is applicable, followed by h:mm
    #Update - h:mm:ss AM/PM or hh:mm:ss AM/PM
    #Need to remove leading 0's
    if int(inputmonth) < 10:
        inputdate = inputmonth[-1:] +'/'
    else:
        inputdate = inputmonth + '/'
    if int(inputday) < 10:
        inputdate += inputday[-1:] + '/' + inputyear + ' '
    else:
        inputdate += inputday + '/' + inputyear + ' '
    #while i < data.shape[0]:
     #   t = (datetime.datetime.combine(datetime.date(1, 1, 1), t) + datetime.timedelta(minutes=5)).time()
        #inputdate += str(t)[:-3] will keep adding, only want temporary add
      #  print(inputdate + str(t)[:-3]) #adds 5 min for every row, too much? should be same time 7 times
     #   i += 1
    #Let's try something else. May not be that efficient though
    for x in range(0,287): #Create all time spots
        t = (datetime.datetime.combine(datetime.date(1, 1, 1), t) + datetime.timedelta(minutes=5)).time()
        #print(inputdate + str(t)[:-3]) #see update to how to look for time
        #t.strftime("%I:%M" %p)
        #print(t.strftime('%I:%M:%S %p'))
        if t.hour < 10:
            inputdate2 = inputdate + t.strftime('%I:%M:%S %p')[1:]
        else:
            inputdate2 = inputdate + t.strftime('%I:%M:%S %p')
        i = 0; minutedata = 0
        #print(inputdate2)
        while i < data.shape[0]:
            # if data['Time Stamp'][i] == '4/20/2019  12:05:00 AM': #replace with inputdate2
            if data['Time Stamp'][i] == '4/20/2019 0:05': #replace with inputdate2
                print(data['Gen MW'][i]) #Seems to be a problem here, as this won't print
                #Got it. Time Stamp when read via pandas, as seen when printing data
                # Is (for example) 04/20/2019 00:05:00
                # Let's adjust for that
                minutedata += data['Gen MW'][i]
                print(minutedata)
            i += 1
        if minutedata > peakminute:
            peakminute = minutedata

    print(peakminute)

def VOIDpeakfromonegensource():
    global inputday, inputmonth, inputyear
    peakhour = 0; peakminute = 0;  i = 0
    #CSV files being examined list power every five minutes
    #MM/DD/YYYY hh:mm:ss
    #I think it would be quicker to check a row and then all times instead of a time and then all rows since there are 2000+ rows and 287 times
    while i < data.shape[0]:
        t = datetime.time(minute=5)
        minutedata = 0
        for x in range(0,287):
            inputdate = inputmonth.zfill(2) + "/" + inputday.zfill(2) + "/" + inputyear + ' ' + str(t)
            #print(inputdate)
            if data['Time Stamp'][i] == inputdate: #'04/20/2019 00:05:00'
                minutedata += data['Gen MW'][i]
                print(data['Gen MW'][i])
            if minutedata > peakminute:
                peakminute = minutedata
                peakminuteS = str(t)
            t = (datetime.datetime.combine(datetime.date(1, 1, 1), t) + datetime.timedelta(minutes=5)).time()
        i += 1
    print(peakminute)
    print(peakminuteS)

#This code final produces a peak. However, since I checked all times within one cell, I only found peak of one cell.
#Could keep above code as peak minute for one generation source
def peak():
    global inputday, inputmonth, inputyear
    peakhour = 0; peakminute = 0;  i = 0; hourgen = 0; minutegen = 0
    t = data['Time Stamp'][0] #Get first time stamp
    h = t[11:13] #Get first hour
    #print(h) #print(t)
    while i < data.shape[0]:

        #To find hourly energy consumption
        if h == data['Time Stamp'][i][11:13]:
            hourgen += data['Gen MW'][i]
        else:
            h = data['Time Stamp'][i][11:13]
            hourgen = data['Gen MW'][i]

        #To find minute based energy consumption
        if data['Time Stamp'][i] == t:
            minutegen += data['Gen MW'][i]
        else:
            t = data['Time Stamp'][i]
            minutegen = data['Gen MW'][i]

        #Reset peaks if necessary
        if minutegen > peakminute:
            peakminute = minutegen
            peakminuteS = t[11:16]
        if hourgen > peakhour:
            peakhour = hourgen
            peakhourS = h

        i += 1

        #print(h)#print(t)
    print(peakminute)
    print(peakminuteS)
    print(peakhour)
    print(peakhourS)




#--------------------------------------------------------------------------------
#Program

#user_input()
inputyear = '2019'
inputmonth = '4'
inputday = '20'
data = access_data()
#print(data)
peak()




#energy_sum1()
#energy_sum_print()
