#!/usr/bin/python3
""" Writes an Object to a text file, using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file, using a JSON representation """
    with open(filename, "w", encoding="utf-8") as my_file:
        return json.dump(my_obj, my_file)
