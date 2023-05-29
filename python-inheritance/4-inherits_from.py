#!/usr/bin/python3
""" Determines if an object inherited from a specific class """


def inherits_from(obj, a_class):
    """ Return: True if object inherited from a_class; Otherwise False """
    return isinstance(obj, a_class)
