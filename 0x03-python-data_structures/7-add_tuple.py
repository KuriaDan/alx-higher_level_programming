#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tup = ()
    tuple1 = tuple_a + (0, 0)
    tuple2 = tuple_b + (0, 0)
    tup = tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]
    return tup
