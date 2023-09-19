#!/usr/bin/python3
"""module contains a BaseGeometry class"""


class BaseGeometry:
    """a class BaseGeometry"""

    def area(self):
        """raise an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """a method that validates an integer value

        Args:
            name (str): first argument
            value (int): second argument

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
