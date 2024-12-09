#!/usr/bin/env python3
"""AoC day 4, 2024: Ceres Search"""

import pathlib
import sys

from utils import partition


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

    def find_A_positions(grid: list[str]) -> list[tuple[int, int]]:
        return [
            (i, j) for i, row in enumerate(grid) for j, c in enumerate(row) if c == "A"
        ]

    def neighbors(grid: list[str], position: tuple[int, int]) -> list[str]:
        height, width = len(grid), len(grid[0])
        x, y = position
        neighs = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                new_x, new_y = x + i, y + j
                if 0 <= new_x < height and 0 <= new_y < width:
                    neighs.append(grid[new_x][new_y])

        return neighs if len(neighs) == 9 else []

    def check_X_patterns(matrix: list[list[str]]) -> bool:
        """Check for a X-MAS pattern in a 3x3 submatrix"""
        patterns = [list("MAS"), list("SAM")]
        diag = [matrix[i][i] for i in range(3)]
        anti_diag = [matrix[i][2 - i] for i in range(3)]
        return diag in patterns and anti_diag in patterns

    a_positions = find_A_positions(data)
    neighborhoods = [neighbors(data, pos) for pos in a_positions]
    matrices = [partition(neigh, 3) for neigh in neighborhoods]

    return sum(check_X_patterns(m) for m in matrices if m)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
