import unittest
import table
import pandas as pd
import numpy as np
import re

self = table.tables()

#test if course numbers are negative
def test_crseNum(self):
	for i,rows in self.iterrows():
		if int(rows[2]) < 0:
			print('Invalid course number')
			return False
		else:
			print('Passed')
			return True
	
#test if table contains subjects it should not		
def test_subjects(self):
	subjects = ['APPM','ASEN','AREN','ASEN','CHEN','CSCI','CVEN','ECEN','MATH','MCEN','PHYS']
	for i,rows in self.iterrows():
		if rows[1] not in subjects:
			print('Invalid subjects in courses')
			return False
		else:
			print('Passed')
			return True

#test if classes are considered undergrad level
def test_undergrad(self):
	for i,rows in self.iterrows():
		if int(rows[2]) > 5000:
			print('Courses contain higher than undergrad courses')
			return False
		else:
			print('Passed')
			return True
			
test_crseNum(self)
test_subjects(self)
test_undergrad(self)

