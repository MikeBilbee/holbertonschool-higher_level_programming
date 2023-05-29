#!/usr/bin/python3
""" Determines if an object is an exact instance of a class """


def is_same_class(obj, a_class):
    """ Return: True if obj is the exact class a_class; Otherwise False """
    return(type(obj) == a_class)
