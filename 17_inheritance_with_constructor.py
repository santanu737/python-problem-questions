class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name



class uqstudent(Student):
    def __init__(self, roll, name, idp):
        super().__init__(roll, name)
        self.idp = idp

    def show(self):
        print(self.roll)
        print(self.name)
        print(self.idp)


obj = uqstudent(101, "Ajay", "IQT")
obj.show()
