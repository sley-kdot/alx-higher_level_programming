#!/usr/bin/python3
"""module contains a function that writes an Object to a text"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file
     using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        data = json.dumps(my_obj)
        write_file = f.write(data)
