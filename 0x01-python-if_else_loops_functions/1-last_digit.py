#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = abs(number) % 10
message = "Last digit of "
if number < 0:
    last_digit = -last_digit
if last_digit > 5:
    print("{}{} is {} and is greater than 5".format(message, number, last_digit))
elif last_digit == 0:
    print("{}{} and is {}".format(message, number, last_digit))
else:
    print("{}{} is {} and is less than 6 and not 0".format(message, number, last_digit))

