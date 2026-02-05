#!/usr/bin/python3

for i in range(0, 100):
    fmt_str = f"{i:02}"
    if i < 99:
        end_char = ", "
    else:
        end_char = ""
    print(fmt_str, end=end_char)
print()
