#!/usr/bin/python3
def print_last_digit(number):
    if number >= 10:
        last = abs(number) % 10
    else:
        last = number
    if number < 0 and last > 0:
        last = last * -1
    return last
