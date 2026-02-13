class Circle:
    def __init__(self,radius):
        self.radius = radius

class Rectangle:
    def __init__(self,wigth,height):
        self.wight = wigth
        self.height = height


        
def calculate_area(Shape):
    if isinstance(Shape,Circle):
        return 3.13 * Shape.raduis **2
    elif isinstance(Shape,Rectangle):
        return Shape.width * Shape.height
    else:
        raise ValueError("Unknow shape")