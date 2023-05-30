#!/usr/bin/python3
""" Appends a string to a text file and returns # of char """


def append_write(filename="", text=""):
    """ Reads file and prints it to STDOUT """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return(my_file.write(text))
