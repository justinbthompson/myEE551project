#Justin Thompson EE551 Python Final Project
#I pledge my honor I have abided by the Stevens Honor System -Justin Thompson

#New York State Energy Consumption Data Analyzer

#See README.md for introduction and requirements


#--------------------------------------------------------------------------------
#Import functions from function file
from myProject.ProjectFinalCode.project_functions import *


#--------------------------------------------------------------------------------
#Program

print("Welcome to the New York State Energy Data Analyzer") #Boot-up message
#while loop to have program running continuously
while True:
    date = user_input()         #Requests user input and date the user wants to examine
    data = access_data(date)    #Collects the data based on user input, saves it as data
    analyze_data(data,date)     #Analyzes the data
    #analyze_data_method2(data, date)   #Quicker analysis function not in use, explained above
    print('')

