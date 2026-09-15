"""
Question 3:
Write a program using tuple to store the name of 5 cities.
a) Print all items.
b) Print last two cities.
c) Print city that present twice in the tuple.
"""

# Storing 5 cities in a tuple (one city repeated intentionally to test part c)
cities = ("Kolkata", "Mumbai", "Delhi", "Chennai", "Kolkata")

# a) Print all items
print("All cities:")
for city in cities:
    print(city)

# b) Print last two cities
print("\nLast two cities:", cities[-2:])

# c) Print city that present twice in the tuple
print("\nCity(ies) appearing twice:")
seen = set()
duplicates = set()
for city in cities:
    if city in seen:
        duplicates.add(city)
    else:
        seen.add(city)

if duplicates:
    for city in duplicates:
        print(city)
else:
    print("No city appears twice.")
