#!/usr/bin/python3
"""Student class Module"""


class Student():
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initializes Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets dict with filter"""
        if type(attrs) is list and all([type(attr) == str for attr in attrs]):
            return {key: val for key, val in self.__dict__.items() if key in
                    attrs}
        else:
            return self.__dict__.copy()
