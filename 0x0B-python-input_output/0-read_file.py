#!/usr/bin/python3
"""Read file"""


def read_file(filename=""):
    """a function that reads a text file (UTF8)
    and prints it to stdout

    Args:
        filename(any): name of the file

    """
    with open('my_file_0') as f:
        for line in f:
            print(line, end="")
