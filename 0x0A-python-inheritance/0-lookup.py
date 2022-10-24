#!/usr/bin/python3
"""
Function that returns a list of available
attributes and methods of an object"""


def lookup(obj):
    """
    Function: lookup()
    returns a list objectd
    """

    return list(dir(obj))
