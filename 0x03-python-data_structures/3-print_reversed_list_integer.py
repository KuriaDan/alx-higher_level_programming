#!/usr/bin/python3
from re import I


def print_reversed_list_integer(my_list=[]):
    for i in range(1, len(my_list) + 1):
        j = -1 * i
        print('{:d}'.format(my_list[j]))
