#!/usr/bin/python3
"""Module to see if objects are same"""


def is_same_class(obj, a_class):
    """Returns:
    True: if the object is exactly an instance of the specified class
    False: otherwise"""
    return type(obj) == a_class
