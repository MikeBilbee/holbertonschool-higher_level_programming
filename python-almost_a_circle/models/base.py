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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns JSON list of of all dictionaries """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes list_objs to a file """
        filename = cls.__name__ + ".json"
        jstring = []
        with open(filename, "w") as file:
            if list_objs is None:
                file.write("[]")
            else:
                jstring = [i.to_dictionary() for i in list_objs]
                file.write(Base.to_json_string(jstring))

    @staticmethod
    def from_json_string(json_string):
        """ Returns JSOn string json-string """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)
