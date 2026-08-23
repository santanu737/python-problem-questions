import math

class Triangle:
    def __init__(self, s1, s2, s3, a1, a2, a3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

class EquilateralTriangle(Triangle):
    def cal_area(self):
        area = (math.sqrt(3)/4) * (self.s1**2)
        return area
    
    def find_angle(self):
        t1 = math.tan(math.radians(self.a1))
        t2 = math.tan(math.radians(self.a2))
        t3 = math.tan(math.radians(self.a3))
        return t1, t2, t3

class Scalene(Triangle):
    def cal_perimeter(self):
        peri = self.s1 + self.s2 + self.s3
        return peri
    
    def cal_area(self):
        s = self.cal_perimeter()/2
        area = math.sqrt(s*(s-self.s1)*(s-self.s2)*(s-self.s3))
        return int(area)

et = EquilateralTriangle(6,6,6,60,60,60)
print("Area:", et.cal_area())
print("Tangents:", et.find_angle())

sca = Scalene(3,4,5,40,60,80)
print("Perimeter:", sca.cal_perimeter())
print("Area:", sca.cal_area())