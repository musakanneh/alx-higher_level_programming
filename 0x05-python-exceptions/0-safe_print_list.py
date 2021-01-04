#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list.
    """
    list_count = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            list_count += 1
        except IndexError:
            break
    print("")
    return list_count
