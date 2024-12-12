#!/usr/bin/env python3
"""AoC day 12, 2024: Garden Groups"""

import pathlib
import sys
from collections import deque


def parse_data(puzzle_input: str) -> list[list[str]]:
    """Parse input data"""
    return [list(line) for line in puzzle_input.splitlines()]


def get_regions(data: list[list[str]]) -> list[set]:
    rows = len(data)
    cols = len(data[0])

    regions = []
    seen = set()

    for r in range(rows):
        for c in range(cols):
            if (r, c) in seen:
                continue
            region = {(r, c)}
            plant = data[r][c]
            queue = deque([(r, c)])
            while queue:
                qr, qc = queue.popleft()
                for nr, nc in ((qr - 1, qc), (qr + 1, qc), (qr, qc - 1), (qr, qc + 1)):
                    if (nr, nc) in region:
                        continue
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if data[nr][nc] != plant:
                        continue

                    region.add((nr, nc))
                    queue.append((nr, nc))

            seen |= region
            regions.append(region)

    return regions


def part1(regions: list[set]) -> int:
    """Solve part 1"""

    def perimeter(region):
        result = 0
        for r, c in region:
            result += 4
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (nr, nc) in region:
                    result -= 1
        return result

    return sum(len(region) * perimeter(region) for region in regions)


def part2(regions: list[set]) -> int:
    """Solve part 2"""

    return 0


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    regions = get_regions(data)
    return part1(regions), part2(regions)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
