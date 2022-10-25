#!/usr/bin/python3
import json


"""
Function that returns the JSON representation of an object
"""


def to_json_string(my_obj):
    """
    returns a json representation
    args:
        my_obj: object to convert
    """

    return json.dumps(my_obj)
