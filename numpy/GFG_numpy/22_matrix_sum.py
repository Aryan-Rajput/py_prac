# Python | Numpy matrix.sum()

# The matrix.sum() method returns the sum of all the elements in the matrix.
import numpy as np
m = np.matrix([[4, 1],
              [12, 3]])
out = m.sum()
print(out)
# Output: 20

# ---------------------------------------------------------------------------------------

m = np.matrix([[4, 1, 9],
               [12, 3, 1],
               [4, 5, 6]])
out = m.sum(axis=1)
print(out)
# Output: [[14]
#          [16]
#          [15]]

# ----------------------------------------------------------------------------------------

m = np.matrix([[4, 1, 9],
                [12, 3, 1],
                [4, 5, 6]])
out = m.sum(axis=0)
print(out)
# Output: [[20  9 16]]