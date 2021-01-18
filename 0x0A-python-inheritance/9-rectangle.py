#!/usr/bin/python3

"""Defines a class Rectangle that inherits
from the BaseGeometry class.

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits
    from the BaseGeometry

    """

    def __init__(self, width, height):
        """Instantiation of width and height"""
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str()
        representation of a Rectangle.

        """
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
