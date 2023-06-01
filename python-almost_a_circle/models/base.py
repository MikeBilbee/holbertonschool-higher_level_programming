#!/usr/bin/python3
""" Class: Base """

import json


class Base:
    """ Defines a Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Returns JSON list of of all dictionaries """
        jsonString = json.dump(list_dictionaries)
