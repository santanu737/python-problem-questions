class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)



class Bus(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def display(self):
        self.show()
        print("Seat no:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)


b1 = Bus("Bus", 3, "Mumbai", "Delhi")
b1.display()
