# trim_zeros() in Python

import numpy as np

a = np.array([0, 0, 3, 4, 0, 5, 0, 0])
res = np.trim_zeros(a)
print(res)

# filt (array_like): A 1-D array of numeric values from which zeros will be trimmed.
# trim (str, optional): Indicates which zeros to remove, 
#   'f' for leading (front), 'b' for trailing (back) and 'fb' (default) for both.
# Returns: A 1-D array with the leading and/or trailing zeros removed.

b = np.array([0, 0, 0, 7, 8, 9, 0])
res2 = np.trim_zeros(b, 'f')
print(res2) 
res3 = np.trim_zeros(b, 'b')
print(res3)
res4 = np.trim_zeros(b, 'fb')
print(res4)

# Output:
# [3 4 0 5] <-- res
# [7 8 9 0] <-- res2
# [0 0 0 7 8 9] <-- res3
# [7 8 9] <-- res4

# Note: The trim_zeros function only works with 1-D arrays.
# For multi-dimensional arrays, consider using boolean indexing or other methods to remove zeros.
# Example with multi-dimensional array using boolean indexing
c = np.array([[0, 1, 0], [2, 0, 3], [0, 0, 0]])
c_nonzero = c[np.any(c != 0, axis=1)]
print(c_nonzero)
# Output:
# [[0 1 0]
#  [2 0 3]]
# Here, we removed rows that are entirely zeros.
