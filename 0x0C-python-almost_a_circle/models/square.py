#!/usr/python3
"""module that contains a Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a Square class that inherits a Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """instance attributes

        Args:
            size (int): first argument
            x (int): second argument
            y (int): third argument
            id (int) forth argument
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """a method that returns a string representation of a class"""
        return "[Square] ({}) {:d}/{:d} - {:d}".format(
                self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter method for size size attribute"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size attribute"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """a method that assigns attributes"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
                i += 1
        if kwargs:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'size':
                    self.size = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        """a method that returns a dict. representation of a class"""
        value = {
                'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y
                }
        return value
