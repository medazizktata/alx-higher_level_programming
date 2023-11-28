#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of "
ld = number % 1000
if ld > 5:
    str2 = " and is greater than 5\n"
elif ld == 0:
    str2 = " and is 0\n"
elif ld < 6 and ld != 0:
    str2 = " and is less than 6 and not 0\n"
print(str1 + number + str2 + '\n')
