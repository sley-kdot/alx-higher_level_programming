#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not a_dictionary:
        return None
    else:
        return max(a_dictionary)
