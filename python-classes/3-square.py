#!/usr/bin/python3
"""This is the square class!"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        """This initializes a Square with a size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This initializes the Square with an area"""
        self.__area = self.__size ** 2
        return self.__area
