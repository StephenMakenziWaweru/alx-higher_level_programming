#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    len = 0
    for i in matrix:
        len += 1
    for i in matrix:
        for x in i:
            print("{}{}".format(x, " " if x != i[-1] else "\n"), end="")
    if len == 0:
        print("")
