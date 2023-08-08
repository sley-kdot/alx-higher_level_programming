def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            string = chr(ord(str[i]) - 32)
        else:
            string = chr(ord(str[i]))
        print("{}".format(string), end="")
