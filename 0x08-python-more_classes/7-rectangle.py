#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ Rectangle class"""
    number_of_instances = 0
    """int: number of instances"""

    print_symbol = "#"
    """any type: symbol for printing rectangle"""

    def __init__(self, width=0, height=0):
        """Initialiazes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return (self._width)

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        return (self._height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._height == 0 or self._height == 0:
            return 0
        return 2 * (self._height + self._width)

    def __str__(self):
        """Returns a string rep of the rectangle"""
        if self._height == 0 or self._height == 0:
            return ""
        return ((str(self.print_symbol) * self._width + "\n") *
                self._height)[:-1]

    def __repr__(self):
        '''Returns formal string representation...'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        """Called when deleting an instance of rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
