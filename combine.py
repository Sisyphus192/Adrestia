import pandas as pd
import numpy as np

local_path = 'APPM.csv'
df = pd.read_csv(local_path)
dfAPPM = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'ASEN.csv'
df = pd.read_csv(local_path)
dfASEN = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'CHEN.csv'
df = pd.read_csv(local_path)
dfCHEN = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'CSCI.csv'
df = pd.read_csv(local_path)
dfCSCI = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'CVEN.csv'
df = pd.read_csv(local_path)
dfCVEN = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'ECEN.csv'
df = pd.read_csv(local_path)
dfECEN = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'MATH.csv'
df = pd.read_csv(local_path)
dfMATH = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'MCEN.csv'
df = pd.read_csv(local_path)
dfMCEN = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'PHYS.csv'
df = pd.read_csv(local_path)
dfPHYS = df.loc[:,['Subject','Crse','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
allClasses = [dfAPPM,dfASEN,dfCHEN,dfCSCI,dfCVEN,dfECEN,dfMATH,dfMCEN,dfPHYS]
classes = pd.concat(allClasses)
classes = classes.dropna()
#classes[classes.CourseOverall != 'nan']
np.savetxt('ClassesInfo.txt',classes, fmt='%s')
classes.head()