#!/usr/bin/env python3
"""AoC day 9, 2024: Disk Fragmenter"""

import pathlib
import sys
from bisect import insort
from typing import Optional

from utils import ilist, partition


class Disk:
    def __init__(self, input_str: str) -> None:
        self.files = {}
        self.free = []
        self.attempted = set()

        disk_map = partition(ilist(input_str + "0"), 2)
        current_pos = 0

        for i, (file_size, gap_size) in enumerate(disk_map):
            self.files[i] = list(range(current_pos, current_pos + file_size))
            current_pos += file_size
            self.free.extend(range(current_pos, current_pos + gap_size))
            current_pos += gap_size

    @property
    def checksum(self) -> int:
        if not self.files:
            return 0

        return sum(file_id * sum(blocks) for file_id, blocks in self.files.items())

    def __str__(self) -> str:
        length = (
            max(
                max(self.free) if self.free else 0,
                max(max(pos) for pos in self.files.values()) if self.files else 0,
            )
            + 1
        )

        out = ["."] * length

        for file_id, blocks in self.files.items():
            for pos in blocks:
                out[pos] = str(file_id)

        return "".join(out)

    def add_free_block(self, block):
        insort(self.free, block)

    def compact_single(self) -> bool:
        if not self.free:
            return False

        first_gap = self.free.pop(0)

        for file_id in sorted(self.files, reverse=True):
            if not self.files[file_id]:
                continue

            last_block = self.files[file_id][-1]

            if last_block > first_gap:
                self.add_free_block(last_block)
                self.files[file_id][-1] = first_gap
                self.files[file_id].sort()
                return True

        self.add_free_block(first_gap)

        return False

    def find_contiguous_space(self, size: int) -> Optional[int]:
        if len(self.free) < size:
            return None

        for i in range(len(self.free) - size + 1):
            if self.free[i + size - 1] - self.free[i] == size - 1:
                return self.free[i]

        return None

    def compact_blocks(self) -> bool:
        if not self.free:
            return False

        for file_id in sorted(self.files, reverse=True):
            if file_id in self.attempted:
                continue

            block = self.files[file_id]
            size = len(block)

            if not size:
                self.attempted.add(file_id)
                continue

            current_start = min(block)
            if start_pos := self.find_contiguous_space(size):
                if start_pos >= current_start:
                    self.attempted.add(file_id)
                    continue

                new_pos = list(range(start_pos, start_pos + size))
                old_pos = sorted(block)

                for pos in new_pos:
                    self.free.remove(pos)

                self.free.extend(old_pos)
                self.free.sort()

                self.files[file_id] = new_pos
                self.attempted.add(file_id)
                return True

            self.attempted.add(file_id)

        return False


def parse_data(puzzle_input: str) -> "Disk":
    """Parse input data"""
    return Disk(puzzle_input)


def part1(puzzle_input: str) -> int:
    """Solve part 1"""
    disk = parse_data(puzzle_input)
    while disk.compact_single():
        pass
    return disk.checksum


def part2(puzzle_input: str) -> int:
    """Solve part 2"""
    disk = parse_data(puzzle_input)
    while disk.compact_blocks():
        pass
    return disk.checksum


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    return part1(puzzle_input), part2(puzzle_input)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
