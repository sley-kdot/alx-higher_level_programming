#!/usr/bin/python3
"""module thay contains a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """a Rectangle class that inherits from Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialized attributes

        Args:
            width (int): first argument
            height (int): second argument
            x (int): third argument
            y (int): forth argument
            id (int): fifth argument
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """a method that returns a str representation of the class"""
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Getter method for width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width attribute

        Args:
            value (int): value to be assigned to width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter method for height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height attribute

        Args:
            value (int): value to be assigned to height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter method for x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method of x attribute

        Args:
            value (int): value to be assigned to x

        Raises:
            TypeError: if x is not an integer
            ValueError: if x is less 0
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter method of y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method of y attribute

        Args:
            value (int): value to be assigned to y

        Raises:
            TypeError: if y is not an integer
            ValueError: if y is less than 0
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """a method that calculates the area of a Rectangle

        Returns: width * height
        """
        return (self.width * self.height)

    def display(self):
        """a method that prints in stdout the Rectangle instance
         with the character #"""
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            for j in range(self.__x):
                print(" ", end='')
            for col in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """a method that assigns an argument to each attribute"""
        i = 0
        if args:
            for arg in args:
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
                i += 1
        if kwargs:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                elif key == 'width':
                    self.width = val
                elif key == 'height':
                    self.height = val
                elif key == 'x':
                    self.x = val
                elif key == 'y':
                    self.y = val

    def to_dictionary(self):
        """a method that returns the dict. representation of a Rectangle"""
        value = {
                'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y
                }
        return value
