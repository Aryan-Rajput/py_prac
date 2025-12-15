# Make a Pandas DataFrame with Two-dimensional List - Python
import pandas as pd
import numpy as np

# If you already have data stored as a two-dimensional list (a list inside another list, like a table),
# you can turn it into a Pandas DataFrame so it’s easier to view, label, and work with similar to working in Excel.


# Using pd.DataFrame()
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

# Using pd.DataFrame.from_records()
data = [['Alex', 10], ['Bob', 12], ['Clarke', 13]]
df = pd.DataFrame.from_records(data, columns=['Name', 'Age'])
print(df)

# difference between pd.DataFrame() and pd.DataFrame.from_records() is minimal in this case,
# but pd.DataFrame.from_records() is more versatile for complex data structures.
# eg when dealing with structured arrays or records with named fields.

# Using pd.DataFrame.from_dict()
data = [['Geek1', 26, 'Scientist'], ['Geek2', 31, 'Researcher'], ['Geek3', 24, 'Engineer']]
columns = ['Name', 'Age', 'Occupation']
df = pd.DataFrame.from_dict(dict(zip(columns, zip(*data))))
print(df)

# Creating a DataFrame with Specified Data Types
ata = [['Geek1', 'Reacher', 25], ['Geek2', 'Pete', 30], ['Geek3', 'Wilson', 26], ['Geek4', 'Williams', 22]]
columns = ['FName', 'LName', 'Age']
df = pd.DataFrame(data, columns=columns)
print(df)


