#!/usr/bin/python3
"""First Rectangle"""


class Rectangle(Base):
    """A rectangle class that inherits from the base class

    Args:
        Base(model): the inherited model

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width
        self.height
        """Constructs the rectange's attributes"""

    @property
    def width(self):
        self.width = width

    @width.setter
    def width(self):
        self.__width = width

    @property
    def height(self):
        self.height = height

    @width.setter
    def height(self):
        self.__height = height
