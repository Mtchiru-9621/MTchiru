import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50])

# Slice elements (index 1 to 3)
slice_arr = arr[1:4]

# Broadcasting operation (add 5 to every element)
broadcast = arr + 5

# Compare with Python list multiplication
py_list = [10, 20, 30, 40, 50]
list_result = [x * 2 for x in py_list]

# NumPy vectorized multiplication
numpy_result = arr * 2

print("Original array:", arr)
print("Sliced array:", slice_arr)
print("Broadcast result:", broadcast)
print("Python list multiplication:", list_result)
print("NumPy multiplication:", numpy_result)