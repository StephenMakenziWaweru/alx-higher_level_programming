#!/usr/bin/python3
"""Base class module"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string rep of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
