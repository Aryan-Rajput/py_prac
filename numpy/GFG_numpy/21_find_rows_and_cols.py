# Find the number of rows and columns of a given matrix using NumPy
import numpy as np

# Using .shape Attribute

matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rows, cols = matrix.shape
print("rows: ", rows)
print("columns: ", cols)

# Using numpy.shape() Function
matrix = np.array([[10, 20, 30, 40], [50, 60, 70, 80]])
rows, cols = np.shape(matrix)
print("rows: ", rows)
print("columns: ", cols)

# difference between .shape attribute and numpy.shape() function
# The .shape attribute is accessed directly from the NumPy array object, while numpy.shape()
# is a function that takes the array as an argument and returns its shape.

# --------------------------------------------------------------------------------------------------------------------------------------

# Using Indexing

matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45], [50, 55, 60]])
rows = len(matrix)
cols = len(matrix[0])   
print("rows: ", rows)
print("columns: ", cols)

# Note: This method assumes that the matrix is non-empty and rectangular (all rows have the same number of columns).

# --------------------------------------------------------------------------------------------------------------------------------------

# Using numpy.size() Function
matrix = np.array([[2, 4, 6, 8], [10, 12, 14, 16], [18, 20, 22, 24]])
rows = np.size(matrix, 0)  # size along axis 0 (rows)
cols = np.size(matrix, 1)  # size along axis 1 (columns)
print("rows: ", rows)
print("columns: ", cols)
# Note: The numpy.size() function can be used to find the size of a specific axis in a NumPy array.
# Here, we specify axis=0 to get the number of rows and axis=1 to get the number of columns.

# --------------------------------------------------------------------------------------------------------------------------------------

# Using numpy.reshape()
matrix = np.array([[1, 3, 5, 7], [9, 11, 13, 15]])
reshaped_matrix = np.reshape(matrix, (2, 4))  # reshape to 2 rows and 4 columns
rows, cols = reshaped_matrix.shape
print("rows: ", rows)
print("columns: ", cols)
# Note: The numpy.reshape() function is primarily used to change the shape of an array.