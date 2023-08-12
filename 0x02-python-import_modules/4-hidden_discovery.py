#!/usr/bin/python3
if __name__ == "main":
    import hidden_4
    for i in dir(hidden_4):
        if i[:2] == "__":
            continue
        print("{}".format(i))
