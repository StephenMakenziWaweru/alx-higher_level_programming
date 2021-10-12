#!/usr/bin/python3
"""Module with load_from_json_file mtd"""
import json


def load_from_json_file(filename):
    """Method that creates an Object from a “JSON file”"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.loads(f.read())
