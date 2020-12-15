#!/usr/bin/python3


def element_at(my_list, idx):
    """
     A function that retrieves an element from a list like in C.
    """
    list_idx = my_list[idx]  
    for i in range(list_idx):
        if idx > (list_idx) - 1 or idx < list_idx:
           return None
        return (my_list[idx])
