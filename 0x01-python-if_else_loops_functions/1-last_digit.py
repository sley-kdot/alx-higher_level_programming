#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
string = "and is less than 6 and not 0"
if number < 0:
    last_digit = ((number * -1) % 10) * -1
if number > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif number == 0:
    print(f"Last digit of {numberii} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is {last_digit} {string}")
