import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the retail dataset
df = pd.read_csv(r'D:\Learning\Python\SIC-CP\Data\retail_store_inventory.csv')

# Filter to keep only the first 8 rows
df = df.head(8)

# Assume the dataset contains 'Product ID', 'Units Ordered', and 'Units Sold' columns
# Create a bar width and position for each bar
bar_width = 0.35
index = np.arange(len(df['Product ID']))

# Plot the bar chart
plt.figure(figsize=(12, 6))
plt.bar(index, df['Units Ordered'], bar_width, label='Units Ordered', color='blue')
plt.bar(index + bar_width, df['Units Sold'], bar_width, label='Units Sold', color='green')

# Adding titles and labels
plt.title('Comparison of Units Ordered and Units Sold for Each Product ID', fontsize=16)
plt.xlabel('Product ID', fontsize=14)
plt.ylabel('Units', fontsize=14)
plt.xticks(index + bar_width / 2, df['Product ID'], rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.tight_layout()  # Adjust layout to avoid label clipping
plt.grid(axis='y')

plt.show()
