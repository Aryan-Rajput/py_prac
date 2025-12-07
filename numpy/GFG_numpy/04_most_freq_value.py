# how to find the most frequent value in the NumPy array. 

import numpy as np

# way 1
# --> 1. Apply bincount() method of NumPy to get the count of occurrences of each element in the array.
# --> 2. The n, apply argmax() method to get the value having a maximum number of occurrences(frequency).

arr = np.array([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5])
print("Original Array:", arr)
# Get the count of occurrences of each element
counts = np.bincount(arr)
print("Counts:", counts)
# Get the most frequent value
most_frequent_value = np.argmax(counts)
print("Most Frequent Value (Way 1):", most_frequent_value)

# way 2
# --> 1. Use np.unique() method with return_counts=True to get unique elements and their counts.
# --> 2. Then use np.argmax() on the counts to find the index of the most frequent element.
arr2 = np.array([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5])
print("Original Array:", arr2)
# Get unique elements and their counts
unique_elements, counts = np.unique(arr2, return_counts=True)
print("Unique Elements:", unique_elements)
print("Counts:", counts)
# Get the index of the most frequent element
most_frequent_index = np.argmax(counts)
# Get the most frequent value using the index
most_frequent_value2 = unique_elements[most_frequent_index]
print("Most Frequent Value (Way 2):", most_frequent_value2)

# ------------------------------------------------------------------------------------------------------------------

# we can also use scipy.stats.mode() to find the most frequent value in a NumPy array
# but here we are focusing on numpy methods only

# ------------------------------------------------------------------------------------------------------------------

# it also can be used for 2d arrays but we need to specify the axis along which we want to find the most frequent value
# Example for 2D array
arr_2d = np.array([[1, 2, 2],
                   [3, 4, 4],
                   [3, 4, 4],
                   [3, 4, 4],
                   [4, 5, 5],
                   [4, 5, 5]])
print("Original 2D Array:\n", arr_2d)
# Get unique elements and their counts along axis 0 (columns)
unique_elements_2d, counts_2d = np.unique(arr_2d, return_counts=True, axis=0)

# Get the index of the most frequent element along axis 0
most_frequent_index_2d = np.argmax(counts_2d, axis=0)

# Get the most frequent values using the indices
most_frequent_values_2d = unique_elements_2d[most_frequent_index_2d]

print("Most Frequent Values in 2D Array (Way 2):", most_frequent_values_2d)
# Note: For 2D arrays, the concept of "most frequent value" can be ambiguous depending on 
# whether you want it per row, per column, or overall.
# Here, we demonstrated it along the columns (axis=0).

