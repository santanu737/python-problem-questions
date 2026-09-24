
# Q3. write a python program to create a dataframe using dictionary
# for five employees - employee-ID, employee-name, department, salary
# print first two employees, last two employees, employee with max salary

import pandas as pd

data = {
"emp-ID": [1,2, 3,4, 5],
"emp-name": ["Amit","Santanu", "Ajoy","Anil", "Barnun"],
"dept":["CSE", "CSE","Cyber", "Physics","Math"],
"salary": [10000,20000, 30000,40000, 50000]
}
df= pd.DataFrame(data)
print(df)

# first two employees
print(df.head(2))

# last two employees
print(df.tail(2))

# employee with max salary
print(df[df['salary']== df['salary'].max()])