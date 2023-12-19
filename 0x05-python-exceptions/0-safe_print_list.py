#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if x == 0:
        print()
        return 0
    try:
        count = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        count -= 1
        pass
    print()
    return count
