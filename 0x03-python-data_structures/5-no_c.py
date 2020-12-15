#!/usr/bin/env python3


def no_c(my_string):
    """
    A function that removes all characters c and C from a string.
    """
    str = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            str += char
    return str
