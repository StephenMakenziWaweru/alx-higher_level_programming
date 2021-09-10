#!/usr/bin/python3
def no_c(my_string):
    tmp = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            tmp += i
    str = tmp
    return str
