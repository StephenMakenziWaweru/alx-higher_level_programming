#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len = 0
    new_list = [x for x in my_list]
    for i in my_list:
        len += 1
    if idx < 0:
        return new_list
    if idx > len - 1:
        return new_list
    new_list.pop(idx)
    new_list.insert(idx, element)
    return new_list
