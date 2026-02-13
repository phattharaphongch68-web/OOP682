#Open-closed Principle (OCP) status that solfware entities
#(classes, modules,functions,etc. )
#should be open for extension but closed for modifile

from abc import abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,wigth,height):
        self.wight = wigth
        self.height = height

    def area(self):
        return self.wight * self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.raduis = radius

    def area(self):
        return 3.14 * self.raduis ** 2

