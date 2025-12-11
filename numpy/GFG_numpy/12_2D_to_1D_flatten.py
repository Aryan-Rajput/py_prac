# Flatten a 2d numpy array into 1d array

import numpy as np

ini_array1 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])

# printing initial arrays
print(&quot;initial array&quot;, str(ini_array1))

# Multiplying arrays
res1 = ini_array1.flatten()

# printing res1
print(&quot;New resulting array: &quot;, res1)


# ----------------------------------------------------------------------------------

# using ravel() function

ini_array2 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])

# printing initial arrays
print(&quot;initial array&quot;, str(ini_array2))

# Multiplying arrays
res2 = ini_array2.ravel()

# printing res2
print(&quot;New resulting array: &quot;, res2)

# ----------------------------------------------------------------------------------

# using reshape() function

ini_array3 = np.array([[1, 2, 3], [2, 4, 5], [1, 2, 3]])

# printing initial arrays
print(&quot;initial array&quot;, str(ini_array3))

# Multiplying arrays
res3 = ini_array3.reshape([1, 9])

# printing res3
print(&quot;New resulting array: &quot;, res3)