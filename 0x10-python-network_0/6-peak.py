#!/usr/bin/python3


def find_peak(list_of_integers):
    """Find a peak in a list of integers.

    Example:
        [1, 2, 4, 6, 3] -> 6
        [4, 2, 1, 2, 3, 1] -> 3 # but 4 is also a peak

    Returns: integer that is the peak.
    """
    l = len(list_of_integers)
    n = l // 2
    v = 0
    while v < l:
        v += 1
        if n == 0:
            gtl = True
        else:
            gtl = False
        if n == l - 1:
            gtr = True
        else:
            gtr = False
        if n > 0:
            if list_of_integers[n - 1] < list_of_integers[n]:
                gtl = True
        if n < l - 1:
            if list_of_integers[n] > list_of_integers[n + 1]:
                gtr = True
        if gtl and gtr:
            return list_of_integers[n]
        if not gtr:
            n += (l - n) // 2
        elif not gtl:
            n -= n // 2
