#!/usr/bin/python3
"""Square module - assigns size of the square and
checks for type and value"""


class Square:
    """defines a square with private instance attribute size"""
    def __init__(self, size=0):
        """assigns size of the square and checks for type and value"""
        
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    def area(self):
        """public instance method returns current sqr area"""
        return self.__size ** 2
