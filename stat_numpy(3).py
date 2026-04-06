import numpy as np

# Test Case 1: Weekly rainfall data (in mm)
rainfall = np.array([10, 20, 15, 25, 30, 18, 22])

std_dev = np.std(rainfall)

print("Rainfall Data:", rainfall)
print("Standard Deviation of Rainfall:", std_dev)


# Test Case 2: Student exam scores
scores = np.array([60, 70, 80, 90, 75, 85, 95])

mean_score = np.mean(scores)
median_score = np.median(scores)

print("\nStudent Scores:", scores)
print("Mean Score:", mean_score)
print("Median Score:", median_score)


# Extra: Variance
variance = np.var(scores)

print("Variance of Scores:", variance)