#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        c = None
    else:
        c = sentence[0]
    tup = (length, c)
    return tup
