# Reverse a Numpy Array - Python

# Using numpy.flip()
# The numpy.flip() function reverses the order of array elements
# along the specified axis. It preserves shape of the array and
# works efficiently for both 1D and multi-dimensional arrays

import numpy as np
arr = np.array([1, 2, 3, 6, 4, 5])
rev = np.flip(arr)
print(rev)

# Using Slicing ([::-1])
# Slicing with [::-1] is a Pythonic way to reverse arrays. It creates a 
# copy of the array in reversed order. While simple and readable, it may
# use slightly more memory since it creates a copy

arr2 = np.array([1, 2, 3, 6, 4, 5])
rev2 = arr2[::-1]
print(rev2)

# but when we use slicing for multi-dimensional arrays we need to specify
# all the colons for all the dimensions except the one we want to reverse

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rev2d = arr2d[::-1, ::-1]
print(rev2d)

# Using numpy.flipud()
# The numpy.flipud() function flips an array vertically (up-down). For 1D 
# arrays, it behaves like numpy.flip(). For 2D arrays, it reverses rows. 
# It is slightly less general than numpy.flip().

arr3d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rev3d = np.flipud(arr3d)
print(rev3d)

# difference between flip and flipud
# flip can reverse along any axis while flipud only reverses along vertical axis
arr3d_flip = np.flip(arr3d, axis=1)  # reversing along horizontal axis
print(arr3d_flip)
# flipud only reverses along vertical axis
arr3d_flipud = np.flipud(arr3d)  # reversing along vertical axis
print(arr3d_flipud)