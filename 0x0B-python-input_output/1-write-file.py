#!/usr/bin/python3
"""
writes text into a file
"""


def write_file(filename="", text=""):
    """
    writes text in a file
    Args:
        filename: name of file
        text: string to write into the file
    Returns: number of characters written
    """

    with open(filename, 'w+') as f:
        return f.write(text)
