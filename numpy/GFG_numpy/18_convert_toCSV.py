# Convert a NumPy array into a CSV file

import pandas as pd
import numpy as np

# Different methods to convert a NumPy array to a CSV file are:
# -  1. Using DataFrame.to_csv() method
# -  2. Using NumPy_array.tofile() method
# -  3. Using NumPy.savetxt() method
# -  4. Using File Handling operations

# --------------------------------------------------------------------------------------------------------------------------------------

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

DF.to_csv("..\\GFG_numpy\\csv\\data2.csv", index=False)  # index=False to avoid writing row indices/labels

# --------------------------------------------------------------------------------------------------------------------------------------

# Convert a NumPy array into a CSV using numpy_array.tofile()

arr2 = np.arange(1,11)
print(arr2)

# use the tofile() method 
# and use ',' as a separator
arr2.tofile("..\\GFG_numpy\\csv\\to_file_data1.csv", sep = ',')

# --------------------------------------------------------------------------------------------------------------------------------------

# Convert a NumPy array into a CSV using numpy.savetxt()
arr3 = np.arange(1,21).reshape(4,5)
print(arr3)
# use the savetxt() method
np.savetxt("..\\GFG_numpy\\csv\\savetxt_data1.csv", arr3, delimiter=',')
# here the output shows the values in float format by default
# to change that we can use the fmt parameter to specify the format
np.savetxt("..\\GFG_numpy\\csv\\savetxt_data2.csv", arr3, delimiter=',', fmt='%d')

# --------------------------------------------------------------------------------------------------------------------------------------

# Convert a NumPy array into a CSV using file handling
arr4 = np.arange(1,16).reshape(3,5)
print(arr4)
# open a file in write mode
with open("..\\GFG_numpy\\csv\\file_handling_data1.csv", 'w') as f:
    # iterate through the array and write each row to the file
    for row in arr4:
        # convert each element to string and join with commas
        row_str = ','.join(map(str, row))
        # write the row to the file
        f.write(row_str + '\n')
# close the file
f.close()

# we can also use this :-
# create an array
a = np.array([[1, 6, 4],
                [2, 4, 8],
                [3, 9, 1], 
                [11, 23, 43]])

# save array into csv file
rows = ["{},{},{}".format(i, j, k) for i, j, k in a]
text = "\n".join(rows)

with open('..\\GFG_numpy\\csv\\file_handling_data2.csv', 'w') as f:
    f.write(text)

# this method is less efficient for large arrays compared to the other methods mentioned above.

# --------------------------------------------------------------------------------------------------------------------------------------

