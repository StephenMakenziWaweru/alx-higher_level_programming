#!/usr/bin/python3
"""Module with to_json_string method"""
import json


def to_json_string(my_obj):
    """Method that returns the JSON representation of an object"""
    return json.dumps(my_obj)
