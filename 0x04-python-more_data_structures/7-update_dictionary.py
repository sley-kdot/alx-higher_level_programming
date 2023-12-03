#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """a function that replaces or adds key/value in a dictionary"""
    for idx in a_dictionary.keys():
        new_dict = {}
        if idx == key:
            a_dictionary[idx] = value
        else:
            new_dict[key] = value
            a_dictionary.update(new_dict)
            return a_dictionary
