#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    A function that returns the weighted average of all integers tuple
    """
    grade = 0
    weight = 0
    if my_list:
        for i in my_list:
            grade += (i[0] * i[1])
            weight += i[1]
        grade /= weight
    return grade
