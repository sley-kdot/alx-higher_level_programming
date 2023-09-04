#!/usr/bin/python3
"""contains a class representing a square"""


class Square:
    """A class representing a Square"""
    def __init__(self, size=0):
        """Initializate a square object with a given size

        Args:
            size (int): size of square
        """
        self.__size = size

        @property
        def size(self):
            """The size of a square

            Return:
                int: size of square
            """
            return self.__size

        @size.setter
        def size(self, value):
            """Set the size of a square

            Args:
                value (int): The new size of a square

            Raises:
                TypeError: if size is not an integer
                ValueError: if size is not >= 0
            """
            if type(value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        def area(self):
            """calculate the area of a square

            Returns:
                int: area of a square
            """
            return self.__size * self.__size
