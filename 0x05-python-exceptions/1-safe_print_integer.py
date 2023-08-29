#!/usr/bin/python3
def safe_print_integer(value):
    condition = isinstance(value, int)
    try:
        if condition:
            print(value)
            return True
    except:
        return False
