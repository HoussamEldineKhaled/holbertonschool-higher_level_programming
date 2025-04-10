#!/usr/bin/python3
"""check if one inherits from another"""


def inherits_from(obj, a_class):
    """check if subclass"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
