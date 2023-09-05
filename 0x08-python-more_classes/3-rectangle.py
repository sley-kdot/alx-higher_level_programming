#!/usr/bin/python3
"""contains an empty class Rectangle"""


class Rectangle:
    """Blueprint of a Rectangle class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializate a rectangle object with a given width and height

        Args:
            width (int): width of a rectangle
            heigth (int): height of a rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle

        Args:
            value (int): The new width

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is not >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Gets the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle

        Args:
            value (int): The new height

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is not >= 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value

    def area(self):
        """calculates the area of a rectangle

        Returns:
            int: area of a rectangle
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """calculates the perimeter of a rectangle

        Returns:
            int: perimeter of a rectangle
        """
        if self.__height == 0 or self.__height == 0:
            return 0
        else:
            return (self.__height + self.__width) * 2

    def __str__(self):
        """prints a rectangle with character #"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result[:-1]
