
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area_calc(self):
        return self.length * self.width

    def perimeter_calc(self):
        return (self.length + self.width)*2


class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)


rect = Rectangle(3,7)
print(rect.perimeter_calc())
print(rect.area_calc())

sqr = Square(10)
print(sqr.area_calc())
print(sqr.perimeter_calc())
