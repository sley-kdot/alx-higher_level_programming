#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    size = len(argv) - 1
    operators = ["+", "-", "*", "/"]
    if size != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] in operators:
        result = add(int(argv[1]), int(argv[3]))
    elif argv[2] in operators:
        result = sub(int(argv[1]), int(argv[3]))
    elif argv[2] in operators:
        result = mul(int(argv[1]), int(argv[3]))
    elif argv[2] in operators:
        result = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {:d}".format(argv[1], argv[2], argv[3], result))
