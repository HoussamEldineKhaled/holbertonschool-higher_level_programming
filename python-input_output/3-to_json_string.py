#!/usr/bin/python3
"""json string"""


import json

def to_json_string(my_obj):
    """json string

    Args:
       my_obj (str): input object

    Returns:
       str: Json string
    """
    return json.dumps(my_obj)
