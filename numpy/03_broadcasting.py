# Broadcasting
# Practice NumPy broadcasting rules

import numpy as np

# Broadcasting: NumPy automatically expands arrays to perform operations
# Rules:
# 1. Arrays with fewer dimensions are padded with ones on the left
# 2. Arrays with size 1 in a dimension act as if they had the size of the largest array

# Scalar broadcasting
print("--- Scalar Broadcasting ---")
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)
print("Array + 10:", arr + 10)
print("Array * 2:", arr * 2)

# 1D array with 2D array
print("\n--- 1D with 2D Broadcasting ---")
arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
arr1d = np.array([10, 20, 30])

print("2D array:\n", arr2d)
print("1D array:", arr1d)
print("2D + 1D (adds to each row):\n", arr2d + arr1d)

# Column broadcasting
print("\n--- Column Broadcasting ---")
col_arr = np.array([[100], [200], [300]])
print("Column array:\n", col_arr)
print("2D + column array (adds to each column):\n", arr2d + col_arr)

# Broadcasting with different shapes
print("\n--- Different Shapes ---")
a = np.ones((3, 4))
b = np.arange(4)
print("Shape of a:", a.shape)
print("Shape of b:", b.shape)
print("a + b:\n", a + b)

# Outer product using broadcasting
print("\n--- Outer Product ---")
x = np.array([1, 2, 3])
y = np.array([10, 20, 30, 40])
outer = x[:, np.newaxis] * y  # x becomes (3,1), y is (4,) -> result is (3,4)
print("x:", x)
print("y:", y)
print("Outer product:\n", outer)

# Centering data (subtracting mean)
print("\n--- Practical: Centering Data ---")
data = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
mean_per_column = data.mean(axis=0)
print("Original data:\n", data)
print("Mean per column:", mean_per_column)
print("Centered data:\n", data - mean_per_column)

# Normalizing data (min-max scaling)
print("\n--- Practical: Normalizing Data ---")
min_vals = data.min(axis=0)
max_vals = data.max(axis=0)
normalized = (data - min_vals) / (max_vals - min_vals)
print("Normalized data:\n", normalized)

# Broadcasting shape compatibility check
print("\n--- Shape Compatibility ---")
print("(3,4) and (4,) -> Compatible")
print("(3,4) and (3,1) -> Compatible")
print("(3,4) and (3,) -> NOT Compatible (would raise error)")
