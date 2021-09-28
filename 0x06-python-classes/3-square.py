#!/usr/bin/python3
class Square:
    """defines a square with private instance attribute size"""
    def __init__(self, size=0):
        """assigns size of the square and checks for type and value"""
        try:
            self.__size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")

    def area(self):
        """public instance method returns current sqr area"""
        return self.__size ** 2
