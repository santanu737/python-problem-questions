class Book:
    def __init__(self, title):
        self.title = title

    def show(self):
        print("Title of book:", self.title)


class Edition(Book):
    def __init__(self, t, i):
        super().__init__(t)
        self.edi = i

    def show(self):                        
        super().show()                    
        print("Edition:", self.edi)


obj1 = Edition("Python", "4th")
obj1.show()

print()

obj2 = Book("Django")
obj2.show()