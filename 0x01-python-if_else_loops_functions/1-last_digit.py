#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of "
ld = abs(number) % 10
if ld > 5:
    str2 = " and is greater than 5\n"
elif ld == 0:
    str2 = " and is 0\n"
elif ld < 6 and ld != 0:
    str2 = " and is less than 6 and not 0\n"
print(f"{str1}{number} is {ld}{str2}\n")
