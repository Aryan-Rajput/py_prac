# How to convert a list and tuple into NumPy arrays?
import numpy as np
#   1. Using numpy.asarray()
#   2. Using numpy.array()

# list
lst1 = [3, 4, 5, 6]
print(type(lst1))
print(lst1)
print()

# conversion
lst_arr1 = np.asarray(lst1)
print(type(lst_arr1))
print(lst_arr1)
print()


# list
lst2 = [1, 2, 3]
print(type(lst2))
print(lst2)
print()

# conversion
lst_arr2 = np.array(lst2)
print(type(lst_arr2))
print(lst_arr2)
print()

# tuple
tpl1 = ([8, 4, 6], [1, 2, 3])
print(type(tpl1))
print(tpl1)
print()

# conversion
tpl_arr1 = np.asarray(tpl1)
print(type(tpl_arr1))
print(tpl_arr1)

# tuple
tpl2 = ([8, 4, 6], [1, 2, 3])
print(type(tpl2))
print(tpl2)
print()

# conversion
tp_arr2 = np.array(tpl2)
print(type(tp_arr2))
print(tp_arr2)

# so why should we use one over the other?
# Generally, numpy.array() is more versatile and is the preferred choice for creating NumPy arrays.
# However, numpy.asarray() can be useful when you want to ensure that the input is converted to an array without making unnecessary copies.