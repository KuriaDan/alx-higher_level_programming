#!/usr/bin/python3
"""
function that appends a string at the end of a
text file (UTF8) and returns the number of characters
added:
"""


def append_write(filename="", text=""):
    """
    appends string at the end of file
    args:
        filename: name of file
        text: text to append
    """

    with open(filename, 'a+') as f:
        return f.write(text)
