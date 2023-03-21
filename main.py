from abc import ABC, abstractmethod
from math import sqrt
class Polygon(ABC):
    @abstractmethod
    def sides(self):
        pass
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
    def figure(self):
        return "it is a 2-diamensional plane figure"

class Rectangle(Polygon):
    def sides(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def extramethod(self):
        return "Rectangle has 4 sides"
class Triangle(Polygon):
    def sides(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = self.perimeter()
        return sqrt(s*(s-self.a)*(s-s*self.b)*(s-self.c))
    def perimeter(self):
        return (self.a+self.b+self.c)/2
    def extramethod(self):
        return "Triangle has 3 sides"
class Square(Polygon):
    def sides(self, side):
        self.side = side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*(self.side)
    def extramethod(self):
        return "Square has 4 sides"

rect = Rectangle()
rect.sides(10,20)
trai = Triangle()
trai.sides(10,20,30)
squa = Square()
squa.sides(10)

for obj in [rect, trai,squa]:
    print(obj.area())
    print(obj.perimeter())
    print(obj.extramethod())
