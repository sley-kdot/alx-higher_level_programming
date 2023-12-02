#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """prints a matrix of integers"""
    size = len(matrix)
    for row in range(size):
        row_length = len(matrix[row])
        for col in range(row_length):
            if col != row_length - 1:
                print("{:d}".format(matrix[row][col]), end=" ")
            else:
                print("{:d}".format(matrix[row][col]), end="")
        print()
