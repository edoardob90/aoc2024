"""Utility functions for AoC"""

from typing import Optional


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


def ilist(string: str, sep: Optional[str] = None) -> list[int]:
    """
    Return a list of integers from a string where
    numbers are separated by `sep`
    """
    return [int(x) for x in (list(string) if sep is None else string.split(sep))]
