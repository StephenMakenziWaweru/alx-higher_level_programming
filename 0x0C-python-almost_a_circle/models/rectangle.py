#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """rectangle's x pos"""
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """rectangle's y pos"""
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def width(self):
        """rectangle's width"""
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @property
    def height(self):
        """rectangle's height"""
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
