#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    str = ""
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            print("{:d}".format(matrix[row, col]), end=" ")
        print()
