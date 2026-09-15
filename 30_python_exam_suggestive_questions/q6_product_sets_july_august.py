"""
Question 6:
Create two set of product names that are bought during July & August.
1) Find the product name that is bought only in July.
2) Find the product that are bought in both month.
3) Find the total product that are bought in July & August.
"""

# Two sets of product names bought in July and August
july_products = {"Pen", "Notebook", "Bag", "Bottle", "Charger"}
august_products = {"Bottle", "Charger", "Umbrella", "Shoes"}

# 1) Find the product name that is bought only in July
only_july = july_products - august_products
print("Products bought only in July:", only_july)

# 2) Find the product that are bought in both month
both_months = july_products & august_products
print("Products bought in both months:", both_months)

# 3) Find the total product that are bought in July & August
total_products = july_products | august_products
print("Total products bought in July & August:", total_products)
print("Total count of distinct products:", len(total_products))
