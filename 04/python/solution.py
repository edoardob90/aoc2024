#!/usr/bin/env python3
"""AoC day 4, 2024: Ceres Search"""

import pathlib
import sys


def parse_data(puzzle_input: str) -> list[str]:
    """Parse input data"""
    return puzzle_input.splitlines()


def part1(data: list[str]) -> int:
    """Solve part 1"""

    def count_patterns(lines: list[str]) -> int:
        return sum(line.count("XMAS") + line.count("SAMX") for line in lines)

    def count_vertical(lines: list[str]) -> int:
        cols = ["".join(col) for col in zip(*lines)]
        return count_patterns(cols)

    def get_diagonal(grid: list[str], offset: int) -> str:
        height, width = len(grid), len(grid[0])
        row, col = (-offset, 0) if offset < 0 else (0, offset)
        return "".join(
            grid[row + i][col + i] for i in range(min(height - row, width - col))
        )

    def count_diagonal(lines: list[str], reversed: bool = False) -> int:
        grid = [line[::-1] for line in lines] if reversed else lines
        n = len(lines)
        return count_patterns([get_diagonal(grid, k) for k in range(4 - n, n - 4 + 1)])

    verticals = ["".join(col) for col in zip(*data)]

    return (
        count_patterns(data)
        + count_patterns(verticals)
        + count_diagonal(data)
        + count_diagonal(data, reversed=True)
    )


def part2(data: list[str]) -> int:
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
