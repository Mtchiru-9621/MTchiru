import numpy as np

# Traffic flow matrix (vehicles per minute)
traffic_flow = np.array([
    [30, 20],   # North → East, West
    [15, 25]    # South → East, West
])

print("Original Traffic Flow:\n", traffic_flow)

# Step 1: Adaptive signal control (based on incoming traffic)
row_total = np.sum(traffic_flow, axis=1)
adaptive = np.array([
    [row_total[0]/np.sum(row_total), 1 - row_total[0]/np.sum(row_total)],
    [row_total[1]/np.sum(row_total), 1 - row_total[1]/np.sum(row_total)]
])

# Step 2: Congestion penalty (reduce flow to crowded roads)
col_total = np.sum(traffic_flow, axis=0)
penalty = 1 / (col_total + 1)
penalty = penalty / np.sum(penalty)
penalty_matrix = np.tile(penalty, (2,1))

# Step 3: Combine both techniques
transformation = adaptive * penalty_matrix

# Normalize rows (important)
transformation = transformation / np.sum(transformation, axis=1, keepdims=True)

print("\nFinal Transformation Matrix:\n", transformation)

# Step 4: Apply transformation
optimized_flow = np.dot(traffic_flow, transformation)

print("\nOptimized Traffic Flow:\n", optimized_flow)

# Step 5: Simulation over time
flow = optimized_flow.copy()
for i in range(2):
    flow = np.dot(flow, transformation)
    print(f"\nAfter step {i+1}:\n", flow)

# Step 6: Traffic summary
print("\nIncoming:", np.sum(traffic_flow, axis=1))
print("Outgoing:", np.sum(optimized_flow, axis=0))
print("Total Before:", np.sum(traffic_flow))
print("Total After:", np.sum(optimized_flow))