import math

class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def cal_area(self):
        area = math.pi * self.radius ** 2
        print("Area of circle =", int(area))


class Sphere(Shape):
    def cal_volume(self):
        volume = (4/3) * math.pi * self.radius ** 3
        print("Volume of sphere =", volume)


c1 = Circle(5)
c1.cal_area()

s1 = Sphere(4)
s1.cal_volume()