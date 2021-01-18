#!/usr/bin/python3


"""inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class reps of a rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
