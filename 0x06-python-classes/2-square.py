#!/usr/bin/python3
"""Module that contain a Square class"""


class Square:
    """ Blueprint that defines a Square class """
    def __init__(self, size=0):
        """ Initialization of attribute
        Args:
            size (int): size of square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is not >= 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
