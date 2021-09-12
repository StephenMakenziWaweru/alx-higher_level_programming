#!/usr/bin/python3
def element_at(my_list, idx):
    len = 0
    for x in my_list:
        len += 1
    if idx < 0:
        return None
    elif idx > len - 1:
        return None
    for i in range(len):
        if i == idx:
            return my_list[i]
