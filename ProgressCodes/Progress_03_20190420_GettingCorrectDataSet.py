#TestCode_03
#TestCode to look for the correct data files given a certain date

#External libraries needed, must be installed
import pandas as pd #Python Data Analysis Library
#Python built-in libraries needed
from urllib.request import urlopen #To request data from URL
from io import BytesIO #To obtain zip file from URL
from zipfile import ZipFile #To open items in zip file

#Now must work on creating the URL based off of user input
#For now, will choose inputs in python
inputyear = 2019
inputmonth = 4
inputday = 20

url = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + str(inputyear)+str(inputmonth).zfill(2)+str(inputday).zfill(2) + 'rtfuelmix.csv'
#print(url)
try:
    urlopen(url) #That date exists as csv file in database
    data = pd.read_csv(url)
    print(data)
except: #We need to go through zipfile
    filetoread = str(inputyear)+str(inputmonth).zfill(2)+str(inputday).zfill(2) + 'rtfuelmix.csv'
    url2 = 'http://mis.nyiso.com/public/csv/rtfuelmix/' + str(inputyear)+str(inputmonth).zfill(2) + '01rtfuelmix_csv.zip'
    #print(url2)
    resp = urlopen(url2)
    zf = ZipFile(BytesIO(resp.read()))
    data = pd.read_csv(zf.open(filetoread))
    print(data)


#Recap of TestCode_02
#Read data straight from URL csv file
#data = pd.read_csv(url)
#To read data from zipped csv file
#resp = urlopen(url2)
#zf = ZipFile(BytesIO(resp.read()))
#data2 = pd.read_csv(zf.open(filetoread))
#print(data2)
#filetoread = '20190301rtfuelmix.csv'
#url2 = 'http://mis.nyiso.com/public/csv/rtfuelmix/20190301rtfuelmix_csv.zip'
#url = 'http://mis.nyiso.com/public/csv/rtfuelmix/20190420rtfuelmix.csv'
