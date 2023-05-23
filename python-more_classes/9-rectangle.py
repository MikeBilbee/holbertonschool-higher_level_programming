#!/usr/bin/python3
""" This creates a class that defines a Rectangle"""


class Rectangle:
    """ A class that defines a Rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initialization method for the Rectangle class

        Attributes:
            width: Width of rectangle
            height: Height of rectangle
        self.width = width
        self.height = height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width: Width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter width of the rectangle

        Attributes:
            width: Width of rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height: Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter height of the rectangle

        Attributes:
            height: height of rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
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
                    string += str(self.print_symbol)
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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """returns larger of two rectangles"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 > area_2 or area_1 == area_2:
            return rect_1
        elif area_1 < area_2:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new square of size 'size'"""
        return cls(size, size)
