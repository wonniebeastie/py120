class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

rectangle1 = Rectangle(5, 6)
print(rectangle1.width)  # 5
print(rectangle1.height) # 6

rectangle1.width = 1000 
# AttributeError: property 'width' of 'Rectangle' object has no setter
