# Creating DataFrame from Dictionary of Array/Lists - Python

import pandas as pd  
data = {'Category': ['Array', 'Stack', 'Queue'], 'Marks': [20, 21, 19]}  
df = pd.DataFrame(data)  
print(df)

# for multi-dimensional data
# example 1
data = {'Area': ['Array', 'Stack', 'Queue'], 'Student_1': [20, 21, 19], 'Student_2': [15, 20, 14]}
df = pd.DataFrame(data)
print(df)


# with custom index
data = {'Area': ['Array', 'Stack', 'Queue'], 'Student_1': [20, 21, 19], 'Student_2': [15, 20, 14]}  
df = pd.DataFrame(data, index=['Cat_1', 'Cat_2', 'Cat_3'])  
print(df)

