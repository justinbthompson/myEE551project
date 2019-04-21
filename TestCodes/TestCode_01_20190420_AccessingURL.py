##VOID CODE
##This code was written to access URL of US Energy Information Administration
##Project now takes date from New York ISO


##Trial Code 1, Work done 4-20-2019
##This code is early trials of forming the URL wanted to reach from the requested date

#import requests #to be used to scrape data from URL
import time #built in python time library
import datetime #built in python datetime library and its classes

#Full url example (April 19, 2019): https://www.eia.gov/realtime_grid/#/data/graphs?end=20190419T17&start=20190412T21&bas=000g&regions=0
#The Energy Information Agency lists their URL for real time NY data with two dates, and end date and a start date for the recorded data period
urls = 'https://www.eia.gov/realtime_grid/#/data/graphs?end=' #beginning of url
urlm = 'T00&start=' #small middle section between two dates
urle = 'T00&bas=000g&regions=0' #end of URL changes for region, project scope limited to NY

#Test code for now, will ask user for input
#Must be interger for datetime calculations
#Must be strings when I go for URL
inputyear = 2019
inputmonth = 4
inputday = 18

inputdateS = str(inputyear)+str(inputmonth).zfill(2)+str(inputday).zfill(2)
print(inputdateS)


#Get start date
d = datetime.timedelta(days=7)
inputdate = datetime.date(inputyear, inputmonth, inputday)
outputdate= inputdate - d
print(outputdate)
outputdateS = ''
for i in str(outputdate):
    if i.isdigit():
        outputdateS = outputdateS + i
print(outputdateS)
#figure out how to make only the numbers

#Combine parts of URL to access site
url = urls + inputdateS + urlm + outputdateS + urle
print(url)


