#!/usr/bin/python3
"""Exact same object.
Author: Kanneh

"""


def is_same_class(obj, a_class):
    """A function that returns True if the object is
    exactly an instance of the specified class;
    otherwise False

    Args:
        obj - object of the class
        a_class - the class

    """
    if isinstance(type(obj), a_class):
        return True
    return False
