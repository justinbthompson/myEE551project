#This test code tests that the access_data function works
import unittest

from myEE551projectPowerDemand.ProjectFinalCode.project_functions import *

#class TestDataCollection(unittest.TestCase):

#    def test_datacollectiondate1(self):
#        result1 = access_data(('2018', '01', '01'))
#        result2 = pd.read_csv('20180101rtfuelmix.csv')
#        self.assertEqual(result1, result2)

#    def test_datacollectiondate2(self):
#        result1 = access_data(('2019', '04', '20'))
#        result2 = pd.read_csv('20190420rtfuelmix.csv')
#        self.assertEqual(result1, result2)

#I believe this does not work because unittest requires certain types of values for self.assertEqual
#And the pandas array is not a valid type

class TestAnalyzeData(unittest.TestCase):

    #Comparing data found via program and via known data found, calculated in CSV files in this folder.

    def test_analyzedata20190420(self):

        #Via program
        date = ('2019', '04', '20')
        Idata = access_data(date)
        Idt, Idp, Ipeakhour, IpeakhourS, Ipeakminute, IpeakminuteS = analyze_data(Idata)

        #Known data
        dt = {'All Sources': 3499585.0, 'Dual Fuel': 569157.0, 'Natural Gas': 557019.0, 'Nuclear': 1393077.0, 'Other Fossil Fuels': 43723.0, 'Other Renewables': 52199.0, 'Wind': 117148.0, 'Hydro': 767262.0}
        dp = {'All Sources': 100.0, 'Dual Fuel': 16.26, 'Natural Gas': 15.92, 'Nuclear': 39.81, 'Other Fossil Fuels': 1.25, 'Other Renewables': 1.49, 'Wind': 3.35, 'Hydro': 21.92}
        peakhour = 179357
        peakhourS = '20'
        peakminute = 13241
        peakminuteS = '11:06'

        self.assertEqual(Idt, dt)
        self.assertEqual(Idp, dp)
        self.assertEqual(Ipeakhour, peakhour)
        self.assertEqual(IpeakhourS, peakhourS)
        self.assertEqual(Ipeakminute, peakminute)
        self.assertEqual(IpeakminuteS, peakminuteS)

    def test_analyzed20180101(self):

        #Via program
        date = ('2018', '01', '01')
        Idata = access_data(date)
        Idt, Idp, Ipeakhour, IpeakhourS, Ipeakminute, IpeakminuteS = analyze_data(Idata)

        #Known data
        dt = {'All Sources': 5207115, 'Dual Fuel': 1544996, 'Natural Gas': 786754, 'Nuclear': 1602039, 'Other Fossil Fuels': 119449, 'Other Renewables': 77715, 'Wind': 117142, 'Hydro': 959020}
        dp = {'All Sources': 100.0, 'Dual Fuel': 29.67, 'Natural Gas': 15.11, 'Nuclear': 30.77, 'Other Fossil Fuels': 2.29, 'Other Renewables': 1.49, 'Wind': 2.25, 'Hydro': 18.42}

        self.assertEqual(Idt, dt)
        self.assertEqual(Idp, dp)

    def test_analyzed20180727(self):

        #Via program
        date = ('2018', '07', '27')
        Idata = access_data(date)
        Idt, Idp, Ipeakhour, IpeakhourS, Ipeakminute, IpeakminuteS = analyze_data(Idata)

        #Known data
        dt = {'All Sources': 5680401, 'Dual Fuel': 1754850, 'Natural Gas': 1186495, 'Nuclear': 1574312, 'Other Fossil Fuels': 19159, 'Other Renewables': 84993, 'Wind': 101258, 'Hydro': 959334}
        dp = {'All Sources': 100.0, 'Dual Fuel': 30.89, 'Natural Gas': 20.89, 'Nuclear': 27.71, 'Other Fossil Fuels': 0.34, 'Other Renewables': 1.50, 'Wind': 1.78, 'Hydro': 16.89}

        self.assertEqual(Idt, dt)
        self.assertEqual(Idp, dp)


if __name__ == '__main__':
    unittest.main()
