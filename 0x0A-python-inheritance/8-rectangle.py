#!/usr/bin/python3
"""module contains a Rectangle class"""
BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a Rectangle class that inherits the BaseGeometry class"""

    def __init__(self, width, height):
        """intance attributes

        Args:
            width (int): first argument
            height (int): second argument
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
