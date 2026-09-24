# Q2. write a python program to create a Series of 10 grocery products with price
# print products, find avg price, print products above avg, list products above 50 rs

import pandas as pd

products = pd.Series([40,60, 25,80, 55,30, 90,45, 70,35],
index=["rice","Oil", "salt","Ghee", "sugar","Tea", "milk","Atta", "butter","Soap"])

# printing products with price
print(products)

# avg price
avg_price= products.mean()
print("avg price:",avg_price)

# products above avg price
print(products[products> avg_price])

# product names with price more than 50 rs
print(products[products >50].index.tolist())