#!/usr/bin/python3
def element_at(my_list, idx):
    size = len(my_list)
    if idx < 0:
        return None
    if idx > size:
        return None
    for i in range(size):
        if i == idx:
            return my_list[i]
