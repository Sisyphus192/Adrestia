from sqlalchemy import create_engine
import pandas as pd
import subprocess
import psycopg2
import os

proc = subprocess.Popen('heroku config:get DATABASE_URL -a adrestia', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
db_url = db_url[:8]+'ql'+db_url[8:]
#DATABASE_URL = os.environ['DATABASE_URL']
#print(DATABASE_URL)
#print(db_url)
#conn = psycopg2.connect(db_url)
engine = create_engine(db_url)
#df = pd.read_csv('data/APPM.csv')
#print('hello')
#df[:10].to_sql(con=engine, name='courses', if_exists='replace', index=True)
#print('hello2')
local_path = 'data/APPM.csv'
df = pd.read_csv(local_path)
dfAPPM = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/ASEN.csv'
df = pd.read_csv(local_path)
dfASEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/CHEN.csv'
df = pd.read_csv(local_path)
dfCHEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/CSCI.csv'
df = pd.read_csv(local_path)
dfCSCI = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/CVEN.csv'
df = pd.read_csv(local_path)
dfCVEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/ECEN.csv'
df = pd.read_csv(local_path)
dfECEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/MATH.csv'
df = pd.read_csv(local_path)
dfMATH = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/MCEN.csv'
df = pd.read_csv(local_path)
dfMCEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
local_path = 'data/PHYS.csv'
df = pd.read_csv(local_path)
dfPHYS = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
allClasses = [dfAPPM,dfASEN,dfCHEN,dfCSCI,dfCVEN,dfECEN,dfMATH,dfMCEN,dfPHYS]
classes = pd.concat(allClasses)
classes = classes.dropna()
hours = classes['HoursPerWkInclClass'].tolist()
#print(hours)
newHours = []
for i in range(len(hours)):
    temp = hours[i].split('-')
    #print(temp)
    if len(temp) > 1:
        temp = (int(temp[0])+int(temp[1]))/2
        newHours.append(temp)
    else:
        temp = temp[0].replace('+','')
        temp = int(temp)
        newHours.append(temp)
#print(newHours)
n = classes.columns[4]
classes.drop(n, axis = 1, inplace = True)
classes[n] = newHours
classes['Crse'] = classes['Subject'].map(str)+classes['Crse'].map(str)
classes = classes.loc[:,['Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
#classes.drop(classes.column[0], a)
newClasses = classes.groupby(['Crse','CrsTitle']).mean()
#print(newClasses)
newClasses = newClasses.add_suffix('_Count').reset_index()
newClasses.columns = ['Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']
newClasses['CrseID'] = newClasses.index
#newClasses = classes.loc[:,['CrseID','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
#newClasses.head(10000)
#classes.head(20000)

newClasses.to_sql(con=engine, name='courses', if_exists='replace', index=True)