#!/usr/bin/python3
"""a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure) represented
     by a JSON string

    Args:
        my_obj (str): JSON data to translated to string

    Returns: Python value
    """
    my_obj = json.loads(my_str)
    return my_obj
