#!/usr/bin/python3
"""The square"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class inheriting from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructs the square's attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String method for rectangle class"""
        str_res = ("[Square] ({}) {}/{} - {}"
                   .format(self.id, self.x, self.y, self.width))
        return str_res

    def area(self):
        """Returns the area of the square"""
        return self.width ** 2

    @property
    def size(self):
        """Gets the"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the public class
        Args:
            *args(any): the list of arguments - no-keyworded arguments
            **kwargs(any):
        """
        if not args and not kwargs:
            return
        if args:
            attributes = ["id", "size", "x", "y"]
            for i, j in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], j)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """Converts to dictionary"""
        _map = super().to_dictionary()
        _map["size"] = _map["width"]
        del _map["width"], _map["height"]
        return _map
