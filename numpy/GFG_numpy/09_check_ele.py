# we can easily find whether specific values are present or not. 
# For this purpose, we use the "in" operator. "in" operator is used to check whether certain 
# element and values are present in a given 
# sequence and hence return Boolean values 'True" and "False"

import numpy as np
# Create a NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Check if specific values are present in the array
value_to_check1 = 5
value_to_check2 = 10

is_value1_present = value_to_check1 in arr
is_value2_present = value_to_check2 in arr

print(f"Is {value_to_check1} present in the array? {is_value1_present}")
print(f"Is {value_to_check2} present in the array? {is_value2_present}")