#!/usr/bin/python3
"""A class Square that defines a square
by: (based on 1-square.py)

"""


class Square:
    """Square class with a private attribute
    size.

    """

    def __init__(self, size=0):
        """Initializes the size variable as a private
        instance artribute

        Args:
            __size (int): The __size of the new square.

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
