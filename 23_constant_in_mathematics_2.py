import math

class Triangle:
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

class EquilateralTriangle(Triangle):
    def cal_area(self):
        area = (math.sqrt(3) / 4) * (self.side1 ** 2)
        print("Area of equilateral triangle =", area)

    def find_angle(self):
        t1 = math.tan(math.radians(self.angle1))
        t2 = math.tan(math.radians(self.angle2))
        t3 = math.tan(math.radians(self.angle3))
        print("tan(angle1) =", t1)
        print("tan(angle2) =", t2)
        print("tan(angle3) =", t3)


class Scalene(Triangle):
    def cal_perimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print("Perimeter of scalene triangle =", perimeter)

    def cal_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        print("Area of scalene triangle =", int(area))


e1 = EquilateralTriangle(5, 5, 5, 60, 60, 60)
e1.cal_area()
e1.find_angle()

s1 = Scalene(7, 8, 9, 50, 60, 70)
s1.cal_perimeter()
s1.cal_area()
