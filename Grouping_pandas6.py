import pandas as pd

# Test Case 1: Sales data
sales_data = {
    "Region": ["North", "South", "North", "East", "South", "East"],
    "Revenue": [1000, 1500, 2000, 1200, 1800, 1600]
}

df_sales = pd.DataFrame(sales_data)

print("Sales Data:")
print(df_sales)

# Group by Region and calculate total revenue
region_total = df_sales.groupby("Region")["Revenue"].sum()

print("\nTotal Revenue by Region:")
print(region_total)


# Test Case 2: Student data
student_data = {
    "Department": ["CSE", "ECE", "CSE", "ME", "ECE", "ME"],
    "Marks": [80, 75, 90, 70, 85, 60]
}

df_students = pd.DataFrame(student_data)

print("\nStudent Data:")
print(df_students)

# Group by Department and find average marks
dept_avg = df_students.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(dept_avg)