#!/usr/bin/python3
def uniq_add(my_list=[]):
    size = len(my_list)
    new_list = []
    add_value = 0
    for i in range(size):
        if my_list[i] in new_list:
            continue
        else:
            new_list.append(my_list[i])
            add_value += my_list[i]
    return add_value
