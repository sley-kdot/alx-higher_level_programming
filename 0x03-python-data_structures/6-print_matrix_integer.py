#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    str = ""
    for row in matrix:
        for col in row:
            print("{} {}".format(col, str), end=" ")
        print()
