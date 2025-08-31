import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('supermarket_sales.csv')
branch_sales = df.groupby('branch')['revenue'].sum()
print("Branch Wise sales : ")
print(branch_sales)
products_count=df['product_line'].value_counts()
print("products and its count")
print(products_count)
payment_methods = df['payment_method'].value_counts()
print("payment methods and its count")
print(payment_methods)
#matplotlib
#bar chart
x=branch_sales.index
y=branch_sales.values
plt.bar(x,y,color='skyblue')
plt.xlabel('Branch')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Branch')
plt.show()
#line chart
plt.plot(products_count.index,products_count.values)
plt.xlabel('Product Line')
plt.ylabel('Total count')
plt.title('Total Quantity by Product Line')
plt.show()
#pie chart
labels = payment_methods.index
sizes = payment_methods.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Payment Method Distribution')
plt.axis('equal')
plt.show()