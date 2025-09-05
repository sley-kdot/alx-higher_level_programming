#!/usr/bin/python3
"""module that contains a class MyList"""


class MyList(list):
    """class MyList that inherits from list"""

    def print_sorted(self):
        """method that prints a sorted list"""
        my_list = sorted(self)
        print(my_list)
