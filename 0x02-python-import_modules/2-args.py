#!/usr/bin/python3
import sys
n = len(sys.argv)
if n == 0:
    print('0 arguments.')
else:
    print('{} arguments:'.format(n - 1))
    for i in range(1, n):
        print('{}: {}'.format(i, sys.argv[i]))
