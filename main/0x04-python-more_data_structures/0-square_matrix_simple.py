#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """computes the square value of all integers of a matrix"""
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x * x, row)))
    return new_matrix
