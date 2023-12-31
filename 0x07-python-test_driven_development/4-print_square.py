#!/usr/bin/python3
"""module contains a function that prints a square with the character #"""


def print_square(size):
    """a function that prints a square with the character #

    Args:
        size (int): size length of the square

    Raises:
        TypeError: if size is not an integer
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
