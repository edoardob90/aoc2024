#!/usr/bin/env python3
"""AoC day 2, 2024: Red-Nosed Reports"""

import pathlib
import sys
from itertools import pairwise
from typing import Iterable


def parse_data(puzzle_input: str) -> list[list[int]]:
    """Parse input data"""
    return [list(map(int, line.split())) for line in puzzle_input.splitlines()]


def is_safe(numbers: Iterable[int]) -> bool:
    if len(list(numbers)) <= 1:
        return True

    deltas = []
    for a, b in pairwise(numbers):
        d = b - a
        if not 1 <= abs(d) <= 3:
            return False
        deltas.append(d)

    return all(x > 0 for x in deltas) or all(x < 0 for x in deltas)


def part1(data: list[list[int]]) -> int:
    """Solve part 1"""
    return sum(is_safe(numbers) for numbers in data)


def part2(data: list[list[int]]) -> int:
    """Solve part 2"""

    def is_droppable_safe(numbers: list[int]) -> bool:
        return any(is_safe(numbers[:i] + numbers[i + 1 :]) for i in range(len(numbers)))

    return sum(is_droppable_safe(numbers) for numbers in data)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
