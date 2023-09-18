#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        return "[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".format(
                self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            for j in range(self.__x):
                print(" ", end='')
            for col in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args):
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
        value = {
                'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y
                }
        return value
