#!/usr/bin/python3
def remove_char_at(str, n):
    strc = ""
    for i in range(0, len(str)):
        if i != n:
            strc += str[i]
    return strc
