#!/usr/bin/python3
""" Returns the JSON representation of an object (string) """

import json


def to_json_string(my_obj):
    """ Return: JSON representation of objaect """
    return json.dumps(my_obj)
