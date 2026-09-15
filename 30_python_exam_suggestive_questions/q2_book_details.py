"""
Question 2:
Write a Python program to store book detail (title, author, price, publisher)
in a variable. Now perform:
1) Print type of variable.
2) Add 'edition' in the variable.
3) Show the records of 2 books.
4) Show the record of book with lowest price.
"""

# Storing book details as a tuple, then converting to a list to allow modification
book1 = ("The Alchemist", "Paulo Coelho", 399, "HarperCollins")
book2 = ("Atomic Habits", "James Clear", 499, "Random House")

# 1) Print type of variable
print("Type of book1:", type(book1))

# 2) Add 'edition' in the variable (tuples are immutable, so convert to list first)
book1 = list(book1)
book1.append("1st Edition")
book1 = tuple(book1)

book2 = list(book2)
book2.append("2nd Edition")
book2 = tuple(book2)

print("\nAfter adding edition:")
print("Book 1:", book1)
print("Book 2:", book2)

# 3) Show the records of 2 books
print("\nRecords of 2 books:")
print("Book 1:", book1)
print("Book 2:", book2)

# 4) Show the record of book with lowest price
# price is at index 2 in each tuple
if book1[2] < book2[2]:
    lowest_price_book = book1
else:
    lowest_price_book = book2

print("\nBook with lowest price:", lowest_price_book)
