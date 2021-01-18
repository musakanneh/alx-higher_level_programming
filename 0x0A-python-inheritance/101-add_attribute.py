#!/usr/bin/python3
"""Can I ? - Hell yeah!"""


def add_attribute(obj, attr, value):
    """A function that adds a new attribute to
    an object if it’s possible

    Args:
        obj(obj): input object
        attr(str): name of the attribute
        value(value): value of the attribute

    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
