#!/usr/bin/python3
def uppercase(str):
    for asc in str:
        asc = ord(asc)
        if asc >= 97 and asc <= 122:
            asc = asc - 32
        print("{:c}".format(asc), end="")
    print("")