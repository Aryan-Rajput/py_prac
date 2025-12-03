# Mathematical Operations
# Practice mathematical functions and operations

import numpy as np

# Create sample arrays
arr = np.array([1, 2, 3, 4, 5])
arr2 = np.array([10, 20, 30, 40, 50])

print("Array 1:", arr)
print("Array 2:", arr2)

# Element-wise arithmetic operations
print("\n--- Element-wise Operations ---")
print("Addition:", arr + arr2)
print("Subtraction:", arr2 - arr)
print("Multiplication:", arr * arr2)
print("Division:", arr2 / arr)
print("Power:", arr ** 2)
print("Modulo:", arr2 % arr)

# Universal functions (ufuncs)
print("\n--- Universal Functions ---")
print("Square root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))
print("Natural log:", np.log(arr))
print("Log base 10:", np.log10(arr2))
print("Absolute:", np.abs(np.array([-1, -2, 3, -4, 5])))

# Trigonometric functions
print("\n--- Trigonometric Functions ---")
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
print("Angles (radians):", angles)
print("Sine:", np.sin(angles))
print("Cosine:", np.cos(angles))
print("Tangent:", np.tan(angles[:4]))  # Avoid pi/2 for tan

# Rounding functions
print("\n--- Rounding Functions ---")
decimals = np.array([1.2, 2.5, 3.7, 4.1, 5.9])
print("Original:", decimals)
print("Round:", np.round(decimals))
print("Floor:", np.floor(decimals))
print("Ceil:", np.ceil(decimals))
print("Truncate:", np.trunc(decimals))

# Aggregation functions
print("\n--- Aggregation Functions ---")
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Data:\n", data)
print("Sum (all):", np.sum(data))
print("Sum (axis=0, columns):", np.sum(data, axis=0))
print("Sum (axis=1, rows):", np.sum(data, axis=1))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Std deviation:", np.std(data))
print("Variance:", np.var(data))
print("Min:", np.min(data))
print("Max:", np.max(data))
print("Argmin (index of min):", np.argmin(data))
print("Argmax (index of max):", np.argmax(data))

# Cumulative functions
print("\n--- Cumulative Functions ---")
print("Cumulative sum:", np.cumsum(arr))
print("Cumulative product:", np.cumprod(arr))

# Comparison operations
print("\n--- Comparison Operations ---")
print("arr > 3:", arr > 3)
print("arr == 3:", arr == 3)
print("Any > 3:", np.any(arr > 3))
print("All > 0:", np.all(arr > 0))

# Statistical functions
print("\n--- Statistical Functions ---")
print("Percentile 50:", np.percentile(data, 50))
print("Percentile 25:", np.percentile(data, 25))
print("Percentile 75:", np.percentile(data, 75))
print("Correlation coefficient:\n", np.corrcoef(arr, arr2))
