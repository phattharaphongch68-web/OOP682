class Rectangle:
    def __init__(self,widht,height):
        self.widht = widht
        self.height = height

    def set_widht(self,width):
        self.widht = width

    def set_height(self,height):
        self.height = height

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)
    def set_widht(self,width):
        self.widht = width
        self.height = width

    def set_height(self,height):
        self.height = height
        self.widht = height

def resize_rectangle(rectangle,new_widht,new_height):
    rectangle.set_widht(new_widht)
    rectangle.set_height(new_height)
    return rectangle.widht * rectangle.height


rect = Rectangle(2,3)
print("Rectangle area:",resize_rectangle(rect,4,5)) 
square = Square(4)
print("Square area:",resize_rectangle(square,5,5)) 