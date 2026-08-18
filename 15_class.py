class Student:
    def __init__(self,name,roll_no,department,marks):
        self.name=name
        self.roll_no =roll_no
        self.department= department
        self.marks = marks

    def show(self):
        print("Name:" ,self.name)
        print("Roll No:",self.roll_no )
        print("Department:",self.department)
        print("Marks:" , self.marks)
        print("")


p1= Student("Amit","101","CSE" ,85)
p2 =Student("Riya","102","ECE",90)
p3=Student("Suresh" ,"103","ME",78)
p4 = Student("Priya","104" ,"CSE",88)
p5=Student("Kavya","105","EE" ,92)

p1.show()
p2.show()
p3.show()
p4.show()
p5.show()