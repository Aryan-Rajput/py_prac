#  np.isnan() function along with the Bitwise NOT operator (~) can be used to remove NaN values from a NumPy array.

import numpy as np


# Create a NumPy array with NaN values
arr_with_nan = np.array([1, 2, np.nan, 4, np.nan, 6])
print("original array:", arr_with_nan)

# Remove NaN values using np.isnan() and Bitwise NOT operator
cleaned_arr = arr_with_nan[~np.isnan(arr_with_nan)]
print("after cleaning:", cleaned_arr)

# now for 2d array if we want to rempove rows with NaN values
arr_2d_with_nan = np.array([[1, 2, np.nan], [4, 5, 6], [np.nan, 8, 9]])
print("orignal:\n", arr_2d_with_nan)

# Remove rows with NaN values
cleaned_2d_arr = arr_2d_with_nan[~np.isnan(arr_2d_with_nan).any(axis=1)]
print("after cleaning\n", cleaned_2d_arr)

# Output:
# original array: [ 1.  2. nan  4. nan  6.]
# after cleaning: [1. 2. 4. 6.]
# orignal:
#  [[ 1.  2. nan]
#  [ 4.  5.  6.]
#  [nan  8.  9.]]
# after cleaning
# [[4. 5. 6.]]


