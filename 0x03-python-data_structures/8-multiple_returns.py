#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    if sen_len == 0:
        first_c = None
    else:
        first_c = sentence[0]
    return sen_len, first_c
