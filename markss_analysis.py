import numpy as np

A = np.array([[5, 8, 2],
              [7, 1, 6],
              [9, 3, 4]])

# row sum
row_sum = np.sum(A, axis=1)

# column sum
col_sum = np.sum(A, axis=0)

# maximum and minimum values
max_val = np.max(A)
min_val = np.min(A)

print("Matrix:\n", A)
print("Row sum:", row_sum)
print("Column sum:", col_sum)
print("Maximum value:", max_val)
print("Minimum value:", min_val)