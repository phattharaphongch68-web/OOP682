#LSP (Liskov Subtitution Principle)
#กล่าวว่า วัตถุของซับคลาสจะสามารถแทนที่วัตถุที่ซูเปอร์ได้โดยที่ไม่ทำให้โปรแกรมทำงานผิดพลาด
#Good Idea for lsp adherence
from abc import abstractmethod

class Shape:
    @abstractmethod
    def resize(self, new_width, new_height):
        pass

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def resize(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

    def area(self):
        return self.width * self.height
    
class Square(Shape):
    def __init__(self, side):
        self.side = side
    def resize(self, new_width, new_height):
        self.side = new_width

    def area(self):
        return self.side * self.side


def resize(shape, new_width, new_height):
    shape.resize(new_width, new_height)
    return shape.area()


rect = Rectangle(2, 3)
print("Rectangle area:", resize(rect, 4, 5))  # Output: Rectangle area: 20
square = Square(4)
print("Square area:", resize(square, 5, 5))  # Output: Square area: 25
