#!/usr/bin/python3
"""Module with save_to_json_file method"""
import json


def save_to_json_file(my_obj, filename):
    """Method that writes an Object to a text file using JSON rep"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
