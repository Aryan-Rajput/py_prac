# Change the Data Type of the Given NumPy Array

# NumPy arrays are homogenous, meaning all elements in a NumPy array are of the 
# same data type and referred to as array type. You might want to change the data
# type of the NumPy array to perform some specific operations on the entire data set. 

# In this tutorial, we are going to see how to change the data type of the given
# NumPy array. We will use the astype() function of the NumPy library to change
# the data type of the NumPy array.

# ndarray.astype(dtype, order='K', casting='unsafe', subok=True, copy=True)

# dtype: The data type you want to change into.
# order: Controls the memory layout order of the result. Options are ‘C’, ‘F’, ‘A’, ‘K’.
# casting: Controls the type of data casting. Options are ‘no’, ‘equiv’, ‘safe’, ‘same_kind’, ‘unsafe’.
# subok: If True, then sub-classes will be passed-through, otherwise the returned array will be forced to be a base-class array.
# copy: By default, astype() returns a newly allocated array. If set to false, the input array is returned instead of a copy.

import numpy as np
# Create a numpy array
arr = np.array([10, 20, 30, 40, 50])
# Print the array
print(arr)
# Print the data type of the array
print("Data type of arr:", arr.dtype)
# Change the data type of the array to float
arr_float = arr.astype(float)
# Print the new array
print(arr_float)
# Print the data type of the new array
print("Data type of arr_float:", arr_float.dtype)
# Change the data type of the array to string
arr_str = arr.astype(str)
# Print the new array
print(arr_str)
# Print the data type of the new array
print("Data type of arr_str:", arr_str.dtype) # <-- here <U21 means Unicode string of max length 21
# Change the data type of the array to boolean
arr_bool = arr.astype(bool)
# Print the new array
print(arr_bool)
# Print the data type of the new array
print("Data type of arr_bool:", arr_bool.dtype)
# Note: Non-zero values are converted to True, and zero values are converted to False
# You can change the data type to any valid NumPy data type like int, float, complex, str, bool, etc.

# Additional Examples
# Create a 2D numpy array with random values
a1 = np.random.rand(3, 4)
a1 = a1 * 100
a1 = a1.astype(int)
print(a1)

# Create a 3D numpy array with random values
a2 = np.random.rand(2, 3, 4)
a2 = a2 * 100
a2 = a2.astype(int)
print(a2)

# Trigonometric functions example
a3 = np.array([0, 30, 45, 60, 90])
print("a3:", a3)
# Convert degrees to radians
a3_rad = np.deg2rad(a3)
print("a3 in radians:", a3_rad)
# Calculate sine of the angles in radians
a3_sin = np.sin(a3_rad)
print("Sine of a3:", a3_sin)
# Print("Sine:", np.sin(a3_rad))
# etc ...
# Similarly, you can use np.cos(), np.tan(), etc. for other trigonometric functions.

