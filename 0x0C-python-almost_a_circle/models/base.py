#!/usr/bin/python3
"""Base class module"""


class Base():
    """Base class"""
    __bn_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = id
