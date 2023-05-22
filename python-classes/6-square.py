#!/usr/bin/python3
"""This is the square class!"""


class Square:
    """This class defines a square"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size <= 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.position[0]):
                    print(end=" ")
                for k in range(self.size):
                    print("#", end="")
                print()

    @property
    def position(self):
        return self.__position

    @property
    def size(self):
        return self.__size

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
