# sales_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("supermarket_sales.csv")

print("Dataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())

# Total Sales
print("\nTotal Revenue:")
print(df['Total'].sum())

# Branch-wise Sales
branch_sales = df.groupby('Branch')['Total'].sum()

plt.figure(figsize=(6,4))
branch_sales.plot(kind='bar')
plt.title("Branch Wise Revenue")
plt.ylabel("Revenue")
plt.savefig("branch_sales.png")
plt.show()

# Product Line Analysis
plt.figure(figsize=(10,5))
df.groupby('Product line')['Total'].sum().sort_values().plot(kind='barh')
plt.title("Revenue by Product Line")
plt.savefig("product_line_sales.png")
plt.show()

# Payment Methods
plt.figure(figsize=(6,4))
sns.countplot(x='Payment', data=df)
plt.title("Payment Methods")
plt.savefig("payment_methods.png")
plt.show()

# Customer Ratings
plt.figure(figsize=(6,4))
sns.histplot(df['Rating'], bins=10)
plt.title("Customer Ratings")
plt.savefig("ratings_distribution.png")
plt.show()

print("\nAnalysis Completed Successfully")
