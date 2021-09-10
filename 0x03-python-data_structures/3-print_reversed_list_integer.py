#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    len = 0
    for i in my_list:
        len += 1
    for x in range((len - 1), -1, -1):
        print(my_list[x])
