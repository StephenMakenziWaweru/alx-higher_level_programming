#!/usr/bin/python3
"""Module containing a function for reading a txt file(UTF8)"""


def read_file(filename=""):
    """Method that reads a text file (UTF8) and prints it to stdouts"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
