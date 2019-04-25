#This test code tests that the access_data function works
import unittest
import pandas as pd

from myProject.ProjectFinalCode.project_functions import *


class TestDataCollection(unittest.TestCase):

    def datacollectiondate1(self):
        result1 = access_data(('2018', '01', '01'))
        result2 = pd.read_csv('20180101rtfuelmix.csv')
        self.assertEqual(result1, result2)


