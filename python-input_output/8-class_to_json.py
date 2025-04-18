#!/usr/bin/python3
"""class to json"""


def class_to_json(obj):
    """method for class to json

    Args:
       obj: input object class

    Return: object dictionary
    """
    return obj.__dict__
