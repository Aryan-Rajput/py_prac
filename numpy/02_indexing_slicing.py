# Indexing and Slicing
# Practice accessing and slicing array elements

import numpy as np

# Create sample arrays
arr1d = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
arr2d = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12]])

print("1D Array:", arr1d)
print("2D Array:\n", arr2d)

# Basic indexing (1D)
print("\n--- 1D Indexing ---")
print("First element:", arr1d[0])
print("Last element:", arr1d[-1])
print("Third element:", arr1d[2])

# Basic indexing (2D)
print("\n--- 2D Indexing ---")
print("Element at row 0, col 1:", arr2d[0, 1])
print("Element at row 2, col 3:", arr2d[2, 3])
print("First row:", arr2d[0])
print("First column:", arr2d[:, 0])

# Slicing (1D)
print("\n--- 1D Slicing ---")
print("Elements 2 to 5:", arr1d[2:6])
print("First 4 elements:", arr1d[:4])
print("Last 3 elements:", arr1d[-3:])
print("Every 2nd element:", arr1d[::2])
print("Reversed array:", arr1d[::-1])

# Slicing (2D)
print("\n--- 2D Slicing ---")
print("First 2 rows:\n", arr2d[:2])
print("Last 2 columns:\n", arr2d[:, -2:])
print("Subarray (rows 0-1, cols 1-2):\n", arr2d[:2, 1:3])

# Boolean indexing
print("\n--- Boolean Indexing ---")
print("Elements > 40:", arr1d[arr1d > 40])
print("Elements divisible by 3:", arr1d[arr1d % 3 == 0])

# Boolean indexing on 2D
print("2D elements > 5:", arr2d[arr2d > 5])

# Fancy indexing (using arrays of indices)
print("\n--- Fancy Indexing ---")
indices = np.array([0, 2, 4])
print("Elements at indices 0, 2, 4:", arr1d[indices])

# 2D fancy indexing
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 1, 2])
print("Diagonal elements:", arr2d[row_indices, col_indices])

# Combining conditions
print("\n--- Combined Conditions ---")
print("Elements > 20 AND < 60:", arr1d[(arr1d > 20) & (arr1d < 60)])
print("Elements < 20 OR > 70:", arr1d[(arr1d < 20) | (arr1d > 70)])

# Using np.where
print("\n--- np.where ---")
result = np.where(arr1d > 50, arr1d, 0)  # Keep if > 50, else 0
print("Keep if > 50, else 0:", result)
