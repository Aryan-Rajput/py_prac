# Creating Pandas dataframe using list of lists
import numpy as np
import pandas as pd

data = [['John', 28, 'Engineer'], ['Anna', 24, 'Doctor'], ['Mike', 32, 'Artist']]
columns = ['Name', 'Age', 'Profession']
df = pd.DataFrame(data, columns=columns)
print(df)

# initialize list of lists 
data = [['DS', 'Linked_list', 10], ['DS', 'Stack', 9], ['DS', 'Queue', 7],
        ['Algo', 'Greedy', 8], ['Algo', 'DP', 6], ['Algo', 'BackTrack', 5], ] 

# Create the pandas DataFrame 
df = pd.DataFrame(data, columns = ['Category', 'Name', 'Marks']) 

# print dataframe. 
print(df)

# for missing values

data = [['Geek1', 28, 'Engineer'],
        ['Geek2', None, 'Data Scientist'],
        ['Geek3', 32, None]]

columns = ['Name', 'Age', 'Occupation']

df = pd.DataFrame(data, columns=columns)
df = df.replace({None: np.nan})  # Replacing None with NaN for missing values
print(df)

# handeling different data types
data = [['Geek1', 28, 'Engineer'],
        ['Geek2', 25, 'Data Scientist'],
        ['Geek3', '32', 'Manager']]  # Age represented as a string

columns = ['Name', 'Age', 'Occupation']

df = pd.DataFrame(data, columns=columns)
df['Age'] = pd.to_numeric(df['Age'])  # Convert 'Age' column to numeric, handling errors
print(df)
# here the 'Age' column will be converted to numeric type, and any non-convertible values will be set to NaN.