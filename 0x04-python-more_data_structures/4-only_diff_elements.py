#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    finding the symetric difference between the two sets
    Returns a new set with elements in either the set or the other set but not in both
    """
    return set_1 ^ set_2
