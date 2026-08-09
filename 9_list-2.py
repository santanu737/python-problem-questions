marks=[]

print("enter marks of 20 stu.:")

for i in range(1,21):
    mark=int(input("enter mark:"))
    marks.append(mark)

print("marks are ",marks)


avg_marks=sum(marks)/len(marks)
print("average marks :",avg_marks)


count=0
for mark in marks:
    if mark>avg_marks:
        count+=1
print("students those are scoring more than avg is:",count)


# frequent=marks[0]
# max_count =marks.count(frequent)

# for i  in  marks:
#     if marks.count(i)>max_count:
#         max_count=marks.count(i)
#         frequent=i

# print("marks that scored by max no of students :",frequent)