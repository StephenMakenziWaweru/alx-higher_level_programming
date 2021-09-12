#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    len = 0
    for i in my_list:
        len += 1
    for x in range(-1, -(len + 1), -1):
        print("{:d}".format(my_list[x]))
