#!/usr/bin/env python3
"""AoC day 5, 2024: Print Queue"""

import pathlib
import sys
from collections import defaultdict
from functools import cmp_to_key


def parse_data(puzzle_input: str) -> tuple[dict[tuple, bool], list[list[int]]]:
    """Parse input data"""
    _rules, _updates = puzzle_input.split("\n\n")

    rules = defaultdict(bool)
    for rule in _rules.splitlines():
        a, b = rule.split("|")
        rules[(int(a), int(b))] = True

    updates = [list(map(int, line.split(","))) for line in _updates.split("\n")]

    return rules, updates


def is_ordered(rules: dict[tuple, bool], update: list[int]) -> bool:
    n = len(update)
    for i in range(n):
        for j in range(i + 1, n):
            key = update[i], update[j]
            if not rules[key]:
                return False
    return True


def part1(data: tuple[dict, list[list[int]]]) -> int:
    """Solve part 1"""
    rules, updates = data
    return sum(
        update[len(update) // 2] for update in updates if is_ordered(rules, update)
    )


def part2(data: tuple[dict, list[list[int]]]) -> int:
    """Solve part 2"""
    rules, updates = data
    unordered = list(filter(lambda update: not is_ordered(rules, update), updates))

    def cmp(i: int, j: int) -> int:
        if i == j:
            return 0
        if rules[(i, j)]:
            return -1
        return 1

    ordered = [sorted(u, key=cmp_to_key(cmp)) for u in unordered]

    return sum(update[len(update) // 2] for update in ordered)


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
