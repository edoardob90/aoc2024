#!/usr/bin/env python3
"""AoC day 18, 2024: RAM Run"""

import pathlib
import sys
from collections import deque

from utils import ilist


def parse_data(puzzle_input: str) -> list[list[int]]:
    """Parse input data"""
    return [ilist(line, sep=",") for line in puzzle_input.splitlines()]


def part1(data: list[list[int]], n: int = 70, bytes: int = 1024) -> int:
    """Solve part 1"""
    grid = [[0] * (n + 1) for _ in range(n + 1)]
    for col, row in data[:bytes]:
        grid[row][col] = 1

    queue = deque([(0, 0, 0)])
    seen = {(0, 0)}

    while queue:
        row, col, distance = queue.popleft()
        for nr, nc in ((row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)):
            if nr < 0 or nc < 0 or nr > n or nc > n:
                continue
            if (nr, nc) in seen:
                continue
            if grid[nr][nc] == 1:
                continue
            if nr == nc == n:
                return distance + 1
            seen.add((nr, nc))
            queue.append((nr, nc, distance + 1))
    return 0


def part2(data: list[list[int]]) -> int:
    """Solve part 2"""
    return 0


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
