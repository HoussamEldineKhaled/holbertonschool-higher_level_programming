#!/usr/bin/python3
"""
indent text
"""


def text_indentation(text):
    """

    Args:
    text: imput string

    Raises:
    TypeError: if not string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            while i + 1 < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
