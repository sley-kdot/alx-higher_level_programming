#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for letter in my_string:
        if "C" == letter or "c" == letter:
            continue
        new_str += letter
    return new_str
