#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        rev = my_list[::-1]
        for num in rev:
            print("{:d}".format(num))
