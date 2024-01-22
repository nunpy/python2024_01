# abstract
# 추상 클래스

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_round(self):
        pass

class Circle(Shape):
    def __init__(self,r):
        self.radius = r

    def get_area(self):
        return 3.14 * self.radius ** 2

    def get_round(self):
        return 3.14 * self.radius * 2



class Square(Shape):
    def __init__(self, l):
        self.length = l

    def get_area(self):
        return self.length ** 2

    def get_round(self):
        return self.length * 4




class Triangle(Shape):
    def __init__(self, l, h):
        self.length = l
        self.height = h

    def get_area(self):
        return self.length * self.height * 0.5

    def get_round(self):
        return self.length * 3

a = Square(4)
print(a.get_area())

b = Triangle(3,4)
print(b.get_area())




