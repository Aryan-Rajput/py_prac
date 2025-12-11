# count_nonzero method

# When working with arrays, sometimes you need to quickly count how many elements are not equal to zero. NumPy makes this super easy with the numpy.count_nonzero() function.

# This is useful when:

# You want to count valid entries in datasets.
# You’re filtering out missing (zero) values.
# You need quick statistics on arrays.

import numpy as np
arr = [0, 1, 0, 2, 3]
result = np.count_nonzero(arr)
print(result)  # Output: 3

# arr: array_like - Input array.
# axis: int or tuple, optional - None counts over the whole array; int/tuple counts along given axis (row/column).
# keepdims: bool, optional - If this is set to True, the reduced axes will be left in the result as dimensions with size one.

# Example with axis
matrix = np.array([[0, 1, 0], [2, 0, 3]])
row_counts = np.count_nonzero(matrix, axis=1)
print(row_counts)  # Output: [1 2]