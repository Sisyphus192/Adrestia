import pandas as pd
import numpy as np
import re

def tables():
    local_path = '../data/APPM.csv'
    df = pd.read_csv(local_path)
    dfAPPM = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/ASEN.csv'
    df = pd.read_csv(local_path)
    dfASEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/CHEN.csv'
    df = pd.read_csv(local_path)
    dfCHEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/CSCI.csv'
    df = pd.read_csv(local_path)
    dfCSCI = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/CVEN.csv'
    df = pd.read_csv(local_path)
    dfCVEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/ECEN.csv'
    df = pd.read_csv(local_path)
    dfECEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/MATH.csv'
    df = pd.read_csv(local_path)
    dfMATH = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/MCEN.csv'
    df = pd.read_csv(local_path)
    dfMCEN = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    local_path = '../data/PHYS.csv'
    df = pd.read_csv(local_path)
    dfPHYS = df.loc[:,['Subject','Crse','CrsTitle','CourseOverall','HoursPerWkInclClass','Challenge','HowMuchLearned']]
    allClasses = [dfAPPM,dfASEN,dfCHEN,dfCSCI,dfCVEN,dfECEN,dfMATH,dfMCEN,dfPHYS]
    classes = pd.concat(allClasses)
    classes = classes.dropna()
    #classes[classes.CourseOverall != 'nan']
    #np.savetxt('ClassesInfo.txt',classes, fmt='%s')
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
    #np.savetxt('ClassesInfo.txt',newClasses, fmt='%s')
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
    #newClasses.head(1000)
    dfAPPM = newClasses.loc[newClasses['Subject']=='APPM',:]
    #dfAPPM.head(1000)
    return newClasses
    
