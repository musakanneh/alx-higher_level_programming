#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    list = []
    for i in my_list:
        if i % 2:
            list = list + [False]
        else:
            list = list + [True]
    return list
