#!/usr/bin/python3
"""module that contains a function that write a string to a text file"""


def write_file(filename="", text=""):
    """a function that writes a string to a text file (UTF8)
     and returns the number of characters written

    Args:
        filename (file): file to be written
        text (str): string of text to write in file

    Returns: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        write_file = f.write(text)

    return write_file
