import numpy as np

# Marks of 3 students in 3 subjects
marks = np.array([[18, 20, 22],
                  [15, 17, 19],
                  [20, 16, 18]])

# Reshape matrix to single row (1 × 9)
reshaped = marks.reshape(1, 9)

# Compute total marks of each student
total_marks = np.sum(marks, axis=1)

# Example arrays for element-wise multiplication
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])

element_product = a * b

print("Original 3x3 marks matrix:\n", marks)
print("\nReshaped matrix (1x9):\n", reshaped)
print("\nTotal marks of each student:", total_marks)
print("\nElement-wise multiplication:", element_product)