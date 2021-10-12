#!/usr/bin/python3
"""Module with a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """that writes a string to a text file and returns no. of chars written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
