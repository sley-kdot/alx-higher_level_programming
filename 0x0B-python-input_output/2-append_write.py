#!/usr/bin/python3
"""
module that contains a function that appends a string at the end of a text file
"""


def append_write(filename="", text=""):
    """a function that appends a string at the end of a text file (UTF8)
     and returns the number of characters added

    Args:
        filename (file): file to be written
        text (str): string of text to write in file

    Returns: number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        append_file = f.write(text)

    return append_file
