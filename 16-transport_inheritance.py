class Transport:
    def get_val(self, type):
        self.type = type

    def show(self):
        print("Transport type:", self.type)



class Bus(Transport):
    def input_val(self, seat_no, source, destination):
        self.seatno = seat_no
        self.source = source
        self.destination = destination

    def display(self):
        print("Seat no:", self.seatno)
        print("Source:", self.source)
        print("Destination:", self.destination)


B1 = Bus()
B1.get_val("Bus")         
B1.input_val(12, "Howrah", "Kolkata")

B1.show()                 
B1.display()               
