#!/usr/bin/python3
"""from json string"""


import json


def from_json_string(my_str):
    """from json string

    Args:
       my_str: string input

    Return: the json parse
    """

    return json.parse(my_str)
