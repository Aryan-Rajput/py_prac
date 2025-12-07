# provides a function known as 'numpy.pad()' to construct the borders of an array.
import numpy as np
# Create a 2-D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
print("Original Array:\n", arr)
# Pad the array with a border of width 1 and constant value 0
padded_arr = np.pad(arr, pad_width=1, mode='constant', constant_values=0)
print("Padded Array with constant border:\n", padded_arr)

# Different modes of padding
# 1. 'edge' mode: Pads with the edge values of the array
# 2. 'reflect' mode: Pads with the reflection of the array
# 3. 'symmetric' mode: Pads with the symmetric reflection of the array

# Example of 'edge' mode
edge_padded_arr = np.pad(arr, pad_width=1, mode='edge')
print("Edge Padded Array:\n", edge_padded_arr)

# Example of 'reflect' mode
reflect_padded_arr = np.pad(arr, pad_width=1, mode='reflect')
print("Reflect Padded Array:\n", reflect_padded_arr)

# Example of 'symmetric' mode
symmetric_padded_arr = np.pad(arr, pad_width=1, mode='symmetric')
print("Symmetric Padded Array:\n", symmetric_padded_arr)

# Note: The 'pad_width' parameter can be an integer or a tuple specifying the number of values to pad
# on each axis. The 'mode' parameter determines how the padding is done.

# You can also specify different pad widths for each axis by providing a tuple of tuples.
# Example of different pad widths for each axis
custom_padded_arr = np.pad(arr, pad_width=((2, 1), (3, 2)), mode='constant', constant_values=0)
print("Custom Padded Array with different pad widths:\n", custom_padded_arr)