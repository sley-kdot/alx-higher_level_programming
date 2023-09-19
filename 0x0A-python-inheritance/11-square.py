#!/usr/bin/python3
"""module contains the Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a Square class"""
    def __init__(self, size):
        """instance attributes

        Args:
            size (int): size of a square
        """ 
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(width=size, height=size)

    def __str__(self):
        """returns a string representation of a square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """calculates the area of a square

        Returns: size * size
        """
        return self.__size ** 2
