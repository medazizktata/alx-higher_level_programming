#!/usr/bin/python3
import random

number = random.randint(-10, 10)
number is greater than 0, equal to 0, or less than 0
if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
