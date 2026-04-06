import numpy as np

# Test Case 1: Multiply two 2x2 matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

multiplication = np.dot(A, B)

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nMultiplication Result:")
print(multiplication)


# Test Case 2: Transpose and dot product
C = np.array([[1, 2],
              [3, 4],
              [5, 6]])   # 3x2 matrix

D = np.array([[1, 0, 1],
              [0, 1, 0]])  # 2x3 matrix

transpose_C = C.T

dot_product = np.dot(transpose_C, D)

print("\nMatrix C:")
print(C)

print("\nTranspose of C:")
print(transpose_C)

print("\nMatrix D:")
print(D)

print("\nDot Product Result:")
print(dot_product)


# Extra: Matrix Inverse (for 2x2)
inverse_A = np.linalg.inv(A)

print("\nInverse of Matrix A:")
print(inverse_A)