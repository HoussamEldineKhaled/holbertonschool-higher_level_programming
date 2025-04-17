#!/usr/bin/python3
"""load from a json file"""


import json


def load_from_json_file(filename):
    """load json file

    Args:
       filename(str): name of the file

    Return: object of the json file
    """
    with open(filename, 'r') as file:
        return json.load(file)
