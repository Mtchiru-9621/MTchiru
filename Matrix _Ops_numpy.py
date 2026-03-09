import numpy as np

# Define two 2×2 matrices
A = np.array([[2, 4],
              [6, 8]])

B = np.array([[1, 3],
              [5, 7]])

# Matrix multiplication
multiply = np.dot(A, B)

# Matrix transpose
transpose_A = A.T

# Element-wise division
division = A / B

print("Matrix A:\n", A)
print("Matrix B:\n", B)

print("\nMatrix Multiplication (A × B):\n", multiply)
print("\nTranspose of A:\n", transpose_A)
print("\nElement-wise Division (A / B):\n", division)