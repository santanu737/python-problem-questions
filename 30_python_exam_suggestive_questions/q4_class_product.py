"""
Question 4:
Create class Product with prod-id, full-name, quantity.
1) Initialise with constructor.
2) show() method to display the records.
3) Create 2 objects P1, P2 and show the detail.
"""


class Product:
    # 1) Initialise with constructor
    def __init__(self, prod_id, full_name, quantity):
        self.prod_id = prod_id
        self.full_name = full_name
        self.quantity = quantity

    # 2) show() method to display the records
    def show(self):
        print(f"Product ID : {self.prod_id}")
        print(f"Full Name  : {self.full_name}")
        print(f"Quantity   : {self.quantity}")
        print("-" * 30)


# 3) Create 2 objects P1, P2 and show the detail
P1 = Product(101, "Wireless Mouse", 25)
P2 = Product(102, "Mechanical Keyboard", 15)

print("Product 1 Details:")
P1.show()

print("Product 2 Details:")
P2.show()
