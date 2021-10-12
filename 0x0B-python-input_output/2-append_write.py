#!/usr/bin/python3
"""Module with a function that appends a string to a text file"""


def append_write(filename="", text=""):
    """Mtd that appends a string to a text file and returns no.\
        of chars added"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
