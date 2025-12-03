# Reshaping and Stacking Arrays
# Practice reshaping and combining arrays

import numpy as np

# Create sample array
arr = np.arange(12)
print("Original array:", arr)
print("Shape:", arr.shape)

# Reshape
print("\n--- Reshape ---")
reshaped_3x4 = arr.reshape(3, 4)
print("Reshaped to 3x4:\n", reshaped_3x4)

reshaped_4x3 = arr.reshape(4, 3)
print("Reshaped to 4x3:\n", reshaped_4x3)

reshaped_2x2x3 = arr.reshape(2, 2, 3)
print("Reshaped to 2x2x3:\n", reshaped_2x2x3)

# Using -1 for automatic dimension calculation
print("\n--- Auto Dimension with -1 ---")
# Automatically calculates 4
print("Reshape to (3, -1):\n", arr.reshape(3, -1))

# Automatically calculates 6
print("Reshape to (-1, 2):\n", arr.reshape(-1, 2))

# Flatten (returns copy)
print("\n--- Flatten ---")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print("Original matrix:\n", matrix)
print("Flattened:", matrix.flatten())

# Ravel (returns view if possible)
print("\n--- Ravel ---")
print("Raveled:", matrix.ravel())

# Transpose
print("\n--- Transpose ---")
print("Transposed:\n", matrix.T)

# Resize (modifies array in-place or returns new array)
print("\n--- Resize ---")
arr_copy = arr.copy()
print("np.resize to (4, 4):\n", np.resize(arr_copy, (4, 4)))
# Repeats elements if needed

# Adding dimensions
print("\n--- Adding Dimensions ---")
arr1d = np.array([1, 2, 3])
print("Original shape:", arr1d.shape)

# Using np.newaxis
row_vector = arr1d[np.newaxis, :]
print("Row vector shape:", row_vector.shape)

col_vector = arr1d[:, np.newaxis]
print("Column vector shape:", col_vector.shape)

# Using expand_dims
print("expand_dims axis=0:", np.expand_dims(arr1d, axis=0).shape)
print("expand_dims axis=1:", np.expand_dims(arr1d, axis=1).shape)

# Squeeze (remove dimensions of size 1)
print("\n--- Squeeze ---")
arr_with_ones = np.array([[[1, 2, 3]]])
print("Shape with size-1 dims:", arr_with_ones.shape)
print("Squeezed shape:", np.squeeze(arr_with_ones).shape)

# Stacking arrays
print("\n--- Vertical Stack (vstack) ---")
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a:", a)
print("b:", b)
print("vstack:\n", np.vstack([a, b]))

print("\n--- Horizontal Stack (hstack) ---")
print("hstack:", np.hstack([a, b]))

# Stack along new axis
print("\n--- Stack (new axis) ---")
print("stack axis=0:\n", np.stack([a, b], axis=0))
print("stack axis=1:\n", np.stack([a, b], axis=1))

# Concatenate
print("\n--- Concatenate ---")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
print("arr1:\n", arr1)
print("arr2:\n", arr2)
print("Concatenate axis=0:\n", np.concatenate([arr1, arr2], axis=0))
print("Concatenate axis=1:\n", np.concatenate([arr1, arr2], axis=1))

# Splitting arrays
print("\n--- Splitting ---")
arr = np.arange(12).reshape(3, 4)
print("Original:\n", arr)
print("hsplit into 2:\n", np.hsplit(arr, 2))
print("vsplit into 3:\n", np.vsplit(arr, 3))

# Tile and repeat
print("\n--- Tile and Repeat ---")
small = np.array([1, 2, 3])
print("Original:", small)
print("Tile (2):", np.tile(small, 2))
print("Tile (2, 3):\n", np.tile(small, (2, 3)))
print("Repeat (each 3 times):", np.repeat(small, 3))
