#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    for t in set(my_list):
        i += t
    return i
