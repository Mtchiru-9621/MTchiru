import numpy as np

# sales data (units sold)
sales = np.array([[20, 15, 30],
                  [25, 18, 22],
                  [30, 20, 35]])

# total sales per product
product_sales = np.sum(sales, axis=0)

# best selling product index
best_product = np.argmax(product_sales)

print("Sales matrix:\n", sales)
print("Total sales per product:", product_sales)
print("Best selling product index:", best_product)