#!/usr/bin/python3
"""
Function that returns the JSON representation of an object
"""


import json


def to_json_string(my_obj):
    """
    returns a json representation
    args:
        my_obj: object to convert
    """

    return json.dumps(my_obj)
