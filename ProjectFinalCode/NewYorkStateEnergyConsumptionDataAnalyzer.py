#Justin Thompson EE551 Python Final Project
#I pledge my honor I have abided by the Stevens Honor System -Justin Thompson

#New York State Energy Consumption Data Analyzer

#See README.md for introduction and requirements


#--------------------------------------------------------------------------------
#Import functions from function file
from myEE551projectPowerDemand.ProjectFinalCode.project_functions import *
#--------------------------------------------------------------------------------
#Program

print("Welcome to the New York State Energy Data Analyzer") #Boot-up message
#while loop to have program running continuously
while True:
    date = user_input()         #Requests user input and date the user wants to examine
    data = access_data(date)    #Collects the data based on user input, saves it as data
    dt, dp, peakhour, peakhourS, peakminute, peakminuteS = analyze_data(data)     #Analyzes the data
    #Print data found
    print('Daily Total Energy Usage for ' + str(date[0]) + '-' + str(date[1]) + '-' + str(date[2]) + ': \n')
    print(str(dt['All Sources']) + " MW \n")
    print('Daily Total Energy Usage Per Energy Source: \n')
    for x, y in dt.items():
        if x not in 'Daily Total All Sources':
            print(x + ": " + str(y) + " MW (" + str(dp[x]) + "%)")
    print('\nPeak Energy Consumption occurred at ' + peakminuteS + ', with ' + str(peakminute) + ' MW')
    print('Peak Energy Consumption over an hour occured at hour ' + peakhourS + ', with ' + str(peakhour) + ' MW')
    print('')

