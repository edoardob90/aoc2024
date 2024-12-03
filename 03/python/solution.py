#!/usr/bin/env python3
"""AoC day 3, 2024: Mull It Over"""

import pathlib
import re
import sys


def parse_data(puzzle_input: str) -> str:
    """Parse input data"""
    return "".join(puzzle_input.splitlines())


def part1(data: str) -> int:
    """Solve part 1"""
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    return sum(int(a) * int(b) for a, b in pattern.findall(data))


def part2(data: str) -> int:
    """Solve part 2"""
    pattern = re.compile(r"(?:(don't|do).*?)?mul\((\d{1,3}),(\d{1,3})\)")
    do = True
    return sum(
        (do := flag != "don't" if flag else do) and int(a) * int(b)
        for flag, a, b in pattern.findall(data)
    )


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
