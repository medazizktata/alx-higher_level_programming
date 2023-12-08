#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    merged_set = set()
    merged_set = set_1.symmetric_difference(set_2)
    return merged_set
