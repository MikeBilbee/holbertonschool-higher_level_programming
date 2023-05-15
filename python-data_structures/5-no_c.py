#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    if my_string:
        for t in my_string:
            if t != 'C' and t != 'c':
                new_string += t
    return new_string
