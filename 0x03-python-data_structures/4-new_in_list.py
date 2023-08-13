#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_cpy = list(my_list)
    size = len(my_list)
    if idx < 0:
        return list_cpy
    if idx > size:
        return list_cpy
    for i in range(size):
        if i == idx:
            list_cpy[i] = element
    return list_cpy
