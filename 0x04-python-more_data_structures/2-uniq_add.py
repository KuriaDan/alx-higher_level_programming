#!/usr/bin/python
def uniq_add(my_list=[]):
    """
    a one-liner to convert the original list into a set as they
    contain no duplicate elements, reconvert it into a list and
     find the sum of the eements
    """
    return sum(list(set(my_list)))
