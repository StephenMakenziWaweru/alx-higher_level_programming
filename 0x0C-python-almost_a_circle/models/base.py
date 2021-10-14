#!/usr/bin/python3
"""Base class module"""


class Base():
    """Base class"""
    ___nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.___nb_objects += 1
            self.id = Base.___nb_objects
