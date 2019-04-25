#TestCode_00
#Running version of final code
#Last updated 2019-04-24 10:30 PM


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

#User input function requests input from user
#The user will be prompted to specify a year, month, and day
#This will be the date the user searches data for, and will help make URL link
#Output of this function will be the date
def user_input():
    print("Please find a day you want to analyze") #Boot-up message
    #Select Year
    x = True
    while x is True:
        print("Please enter the year of the day you want to examine \n Choose 2018 or 2019")
        inputyear = input("yyyy >")
        if (inputyear == '2018') | (inputyear == '2019'):
            x = False
    #Select Month
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
    #Select day
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
    return inputyear, inputmonth, inputday


#Access data function takes the date from user_input() to create URL and access the data of that date
#date[0] = inputyear, date[1] = inputmonth, date[2] = inputday
#This function outputs the raw data from NY ISO
def access_data(date):
    #Create an initial URL based on the input data
    url = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + date[0]+date[1]+date[2]+ 'rtfuelmix.csv'
    #Try to see if CSV file of date requested is directly posted on NY ISO database
    try:
        urlopen(url) #That date requested has a CSV file directly posted on NY ISO database
        data = pd.read_csv(url) #Use pandas to collect raw data
    #If the CSV file of date requested is not directly posted, it will be posted through a monthly zip file
    #The file will have to be accessed through the URL of the zip file
    except:
        filetoread = str(date[0])+str(date[1]).zfill(2)+str(date[2]).zfill(2) + 'rtfuelmix.csv'
        url2 = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + str(date[0])+str(date[1]).zfill(2) + '01rtfuelmix_csv.zip'
        resp = urlopen(url2)
        zf = ZipFile(BytesIO(resp.read()))
        data = pd.read_csv(zf.open(filetoread))
    return data

#Analyze data function is the core of this program
#Its primary purpose is to input the data from access_data(), analyze it, and print the results
#This includes finding total daily energy consumption, energy consumption per generation source, percentage by source, and peak times
#It then outputs a print statement displaying all this information
#It also takes date as an input to print the date information
def analyze_data(data, date):
    #Dictionary dt will be used to match a key of a generation source with a value of its total generation
    #Dictionary dp will be used to match a key of a generation source with its percentage of total generation
    #Reset dt and dp for new data set
    dt = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}
    dp = {'All Sources':0,'Dual Fuel':0, 'Natural Gas':0, 'Nuclear': 0,
          'Other Fossil Fuels':0, 'Other Renewables':0, 'Wind':0, 'Hydro':0}

    #Loop tracker and peak tracker variables
    i = 0; peakhour = 0; peakminute = 0; hourgen = 0; minutegen = 0
    t = data['Time Stamp'][0] #Get first time stamp
    h = t[11:13] #Get first hour

    #This while loop goes through all the data cells in the chosen CSV files
    while i < data.shape[0]: #data.shape[0] = number of rows in data, data.shape[1] = number of columns

        #Total Daily Energy Consumption
        dt['All Sources'] += data['Gen MW'][i]

        #Daily Energy Consumption Per Generation Source
        for x in dt:
            if data['Fuel Category'][i] == x:
                dt[x] += data['Gen MW'][i]

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

    for x in dp: #Find percentage of total energy usage for generation source
        dp[x] = round(100*dt[x]/dt['All Sources'],2)

    print('Daily Total Energy Usage for ' + str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + ': \n')
    print(str(dt['All Sources']) + " MW \n")
    print('Daily Total Energy Usage Per Energy Source: \n')
    for x, y in dt.items():
        if x not in 'Daily Total All Sources':
            print(x + ": " + str(y) + " MW (" + str(dp[x]) + "%)")
    print('\nPeak Energy Consumption occurred at ' + peakminuteS + ', with ' + str(peakminute) + ' MW')
    print('Peak Energy Consumption over an hour occured at hour ' + peakhourS + ', with ' + str(peakhour) + ' MW')


#This function is another way to analyze the data, which is much quicker in computing time.
#It has similar inputs as outputs as the last, but it uses pandas to analyze data.
#I chose to use the previous function to show concepts learned in this course.
#Since it is not in use, it does not have the full functionality as the function above.
def analyze_data_method2(data, date):
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
    print('Daily Total Energy Usage for ' + str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + ': \n')
    print(str(dt['All Sources']) + " MW \n")
    print('Daily Total Energy Usage Per Energy Source: \n')
    for x, y in dt.items():
        if x not in 'Daily Total All Sources':
            print(x + ": " + str(y) + " MW (" + str(dp[x]) + "%)")


#--------------------------------------------------------------------------------
#Program

print("Welcome to the New York State Energy Data Analyzer") #Boot-up message
#while loop to have program running continuously
while True:
    date = user_input()         #Requests user input and date the user wants to examine
    #data = access_data(date)    #Collects the data based on user input, saves it as data
    analyze_data(data,date)     #Analyzes the data
    analyze_data_method2(data, date)   #Quicker analysis function not in use, explained above
    print('')

