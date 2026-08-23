names=[]
marks=[]
print("enter names of 10 stu.:")

for i in range(1,11):
    name=input("enter name:")
    names.append(name)

print("names are",names)


print("enter marks of 10 stu.:")

for i in range(1,11):
    mark=int(input("enter mark:"))
    marks.append(mark)

print("marks are ",marks)




max_marks=max(marks)
min_marks=min(marks)

max_marks_index=marks.index(max_marks)
min_marks_index=marks.index(min_marks)



high=names[max_marks_index]
low=names[min_marks_index]

print("maximum marks scored by:",high)
print("minimum marks scored by ",low)
