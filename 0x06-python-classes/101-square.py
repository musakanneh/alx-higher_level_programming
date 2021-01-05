#!/usr/bin/python3
"""Write a class Square that defines a square by:
(based on 5-square.py)
"""


class Square:
    """Square class with a private attribute -
    size.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the size variable as a private
        instance artribute

        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Instantiation with optional size of square"""
        return self.__size

    @size.setter
    def size(self, size_value):
        """Gets the size of the square"""
        self.__size = size_value

        if not isinstance(size_value, int):
            raise TypeError("size must be an integer")
        elif size_value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Get/set the current position of the square."""
        return self.__position

    @position.setter
    def position(self, size_value):
        """Must be a tuple of 2 positive integers,
        otherwise raise a TypeError exception

        """
        self.__position = size_value

        if (not isinstance(size_value, tuple) or
                len(size_value) != 2 or
                not all(isinstance(num, int) for num in size_value) or
                not all(num >= 0 for num in size_value)):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the '#' character."""
        if self.__size == 0:
            print("")
            return
        for i in range(0, self.__position[1]):
            [print("")]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size != 0:
            [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if i != self.__size - 1:
                print("")
        return ("")
