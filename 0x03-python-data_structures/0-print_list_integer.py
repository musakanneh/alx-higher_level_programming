#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    A function that prints all integers of a list.
    """
    i = 0
    for i in range(len(my_list)):
        print("{}".format(my_list[i]))
