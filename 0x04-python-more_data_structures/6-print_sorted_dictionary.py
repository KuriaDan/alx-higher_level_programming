#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    sorting the keys using the sorted function then accessing
    the value to that key.
    """
    for i in sorted(a_dictionary):
        print(i + ':', a_dictionary[i])
