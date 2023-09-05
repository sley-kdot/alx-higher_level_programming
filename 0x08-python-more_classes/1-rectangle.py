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
        """Sets the width of a rectangle"""
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
        """Sets the height of a rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
