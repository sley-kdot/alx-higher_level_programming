#!/usr/bin/python3
"""contains a class representing a square"""


class Square:
    """A class representing a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializate a square object with a given size

        Args:
            size (int): size of square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """gets the position of a square"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the position of a square
        Args:
            value (int): The new position of a square

        Raises:
            TypeError: if size is not an integer
            ValueError: if position  not >= 0
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        for item in value:
            msg = "position must be a tuple of 2 positive integers"
            if type(item) is not int:
                raise TypeError(msg)
            if item < 0:
                raise TypeError(msg)
        self.__position = value

    def area(self):
        """calculate the area of a square

        Returns:
            int: area of a square
        """
        return self.__size * self.__size

    def my_print(self, size=0, position=(0, 0)):
        """prints in stdout the square with the character #

        Args:
            size (int): first parameter
            position (tuple): second parameter
        """
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end='')
            for k in range(self.__size):
                print("#", end='')
            print()
