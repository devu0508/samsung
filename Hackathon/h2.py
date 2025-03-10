import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'D:\Learning\Python\SIC-CP\Data\scanner_data.csv\scanner_data.csv')

df = df.head(8)


sku_stock_data = df.groupby('SKU')['Sales_Amount'].sum()

# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sku_stock_data, labels=sku_stock_data.index, autopct='%1.1f%%', startangle=140)
plt.title('SKU vs Sales amount')
plt.axis('equal')  
plt.show()