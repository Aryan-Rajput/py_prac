import numpy as np
# diff methods of comparing two NumPy arrays
# --> 1 using np.array_equal()
    # The array_equal() function is the simplest and most reliable way to compare two arrays. It checks whether:
    # Both arrays have the same shape
    # All elements are exactly the same
# --> 2 using np.array_equiv()
    # The array_equiv() function is similar to array_equal(), but it allows for broadcasting. It checks whether:
    # Both arrays can be broadcast to the same shape 
# --> 3 using np.allclose()
    # This method is useful when comparing floating-point arrays where small numerical differences may exist.
    # It checks if all elements are approximately equal within a specified tolerance.
# Using == and .all()
    # This method uses the element-wise equality operator (==) to compare the arrays and then applies 
    # the .all() method to check if all comparisons are True.

# Example arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr3 = np.array([[1, 2, 3], [4, 5, 7]])
arr4 = np.array([[1, 2], [3, 4], [5, 6]])
# 1. Using np.array_equal()
print("Using np.array_equal():")
print("arr1 & arr2 :", np.array_equal(arr1, arr2))  # true
print("arr1 & arr3 :", np.array_equal(arr1, arr3))  # false
print("arr1 & arr4 :", np.array_equal(arr1, arr4))  # false  

# 2. Using np.array_equiv()
print("\nUsing np.array_equiv():")
print("arr1 & arr2 -->:", np.array_equiv(arr1, arr2))  # true
print("arr1 & arr3 -->:", np.array_equiv(arr1, arr3))  # false
print("arr1 & arr4 -->:", np.array_equiv(arr1, arr4))  # false

# 3. Using np.allclose()
arr5 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
arr6 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0001]])
arr7 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0000001]])
print("\nUsing np.allclose():") 
print("arr5 & arr6 are approximately equal:", np.allclose(arr5, arr6))  # false
print("arr5 & arr7 are approximately equal:", np.allclose(arr5, arr7))  # true
print("arr6 & arr7 are approximately equal:", np.allclose(arr5, arr7))  # true
print("arr1 & arr3 are approximately equal:", np.allclose(arr1, arr3))  # false   

# 4. Using == and .all()
print("\nUsing == and .all():")
print("arr1 & arr2 are equal:", (arr1 == arr2).all())  # true
print("arr1 & arr3 are equal:", (arr1 == arr3).all())  # false

# ------------we cannot compare arrays of different shapes using this method
# print("arr1 & arr4 are equal:", (arr1 == arr4).all())  # false    

# Note: When comparing floating-point arrays, prefer using np.allclose() over direct equality checks to account for precision issues.
# Also, be cautious when using == and .all() for floating-point comparisons due to potential precision errors.

# we can also use comparison operators like <, >, <=, >= to compare two arrays element-wise
arr8 = np.array([[1, 2, 3], [4, 5, 6]])
arr9 = np.array([[1, 2, 0], [4, 0, 6]])
print("arr8 < arr9:\n", arr8 < arr9)
print("arr8 > arr9:\n", arr8 > arr9)
print("arr8 <= arr9:\n", arr8 <= arr9)
print("arr8 >= arr9:\n", arr8 >= arr9)
