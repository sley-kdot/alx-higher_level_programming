#!/usr/bin/python3
def uppercase(str):
    word = ""
    for i in str:
        char = ord(i)
        if char >= 97 and char <= 122:
            word = chr((char - 32))
        else:
            word = chr(char)
        print("{}".format(word), end="")
    print("")
