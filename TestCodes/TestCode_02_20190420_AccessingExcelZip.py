#Test code to read Excel data straight from website as well as from zip file on website

#import csv #Python built-in CSV reader. Not in use
import pandas as pd #Python Data Analysis Library, must be installed
from zipfile import ZipFile #Python built-in ZIP file reader

#Test code to read data from csv file

#Test subject, April 20th. Note this URL may eventually be void.
#To repeat this test in future, find newest data at http://mis.nyiso.com/public/P-63list.htm
url = 'http://mis.nyiso.com/public/csv/rtfuelmix/20190420rtfuelmix.csv'
data = pd.read_csv(url)
print(data)

#NY ISO only posts csv data for last ~10 days
#Eariler data posted in zip files per month
#Need to read CSV file from zip file
filetoread = '20190301rtfuelmix.csv'
url2 = 'http://mis.nyiso.com/public/csv/rtfuelmix/20190301rtfuelmix_csv.zip'
#localziptest = 'C:/Users/Test/Desktop/20190401rtfuelmix_csv.zip'
#zf = zipfile.ZipFile(url2)
#zf = zipfile.ZipFile(localziptest)
#data2 = pd.read_csv(zf.open(filetoread))
#print(data2)
#Method above only works for local zip files. Need to find away for zip files from internet

from urllib.request import urlopen
from io import BytesIO

resp = urlopen(url2)
zf = ZipFile(BytesIO(resp.read()))
data2 = pd.read_csv(zf.open(filetoread))
print(data2)

#This works
#Idea from Vishal on https://stackoverflow.com/questions/5710867/downloading-and-unzipping-a-zip-file-without-writing-to-disk


