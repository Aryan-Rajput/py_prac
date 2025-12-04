import numpy as np

a = np.array([1, 2, 3])
print(a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# dtype - data type of array elements
c = np.array([1, 2, 3], dtype=np.float64)

# difference between float and np.float64
d = np.array([1, 2, 3], dtype=float)
print(c)
print(d)

# np.arange - like python range but returns array
arr_range = np.arange(0, 10, 2)  # start, stop, step
# print(arr_range)

# np.arange ccan be used wih reshape to create multi-d arrays
arr_r = np.arange(1, 126).reshape(5, 5, 5)  # 5x5x5 array
arr_r = np.arange(1, 26).reshape(5, 5)  # 5x5 array
# print(arr_r)

# np.ones and np.zeros 
# can also include functions
arr_ones = np.ones((3, 4), dtype=np.int32)  # 3x4 array
arr_zeros = np.zeros((2, 3))  # 2x3 array
print(arr_ones)
print(arr_zeros)

# np.random.rand it will create array of given shape and
# fill with random values between 0 and 1
# np.randint(low, high=None, size=None, dtype=int)
arr_rand = np.random.rand(3, 2)  # 3x2 array
print(arr_rand)

# np.linspace - returns evenly spaced numbers over a specified interval
arr_lin = np.linspace(0, 1, 5)  # start, stop, num of points
print(arr_lin)

# Creating identity matrix
identity = np.eye(4)
print("\nIdentity matrix:\n", identity)

# Creating empty array (uninitialized)
empty_arr = np.empty((2, 3))
print("\nEmpty array:\n", empty_arr)

# Array attributes
print("\n--- Array Attributes ---")
print("Shape:", arr_r.shape)
print("Dimensions:", arr_r.ndim)
print("Size:", arr_r.size)
print("Data type:", arr_r.dtype)

# Changing data type
float_arr = np.array([1, 2, 3], dtype=np.float64)
print("\nFloat array:", float_arr, "dtype:", float_arr.dtype)

# # shape manipulation 
# print("\n--- Shape Manipulation ---")
matrix = np.array([[1, 2, 3], [4, 5, 6]])
# print("Original shape:", matrix.shape)
reshaped = matrix.reshape(3, 2)
# print("Reshaped (3,2):\n", reshaped)
reshaped_2x3 = matrix.reshape(2, 3)
# print("Reshaped (2,3):\n", reshaped_2x3)

# nparry.shape returns a tuple representing the dimensions of the array
arr = np.arange(12)
# print("\nOriginal array:", arr)
# print("Shape:", arr.shape)
reshaped_3x4 = arr.reshape(3, 4)
# print("Reshaped to 3x4:\n", reshaped_3x4)

# itemsize - size in bytes of each element
arr_itmize_1 = np.array([1, 2, 3], dtype=np.int32)
arr_itmize_2 = np.array([1, 2, 3], dtype=np.int64)
# print(arr_itmize_1)
# print(arr_itmize_1)
print("Item size (bytes):", arr_itmize_1.itemsize)
print("Item size (bytes):", arr_itmize_2.itemsize)
# print("Total size (bytes):", arr.nbytes)

# changing shape using -1
arr_neg = np.arange(8)
print(arr_neg)
reshaped_neg = arr_neg.reshape(2, 4)  # infers second dimension
print(reshaped_neg)




# --------------------------------------------------------------------------------------------------------------------------------------------------------

# import numpy as np

# array operations

a1 = np.arange(12).reshape(3, 4)
a2 = np.arange(12, 24).reshape(3, 4)

# scaler operations
print(a1 + 10)
print(a1 * 2)
print(a1 / 2)
print(a1 - 5)
print(a1 ** 2)
print(a1 % 2)

# relational operations
print(a1 > 5)
print(a1 <= 8)
print(a1 == 3)
print(a1 != 10)

# [[False False False False]
#  [False False  True  True]
#  [ True  True  True  True]]

# [[ True  True  True  True]
#  [ True  True  True  True]
#  [ True False False False]]

# [[False False False  True]
#  [False False False False]
#  [False False False False]]

# [[ True  True  True  True]
#  [ True  True  True  True]
#  [ True  True False  True]]

# vectorized operations
print(a1 + a2)
print(a1 * a2)
print(a2 - a1)
print(a2 / a1)
print(a1 ** 2)
print(a2 % 3)


