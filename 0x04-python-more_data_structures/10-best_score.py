#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max = next(iter(a_dictionary.values()))
    key_max = next(iter(a_dictionary))
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            key_max = key
    return key_max
