import numpy as np

# Create 3x3 array (3 subjects × 3 students)
marks = np.array([[10, 20, 30],
                  [15, 25, 35],
                  [20, 30, 40]])

print("Original 3x3 Array:")
print(marks)

# Test Case 1: Reshape to (1, 9)
reshaped_marks = marks.reshape(1, 9)

print("\nReshaped Array (1x9):")
print(reshaped_marks)

# Test Case 2: Element-wise multiplication
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 * arr2

print("\nElement-wise Multiplication:")
print(result)

# Bonus: Double marks using broadcasting
bonus_marks = marks * 2

print("\nBonus Marks (Doubled):")
print(bonus_marks)

# Total marks per student (column-wise sum)
total_marks = np.sum(marks, axis=0)

print("\nTotal Marks of Each Student:")
print(total_marks)