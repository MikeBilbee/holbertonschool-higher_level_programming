#!/usr/bin/python3
""" Returns the dictionary description with simple data structure """

import sys


def class_to_json(obj):
    """ Returns the dictionary description with simple data structure """
    return vars(obj)
