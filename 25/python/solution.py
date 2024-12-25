#!/usr/bin/env python3
"""AoC day 25, 2024: Code Chronicle"""

import pathlib
import sys


def parse_data(puzzle_input: str) -> tuple[list[list[int]], list[list[int]]]:
    """Parse input data"""
    keys = []
    locks = []

    for block in puzzle_input.split("\n\n"):
        grid = list(zip(*block.splitlines()))
        if grid[0][0] == ".":
            keys.append([row.count("#") - 1 for row in grid])
        else:
            locks.append([row.count("#") - 1 for row in grid])

    return locks, keys


def part1(locks: list[list[int]], keys: list[list[int]]) -> int:
    """Solve part 1"""
    return sum(
        all(x + y <= 5 for x, y in zip(lock, key)) for lock in locks for key in keys
    )


def part2() -> None:
    """Solve part 2"""
    print("It's Christmas, there's no Part 2! 🎄")


def solve(puzzle_input: str) -> tuple[int, None]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(*data), part2()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
