import pandas as pd
import matplotlib.pyplot as plt # Needed for the plot() function
print(df.head())
print(df.info())
# Group the DataFrame by 'Product' and sum the 'Sales' column
product_sales = df.groupby('Product')['Sales'].sum()

print("\n### Total Sales by Product ###")
print(product_sales.sort_values(ascending=False))
# Plotting the results as a Bar Chart for easy comparison
product_sales.sort_values(ascending=False).plot(
    kind='bar',
    title='Total Sales by Product',
    ylabel='Total Sales Amount',
    xlabel='Product'
)

# Display the chart
plt.tight_layout() # Adjusts the plot to fit all labels
plt.show()
