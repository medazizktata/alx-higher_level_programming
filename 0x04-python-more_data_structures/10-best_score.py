#!/usr/bin/python3
def best_score(a_dictionary):
    max = next(iter(a_dictionary.values()))
    for key, value in a_dictionary.items():
        if value > max:
            max = value
            k = key
    return k
