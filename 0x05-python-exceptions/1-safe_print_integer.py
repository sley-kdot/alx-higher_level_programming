#!/usr/bin/python3
def safe_print_integer(value):
    condition = isinstance(value, int)
    try:
        if condition:
            print("{:d}".format(value))
            return True
    except Exception:
        return False
