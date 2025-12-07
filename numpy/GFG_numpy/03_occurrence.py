# to identify the count of occurrences of each element in a NumPy array
import numpy as np
# Create a 2d NumPy array
arr = np.array([[1, 2, 2, 3],
                [4, 1, 2, 3],
                [1, 5, 6, 3]])
print("Original Array:\n", arr) 
# Find unique elements and their counts
unique_elements, counts = np.unique(arr, return_counts=True)
print("Unique Elements:", unique_elements)

# we can use also check the occurrence of a specific element or sequence in the array
element_to_check = 2
occurrence_count = np.sum(arr == element_to_check)
print(f"Occurrence of element {element_to_check}:", occurrence_count)

# for checking sequence occurrence we can use the following approach
sequence_to_check = [1, 2]
# Flatten the array to 1D for sequence checking
# the flatten() function returns a copy of the array collapsed into one dimension
# eg
flattened_arr = arr.flatten()
print("Flattened Array:", flattened_arr)
# why flatten() instead of ravel()?
# because ravel() returns a flattened array as well but it returns a view of the original array whenever possible
# so if we modify the raveled array it may affect the original array whereas flatten() always returns a copy 


# also what are the use cases of flattening an array?
# --> 1. When we want to perform operations that require a 1D array, such as certain 
#        statistical calculations or data processing tasks.
#               but you may ask what kind of statistical calculations?
#               for example, calculating the histogram of pixel intensities in an image often requires flattening 
#               the 2D or 3D array of pixel values into a 1D array.
# --> 2. When we want to simplify the structure of the array for easier iteration or manipulation.


# Create a sliding window view of the flattened array
def count_sequence_occurrences(array, sequence):
    seq_len = len(sequence)
    count = 0
    for i in range(len(array) - seq_len + 1):
        if np.array_equal(array[i:i+seq_len], sequence):
            count += 1
    return count
sequence_count = count_sequence_occurrences(flattened_arr, sequence_to_check)
print(f"Occurrence of sequence {sequence_to_check}:", sequence_count)

# or we can use repr(arr).count('1, 2') to count the occurrence of sequence [1,2] in the array

output = repr(arr).count('1, 2')
print(f"Occurrence of sequence {sequence_to_check} using repr method:", output)


