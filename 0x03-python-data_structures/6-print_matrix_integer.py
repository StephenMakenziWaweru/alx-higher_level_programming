#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for submat in matrix:
        print(" ".join("{:d}".format(elmt) for elmt in submat))
