#!/usr/bin/python3
""" This creates a class that defines a Rectangle"""


class Rectangle:
    """ A class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initialization method for the Rectangle class

        Attributes:
        width: Width of rectangle
        height: Height of rectangle
        self.width = width
        self.height = height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width > 0 and self.height > 0:
            return (self.width * 2) + (self.height * 2)
        else:
            return 0

    def __str__(self):
        """Prints string representation of rectangle"""
        string = ""
        if self.width > 0 and self.height > 0:
            for row in range(self.height):
                for col in range(self.width):
                    string += '#'
                if row < self.height - 1:
                    string += '\n'
            return string
        else:
            return string

    def __repr__(self):
        """Return literal string representation"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) +\
            ")"

    def __del__(self):
        """Prints after deletion"""
        print("Bye rectangle...")
