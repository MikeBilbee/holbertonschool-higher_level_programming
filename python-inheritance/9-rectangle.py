#!/usr/bin/python3
""" Class: Rectangle """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines a rectangle bassed on inherited traits from geometry """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns: area of self """
        return self.__width * self.__height

    def __str__(self):
        """ Returns width and height of rectangle """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
