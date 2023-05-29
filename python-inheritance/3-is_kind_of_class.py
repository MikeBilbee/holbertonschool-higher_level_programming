#!/usr/bin/python3
""" Determines if an object is an instance of a class that has inherited """


def is_kind_of_class(obj, a_class):
    """ Return: True if object has inherited from super class; Otherwise False """
    return isinstance(obj, a_class)
