#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    a = int(argv[1])
    b = int(argv[3])
    size = len(argv) - 1
    operators = ["+", "-", "*", "/"]
    if size != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)
    elif argv[2] in operators:
        result = add(a, b)
    elif argv[2] in operators:
        result = sub(a, b)
    elif argv[2] in operators:
        result = mul(a, b)
    elif argv[2] in operators:
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, result))
