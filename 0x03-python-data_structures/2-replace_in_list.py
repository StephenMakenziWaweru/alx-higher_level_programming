#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    len = 0
    for i in my_list:
        len += 1
    if idx < 0:
        return my_list
    elif idx > len - 1:
        return my_list
    my_list.pop(idx)
    my_list.insert(idx, element)
    return (my_list)
