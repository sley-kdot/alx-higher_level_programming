#!/usr/bin/python3
"""contains an empty class Rectangle"""


class Rectangle:
    """Blueprint of a Rectangle class that defines a rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializate a rectangle object with a given width and height

        Args:
            width (int): width of a rectangle
            heigth (int): height of a rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
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
                result += str(self.print_symbol)
            result += "\n"
        return result[:-1]

    def __repr__(self):
        """representation of the rectangle to be able to recreate
        a new instance by using eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """prints a message when an instance if Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """method that returns the biggest rectangle based on the area

        Args:
            rect_1 (int): first argument
            rect_2 (int): second argument

        Raises:
            TypeError: if rect_1 and rect_2 is not an instance of Rectangle

        Returns: rect_1 if >= rect_2, otherwise rect_2
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method that returns a new Rectangle instance

        Args:
            size (int): size of square

        Returns: constructor of new Rectangle
        """
        return cls(size, size)
