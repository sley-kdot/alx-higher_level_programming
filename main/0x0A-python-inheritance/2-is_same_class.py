#!/usr/bin/python3
"""module a function that returns True of False"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly an instance of the
    specified class otherwise False."""
    return type(obj) == a_class
