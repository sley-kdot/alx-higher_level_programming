#!/usr/bin/python3
"""module contains a function that reads a text file"""


def read_file(filename=""):
    """function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
    for line in read_file:
        print(line, end='')
