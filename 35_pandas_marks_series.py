# Q1. write a python program to create a Series of marks of 5 students
# update a value in the series, use size function, use mean function
# and print only the marks greater than 50

import pandas as pd

marks = pd.Series([50,90, 45,85, 95], index=["rifa","Rita", "keya","Mita", "amit"])
print(marks)

# updating amit's marks
marks['amit']= 35

# size fun - gives no. of elements
print("size:",marks.size)

# mean fun - avg marks
print("mean:", marks.mean())

# only marks above 50
print(marks[marks> 50])


