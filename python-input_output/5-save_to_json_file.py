#!/usr/bin/python3
"""save to a json file"""


import json


def save_to_json_file(my_obj, filename):
    """method for saving

    Args:
       my_obj: input object
       filename: name of file
"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
