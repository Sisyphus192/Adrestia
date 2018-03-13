import pandas as pd
import numpy as np

df = pd.read_csv('CHEN.csv')
#print(df.head())
classes = {}

# seperate the data frame by class num into a dictionary
df = df[df['FormsReturned'] > 0]
df['HoursPerWkInclClass'] = df['HoursPerWkInclClass'].astype('category')
#print(df.iloc[2477])
#print(df['HoursPerWkInclClass'].isnull().sum().sum())
df['HoursPerWkInclClass'] = df['HoursPerWkInclClass'].cat.rename_categories([2,11,14,17,5,8]).astype('int')
#print(df.iloc[2477])
#print(df['HoursPerWkInclClass'].isnull().sum().sum())
for i in df.Crse.unique():
    classes[i] = df[df['Crse'] == i]

#print(classes[1300].head())

def difficulty(crseID):
    return np.average(classes[i]['Challenge'], weights=classes[i]['FormsReturned'])

def workload(crseID):
    classes[crseID] = classes[crseID][classes[crseID]['HoursPerWkInclClass']>0]
    return np.average(classes[crseID]['HoursPerWkInclClass'], weights=classes[crseID]['FormsReturned'])


def find_hardest_crse():
    hardest = {}
    for i in classes:
        if i < 5000:
            hardest[i] = np.average(classes[i]['Challenge'], weights=classes[i]['FormsReturned'])
    s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get, reverse=True)]
    for i in range(10):
        print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))

def find_easiest_crse():
    hardest = {}
    for i in classes:
        if i < 5000:
            hardest[i] = np.average(classes[i]['Challenge'], weights=classes[i]['FormsReturned'])
    s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get)]
    for i in range(10):
        print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))

def find_best_crse():
     hardest = {}
     for i in classes:
         if i < 5000:
             hardest[i] = np.average(classes[i]['CourseOverall'], weights=classes[i]['FormsReturned'])
     s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get, reverse=True)]
     for i in range(10):
         print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))

def find_worst_crse():
    hardest = {}
    for i in classes:
        if i < 5000:
            hardest[i] = np.average(classes[i]['CourseOverall'], weights=classes[i]['FormsReturned'])
    s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get)]
    for i in range(10):
        print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))

def find_most_interesting_crse():
     hardest = {}
     for i in classes:
         if i < 5000:
             hardest[i] = np.average(classes[i]['HowMuchLearned'], weights=classes[i]['FormsReturned'])
     s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get, reverse=True)]
     for i in range(10):
         print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))

def find_least_interesting_crse():
    hardest = {}
    for i in classes:
        if i < 5000:
            hardest[i] = np.average(classes[i]['HowMuchLearned'], weights=classes[i]['FormsReturned'])
    s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get)]
    for i in range(10):
        print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))

def find_highest_workload_crse():
     hardest = {}
     for i in classes:
         if i < 5000:
             classes[i] = classes[i][classes[i]['HoursPerWkInclClass']>0]
             hardest[i] = np.average(classes[i]['HoursPerWkInclClass'], weights=classes[i]['FormsReturned'])
     s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get, reverse=True)]
     for i in range(10):
         print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))

def find_lowest_workload_crse():
    hardest = {}
    for i in classes:
        if i < 5000:
            classes[i] = classes[i][classes[i]['HoursPerWkInclClass']>0]
            hardest[i] = np.average(classes[i]['HoursPerWkInclClass'], weights=classes[i]['FormsReturned'])
    s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get)]
    for i in range(10):
        print("{0}, {1}, {2:.2f}".format(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1]))
