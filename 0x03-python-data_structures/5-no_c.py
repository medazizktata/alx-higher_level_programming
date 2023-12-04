#!/usr/bin/python3
def no_c(my_string):
    i = 0
    while i < len(my_string):
        if ord(my_string[i]) == 67 or ord(my_string[i]) == 99:
            my_string = my_string[:i] + my_string[(i + 1):]
        else:
            i += 1
        return my_string
