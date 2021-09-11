#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len = 0
    for i in my_list:
        len += 1
    if idx >= 0 and idx < len:
        del my_list[idx]
    return my_list
