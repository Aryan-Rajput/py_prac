# In NumPy, you can extract 2D diagonals from each sub-array of a 3D array using numpy.diagonal() function.

import numpy as np
# Create a 3D NumPy array
arr_3d = np.array([[[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],

                   [[10, 11, 12],
                    [13, 14, 15],
                    [16, 17, 18]]])

# Extract diagonals from each 2D sub-array
diagonals = arr_3d.diagonal(axis1=2, axis2=1)
# axis1 and axis2 specify the two axes to extract the diagonals from.

# but what if i want the other diagonal
# we can achieve this by flipping the 2D arrays along the last axis before extracting the diagonals
flipped_arr_3d = np.flip(arr_3d, axis=2)
# np.flip() function is used to reverse the order of elements in an array along a specified axis.
    # Here, axis=2 indicates that we want to flip the elements along the last axis (the columns of each 2D sub-array).
print("Original 3D Array:\n", arr_3d)
print("Flipped 3D Array:\n", flipped_arr_3d)
# Now extract the diagonals from the flipped arrays
other_diagonals = flipped_arr_3d.diagonal(axis1=2, axis2=1)

print("\nDiagonals from each 2D sub-array:\n", diagonals)
print("\nOther Diagonals from each 2D sub-array:\n", other_diagonals)