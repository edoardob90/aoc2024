#!/usr/bin/env python3
"""AoC day 13, 2024: Claw Contraption"""

import pathlib
import re
import sys
from typing import NamedTuple

from utils import partition


class Machine(NamedTuple):
    button_a: tuple[int, int]
    button_b: tuple[int, int]
    prize: tuple[int, int]


def parse_data(puzzle_input: str) -> list[Machine]:
    """Parse input data"""
    machines = []
    for block in puzzle_input.split("\n\n"):
        coords = [
            tuple(pair)
            for pair in partition(tuple(map(int, re.findall(r"\d+", block))), 2)
        ]
        machines.append(Machine(*coords))
    return machines


def det(v1: tuple[int, int], v2: tuple[int, int]) -> int:
    """Determinant of a 2x2 matrix of (v1, v2) row vectors"""
    x1, y1 = v1
    x2, y2 = v2
    return x1 * y2 - y1 * x2


def win_machine(machine: Machine, bias: int = 0) -> int | None:
    """
    Find the winning solution for a machine, and return the cost.
    If no solution exists, returns `None`.
    """
    a, b, p = machine
    if bias:
        p = (p[0] + bias, p[1] + bias)

    # Zero determinant => no solution
    if (det_c := det(a, b)) == 0:
        return None

    # Cramer's rule
    x = det(p, b) / det_c
    y = det(a, p) / det_c

    if x.is_integer() and y.is_integer():
        return int(3 * x + y)

    return None


def part1(machines: list[Machine]) -> int:
    """Solve part 1"""
    return sum(cost for m in machines if (cost := win_machine(m)) is not None)


def part2(machines: list[Machine]) -> int:
    """Solve part 2"""
    BIAS = 10_000_000_000_000
    return sum(cost for m in machines if (cost := win_machine(m, BIAS)) is not None)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
