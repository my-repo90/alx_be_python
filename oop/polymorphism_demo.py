from math import pi

#   base class (Shape)
class Shape:
    def __init__(self):
        pass
    def area(self):
        raise NotImplementedError
    # indicating that derived classes need to override this method
#   derived class (Rectangle)

class Rectangle(Shape):
    def __init__(self , length , width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self , radius):
        super().__init__()
        self.radius = radius

    def area(self):
        return pi * (self.radius) ** 2
     

