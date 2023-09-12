#!/usr/bin/python3
"""
module contains a function that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """a function that returns the JSON representation of an object (string)

    Args:
        my_obj (str): string to be translated into a JSON-formatted data

    Returns: a JSON representation of an object
    """
    json_str = json.dumps(my_obj)
    return json_str
