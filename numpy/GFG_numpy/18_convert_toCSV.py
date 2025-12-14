# Convert a NumPy array into a CSV file

import pandas as pd
import numpy as np

# Different methods to convert a NumPy array to a CSV file are:
# -  1. Using DataFrame.to_csv() method
# -  2. Using NumPy_array.tofile() method
# -  3. Using NumPy.savetxt() method
# -  4. Using File Handling operations

# create a dummy array
arr = np.arange(1,11).reshape(2,5)
print(arr)

# convert array into dataframe
DF = pd.DataFrame(arr)

# save the dataframe as a csv file
# DF.to_csv("data1.csv")

# if wew want to save the csv in a certain location, we can provide the full path
# for example: we want to save it in C:\Users\aryrajpu\Desktop\All_Folders\vs_py\py_repo\py_prac\py_prac\numpy\GFG_numpy\csv
DF.to_csv("C:/Users/aryrajpu/Desktop/All_Folders/vs_py/py_repo/py_prac/py_prac/numpy/GFG_numpy/csv/data1.csv")
# DF.to_csv("<full_path>/data1.csv")

DF.to_csv("..\GFG_numpy\csv\data2.csv", index=False)  # index=False to avoid writing row indices/labels

