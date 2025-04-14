#!/usr/bin/python3
"""writting"""


def write_file(filename="", text=""):
    """write method

    Args:
       filename (str): name of file
       text (str): text to be written
    """

    with open(filename, "w", encoding="UTF-8") as file:
        return file.write(text)
