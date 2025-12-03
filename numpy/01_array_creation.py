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
