from sqlalchemy import create_engine
import pandas as pd
import subprocess
import psycopg2
import os
import numpy as np

proc = subprocess.Popen('heroku config:get DATABASE_URL -a adrestia2', stdout=subprocess.PIPE, shell=True)
db_url = proc.stdout.read().decode('utf-8').strip() + '?sslmode=require'
db_url = db_url[:8]+'ql'+db_url[8:]
#DATABASE_URL = os.environ['DATABASE_URL']
#print(DATABASE_URL)
#print(db_url)
#conn = psycopg2.connect(db_url)
engine = create_engine(db_url)#'mysql://root:@localhost/adrestiadb')
#df = pd.read_csv('data/APPM.csv')
#print('hello')
#df[:10].to_sql(con=engine, name='courses', if_exists='replace', index=True)
#print('hello2')

"""
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
"""
allClasses = []
for file in os.listdir("./data"):
    if file.endswith(".csv"):
        allClasses.append(pd.read_csv("./data/"+str(file)))

#print(allClasses[0])


rawClasses = pd.concat(allClasses)
rawClasses = rawClasses[rawClasses.HoursPerWkInclClass != 'S']
rawClasses = rawClasses[rawClasses.HoursPerWkInclClass.notnull()]
rawClasses['Yearterm'] = rawClasses['Yearterm'].astype(str)
rawClasses['Crse'] = rawClasses['Crse'].astype(str)
rawClasses = rawClasses[rawClasses.Yearterm.str[-1] != '4']
rawClasses = rawClasses[rawClasses.Yearterm.str[:4].isin(['2012', '2013', '2014', '2015', '2016', '2017', '2018'])]
rawClasses = rawClasses[rawClasses.CrsTitle != 'REC']
rawClasses = rawClasses[rawClasses.CrsTitle != 'RECITATION']
rawClasses = rawClasses[rawClasses.CrsTitle != 'LAB']
#print(rawClasses["CrsTitle"])
rawClasses['HoursPerWkInclClass'] = rawClasses['HoursPerWkInclClass'].astype('category')
rawClasses['HoursPerWkInclClass'] = rawClasses['HoursPerWkInclClass'].cat.rename_categories([2,11,14,17,5,8]).astype('int')
rawClasses['CrseID'] = rawClasses["Subject"] + rawClasses["Crse"]
classes = {}
for i in rawClasses.CrseID.unique():
    classes[i] = rawClasses[rawClasses['CrseID'] == i]

#print(classes['PHYS3210'].head())

finalClasses = []
for i in list(classes.keys()):
    finalClass = {}
    finalClass['CrseID'] = i
    finalClass['Crse'] = i[-4:]
    finalClass['Subject'] = i[:4]
    finalClass['CrsTitle'] = list(classes[i]['CrsTitle'])[0]
    finalClass['Challenge'] = round(np.average(classes[i]['Challenge'], weights=classes[i]['FormsReturned']), 2)
    finalClass['HoursPerWkInclClass'] = round(np.average(classes[i]['HoursPerWkInclClass'], weights=classes[i]['HoursPerWkInclClass']), 2)
    finalClass['CourseOverall'] = round(np.average(classes[i]['CourseOverall'], weights=classes[i]['CourseOverall']), 2)
    finalClass['HowMuchLearned'] = round(np.average(classes[i]['HowMuchLearned'], weights=classes[i]['HowMuchLearned']), 2)
    finalClasses.append(finalClass)



finalClasses = pd.DataFrame(finalClasses)
#print(finalClasses)
finalClasses.to_sql(con=engine, name='courses', if_exists='replace', index=True)


""" 
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
newClasses = newClasses.loc[:,['CrseID','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
#newClasses.head(10000)
#classes.head(20000)
subject = []
number = []
for i,row in newClasses.iterrows():
    #print(row[1])
    sub = row[1][0:4]
    num = row[1][4:8]
    subject.append(sub)
    number.append(num)
    #print(sub,num)
newClasses['Subject'] = subject
newClasses['Crse'] = number
newClasses = newClasses.loc[:,['CrseID','Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]

newClasses.to_sql(con=engine, name='courses', if_exists='replace', index=True)
"""
