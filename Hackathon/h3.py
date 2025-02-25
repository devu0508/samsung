import pandas as pd
import matplotlib.pyplot as plt

# Load the retail dataset
df = pd.read_csv(r'D:\Learning\Python\SIC-CP\Data\retail_store_inventory.csv')

# Filter to keep only the first 8 rows
df = df.head(8)

# Assume the dataset contains 'Category' and 'Units Sold' columns
# Let's sum the units sold for each category
category_counts = df.groupby('Category')['Units Sold'].sum()

# Plot the bar chart
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='orange')

# Adding titles and labels
plt.title('Units Sold vs Category', fontsize=16)
plt.xlabel('Category', fontsize=14)
plt.ylabel('Units Sold', fontsize=14)

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()  # Adjust layout to avoid label clipping
plt.show()
