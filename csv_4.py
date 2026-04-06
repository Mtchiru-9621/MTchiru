import pandas as pd

data = {
    "District": ["Bangalore", "Mysore", "Mangalore", "Hubli", "Belgaum"],
    "Cases": [10000, 5000, 3000, 4000, 3500],
    "Deaths": [200, 100, 50, 80, 60],
    "Recovered": [9500, 4800, 2900, 3800, 3300]
}

df = pd.DataFrame(data)

df.to_csv("covid_data.csv", index=False)

print("CSV file created successfully!")

# Test Case 1: Load COVID dataset
covid_data = pd.read_csv("covid_data.csv")

print("First 5 Records:")
print(covid_data.head())


# Test Case 2: Load employee dataset
employee_data = pd.read_csv("employee.csv")

print("\nDataset Info:")
print(employee_data.info())

print("\nStatistical Summary:")
print(employee_data.describe())


# Access specific columns
print("\nAge and Salary:")
print(employee_data[['Age', 'Salary']])