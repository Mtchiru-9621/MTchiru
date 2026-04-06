import pandas as pd

# Sample company dataset
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Salary": [50000, None, 60000, None, 55000],
    "Joining_Date": ["2022-01-10", "2021-05-15", "2020-08-20", "2022-03-12", "2021-11-01"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)


# Test Case 1: Fill missing salary with mean
mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

print("\nAfter Filling Missing Salary:")
print(df)


# Convert Joining_Date to proper date format
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("\nAfter Date Conversion:")
print(df)


# Test Case 2: Remove duplicate entries
product_data = {
    "Product": ["Laptop", "Phone", "Tablet", "Phone", "Laptop"],
    "Price": [50000, 20000, 15000, 20000, 50000]
}

df_products = pd.DataFrame(product_data)

print("\nOriginal Product Data:")
print(df_products)

df_products = df_products.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(df_products)