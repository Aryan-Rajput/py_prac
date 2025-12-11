# flatten() Function
# The flatten() function creates a copy of the array and returns it in 1D form.

import numpy as np
matrix = np.array([[10, 20, 30], [40, 50, 60]])
flat = matrix.flatten()
print(flat)


m2 = np.array([[6, 9], [8, 5], [18, 21]])
f2 = m2.flatten()
print(f2)

