import math

from shape import Circle 
class Shape:
  def area(self):
    raise NotImplementedError("subclasses")
  
class circle(Shape):
  def _init_(self,radius):
    self.radius = radius
  def area(self):
    return math.pi * self.radius**2
class Rectangle(Shape):
  def __init__(self,width,height):
    self.width = width
    self.height = height
    
  def area(self):
    return self.height * self.width
  
circle = Circle(20)
rectangle = Rectangle(5,8)

print(circle.area)
print(rectangle.area)
    