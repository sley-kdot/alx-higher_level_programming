#!/usr/bin/python3
"""Module that contain a Sqaure class """


class Square:
    """ Blueprint that defines a Square class """
    def __init__(self, size):
        """ Initialization of attribute
        Args:
            size (int): size of square
        """
        self.__size = size
