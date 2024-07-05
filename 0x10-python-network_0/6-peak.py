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

    mid_idx = length // 2
    
    if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] and\
       list_of_integers[mid_idx + 1] < list_of_integers[mid_idx]:
        return list_of_integers[mid_idx]
    if list_of_integers[mid_idx - 1] >= list_of_integers[mid_idx]:
        a_list = list_of_integers[:mid_idx]
    else:
        a_list = list_of_integers[mid_idx + 1:]

    return find_peak(a_list)
