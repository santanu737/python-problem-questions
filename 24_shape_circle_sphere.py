import math

class Shape:
    def __init__(self, r):
        self.r = r

class Circle(Shape):
    def cal_area(self):
        area = math.pi * self.r * self.r
        return area

class Sphere(Shape):
    def cal_volume(self):
        vol = (4/3) * math.pi * self.r**3        #use pow method of math class
        return vol

c1 = Circle(5)
print("Area of circle:", c1.cal_area())

s1 = Sphere(5)
print("Volume of sphere:", s1.cal_volume())