#!/usr/bin/python3
"""contains a module that adds two integers"""


def add_integer(a, b=98):
    """calculates the sum of two integers

    Args:
        a (int): first argument
        b (int): second argument

    Returns: sum of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
