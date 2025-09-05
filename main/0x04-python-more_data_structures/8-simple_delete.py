#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """a function that deletes a key in a dictionary"""
    new_dict = a_dictionary.copy()
    for idx in new_dict:
        if idx == key:
            del a_dictionary[key]
    return a_dictionary
