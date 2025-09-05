#!/usr/bin/python3
"""Module contains a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """prints a name

    Args:
        first_name (str): first argument
       last_name (str): second argument
    Raises:
        TypeError: exception if arguments are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
