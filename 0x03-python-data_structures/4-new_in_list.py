#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        my_list_copy = my_list
        my_list_copy[idx] = element
        retrun my_list_copy
