import math

class Shape:
    def area(self):
        raise NotImplementedError
        
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius **2
    
class Rectangle(Shape):
    def __init__(self,width, hieght):
        self.width = width
        self.hieght = hieght
    def area(self):
        return self.width * self.hieght
    
class Triangle(Shape):
    def __init__(self,height,breath):
        self.height = height
        self.breath = breath
    def area(self):
        return 0.5 * self.height*self.breath
    
circle =Circle(20)
rectangle = Rectangle(7,9)
triangle = Triangle(2,9)
print(f"Area of circle:{circle.area()}")
print(f"Area of rectangle:{rectangle.area()}")
print(f"Area of triangle: {triangle.area()}")