#!/usr/bin/python3
""" Writes a string to a text file and returns the number of characters """


def write_file(filename="", text=""):
    """ Writes a string to a .txt file """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return(my_file.write(text))
