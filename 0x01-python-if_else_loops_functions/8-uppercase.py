#!/usr/bin/python3
def uppercase(str):
    for i in str:
        asc = ord(str)
        if asc >=97 and asc <=122:
            asc = asc - 32
        print(chr(asc), end="")
    print("")
