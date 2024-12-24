#!/usr/bin/env python3
"""AoC day 23, 2024: LAN Party"""

import pathlib
import sys
from collections import defaultdict


def parse_data(puzzle_input: str) -> dict[str, set]:
    """Parse input data"""
    graph = defaultdict(set)
    edges = [line.strip().split("-") for line in puzzle_input.splitlines()]

    for x, y in edges:
        graph[x].add(y)
        graph[y].add(x)

    return graph


def part1(graph: dict[str, set]) -> int:
    """Solve part 1"""
    sets = set()

    for x in graph:
        for y in graph[x]:
            for z in graph[y]:
                if z != x and x in graph[z]:
                    sets.add((tuple(sorted([x, y, z]))))

    return len([s for s in sets if any(n.startswith("t") for n in s)])


def part2(graph: dict[str, set]) -> str:
    """Solve part 2"""
    sets = set()

    def search(node: str, required: set):
        key = tuple(sorted(required))
        if key in sets:
            return

        sets.add(key)

        for neighbor in graph[node]:
            if neighbor in required:
                continue
            if not required <= graph[neighbor]:
                continue

            search(neighbor, {*required, neighbor})

    for node in graph:
        search(node, {node})

    return ",".join(sorted(max(sets, key=len)))


def solve(puzzle_input: str) -> tuple[int, str]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
