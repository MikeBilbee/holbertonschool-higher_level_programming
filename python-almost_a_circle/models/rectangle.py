#!/usr/bin/python3
""" Class: Rectangle """


from models.base import Base


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
        """ height setter """
        self.__height = self.hw_validator("height", value)

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, value):
        """x setter """
        self.__x = self.xy_validator("x", value)

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        self.__y = self.xy_validator("y", value)

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init method """
        self.width = self.hw_validator("width", width)
        self.height = self.hw_validator("height", height)
        self.x = self.xy_validator("x", x)
        self.y = self.xy_validator("y", y)
        super().__init__(id)

    def hw_validator(self, name, value):
        """
        Raises: TypeError if Value is not int
                ValueError if value <=0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 1:
            raise ValueError("{:s} must be > 0".format(name))
        return value

    def xy_validator(self, name, value):
        """
        Raises: TypeError if Value is not int
                ValueError if value <=0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(name))
        return value

    def area(self):
        """ initializes area """
        return self.__width * self.__height

    def display(self):
        """ Displays a rectangle """
        for i in range(self.y):
            print()
        for j in range(self.height):
            print("{}{}".format(" " * self.x, "#" * self.width))

    def __str__(self):
        parts = [type(self).__name__, self.id, self.x,
                 self.y, self.width, self.height]
        res = "[{0}] ({1}) {2}/{3} - {4}/{5}".format(*parts)
        return res

    def update(self, *args):
        """ Updates self """
        try:
            self.id = args[0] or self.id
            self.width = args[1] or self.width
            self.height = args[2] or self.height
            self.x = args[3] or self.x
            self.y = args[4] or self.y
        except IndexError:
            return
