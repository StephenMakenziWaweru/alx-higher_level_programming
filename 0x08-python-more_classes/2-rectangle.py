#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """ Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

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
        """returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """return the perimeter of the rectangle"""
        if self._height == 0 or self._height == 0:
            return 0
        return 2 * (self._height + self._width)
