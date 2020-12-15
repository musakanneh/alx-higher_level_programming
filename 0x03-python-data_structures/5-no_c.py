#!/usr/bin/python3


def no_c(my_string):
    """
    A function to remove all characters c and C from a string.
    """
    copy = [x for x in my_string if x != 'c' and x != 'C']
    return ("".join(copy))