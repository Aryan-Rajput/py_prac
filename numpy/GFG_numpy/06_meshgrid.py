import numpy as np
# to build an array containing all possible combinations of elements from two NumPy arrays
# we can use the np.meshgrid() function.
# The np.meshgrid() function takes two 1-D arrays as input and returns two 2-D matrices representing the grid of coordinates.
    # --> np.meshgrid() is used to create coordinate matrices from coordinate vectors.
        # It is commonly used in plotting and 3D surface generation.
        # It generates a grid of points based on the input arrays, which can be useful for evaluating functions over a grid or for visualizing data.

# syntax:
# numpy.meshgrid(*xi, copy=True, sparse=False, indexing='xy')


# all combinations of two NumPy arrays
arr1d = np.array([1, 2, 3])
arr2d = np.array([4, 5, 6])
# Create a meshgrid from the two arrays
X, Y = np.meshgrid(arr1d, arr2d)
print("Array 1D:", arr1d)
print("Array 2D:", arr2d)
print("Meshgrid X:\n", X)
print("Meshgrid Y:\n", Y)
res = np.array(np.meshgrid(arr1d, arr2d)).T.reshape(-1, 2)
# here the reshape(-1, 2) is used to reshape the array into a 2D array with 2 columns
    # --> the .T is used to transpose the array
    #     --> so that each row contains a pair of elements from the two input arrays
    # --> the -1 in reshape means that the number of rows will be automatically calculated 
    #     based on the length of the original array

print("All combinations of two arrays:\n", res)
# we can extend this to more than two arrays as well
a = np.array([0, 1])
b = np.array([0, 1])
c = np.array([0, 1])
d = np.array([0, 1])

# print original arrays
print(a)
print(b)
print(c)
print(d)
# combine all arrays to get all possible combinations
res = np.array(np.meshgrid(a, b, c, d)).T.reshape(-1, 4)
# here the reshape(-1, 4) is used to reshape the array into a 2D array with 4 columns
print("\nCombine array:")
print(res)