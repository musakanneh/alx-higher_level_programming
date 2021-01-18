#!/usr/bin/python3

"""Inherits from subclass - square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A class representation of a square"""

    def __init__(self, size):
        """Initializes a square
        Validate the size of square
        then; reinitialize the size

        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
        self._size = size
