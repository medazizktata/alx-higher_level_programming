#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while true:
        try:
            print(my_list[i])
            i += 1
        except my_list[i] is None:
            break
