#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = set()
    for elt1 in set_1:
        for elt2 in set_2:
            if elt1 == elt2:
                common.add(elt1)
    return common
