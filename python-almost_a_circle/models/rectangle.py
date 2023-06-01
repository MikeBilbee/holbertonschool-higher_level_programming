#!/usr/bin/python3
""" Class: Rectangle """


Base = __import__('base').Base


class Rectangle(Base):
    """ Defines a Rectangle """

    @property
    def width(self):
        """ initiates width """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = self.hw_validator("width", value)

    @property
    def height(self):
        """ Initiates height """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = self.hw_validator("height", value)

    @property
    def x(self):
        """x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter
        """
        self.__x = self.xy_validator("x", value)

    @property
    def y(self):
        """y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """y setter
        """
        self.__y = self.xy_validator("y", value)

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = self.hw_validator("width", width)
        self.height = self.hw_validator("height", height)
        self.x = self.xy_validator("x", x)
        self.y = self.xy_validator("y", y)
        super().__init__(id)
