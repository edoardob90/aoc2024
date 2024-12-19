#!/usr/bin/env python3
"""AoC day 19, 2024: Linen Layout"""

import pathlib
import sys


class Node:
    def __init__(self) -> None:
        self.children: dict[str, "Node"] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = Node()

    def __str__(self) -> str:
        def _build_str(node: Node, indent: int = 0, prefix: str = "") -> str:
            result = []
            if prefix:
                mark = "*" if node.is_end else ""
                result.append(" " * indent + prefix + mark)
            for seq, child in sorted(node.children.items()):
                result.append(_build_str(child, indent + 1, seq))
            return "\n".join(result)

        return _build_str(self.root)

    def insert(self, *patterns: str) -> None:
        for pattern in patterns:
            node = self.root
            for char in pattern:
                if char not in node.children:
                    node.children[char] = Node()
                node = node.children[char]
            node.is_end = True

    def search(self, string: str, debug: bool = False) -> bool:
        n = len(string)
        dp = [True] + [False] * n

        for i in range(n):
            if debug:
                print(dp)

            if not dp[i]:
                continue

            node = self.root
            j = i
            while j < n and string[j] in node.children:
                node = node.children[string[j]]
                j += 1
                if node.is_end:
                    dp[j] = True
                    if j == n:
                        return True
        return dp[n]


def parse_data(puzzle_input: str) -> tuple[list[str], list[str]]:
    """Parse input data"""
    patterns, designs = puzzle_input.split("\n\n")
    return patterns.split(", "), designs.splitlines()


def part1(patterns: list[str], designs: list[str]) -> int:
    """Solve part 1"""
    trie = Trie()
    trie.insert(*patterns)
    return sum(trie.search(d) for d in designs)


def part2(patterns: list[str], designs: list[str]) -> int:
    """Solve part 2"""
    return 0


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(*data), part2(*data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
