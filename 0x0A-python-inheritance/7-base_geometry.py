#!/usr/bin/python3
"""Integer validator
Author: Kanneh

"""


class BaseGeometry:
    """An empty class"""

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
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return value
