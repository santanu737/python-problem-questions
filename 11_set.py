print("Enter 10 fruit names:")
fruits = set()
for i in range(10):
    name = input("Fruit " + str(i+1) + ": ")
    fruits.add(name)

print("Enter 5 summer fruit names:")
summer_fruits = set()
for i in range(5):
    name = input("Summer fruit " + str(i+1) + ": ")
    summer_fruits.add(name)

print("Enter 5 winter fruit names:")
winter_fruits = set()
for i in range(5):
    name = input("Winter fruit " + str(i+1) + ": ")
    winter_fruits.add(name)

print("Here are all the fruits in the 3 sets:")
print("Fruits:", fruits)
print("Summer Fruits:", summer_fruits)
print("Winter Fruits:", winter_fruits)

print("Fruits present in both summer and winter:")
print(summer_fruits.intersection(winter_fruits))

print("Fruits present only in summer, not in winter:")
print(summer_fruits.difference(winter_fruits))

print("Seasonal fruits that are not in the main fruits set:")
seasonal_union = summer_fruits.union(winter_fruits)
print(seasonal_union.difference(fruits))

if "orange" in fruits:
    print("orange is present in the fruits set")
else:
    print("orange is not present in the fruits set")

found_in = []
if "pineapple" in fruits:
    found_in.append("Fruits")
if "pineapple" in summer_fruits:
    found_in.append("Summer Fruits")
if "pineapple" in winter_fruits:
    found_in.append("Winter Fruits")

if found_in:
    print("pineapple found in:", ", ".join(found_in))
else:
    print("pineapple not found in any set")