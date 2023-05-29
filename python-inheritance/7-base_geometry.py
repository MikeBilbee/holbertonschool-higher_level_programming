#!/usr/bin/python3
""" Class: BaseGeometry """


class BaseGeometry:
    """ Defines attributes for basic geometry """
    def area(self):
        """ Assigns Area for geometry """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))

        if value < 1:
            raise ValueError("{:s} must be greater than 0".format(name))
