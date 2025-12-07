# to combine a 1-D array with a 2-D array and iterate over their elements together we have functions like
# np.nditer()
    # --> np.nditer() is used for iterating over arrays efficiently.
    # It provides a flexible way to traverse and manipulate array elements.
import numpy as np

arr1d = np.array([10, 20, 30, 40])
arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
print("1-D Array:", arr1d)
print("2-D Array:\n", arr2d)

# Use np.nditer to iterate over both arrays
print("Iterating over 1-D and 2-D arrays together:")
for x, y in np.nditer([arr1d, arr2d]):
    print(f"1-D element: {x}, 2-D element: {y}")

# nditer function in NumPy is an iterator that allows you to efficiently loop through arrays, even if they have different shapes.
# It provides a way to iterate over multiple arrays simultaneously, broadcasting them as needed.
# This is particularly useful when you want to perform element-wise operations on arrays of different dimensions.
# Example of using nditer with broadcasting
ar1d = np.array([1, 2, 3])
ar2d = np.array([[10, 20, 30],
                 [40, 50, 60]])
print("1-D Array for Broadcasting:", ar1d)
print("2-D Array for Broadcasting:\n", ar2d)
# Use np.nditer to iterate with broadcasting
print("Iterating with Broadcasting:")
for x, y in np.nditer([ar1d, ar2d]):
    print(x, y)

# Note: When using np.nditer with arrays of different shapes, NumPy will automatically apply 
# broadcasting rules to align the shapes for iteration.
# another example
num1 = np.arange(5)
print("1D array:")
print(num1)

num2 = np.arange(10).reshape(2, 5)
print("\n2D array:")
print(num2)

# Combine 1-D and 2-D arrays
for a, b in np.nditer([num1, num2]):
    print("%d:%d" % (a, b))


# Another way to combine 1D and 2D arrays is by using np.meshgrid()
# np.meshgrid() function is used to create coordinate matrices from coordinate vectors.
