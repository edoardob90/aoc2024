#!/usr/bin/env python3
"""AoC day 1, 2024: Historian Hysteria"""

import pathlib
import sys
from collections import Counter


def parse_data(puzzle_input: str) -> tuple[list[int], list[int]]:
    """Parse input data"""
    first, second = [], []
    for line in puzzle_input.splitlines():
        a, b = line.split()
        first.append(int(a))
        second.append(int(b))

    return first, second


def part1(data: tuple[list[int], list[int]]) -> int:
    """Solve part 1"""
    first, second = data
    return sum(abs(a - b) for a, b in zip(sorted(first), sorted(second)))


def part2(data: tuple[list[int], list[int]]) -> int:
    """Solve part 2"""
    first, second = data
    second_counts = Counter(second)
    return sum(num * second_counts[num] for num in first)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
