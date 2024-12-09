"""Utility functions for AoC"""


def partition(data, n, d=None, upto=True):
    """
    Generate sublists of `data`
    with length up to `n` and offset `d`
    """
    offset = d or n
    slices = []
    for i in range(0, len(data), offset):
        slice = data[i : i + n]
        if upto or len(slice) == n:
            slices.append(slice)
    return slices
