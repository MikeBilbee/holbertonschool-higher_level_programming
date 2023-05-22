#!/usr/bin/python3
"""This class defines a Square"""


class Square:
    """This class defines a Square"""
    def __init__(self, size=None):
        """This initializes a square with a size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
