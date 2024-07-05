#!/usr/bin/python3
"""
    find a peak in minmum time
"""


def find_peak(list_of_integers):
    """
        find a peak in O(log(n))
    """
    length = len(list_of_integers)
    if list_of_integers is None or length == 0:
        return None

    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers[0], list_of_integers[1])

    left, right = 0, length - 1
    while right > left:
        m = left + (right - left) // 2
        if list_of_integers[m] > list_of_integers[m + 1]:
            right = m
        else:
            left = m + 1
    return list_of_integers[left]
