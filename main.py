import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')
data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'age': [20, 21, 19, 22, 20], 
        'grade': [85, 90, 78, 92, 88]}
print(df.head())