class Transport:
    def __init__(self, type):
        self.type = type

    def show(self):
        print("Type of Transport:", self.type)


class Boat(Transport):
    def __init__(self, type, capacity, source, destination):
        super().__init__(type)
        self.capacity = capacity
        self.source = source
        self.destination = destination

    def show(self):
        self.show                         
        print("Capacity:", self.capacity)
        print("Source:", self.source)
        print("Destination:", self.destination)


class Bus(Transport):
    def __init__(self, type, seat_no, source, destination):
        super().__init__(type)
        self.seat_no = seat_no
        self.source = source
        self.destination = destination

    def show(self):
        super().show()
        print("Seat no:", self.seat_no)
        print("Source:", self.source)
        print("Destination:", self.destination)

t1 = Boat(50, "Digha", "Kolkata", "Puri")
t1.show()

print()

t2 = Bus(10, "Kolkata", "Puri", "test")
t2.show()