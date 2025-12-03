# Linear Algebra Basics
# Practice linear algebra operations

import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
v = np.array([1, 2])

print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Vector v:", v)

# Matrix multiplication
print("\n--- Matrix Multiplication ---")
print("A @ B (matrix multiply):\n", A @ B)
print("np.matmul(A, B):\n", np.matmul(A, B))
print("np.dot(A, B):\n", np.dot(A, B))

# Element-wise multiplication (NOT matrix multiplication)
print("\nA * B (element-wise):\n", A * B)

# Matrix-vector multiplication
print("\n--- Matrix-Vector Multiplication ---")
print("A @ v:", A @ v)
print("np.dot(A, v):", np.dot(A, v))

# Dot product of vectors
print("\n--- Dot Product ---")
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])
print("v1:", v1)
print("v2:", v2)
print("Dot product:", np.dot(v1, v2))

# Transpose
print("\n--- Transpose ---")
print("A transpose:\n", A.T)
print("np.transpose(A):\n", np.transpose(A))

# Determinant
print("\n--- Determinant ---")
print("Determinant of A:", np.linalg.det(A))

# Inverse
print("\n--- Inverse ---")
A_inv = np.linalg.inv(A)
print("Inverse of A:\n", A_inv)
print("A @ A_inv (should be identity):\n", np.round(A @ A_inv))

# Eigenvalues and eigenvectors
print("\n--- Eigenvalues and Eigenvectors ---")
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Solving linear equations (Ax = b)
print("\n--- Solving Linear Equations ---")
# 2x + 3y = 8
# 4x + 5y = 14
coefficients = np.array([[2, 3], [4, 5]])
constants = np.array([8, 14])
solution = np.linalg.solve(coefficients, constants)
print("Coefficients:\n", coefficients)
print("Constants:", constants)
print("Solution (x, y):", solution)

# Norm (magnitude of vector/matrix)
print("\n--- Norms ---")
print("L2 norm of v1:", np.linalg.norm(v1))
print("L1 norm of v1:", np.linalg.norm(v1, ord=1))
print("Frobenius norm of A:", np.linalg.norm(A))

# Rank
print("\n--- Rank ---")
print("Rank of A:", np.linalg.matrix_rank(A))

# Trace (sum of diagonal elements)
print("\n--- Trace ---")
print("Trace of A:", np.trace(A))

# SVD (Singular Value Decomposition)
print("\n--- SVD ---")
U, S, Vt = np.linalg.svd(A)
print("U:\n", U)
print("S:", S)
print("Vt:\n", Vt)
