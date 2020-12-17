#!/usr/bin/python3


def square_matrix_map(matrix=[]):
    """
    a function that computes the square value of
    all integers of a matrix using map
    """
    return list(map(lambda row: list(map(lambda x: (x*x), row)), matrix))
