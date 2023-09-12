#!/usr/bin/python3
"""module contains a function the returns a list"""


def lookup(obj):
    """a function that returns the list of available attributes and methods
    of an object"""
    return dir(obj)
