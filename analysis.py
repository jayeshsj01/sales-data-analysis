# Import data


import pandas as pd
import matplotlib.pyplot as plt

# Instantly make graphs
plt.style.use('ggplot')

# Load dataset
df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# Show first 5 rows
print(df.head())

# Show columns
print(df.columns)

# Basic info
print(df.info())

# Convert Date format

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

# Monthly Sales analysis


monthly_sales = df.groupby('MONTH_ID')['SALES'].sum()

# Month names
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

plt.figure(figsize=(10,5))

plt.plot(months, monthly_sales.values, marker='o')

for i, value in enumerate(monthly_sales.values):
    plt.text(i, value, f'{int(value)}', ha='center')

# Highlight highest point
max_value = monthly_sales.max()
max_month = monthly_sales.idxmax()

plt.scatter(months[max_month-1], max_value)

# Add value labels
for i, value in enumerate(monthly_sales.values):
    plt.text(i, value, f'{int(value)}', ha='center')

# Labels & styling
plt.title(" Monthly Sales Analysis", fontsize=14)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)

plt.savefig('Graphs/monthly_sales.png')
plt.show()

# Top Selling Products (by PRODUCTLINE)

top_products = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False)

top_products.plot(kind='bar')
plt.title("Sales by Product Line")
plt.xlabel("Product Line")
plt.ylabel("Revenue")

plt.savefig('Graphs/product_line.png')
plt.show()

# Best Countries (VERY IMPORTANT INSIGHT)

country_sales = df.groupby('COUNTRY')['SALES'].sum().sort_values(ascending=False)

country_sales.head(10).plot(kind='bar')
plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Revenue")

plt.savefig('Graphs/countries.png')
plt.show()

#  Best Deal Size Analysis

deal_sales = df.groupby('DEALSIZE')['SALES'].sum()

deal_sales.plot(kind='bar')
plt.title("Sales by Deal Size")
plt.xlabel("Deal Size")
plt.ylabel("Revenue")

plt.savefig('Graphs/deal_size.png')
plt.show()



































