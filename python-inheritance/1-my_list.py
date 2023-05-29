#!/usr/bin/python3
""" Class inherits from list list """


class MyList(list):
    """ Inheriting from list list """
    def __init__(self):
        """ Initializes the object using super() """
        super().__init__()

    def print_sorted(self):
        """ Prints itself sorted """
        print(sorted(self))
