#!/usr/bin/python3
"""Module with from_json_string method"""
import json


def from_json_string(my_str):
    """Method that returns an Object from JSON string"""
    return json.loads(my_str)
