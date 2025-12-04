# array functions 
import numpy as np

# a1 = np.random.random((3, 4))
a1 = np.random.rand(3, 4)
a1 = a1 * 100
a1 = a1.astype(int)
# a2 = np.random(3, 4)

print(a1)
# print(a2)

# max/min/sum/prod
# print("Max:", a1.max())
# print("Min:", a1.min())
# print("Sum:", a1.sum())
# print("Product:", a1.prod())

# now along axis

# print("Max along axis 0:", a1.max(axis=0))
# print("Min along axis 1:", a1.min(axis=1))
# print("Sum along axis 0:", a1.sum(axis=0))

# in product along axis 1 it shows the product of each row 
# for product along axis 0 it shows the product of each column
# print("Product along axis 1:", a1.prod(axis=1))
# print("Product along axis 0:", a1.prod(axis=0))

# for a 3d array
a2 = np.random.rand(2, 3, 4)
a2 = a2 * 100
a2 = a2.astype(int)
print(a2)

# prodyct along axis 0
# print("Product along axis 0:", a2.prod(axis=0))
# prodyct along axis 1
# print("Product along axis 1:", a2.prod(axis=1))
# prodyct along axis 2
# print("Product along axis 2:", a2.prod(axis=2))

# for multi axis product
# print("Product along axis (0, 1):", a2.prod(axis=(0, 1)))
# print("Product along axis (1, 2):", a2.prod(axis=(1, 2)))
# print("Product along axis (0, 2):", a2.prod(axis=(0, 2)))

# mean/median/std/var
# for mode it does not have any inbuilt function in numpy but we can use scipy for that   
# print("Mean:", a1.mean())
# print("Median:", np.median(a1))
# print("Standard Deviation:", a1.std())
# print("Variance:", a1.var())

# now along axis
# print("Mean along axis 0:", a1.mean(axis=0))
# print("Median along axis 1:", np.median(a1, axis=1))
# etc ....

# trignometric functions
a3 = np.array([0, 30, 45, 60, 90])
print("a3:", a3)
# numpy trignometric functions take input in radians
# radian = degree * (pi/180)
# why do we convert to radian ? because unit circle is based on radian measure
a3_rad = np.deg2rad(a3)

# print("Sine:", np.sin(a3_rad))
# print("Cosine:", np.cos(a3_rad))
# print("Tangent:", np.tan(a3_rad))

# dot product
# for a dot product to work the number of columns in first array must be equal to number of rows in second array
a4 = np.array([[1, 2], [3, 4]])
a5 = np.array([[5, 6], [7, 8]])
print("a4:\n", a4)
print("a5:\n", a5)
dot_product = np.dot(a4, a5)
print("Dot Product :\n", dot_product)
# visualization of dot product
# first row of a4 and first column of a5
# (1*5) + (2*7) = 5 + 14 = 19
# first row of a4 and second column of a5
# (1*6) + (2*8) = 6 + 16 = 22
# second row of a4 and first column of a5
# (3*5) + (4*7) = 15 + 28 = 43
# and so on ...

