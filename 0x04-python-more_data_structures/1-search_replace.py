#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    size = len(my_list)
    for i in range(size):
        new_list.append(my_list[i])
        if new_list[i] == search:
            new_list[i] = replace
    return new_list
