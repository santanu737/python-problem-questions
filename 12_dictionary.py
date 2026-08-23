employee = {}

print("Enter records for 5 employees:")
for i in range(1, 6):
    emp_id = "E" + str(i)
    print("Details for", emp_id)
    name = input("Employee Name: ")
    designation = input("Designation: ")
    department = input("Department: ")
    salary = float(input("Salary: "))

    employee[emp_id] = {
        "emp_name": name,
        "designation": designation,
        "department": department,
        "salary": salary
    }

print("Here is the full employee dictionary:")
print(employee)

print("Record of employee E1:")
print(employee["E1"])

print("Department of employee E4:")
print(employee["E4"]["department"])

max_salary_id = "E1"
max_salary = employee["E1"]["salary"]
for emp_id in employee:
    if employee[emp_id]["salary"] > max_salary:
        max_salary = employee[emp_id]["salary"]
        max_salary_id = emp_id

print("Employee with maximum salary is", max_salary_id)
print(employee[max_salary_id])

print("Now let us insert a new employee record:")
new_id = input("Enter new Employee ID: ")
new_name = input("Employee Name: ")
new_designation = input("Designation: ")
new_department = input("Department: ")
new_salary = float(input("Salary: "))

employee[new_id] = {
    "emp_name": new_name,
    "designation": new_designation,
    "department": new_department,
    "salary": new_salary
}

print("Updated employee dictionary:")
print(employee)
