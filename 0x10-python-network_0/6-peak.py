#!/usr/bin/python3
"""
    find a peak in minmum time
"""

def find_peak(list_of_integers):
    """
        find a peak in O(log(n))
    """
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if len(list_of_integers) == 2:
        return max(list_of_integers[0], list_of_integers[1])

    mid_idx = int(len(list_of_integers) / 2)

    if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] and\
        list_of_integers[mid_idx + 1] < list_of_integers[mid_idx]:
        return list_of_integers[mid_idx]
    if list_of_integers[mid_idx - 1] >= list_of_integers[mid_idx]:
        a_list = list_of_integers[:mid_idx]
    else:
        a_list = list_of_integers[mid_idx + 1:]

    return find_peak(a_list)
