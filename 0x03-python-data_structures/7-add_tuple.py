#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples and returns a tuple with 2 integers"""
    a_len = len(tuple_a)
    b_len = len(tuple_b)
    a_list = list(tuple_a)
    b_list = list(tuple_b)
    new_list = []
    if a_len == 1:
        a_list.append(0)
    if b_len == 1:
        b_list.append(0)
    if a_len < 1:
        a_list.append(0)
        a_list.append(0)
    if b_len < 1:
        b_list.append(0)
        b_list.append(0)
    new_list.append(a_list[0] + b_list[0])
    new_list.append(a_list[1] + b_list[1])
    return tuple(new_list)
