#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list.
    """
    count = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end="")
            count += 1
        except Exception as e:
            break;
    print("")
    return count
