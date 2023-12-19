#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError:
                pass
    except IndexError:
        i -= 1
        pass
    print()
    return i
