#!/usr/bin/python3
def no_c(my_string):
    for element in my_string:
        if element in ['c', 'C']:
            continue
        else:
            print(element)
