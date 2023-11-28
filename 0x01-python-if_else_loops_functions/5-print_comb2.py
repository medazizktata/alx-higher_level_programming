#!/usr/bin/python3
for i in range(100):
    if i % 10 == 0:
        print("0{}, ".format(i), end="")
    elif i == 99:
        print(i, '\n')
    else:
        print("{}, ".format(i), end="")
