import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv(r'D:\Learning\Python\SIC-CP\Data\retail_store_inventory.csv')

# Filter to keep only the first 10 rows
df = df.head(10)

# Create a bar graph
plt.figure(figsize=(12, 6))
plt.bar(df['Units Sold'], df['Price'], color='r', width=5)
plt.xlabel('Units Sold', fontsize=15)
plt.ylabel('Price', fontsize=15)
plt.title('Graph Between Units Sold and Price', fontsize=16)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.grid(axis='y')
plt.show()
