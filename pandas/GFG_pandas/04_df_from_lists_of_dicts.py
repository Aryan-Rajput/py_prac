import pandas as pd
import numpy as np
import json
# Create a Pandas DataFrame from List of Dictionaries
# Below are the ways by which we can create a Pandas DataFrame from list of dicts:

# -------------------------------------------------------------------

# 1. Using from_records()

data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks':10, 'For': 20, 'geeks': 30}] 

df = pd.DataFrame.from_records(data,index=['1', '2'])
print(df)

# -------------------------------------------------------------------

# 2. Using pd.DataFrame.from_dict()

data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks':10, 'For': 20, 'geeks': 30}]
df = pd.DataFrame.from_dict(data)
print(df)

# -------------------------------------------------------------------

# 3. Using pd.DataFrame()
data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks':10, 'For': 20, 'geeks': 30}]   
df = pd.DataFrame(data)
print(df)

# -------------------------------------------------------------------

# 4. Using pd.DataFrame() with specified columns
data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks':10, 'For': 20, 'geeks': 30}]   
df = pd.DataFrame(data, columns=['Geeks', 'For'])   
print(df)

# -------------------------------------------------------------------

# 3. Using pd.json_normalize

data = [{'Geeks': 'dataframe', 'For': 'using', 'geeks': 'list'},
        {'Geeks':10, 'For': 20, 'geeks': 30}]
df = pd.json_normalize(data)
print(df)