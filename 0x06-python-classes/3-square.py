#!/usr/bin/python3
"""A class Square that defines a square by:
(based on 2-square.py)

"""


class Square:
    """Square class with a private attribute -
    size.

    """

    def __init__(self, size=0):
        """Initializes the size variable as a private
        instance artribute

        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns the current
        square area

        """
        return (self.__size ** 2)
