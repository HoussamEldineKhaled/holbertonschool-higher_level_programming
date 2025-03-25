#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    value = -100000
    key = ""
    for i in a_dictionary.keys():
        if a_dictionary[i] > value:
            value = a_dictionary[i]
            key = i
            
    return key
