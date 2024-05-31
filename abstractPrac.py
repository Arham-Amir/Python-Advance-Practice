from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    

class Rectangle(Shape):
    def area(self):
        print("Arham Bhi G")

    def perimeter(self):
        print("G Bhi G")

s = Rectangle()

    
    