import numpy as np

# Traffic flow matrix (vehicles per minute)
# Rows = incoming directions
# Columns = outgoing directions

traffic_flow = np.array([
    [30, 20],   # From North → East, West
    [15, 25]    # From South → East, West
])

print("Original Traffic Flow Matrix:")
print(traffic_flow)


# Transformation matrix representing signal optimization
# Shows how traffic is redistributed

transformation = np.array([
    [0.8, 0.2],
    [0.3, 0.7]
])

print("\nSignal Transformation Matrix:")
print(transformation)

new_flow = np.dot(transformation, traffic_flow)

print("\nNew Traffic Flow After Signal Optimization:")
print(new_flow)