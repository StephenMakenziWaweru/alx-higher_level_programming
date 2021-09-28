#!/usr/bin/python3
"""Magic class"""
import math


class MagicClass:
    """Code derived from Python bytecode"""
    def __init__(self, radius=0):
        """Init docstring"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Area docstring"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Circumference docstring"""
        return 2 * math.pi * self.__radius
