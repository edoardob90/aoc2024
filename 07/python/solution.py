#!/usr/bin/env python3
"""AoC day 7, 2024: Bridge Repair"""

import pathlib
import sys


def parse_data(puzzle_input: str) -> list[tuple[int, list[int]]]:
    """Parse input data"""
    lines = []
    for line in puzzle_input.splitlines():
        result, nums = line.split(": ")
        lines.append((int(result), [int(n) for n in nums.split()]))

    return lines


def part1(data: list[tuple[int, list[int]]]) -> int:
    """Solve part 1"""

    def is_obtainable(target, nums) -> bool:
        if len(nums) == 1:
            return target == nums[0]
        if target % nums[-1] == 0 and is_obtainable(target // nums[-1], nums[:-1]):
            return True
        if target - nums[-1] > 0 and is_obtainable(target - nums[-1], nums[:-1]):
            return True
        return False

    return sum(target for target, nums in data if is_obtainable(target, nums))


def part2(data: list[tuple[int, list[int]]]) -> int:
    """Solve part 2"""

    def is_obtainable(target, nums) -> bool:
        if isinstance(target, str):
            try:
                target = int(target)
            except ValueError:
                return False
        if len(nums) == 1:
            return target == nums[0]
        if target % nums[-1] == 0 and is_obtainable(target // nums[-1], nums[:-1]):
            return True
        if target - nums[-1] > 0 and is_obtainable(target - nums[-1], nums[:-1]):
            return True

        if (s := str(target)).endswith(sl := str(nums[-1])) and is_obtainable(
            s.removesuffix(sl), nums[:-1]
        ):
            return True

        return False

    return sum(target for target, nums in data if is_obtainable(target, nums))


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
