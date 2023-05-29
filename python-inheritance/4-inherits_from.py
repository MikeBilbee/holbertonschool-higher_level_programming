#!/usr/bin/python3
""" Determines if an object inherited from a specific class """


def inherits_from(obj, a_class):
    """ Return: True if object inherited from a_class; Otherwise False """
    if type(obj) == a_class:
        return False
    return(issubclass(type(obj), a_class))
