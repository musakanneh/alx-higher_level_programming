#!/usr/bin/python3
"""My integer"""


class MyInt(int):
    """A class that inherits from int"""

    def __eq__(self, value):
        """Not equating the operator"""
        return self.real != value

    def __ne__(self, value):
        """Equating the operator"""
        return self.real == value
