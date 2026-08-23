print("Enter 20 employee names:")
employee_list = []
for i in range(20):
    name = input("Employee " + str(i+1) + ": ")
    employee_list.append(name)

employees = tuple(employee_list)

print("Here is the tuple:")
print(employees)

print("Name and frequency of each name:")
counted_names = []
for name in employees:
    if name not in counted_names:
        counted_names.append(name)
        count = employees.count(name)
        print(name, "appears", count, "times")

print("Distinct names in the tuple:")
distinct_names = tuple(counted_names)
print(distinct_names)

max_freq_name = employees[0]
max_count = employees.count(employees[0])
for name in distinct_names:
    current_count = employees.count(name)
    if current_count > max_count:
        max_count = current_count
        max_freq_name = name

print("Employee with maximum frequency is", max_freq_name, "with", max_count, "occurrences")

sorted_list = list(employees)
sorted_list.sort()
sorted_tuple = tuple(sorted_list)
print("Tuple sorted in alphabetical order:")

print(sorted_tuple)

search_name = input("Enter an employee name to search: ")
if search_name in employees:
    print(search_name, "exists in the tuple")
else:
    print(search_name, "does not exist in the tuple")
