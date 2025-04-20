#!/usr/bin/python3
"""basic serialization"""


import pickle


def serialize_and_save_to_file(data, filename):
    """save to file

    Args:
       data: data
       filename: name of file
"""
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def load_and_deserialize(filename):
    """deserialize file

    Args:
       filename: name of file

    Returns: the loaded pickle
"""
    with open(filename, "rb") as file:
        return pickle.load(file)
