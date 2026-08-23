students = {}

print("enter details for 5 students")
for i in range(5):
    roll_no=input("roll no: ")
    name = input("name: ")
    department=input("department: ")
    marks = int(input("marks: "))

    students[roll_no]={"name":name,"department": department,"marks":marks}

print("full dict")
print(students)

print("sorted by name")
sorted_keys=sorted(students,key = lambda x: students[x]["name"])
for k in sorted_keys:
    print(k,students[k])

print("max marks student")
max_roll = max(students,key= lambda x:students[x]["marks"])
print(max_roll,students[max_roll])

print("avg marks")
avg_marks=sum(list(map(lambda x:students[x]["marks"],students)))/len(students)
print(avg_marks)

print("above avg students")
above_avg=list(filter(lambda x: students[x]["marks"]>avg_marks,students))
for k in above_avg:
    print(k, students[k])
    
