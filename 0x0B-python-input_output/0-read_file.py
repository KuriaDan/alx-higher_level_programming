#!/usr/bin/python3
"""Module used to read a text file"""


def read_file(filename=""):
    """
    Reads file and prints it
    Args:
        filename: name of the file to read
    """

    with open(filename) as open_file:
        contents = open_file.read()
        print(contents, end="")
