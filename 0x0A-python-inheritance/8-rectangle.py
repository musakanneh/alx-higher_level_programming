#!/usr/bin/python3
"""Integer validator
Author: Kanneh

"""


class BaseGeometry:
    """A Base Geometry class"""

    def area(self):
        """Raises an exception because...
        area is not implemented

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the inputs: name and values

        Args:
            name(str) - input name as string
            value(int): pararams validator

        """
        if type(value) not in [int]:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation of width and height"""
        self.integer_validator(width, height)
        self.__width = width
        self.__height = height
