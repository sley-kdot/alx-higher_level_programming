#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    size = len(argv)
    if size == 1:
        print("{:d} argument.".format(size - 1))
    elif size == 2:
        print("{:d} argument:".format(size - 1))
    else:
        print("{:d} arguments:".format(size - 1))
    for i in range(1, size):
        print("{:d}: {}".format(i, argv[i]))
