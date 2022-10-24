#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """ MyList class"""

    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
