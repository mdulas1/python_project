from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
    
     class turtle(shape):
        def _init_(self,radius):
            self.radius = radius
        def area(self):
            return 3.14*self.radius**2  