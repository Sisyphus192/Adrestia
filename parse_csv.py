import pandas as pd

df = pd.read_csv('CSCI.csv')
print(df.head())
classes = {}

# seperate the data frame by class num into a dictionary
for i in df.Crse.unique():
    classes[i] = df[df['Crse'] == i]

print(classes[1300].head())

def get_average_difficulty(crseID):
    return classes[crseID]['Challenge'].mean()

def find_most_difficult_crse():
    hardest = {}
    for i in classes:
        hardest[i] = classes[i]['Challenge'].mean()
    s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get, reverse=True)]
    for i in range(10):
        print(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1])

def find_most_easiest_crse():
     hardest = {}
     for i in classes:
         hardest[i] = classes[i]['Challenge'].mean()
     s = [(k, hardest[k]) for k in sorted(hardest, key=hardest.get)]
     for i in range(10):
         print(s[i][0], classes[s[i][0]]['CrsTitle'].iloc[0], s[i][1])
