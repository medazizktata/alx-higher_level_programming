#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
ld = abs(number) % 10
if number < 0:
    ld = ld * -1
if ld > 5:
    str2 = "and is greater than 5"
elif ld == 0:
    str2 = "and is 0"
elif ld < 6 and ld != 0:
    str2 = "and is less than 6 and not 0"
if number < 0:
    print(f"{str1} {number} is -{ld} {str2}")
else:
    print(f"{str1} {number} is {ld} {str2}")
