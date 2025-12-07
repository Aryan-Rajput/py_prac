# how we can use np.squeeze() function in numpy to remove single-dimensional entries from the shape of an array.

import numpy as np
# Create a NumPy array with single-dimensional entries
arr = np.array([
            [[1], [2], [3]],
            [[4], [5], [6]]
                ])
print("Original:", arr.shape)
# Remove single-dimensional entries using np.squeeze()
squeezed_arr = np.squeeze(arr)
print("After Squeeze:", squeezed_arr.shape)

# now what if we want to remove single-dimensional entries only from specific axes

arr2 = np.array([[[1], [2], [3]], [[4], [5], [6]]])
print("Original:", arr2.shape)
# Remove single-dimensional entries from specific axis (axis=2)
# here the axis=2 represents the third dimension which is of size 1
# the axis=1 represents the second dimension which is of size 3 so it will not be removed
# etc..
squeezed_arr2 = np.squeeze(arr2, axis=1)
print("After Squeeze on axis 2:", squeezed_arr2.shape)

# we use squeeze mostly because we want to remove unwanted dimensions from the array

