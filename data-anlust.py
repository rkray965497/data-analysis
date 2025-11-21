# 1. Import the tool (Pandas)
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load your file into a table (DataFrame)
# IMPORTANT: Replace 'your_sales_data.csv' with your file name
df = pd.read_csv('your_sales_data.csv')
print("Data loaded successfully! Here's a peek:")
print(df.head())
# Group the data by 'Product' and sum the 'Sales_Amount'
sales_by_product = df.groupby('Product')['Sales_Amount'].sum()

print("\nTotal Sales by Each Product:")
print(sales_by_product)
# Group the data by 'Region' and sum the 'Sales_Amount'
sales_by_region = df.groupby('Region')['Sales_Amount'].sum()

print("\nTotal Sales by Each Region:")
print(sales_by_region)
# Plot the results from sales_by_product
plt.figure(figsize=(8, 5))
sales_by_product.plot(kind='bar', color='green')

# Make the chart clear
plt.title('Total Sales by Product')
plt.xlabel('Product Name')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45) # Tilt labels so they don't overlap
plt.show()


[Image of a simple bar chart showing sales amounts for different products]
