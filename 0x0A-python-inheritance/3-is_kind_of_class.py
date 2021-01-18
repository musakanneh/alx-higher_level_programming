#!/usr/bin/python3
"""Same class or inherit from
Author: Kanneh

"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object
    is an instance of, or if the object is an instance
    of a class that inherited from, the specified class;
    otherwise False

    Args:
        obj(any): object of the class
        a_class(type): describes the class

    """
    if isinstance(obj, a_class):
        return True
    return False
