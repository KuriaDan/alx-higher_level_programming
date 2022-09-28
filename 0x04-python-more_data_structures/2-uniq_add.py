#!/usr/bin/python
def uniq_add(my_list=[]):
    """
    a one-liner to convert the original list into a set as they
    contain no duplicate elements and find the sum of the elements
    """
    return sum(set(my_list))
